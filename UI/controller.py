import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._retailer= None
        self._prodotto = None

    #fill🔥
    def fill_anni(self):
        for anno in self._model.get_anni():
            self._view._anni.options.append(ft.dropdown.Option(anno))

    def fill_brand(self):
        for brand in self._model.get_brand():  # sto appendendo al dropdown l'oggetto reatiler
            self._view._brand.options.append(ft.dropdown.Option(brand)) # salvati l'oggetto da qualche parte

    def fill_retailer(self):
        for retailer in self._model.get_retailer():  # sto appendendo al dropdown l'oggetto reatiler
            self._view._retailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code,# 🔑 Chiave univoca dell'opzione
                                                                  text=retailer.Retailer_name,# 🏷️ Testo visibile nel menu a tendina
                                                                  data=retailer,# 📦 Oggetto completo, utile per accedere a tutti gli attributi dopo la selezione
                                                                  on_click=self.read_retailer))  # salvati l'oggetto da qualche parte

    def read_retailer(self, e):
        self._retailer = e.control.data  # l'abbiamo inizializzata a None
        # e.control.data è il risultato di onclick sopra

    #handle👨🏻‍⚕️
    def handle_TopVendite(self, e):
        """
        stampare (al massimo) le migliori 5 vendite: l’anno, il brand del prodotto
        venduto e il retailer che ha effettuato la vendita. Le migliori vendite sono stabilite
        in base al ricavo, dato come Unit_sale_price * Quantity (vedere la tabella
        go_daily_sales del database).
        Il sorting delle vendite deve essere fatto in senso decrescente di ricavo.
        """
        self._view.txt_result.controls.clear() #cancello quello che era uscito prima
        anno_selezionato= self._view._anni.value
        #se non ha selezionato anno, glielo diciamo
                # if anno_selezionato is None:
                #     self._view.create_alert("Attenzione, selezionare un periodo didattico!")
                #     self._view.update_page()
                #     return
        #se non è nullo
        migliori_vendite= self._model.get_migliori_vendite(anno_selezionato)
        for vendita in migliori_vendite:
            self._view.txt_result.controls.append(ft.Text(vendita))
        self._view.update_page()


    def handle_AnalizzaVendite(self,e):
        self._view.txt_result.controls.clear()  # cancello quello che era uscito prima
        anno_selezionato = self._view._anni.value
        brand_selezionato = self._view._brand.value
        retailer_selezionato = self._view._retailer.value
        # se non ha selezionato anno, glielo diciamo
                    # if anno_selezionato is None or brand_selezionato is None or retailer_selezionato is None :
                    #     self._view.create_alert("Attenzione, selezionare tutte le caselle!")
                    #     self._view.update_page()
                    #     return
                    # se non è nullo
        vendite,conteggi= self._model.get_analizza(anno_selezionato,brand_selezionato,retailer_selezionato)

        if (vendite==1):
            self._view.txt_result.controls.append(ft.Text(f"nessuna corrispondenza trovata"))
            self._view.update_page()

        giro=self._model.get_giro(vendite) #somma ricavi vendite
        prodotti_diversi= conteggi["num_prodotti_diversi"]
        retailer_diversi= conteggi["num_retailer_diversi"]
        num_vendite= len(vendite)


        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {giro}\n Numero Vendite:{num_vendite}\n Numero dei retailers coinvolti: {retailer_diversi}\n Numero dei prodotti coinvolti {prodotti_diversi}"))

        self._view.update_page()
