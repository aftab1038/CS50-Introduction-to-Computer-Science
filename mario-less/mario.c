#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("what is height? ");
    }
    while (height > 8 || height < 1);

    for (int row = 0; row < height; row++)
    {
        for (int space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        };

        for (int column = 0; column <= row; column++)
        {
            printf("#");
        };
        printf("\n");
    }
}
