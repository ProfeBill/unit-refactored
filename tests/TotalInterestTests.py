import unittest

import sys
sys.path.append("src")

from Logic import TotalInterest

class TotalInterestTests( unittest.TestCase ):

    def testNormal1( self ):
        #Variables de entrada
        purchase_amount = 200000
        number_payments = 36
        interest_rate = 3.1

        # Valores de Salida esperados
        expected_total_interest = 134726.20

        # LLamar a la funcionalidad
        result = TotalInterest.calculate_total_interest( purchase_amount, number_payments, interest_rate)

        # Verificar el resultado
        self.assertAlmostEqual( result, expected_total_interest, 0 )


# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()