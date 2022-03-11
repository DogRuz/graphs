from typing import List, Dict
import numpy as np


class Calculate:
    def __init__(self, operation: int, vectors: List[List[int]]):
        self.operation = operation
        self.vectors = vectors

    @staticmethod
    def get_swap_operation() -> Dict:
        return {1: 3, 3: 1, 2: 4, 4: 2}

    def swap_operation(self) -> None:
        self.operation = self.get_swap_operation()[self.operation]

    def get_operation_for_id(self):
        return {1: self.add, 2: self.mul, 3: self.subtraction, 4: self.division}.get(self.operation)

    def add(self):
        init_vector = np.array(self.vectors[0])
        for vector in self.vectors[1:]:
            init_vector += np.array(vector)
        return init_vector.tolist()

    def subtraction(self):
        init_vector = np.array(self.vectors[0])
        for vector in self.vectors[1:]:
            init_vector -= np.array(vector)
        return init_vector.tolist()

    def mul(self):
        init_vector = np.array(self.vectors[0])
        for vector in self.vectors[1:]:
            init_vector *= np.array(vector)
            init_vector[init_vector == np.inf] = 0
        return init_vector.tolist()

    def division(self):
        init_vector = np.array(self.vectors[0]).astype(float)
        for vector in self.vectors[1:]:
            init_vector /= np.array(vector).astype(float)
            init_vector[init_vector == np.inf] = 0
        return init_vector.tolist()

    def execute(self):
        operation_method = self.get_operation_for_id()
        result = operation_method()
        return result