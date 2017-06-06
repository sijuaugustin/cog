from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from pymongo import MongoClient
db_client = MongoClient("mongo-slave.propmix.io", port=33017)


@permission_classes((permissions.AllowAny,))
class LeadData(viewsets.ViewSet):

    def list(self, request):

        span_type = ['last 6 Month', 'last 12 Month', 'last 24 Month', 'last 27 Month', 'last 30 Month']
        criteria_type = ['leadcriteria1', 'leadcriteria2', 'leadcriteria3', 'others']

        if ('span' in request.query_params):
            span = str(request.query_params['span'])
        else:
            return Response({'status': 'ERROR',
                             'error': 'un_specified span_type'})

        if ('post' in request.query_params):
            zip_code = str(request.query_params['post'])
        else:
            return Response({'status': 'ERROR',
                             'error': 'un_specified post'})

        if ('criteria' in request.query_params):
            criteria = str(request.query_params['criteria'])
        else:
            return Response({'status': 'ERROR',
                             'error': 'un_specified criteria'})

        if request.query_params['span'] not in span_type:
            return Response({'status': 'ERROR', 'error': 'INVALID_SPAN'})
        if request.query_params['criteria'] not in criteria_type:
            return Response({'status': 'ERROR', 'error': 'INVALID_CRITERIA'})

        data = list(db_client.LeadsData.lead.find({"PostalCode": zip_code}, {"data.%s.%s" % (criteria, span): 1, '_id': 0}))
        if len(data) == 0:
            return Response({'status': 'ERROR', 'error': 'Not Enough Properties Matching with your search'})
        if data[0]['data'] == {}:
            return Response({'status': 'ERROR', 'error': 'Not Enough Properties Matching your search Criteria'})
        if data[0]['data'][criteria] == {}:
            return Response({'status': 'ERROR', 'error': 'Not Enough Properties Matching with your search span '})
        DATA = data[0]['data'][criteria][span]
        Property_info = {'PropertyInformation': DATA}
        return Response(Property_info)
