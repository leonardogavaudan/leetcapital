int romanToInt(char *s)
{
  int value;
  int prevValue;
  int total = 0;

  for (int i = 0; s[i] != '\0'; i++)
  {
    switch (s[i])
    {
    case 'I':
      value = 1;
      break;
    case 'V':
      value = 5;
      break;
    case 'X':
      value = 10;
      break;
    case 'L':
      value = 50;
      break;
    case 'C':
      value = 100;
      break;
    case 'D':
      value = 500;
      break;
    case 'M':
      value = 500;
      break;
    default:
      return 0;
      break;
    }

    if ()
    {
    }
  }
}