#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int x = 0; x < width; x++)
    {
        for (int y = 0; y < height; y++)
        {
            if (image[y][x].rgbtBlue == 0 && image[y][x].rgbtGreen == 0 && image[y][x].rgbtRed == 0)
            {
                image[y][x].rgbtRed = 255;
                image[y][x].rgbtGreen = 255;
                image[y][x].rgbtBlue = 0;
            }
        }
    }
}
