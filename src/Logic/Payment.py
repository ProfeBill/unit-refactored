import sys
sys.path.append("src")

from Logic.purchase import Purchase

# Exepcion personalizada que se usa en un caso de error particular
class TasaExcesiva( Exception ): 
    pass

def calculate_payment(purchase : Purchase):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """

    if purchase.interest_rate*12 > 100 :
        """ Si la tasa anual es mayor que 100, arroja una excepcion """
        raise TasaExcesiva( "La tasa no debe ser superior a 100" )

    if purchase.number_payments == 1 :
        """ Cuando el plazo sea una sola cuota, no se aplican intereses """
        return purchase_amount

    """ La tasa de interés está expresada como un entero entre 1 y 100 """
    i =  purchase.interest_rate / 100
 
    if purchase.interest_rate == 0:
        """ 
        Cuando la tasa sea cero, la cuota es la compra dividida las cuotas
        para evitar error de division por cero 
        """
        return purchase.purchase_amount / purchase.number_payments
    else:         
        return (purchase.purchase_amount * i) / (1 - (1 + i) ** (-purchase.number_payments))

