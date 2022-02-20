# TODO
import cs50

def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25.0

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = float(quarters + dimes + nickels + pennies)

    # Print total number of coins to give the customer
    print(coins)


def get_cents():
    while True:

        num_dollar = cs50.get_float("Change owed: ")
        if num_dollar > 0:
            break


    cents = num_dollar * 100
    return cents


def calculate_quarters(cents):

    quarters = cents // 25.00
    return quarters


def calculate_dimes(cents):

    dimes = cents // 10.00
    return dimes


def calculate_nickels(cents):

    nickels = cents // 5.00
    return nickels

def calculate_pennies(cents):

    cents = cents // 1.00
    return cents


main()
