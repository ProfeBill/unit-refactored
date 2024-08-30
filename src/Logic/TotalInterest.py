import sys
sys.path.append("src")

from Logic import Payment

def calculate_total_interest( purchase_amount, number_payments, interest_rate ):
    # 1. Calcular la cuota mensual
    payment = Payment.calculate_payment( purchase_amount, number_payments,  interest_rate )
    # 2. Multiplica la cuota por el numero de pagos
    total_payments = payment * number_payments

    # 3. Retorne la dierencia
    return total_payments - purchase_amount