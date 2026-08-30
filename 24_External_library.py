from currency_converter import CurrencyConverter

c = CurrencyConverter()

amt = float(input("Enter the amount in USD: "))

new_amt = c.convert(amt, 'USD', 'INR',date='2020-01-01')

print(f"Amountn in INR: {new_amt}")