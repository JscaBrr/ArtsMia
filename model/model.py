import networkx as nx
from database.DAO import DAO
from model.object import Object
import copy

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def getAllNodes(self):
        for i in DAO.getAllNodes():
            self._idMap[i.object_id] = i
        return DAO.getAllNodes()

    def getAllEdges(self):
        edges = []
        for i in DAO.getAllEdges():
            edges.append((self._idMap[i[0]], self._idMap[i[1]], i[2]))
        return edges

    def analizzaOggetti(self):
        self._grafo.add_nodes_from(self.getAllNodes())
        print(self._grafo.number_of_nodes())
        for i in self.getAllEdges():
            self._grafo.add_edge(i[0], i[1], weight=i[2])
        print(self._grafo.number_of_edges())
        return True, self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def computeComponenteConnessa(self, id):
        try:
            self._id = int(id)
            self._dimCC = nx.bfs_tree(self._grafo, self._idMap[self._id]).number_of_nodes()
            return self._dimCC
        except Exception:
            return False

    def calcolaPercorso(self, lun):
        try:
            self._lun = int(lun)
        except Exception:
            return False
        if self._lun < 2 or self._lun > self._dimCC:
            return False
        self._sequenzaOttima = []
        self._costoMax = -1
        self.ricorsione([self._idMap[self._id]], list(self._grafo.neighbors(self._idMap[self._id])), self._lun)
        return sorted(self._sequenzaOttima, key=lambda x: x.object_name), self._costoMax

    def ricorsione(self, parziale, sequenza, lun):
        if len(parziale) == lun:
            costo = self.costo(parziale)
            if costo > self._costoMax:
                self._costoMax = costo
                self._sequenzaOttima = copy.deepcopy(parziale)
        else:
            for n in sequenza:
                if self.vincoli(parziale, n):
                    parziale.append(n)
                    self.ricorsione(parziale, list(self._grafo.neighbors(parziale[-1])), lun)
                    parziale.pop()

    def vincoli(self, parziale, n: Object):
        if parziale[0].classification != n.classification or n in parziale:
            return False
        return True

    def costo(self, parziale):
        totCosto = 0
        for i in range(0, len(parziale)-1):
            totCosto += self._grafo[parziale[i]][parziale[i+1]]['weight']
        return totCosto