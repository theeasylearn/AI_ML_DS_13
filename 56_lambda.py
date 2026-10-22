# example of lambda function
getInterest = lambda amount,rate,year : (amount * rate * year) / 100
celtoFaren = lambda celsius : (celsius * (9/5)) + 32


amount = float(input("Enter amount: "))
rate = float(input("Enter rate: "))
year = int(input("Enter year: "))

celsius = float(input("Enter temperature in Celsius: "))

interest = getInterest(amount,rate,year)
print(f"interest = {interest:.2f}")

fahrenheit = celtoFaren(celsius)
print(f"fahrenheit = {fahrenheit:.2f}")


