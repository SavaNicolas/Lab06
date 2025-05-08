from database.DB_connect import DBConnect
from model.prodotto import Prodotto
from model.retailer import Retailer
from model.vendita import Vendita


class DAO():
    def __init__(self):
        pass

    # fill🔥
    @staticmethod
    def get_anni_dao():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:  # questo controllo va fatto sempre
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT DISTINCT YEAR(g.Date) AS Year FROM go_daily_sales g"""

            cursor.execute(query)

            for row in cursor:
                res.append(row["Year"]) #prende dal dizionario l'anno

            cursor.close()
            cnx.close()
        return res

    @staticmethod
    def get_brand_dao():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:  # questo controllo va fatto sempre
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT DISTINCT g.Product_brand AS Brand FROM go_products g"""

            cursor.execute(query)

            for row in cursor:
                res.append(row["Brand"]) #lista di oggetti prodotto

            cursor.close()
            cnx.close()
        return res

    @staticmethod
    def get_retailer_dao():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:  # questo controllo va fatto sempre
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT * FROM go_retailers g"""

            cursor.execute(query)

            for row in cursor:
                res.append(Retailer(**row))  # lista di oggetti prodotto

            cursor.close()
            cnx.close()
        return res

    # handle👨🏻‍⚕️
    def get_vendite_dao(anno_selezionato):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:  # questo controllo va fatto sempre
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT * FROM go_daily_sales g WHERE YEAR(g.Date) = COALESCE(%s, YEAR(g.Date))"""


            cursor.execute(query, (anno_selezionato,))

            for row in cursor:
                res.append(Vendita(**row))  # lista di oggetti Vendita

            cursor.close()
            cnx.close()
        return res

    def get_analisi_dao(anno_selezionato,brand_selezionato,retailer_selezionato):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:  # questo controllo va fatto sempre
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query1="""SELECT * FROM go_daily_sales g, go_products p, go_retailers r WHERE g.Retailer_code= r.Retailer_code and g.Product_number =p.Product_number AND YEAR(g.Date) = COALESCE(%s, YEAR(g.Date)) AND g.Retailer_code= COALESCE(%s, g.Retailer_code) AND p.Product_brand =COALESCE(%s, p.Product_brand)"""
            cursor.execute(query1, (anno_selezionato,retailer_selezionato,brand_selezionato))

            for row in cursor:
                res.append(Vendita(row["Retailer_code"],
                                   row["Product_number"],
                                   row["Order_method_code"],
                                   row["Date"],
                                   row["Quantity"],
                                   row["Unit_price"],
                                   row["Unit_sale_price"],
                                   ))  # lista di oggetti Vendita

            query2="""SELECT COUNT(DISTINCT p.Product_number) AS num_prodotti_diversi, COUNT(DISTINCT r.Retailer_code) AS num_retailer_diversi FROM go_daily_sales g, go_products p, go_retailers r WHERE g.Retailer_code= r.Retailer_code and g.Product_number =p.Product_number AND YEAR(g.Date) = COALESCE(%s, YEAR(g.Date)) AND g.Retailer_code= COALESCE(%s, g.Retailer_code) AND p.Product_brand =COALESCE(%s, p.Product_brand)"""
            cursor.execute(query2, (anno_selezionato, retailer_selezionato, brand_selezionato))
            conteggi = cursor.fetchone()  # sarà un dizionario con i 2 valori

            cursor.close()
            cnx.close()
        return res,conteggi


if __name__ == '__main__':
    for i in DAO.get_vendite_dao(2015):
        print(i)