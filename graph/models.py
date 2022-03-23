from django.db import models


class Graphs(models.Model):
    name_graph = models.TextField()


class Vectors(models.Model):
    graph = models.ForeignKey(Graphs, on_delete=models.CASCADE)
    index = models.IntegerField()
    value = models.FloatField()


class AdjacencyMatrix(models.Model):
    descendant = models.ForeignKey(Graphs, on_delete=models.CASCADE)
    ancestor = models.ForeignKey(Graphs, on_delete=models.CASCADE, related_name='ancestor_graph')

    @staticmethod
    def get_all_ancestors(graph_id, include_self=True, ancestors_dict=None):
        if ancestors_dict is None:
            ancestors_dict = {}
        if include_self:
            query = AdjacencyMatrix.objects.filter(descendant_id=graph_id).values_list('ancestor_id', flat=True)
            if query.count() > 0:
                ancestors_dict[graph_id] = list(query)
        for c in AdjacencyMatrix.objects.filter(descendant_id=graph_id):
            _ = c.get_all_ancestors(graph_id=c.ancestor_id, include_self=True, ancestors_dict=ancestors_dict)
        return ancestors_dict

    @staticmethod
    def get_all_descendants(graph_id, include_self=True, descendants_dict=None):
        if descendants_dict is None:
            descendants_dict = {}
        if include_self:
            query = AdjacencyMatrix.objects.filter(ancestor_id=graph_id).values_list('descendant_id', flat=True)
            if query.count() > 0:
                descendants_dict[int(graph_id)] = list(query)
        for c in AdjacencyMatrix.objects.filter(ancestor_id=graph_id):
            _ = c.get_all_descendants(graph_id=c.descendant_id, include_self=True, descendants_dict=descendants_dict)
        return descendants_dict
