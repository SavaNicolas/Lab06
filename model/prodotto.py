from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Prodotto:
    Product_number:int #chiave
    Product_line:str
    Product_type:str
    Product:str
    Product_brand:str
    Product_color:str
    Unit_cost: Decimal
    Unit_price:Decimal

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __hash__(self):
        return hash(self.Product_number)

    def __str__(self):
        return f"{self.nome} : ({self.Product_number}) - Brand: {self.Product_brand}"