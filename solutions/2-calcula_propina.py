def calculate_tip(bill_amount, tipPercentage):
    return print(round(bill_amount * (tipPercentage / 100), 2))


calculate_tip(100, 10)  # 10.0
calculate_tip(1524.33, 25)  # 381.08
