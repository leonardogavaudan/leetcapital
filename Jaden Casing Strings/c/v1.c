#include <stdio.h>

char *to_jaden_case(char *jaden_case, const char *string)
{
  const char *strPtr = string;
  char *jadenCasePtr = jaden_case;
  char prevChar = ' ';
  char newChar = '\0';

  while (*strPtr != '\0')
  {
    newChar = *strPtr;

    if (prevChar == ' ' && 'a' <= *strPtr && *strPtr <= 'z')
    {
      newChar = *strPtr - ('a' - 'A');
    }

    *jadenCasePtr = newChar;
    prevChar = *strPtr;

    strPtr++;
    jadenCasePtr++;
  }

  *jadenCasePtr = '\0';
  return jaden_case;
}

int main()
{
  const char *quote = "How can mirrors be real if our eyes aren't real";
  char jadenCaseQuote[100];

  to_jaden_case(jadenCaseQuote, quote);
  printf("Original: %s\n", quote);
  printf("Jaden-Cased: %s\n", jadenCaseQuote);

  return 0;
}