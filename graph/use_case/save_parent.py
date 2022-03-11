from typing import List,Union

from graph.error import GraphNotFound
from graph.models import AdjacencyMatrix, Graphs


class SaveParent:
    def __init__(self, child_vector: Union[str, None], parent_vectors: List[List[int]]):
        self.child_id = child_vector
        self.vectors_ids = parent_vectors

    def set_child_id(self, child_id: str) -> None:
        self.child_id = child_id

    def get_child_id(self) -> str:
        return self.child_id

    def set_vectors_ids(self, vectors_ids: List[List[int]]) -> None:
        self.vectors_ids = vectors_ids

    def get_vectors_ids(self) -> List[List[int]]:
        return self.vectors_ids

    def execute(self):
        for vector_id in self.vectors_ids:
            try:
                ancestor_graph = Graphs.objects.get(id=vector_id)
            except Graphs.DoesNotExist:
                raise GraphNotFound()
            AdjacencyMatrix.objects.get_or_create(ansctor_graph=ancestor_graph, descendant_id=self.child_id)
