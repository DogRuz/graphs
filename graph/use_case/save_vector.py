import uuid
from typing import List,Union

from graph.models import Vectors, Graphs


class SaveVector:
    def __init__(self, name: Union[str, None], vector: List[int]):
        self.name = name
        self.vector = vector

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_vector(self, vector: List[int]) -> None:
        self.vector = vector

    def get_vector(self) -> List[int]:
        return self.vector

    def execute(self):
        name = uuid.uuid4() if self.name is None else self.name
        obj, created = Graphs.objects.get_or_create(name_graph=name)
        if created:
            for index, value in enumerate(self.vector):
                Vectors.objects.get_or_create(index=index, value=value, graph_id=obj.id)
        data = {'vector': self.vector, 'id': obj.id, 'is_created': created, 'name_graph': obj.name_graph}
        return data
