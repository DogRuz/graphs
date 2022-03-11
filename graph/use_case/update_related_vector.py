from typing import Union

from graph.models import AdjacencyMatrix
from graph.use_case.get_vector import GetVector
from graph.use_case.update_vector import UpdateVector
from operation.use_case.get_operation_for_vector import OperationVector
from operation.utils import Calculate


class UpdateRelatedVector:
    def __init__(self, graph_id: int, max_len: Union[int, None] = None):
        self.graph_id = graph_id
        self.max_len = max_len

    def set_graph_id(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_graph_id(self) -> int:
        return self.graph_id

    def set_max_len(self, graph_id: int) -> None:
        self.graph_id = graph_id

    def get_max_len(self) -> int:
        return self.graph_id

    def execute(self):
        all_descendants = AdjacencyMatrix.get_all_descendants(graph_id=self.graph_id)
        if len(all_descendants) > 0:
            max_descendants = max(all_descendants.keys())
            list_graph_id = all_descendants[max_descendants]
        else:
            list_graph_id = [self.graph_id]
        for graph_id in list_graph_id:
            ancestors = AdjacencyMatrix.get_all_ancestors(graph_id=graph_id)
            ancestors_sorted = dict(sorted(ancestors.items(), key=lambda x: x[0]))
            for descendant, ancestors in ancestors_sorted.items():
                vectors = []
                for ancestor in ancestors:
                    vector = GetVector(ancestor).execute()
                    if self.max_len is not None and self.max_len != len(vector):
                        if self.max_len > len(vector):
                            vector += [0 for _ in range(self.max_len-len(vector))]
                        else:
                            vector = vector[0:self.max_len]
                        vector = UpdateVector(graph_id=ancestor, vector=vector).execute()['vector']
                    vectors.append(vector)
                operation_id = OperationVector(descendant).execute().first().operation_id
                descendant_vector = Calculate(operation_id, vectors)
                # descendant_vector.swap_operation()
                descendant_vector = descendant_vector.execute()
                UpdateVector(graph_id=descendant, vector=descendant_vector).execute()
        return None
