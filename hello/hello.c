#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt user for name
    string name = get_string("What's your name? ");

    // TODO: Say hello to user
    printf("Hello, %s\n", name);
    return 0;
}
