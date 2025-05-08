from decimal import Decimal

from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    # fill🔥
    def get_anni(self):
        return DAO.get_anni_dao()

    def get_brand(self):
        brand = DAO.get_brand_dao()
        brand_ordinata= sorted(brand)  # li sto ordinando per cognome
        return brand_ordinata

    def get_retailer(self):
        retailer = DAO.get_retailer_dao()
        retailer.sort(key=lambda x: x.Retailer_name)
        return retailer

    #handle👨🏻‍⚕️
    def get_migliori_vendite(self,anno_selezionato):
        vendite=DAO.get_vendite_dao(anno_selezionato)
        vendite.sort()
        migliori_5= []
        for i in range(0,5):
            migliori_5.append(vendite[i])

        return migliori_5

    def get_analizza(self, anno_selezionato,brand_selezionato,retailer_selezionato):
        vendite,conteggi =DAO.get_analisi_dao(anno_selezionato,brand_selezionato,retailer_selezionato)
        if (len(vendite) == 0):
            return 1,1
        vendite.sort()
        return vendite,conteggi

    def get_giro(self,vendite):
        somma=Decimal("0.0")
        for vendita in vendite:
            somma+=vendita.Ricavo
        return somma





