from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from graph.serializers import GraphSerializer, ParentVectorSerializer
from graph.use_case.delete_vector import DeleteVector
from graph.use_case.get_ancestors import GetAncestors
from graph.use_case.get_vector import GetVector
from graph.use_case.save_parent import SaveParent
from graph.use_case.save_vector import SaveVector
from graph.use_case.update_related_vector import UpdateRelatedVector
from graph.use_case.update_vector import UpdateVector


class GraphView(APIView):
    @staticmethod
    def get(request):
        vector = GetVector(graph_id=request.GET.get("id")).execute()
        return JsonResponse(data={"id_graph": request.GET.get("id"), "vector": vector}, safe=False)

    @staticmethod
    def post(request):
        item_serializer = GraphSerializer(data=request.data)
        item_serializer.is_valid()
        data = SaveVector(**item_serializer.data).execute()
        return JsonResponse(data)

    @staticmethod
    def patch(request):
        item_serializer = GraphSerializer(data=request.data)
        item_serializer.is_valid()
        data = UpdateVector(graph_id=int(request.GET.get("id")), **item_serializer.data).execute()
        if data['is_update_related_vector']:
            UpdateRelatedVector(graph_id=int(request.GET.get("id")), max_len=len(data['vector'])).execute()
        return JsonResponse(data)

    @staticmethod
    def delete(request):
        DeleteVector(graph_id=request.GET.get("id")).execute()
        return JsonResponse(data={}, status=status.HTTP_204_NO_CONTENT)


class ParentVectorView(APIView):
    @staticmethod
    def post(request):
        item_serializer = ParentVectorSerializer(data=request.data)
        item_serializer.is_valid()
        SaveParent(**item_serializer.data).execute()
        return JsonResponse(data={}, status=status.HTTP_200_OK)

    @staticmethod
    def get(request):
        data = GetAncestors(graph_id=request.GET.get("id")).execute()
        return JsonResponse(data=data, status=status.HTTP_200_OK, safe=False)
