from typing import List, Union

from graph.models import Graphs, Vectors


class UpdateVector:
    def __init__(self, vector: List[int], graph_id: int, name: Union[str, None] = None):
        self.name = name
        self.vector = vector
        self.graph_id = graph_id

    def set_graph_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_graph_id(self) -> int:
        return self.graph_id

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_vector(self, vector: List[int]) -> None:
        self.vector = vector

    def get_vector(self) -> List[int]:
        return self.vector

    def update_vector(self):
        for index, value in enumerate(self.vector):
            try:
                vector = Vectors.objects.get(index=index, graph_id=self.graph_id)
            except Vectors.DoesNotExist:
                vector = None
            if vector is None:
                Vectors.objects.create(index=index, graph_id=self.graph_id, value=value)
            else:
                vector.value = value
            vector.save()

    def execute(self):
        data = {}
        obj = Graphs.objects.get(id=self.graph_id)
        if obj is not None:
            obj.name_graph = self.name or obj.name_graph
            vector = Vectors.objects.filter(graph_id=obj.id)
            len_vector = vector.count()
            vector_list = vector.values_list('value', flat=True)
            vector.filter(index__gte=len(self.vector)).delete()
            self.update_vector()
            data = {'vector': self.vector, 'id': obj.id, 'name_graph': obj.name_graph,
                    "is_update_related_vector": len_vector != len(self.vector) or list(vector_list) != self.vector}
        return data
