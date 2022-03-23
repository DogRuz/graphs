from django.views.decorators.cache import cache_page

from django.http import JsonResponse
from rest_framework.views import APIView

from graph.use_case.update_related_vector import UpdateRelatedVector
from graphs import settings
from operation.serializers import OperationsSerializer, ResultSerializer
from operation.use_case.get_all_operations import GetAllOperations
from operation.use_case.get_operation_for_vector import OperationVector
from operation.use_case.save_result_operation import SaveResultOperation
from operation.utils import Calculate

CACHE_TTL = getattr(settings, 'CACHE_TTL', settings.SESSION_EXPIRATION)


class OperationsView(APIView):

    @staticmethod
    @cache_page(CACHE_TTL)
    def get(request):
        result = GetAllOperations().execute().values()
        return JsonResponse(result, safe=False)

    @staticmethod
    def post(request):
        item_serializer = ResultSerializer(data=request.data)
        item_serializer.is_valid()
        data, is_create = SaveResultOperation(**item_serializer.data).execute()
        if not is_create:
            UpdateRelatedVector(graph_id=item_serializer.data['graph_id']).execute()
        return JsonResponse({"vector": data}, safe=False)


class UseOperationView(APIView):

    @staticmethod
    def get(request):
        result = OperationVector(graph_id=request.GET.get("id")).execute()
        return JsonResponse({"operation_id": result.operation_id}, safe=False)

    @staticmethod
    def post(request):
        item_serializer = OperationsSerializer(data=request.data)
        item_serializer.is_valid()
        item_data = item_serializer.data
        get_vector = Calculate(item_data['operation'], item_data['vectors']).execute()
        return JsonResponse({"vector": get_vector}, safe=False)
