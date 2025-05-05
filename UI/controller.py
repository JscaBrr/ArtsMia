import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.clear()
        print( f"Creazione Grafo andata a buon fine:\nnumero nodi: {self._model.getNumNodi()} \nnumero archi: {self._model.getNumArchi()}")
        self._view.txt_result.controls.append(ft.Text(
            f"Creazione Grafo andata a buon fine:\nnumero nodi: {self._model.getNumNodi()} \nnumero archi: {self._model.getNumArchi()}"))
        self._view.update_page()

    def handleCompConnessa(self,e):
        self._view.txt_result.controls.clear()
        try:
            id = int(self._view._txtIdOggetto.value)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.alert("id inserito non valido")
            self._view.update_page()
            return
        if not self._model.checkExistece(id):
            self._view.txt_result.controls.clear()
            self._view.alert("id inserito non esistente")
            self._view.update_page()
            return
        sizeConnessa = self._model.getCompConnessa(id)
        self._view.txt_result.controls.append(ft.Text(f"dimensione della componente connessa per l'id inserito {id}: {sizeConnessa}"))
        self._view.update_page()

