import math
def until_when(expenses_rate, savings_rate, withrawal_rate, yield_rate):
    """"""
    x = math.log(((expenses_rate * (1 / withrawal_rate) * yield_rate)/ savings_rate)+1)
    y = math.log(1 + yield_rate)
    return x / y

def main():

    print(until_when(0.4, 0.6, 0.04, 0.075))

if __name__ == '__main__':
    main()