#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    // Get user to input dollars owned
    float cents_initial;
    do
    {
        cents_initial = get_float("Cents owned: ");
    }
    while (cents_initial < 0);

    int cents = cents_initial;

    int quarters;
    int dimes;
    int nickels;
    int pennies;

    while (cents != 0)
    {
        // Divide by quarters
        quarters = cents / 25;
        cents = cents % 25;
        // Divide by dimes
        dimes = cents / 10;
        cents = cents % 10;
        // Divide by nickel
        nickels = cents / 5;
        cents = cents % 5;
        // Divide by pennies
        pennies = cents / 1;
        cents = cents % 1;
    }

    int sum_coins = quarters + dimes + nickels + pennies;
    // show number of coins
    if (cents == 0)
    {
        int zero_case = 0;
        printf("Number of coins is %i", zero_case);
    }
    else
    {
    printf("Number of coins are %i\n", sum_coins);
    }

}
