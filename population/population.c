#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startsize;
    do
    {
        startsize = get_int("Start Size (minimum 9): ");
    }
    while (startsize < 9);

    // TODO: Prompt for end size
    int endsize;
    do
    {
        endsize = get_int("End Size: ");
    }
    while (startsize > endsize);

    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    while (startsize < endsize)
    {
        startsize = startsize + (startsize / 3) - (startsize / 4);
        year++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", year);
    return 0;
}
