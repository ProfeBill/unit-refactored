class Purchase:
    """  
    Almacena los datos de una compra con tarjeta de crédito
    """
    def __init__( self, purchase_amount=0,interest_rate=0,number_payments=0 ):
        self.purchase_amount = purchase_amount
        self.interest_rate = interest_rate
        self.number_payments = number_payments