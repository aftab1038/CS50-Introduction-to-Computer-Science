#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: Resverse input.wav output.wav");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    char *infile = argv[1];
    FILE *inptr = fopen(infile, "rb");
    if (inptr == NULL)
    {
        printf("COuld not open %s.\n", infile);
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, inptr);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        printf("Not Wave File\n");
    }
    if (header.audioFormat != 1)
    {
        printf("Not Wave File\n");
    }

    // Open output file for writing
    // TODO #5
    char *outfile = argv[2];
    FILE *outptr = fopen(outfile, "wb");
    if (outptr == NULL)
    {
        printf("COuld not open %s.\n", outfile);
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, outptr);

    // Use get_block_size to calculate size of block
    // TODO #7
    int size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    if (fseek(inptr, size, SEEK_END))
    {
        return 1;
    }
    BYTE buffer[size];
    while (ftell(inptr) - size > sizeof(header))
    {
        if (fseek(inptr, -2 * size, SEEK_CUR))
        {
            return 1;
        }
        fread(buffer, size, 1, inptr);
        fwrite(buffer, size, 1, outptr);
    }
    fclose(outptr);
    fclose(inptr);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int size = header.numChannels * header.bitsPerSample / 8;
    return size;
    return 0;
}