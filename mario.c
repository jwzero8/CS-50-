#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    int row;
    int column;
    int space;
    do
    {
        // Prompt user to input correct number

        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // For making rows
    for (row = 0; row < height; row++)
    {
        // For making a right-aligned triangle
        for (space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        // For making columns
        for (column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("\n");
    }
}