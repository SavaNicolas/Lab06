import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title =None
        self._anni=None
        self._brand=None
        self._retailer=None
        self._topVendite=None
        self._analizzaVendite=None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self._anni = ft.Dropdown(label="Anno",options=[])
        self._controller.fill_anni()  # mettimi dentro gli anni🔥

        self._brand = ft.Dropdown(label="brand",options=[])
        self._controller.fill_brand()  # mettimi dentro i brand🔥

        self._retailer = ft.Dropdown(label="retailer",options=[])
        self._controller.fill_retailer()  # mettimi dentro i retailer🔥

        row1 = ft.Row([self._anni, self._brand, self._retailer], alignment=ft.MainAxisAlignment.CENTER)

        #ROW 2
        self._topVendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handle_TopVendite)#👨🏻‍⚕️
        self._analizzaVendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handle_AnalizzaVendite)#👨🏻‍⚕️
        row2 = ft.Row([self._topVendite, self._analizzaVendite],alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)


        self._page.add(row1,row2,self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
