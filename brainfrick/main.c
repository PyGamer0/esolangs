#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <stdlib.h>

#define TAPE_SIZE 65536
#define CODE_SIZE 65536

uint16_t tape[TAPE_SIZE];
uint32_t index_tape = TAPE_SIZE / 2;

uint32_t match_paren(char *x, uint32_t i) {
    int k = 0;
    while (i < strlen(x) - 1) {
        if (x[i] == '[') k++;
        if (x[i] == ']') k--;
        if (k == 0) return i;
        i++;
    }
    exit(1);
}

uint32_t match_parenr(char *x, uint32_t i) {
    int k = 0;
    while (i > 0) {
        if (x[i] == ']') k++;
        if (x[i] == '[') k--;
        if (k == 0) return i;
        i--;
    }
    exit(1);
}

int main(int argc, char **argv) {
    char text[65536]; int i = 0;

    if (argc < 2 || argc > 2) {
        return 1;
    }

    int c;
    char *filename = argv[1];
    FILE *file = fopen(filename, "r");
    while ((c = fgetc(file)) != EOF) text[i++] = c; text[i] = '\0';

    for (i = 0; i < strlen(text) - 1; i++) {
        switch (text[i]) {
        case '+': tape[index_tape]++; break;
        case '-': tape[index_tape]--; break;
        case '.': printf("%c", tape[index_tape]); break;
        case ',': read(STDIN_FILENO, &tape[index_tape], 1); break;
        case '>': index_tape++; break;
        case '<': index_tape--; break;
        case '[': if (tape[index_tape] == 0) i = match_paren(text, i); break;
        case ']': i = match_parenr(text, i) - 1; break;
        }
    }

    return 0;
}
