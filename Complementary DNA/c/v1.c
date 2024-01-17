#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *dna_strand(const char *dna)
{
  if (*dna == '\0')
  {
    return NULL;
  }

  size_t dnaLength = strlen(dna);
  char *str = malloc(dnaLength + 1);
  if (str == NULL)
  {
    return NULL;
  }

  char complimentaryValue;
  for (int i = 0; dna[i] != '\0'; i++)
  {
    switch (dna[i])
    {
    case 'A':
      complimentaryValue = 'T';
      break;
    case 'T':
      complimentaryValue = 'A';
      break;
    case 'G':
      complimentaryValue = 'C';
      break;
    case 'C':
      complimentaryValue = 'G';
      break;
    }

    str[i] = complimentaryValue;
  }

  str[dnaLength] = '\0';

  return str;
}

int main()
{
  const char *dna = "ATGC";
  char *complimentaryStrand = dna_strand(dna);

  if (complimentaryStrand != NULL)
  {
    printf("Original DNA Strand: %s\n", dna);
    printf("Complimentary DNA Strand: %s\n", complimentaryStrand);
    free(complimentaryStrand);
  }
  else
  {
    printf("Error allocating memory for DNA strand.\n");
  }

  return 0;
}