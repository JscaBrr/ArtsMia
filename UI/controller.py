import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handleAnalizzaOggetti(self, e):
        bool, Nnodes, Nedges = self._model.analizzaOggetti()
        self._view.txt_result.controls.clear()
        if bool is True:
            self._view.txt_result.controls.append(ft.Text(f"Creazione grafo eseguita con successo\nNumero nodi: {Nnodes}\nNumero archi: {Nedges}"))
            self._view._btnCompConnessa.disabled = False
        self._view.update_page()

    def handleComponenteConnessa(self, e):
        self._insertedID = self._view._txtIdOggetto.value
        self._view.txt_result.controls.clear()
        if self._insertedID:
            value = self._model.computeComponenteConnessa(self._insertedID)
            if value is False:
                self._view.alert("Si è verificato un errore. Riprova")
            else:
                self._view.txt_result.controls.append(ft.Text(f"Eseguito con successo il calcolo della componente connessa\nNumero nodi: {value}"))
                self._view._btnCercaOggetti.disabled = False
        else:
            self._view.alert("Inserire un ID prima di procedere")
        self._view.update_page()

    def handleCercaOggetti(self, e):
        self._insertedLUN = self._view._txtLUN.value
        result = self._model.calcolaPercorso(self._insertedLUN)
        self._view.txt_result.controls.clear()
        if result is False:
            self._view.alert("Errore. Riprova")
        else:
            percorso, costo = result
            self._view.txt_result.controls.append(ft.Text(f"Calcolo della ricorsione con percorso di dimensione compresa tra 2 e {self._insertedLUN} eseguito\ncosto: {costo}"))
            for i, item in enumerate(percorso, start=1):
                self._view.txt_result.controls.append(ft.Text(f"{i}. {item}"))
        self._view.update_page()




