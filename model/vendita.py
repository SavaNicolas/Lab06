from datetime import datetime
from decimal import Decimal
from dataclasses import dataclass

from model.retailer import Retailer


@dataclass
class Vendita:
    Retailer_code:int
    Product_number:int
    Order_method_code: int

    Date: datetime.date
    Quantity: int
    Unit_price:Decimal
    Unit_sale_price: Decimal


#metodo inizializzato dopo per avere il ricavo
    def __post_init__(self):
        self.Ricavo: float= self.Quantity * self.Unit_price

#abbiamo tripla chiave esterna
    def __eq__(self, other):
        return (self.Product_number == other.Product_number and self.Retailer_code == other.Retailer_code and self.Order_method_code == other.Order_method_code)

    def __hash__(self):
        return hash(self.Product_number, self.Retailer_code, self.Order_method_code)

    def __str__(self):
        return (f"Data:{self.Date}; Ricavo: {self.Ricavo}; Retailer:{self.Retailer_code}; Product:{self.Product_number}")

    #ordine decrescente di ricavo--> metodo lt che viene richiamato quando usiamo sort/sorted

    def __lt__(self, other):
        return self.Ricavo < other.Ricavo