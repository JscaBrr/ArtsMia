import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        for i in DAO.getAllNodes():
            self._idMap[i.object_id] = i

    def creaGrafo(self):
        self._grafo.add_nodes_from(DAO.getAllNodes())
        for i in DAO.getAllEdges():
            self._grafo.add_edge(self._idMap[i.o1], self._idMap[i.o2], weight=i.peso)

    def getNumNodi(self):
        return self._grafo.number_of_nodes()

    def getNumArchi(self):
        return self._grafo.number_of_edges()

    def getCompConnessa(self, id):
        if id not in self._idMap:
            return None
        o = self._idMap[id]
        #v1
        listSuccessors = []
        for i in nx.dfs_successors(self._grafo, o).values():
            listSuccessors.extend(i)
        num = len(listSuccessors)
        print(num)
        #v2
        listPredecessors = []
        for i in nx.dfs_predecessors(self._grafo, o).values():
            listPredecessors.append(i)
        num = len(listPredecessors)
        print(num)
        #v3
        num = nx.dfs_tree(self._grafo, o).number_of_nodes()
        print(num)
        #v4
        num = len(nx.node_connected_component(self._grafo, o))
        print(num)
        return num

    def checkExistece(self, idOggetto):
        return idOggetto in self._idMap













