# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

import sys
# Agrega una ruta donde Python debe buscar a los modulos que se importen en el código
sys.path.append( "src" )

# Las pruebas importan los modulos que hacen el trabajo
from Logic import Payment
from Logic.purchase import Purchase


# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        purchase = Purchase()
        purchase.purchase_amount = 200000
        purchase.interest_rate = 3.1
        purchase.number_payments = 36

        # Variables de salida
        payment = 9297.96
        resultado = Payment.calculate_payment( purchase )
        # Prueba que dos variables sean iguales
        self.assertEqual( payment, round(resultado,2)  )

    def testPayment1_1(self):
        purchase_amount = 850000
        interest_rate = 3.4
        number_payments = 24
        payment = 52377.5
        resultado = Payment.calculate_payment( purchase_amount, interest_rate, number_payments )
        self.assertEqual( payment, round(resultado,2)  )

    def testPayment2(self):
        """ purchase_amount normal con todos los parametros correctos """
        purchase_amount = 480000
        interest_rate = 0
        number_payments = 48
        payment = 10000

        resultado = Payment.calculate_payment( purchase_amount, interest_rate, number_payments )

        self.assertEqual( payment, round(resultado,2)  )


    def testPayment4(self):
        """  purchase_amount a una sola payment """
        purchase_amount = 90000
        interest_rate = 2.4
        number_payments = 1
        payment = 90000
        resultado = Payment.calculate_payment( purchase_amount, interest_rate, number_payments )
        self.assertEqual( payment, round(resultado,2)  )

    def testPayment3(self):
        """ purchase_amount con interest_rate excesiva """
        purchase_amount = 50000
        interest_rate = 12.4
        number_payments = 60
        
        try:
            resultado = Payment.calculate_payment( purchase_amount, interest_rate, number_payments )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Payment.TasaExcesiva  :
            pass  # Forzar Exito

    def testPayment3_v2(self):
        """ purchase_amount con interest_rate excesiva """
        purchase_amount = 50000
        interest_rate = 12.4
        number_payments = 60
        # Para controlar que una funcion si genere una excepcion
        # en el caso de prueba, se usa el metodo assertRaises
        # el primer parametro es la Excepcion esperada
        # el segundo es el metodo que se va a invocar
        # y los demas parametros son los parametros del metodo bajo prueba
        self.assertRaises( Payment.TasaExcesiva,  Payment.calculate_payment, purchase_amount, interest_rate, number_payments )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()