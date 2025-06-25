import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self._page = page
        self._page.title = "TdP exercise on MIA Art database"
        self._page.horizontal_alignment = "CENTER"
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._controller = None
        self._title = None

    def load_interface(self):
        self._title = ft.Text("The MIA Collection database", color="orange", size=24)
        self._page.controls.append(self._title)
        self._btnAnalizzaOggetti = ft.ElevatedButton(text="Analizza Oggetti", on_click=self._controller.handleAnalizzaOggetti, color="white", bgcolor="orange", width=200)
        self._txtIdOggetto = ft.TextField(hint_text="Inserire numero", color="orange", border_color="orange", width=200)
        self._btnCompConnessa = ft.ElevatedButton(text="Componente Connessa", on_click=self._controller.handleComponenteConnessa, color="white", bgcolor="orange", width=200, disabled=True)
        self._txtLUN = ft.TextField(hint_text="Inserire numero", color="orange", border_color="orange", width=200)
        self._btnCercaOggetti = ft.ElevatedButton("Cerca Oggetti", on_click=self._controller.handleCercaOggetti, color="white", bgcolor="orange", width=200, disabled=True)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(ft.Row([self._btnAnalizzaOggetti, self._txtIdOggetto, self._btnCompConnessa], alignment=ft.MainAxisAlignment.CENTER),
                       ft.Row([self.txt_result], alignment=ft.MainAxisAlignment.CENTER))
        self._page.add(ft.Row([ft.Container(width=200), self._txtLUN, self._btnCercaOggetti], alignment=ft.MainAxisAlignment.CENTER))

    def set_controller(self, controller):
        self._controller = controller

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def alert(self, message):
        dlg = ft.AlertDialog(title= ft.Row([ft.Icon(ft.icons.ERROR, color="red"), ft.Text("Errore", color="red")]),
                             content= ft.Text(message, color="red"),
                             actions= [ft.TextButton("OK", on_click=lambda e: self.closeAlert(dlg))])
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def closeAlert(self, dlg):
        dlg.open = False
        self._page.update()



