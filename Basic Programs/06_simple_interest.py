principle = input("Enter the Principle: ")
rate = input("Enter the Rate: ")
year = input("Enter the Years: ")

principle = int(principle)
rate = int(rate)
year = int(year)

sinterest = (principle*rate*year)/100

print("The value of Simple Interest: ", sinterest)