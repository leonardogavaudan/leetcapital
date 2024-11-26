char *reverseWords(char *s) {
  char *head = s;

  while (*s == ' ' && *s != '\0') {
    s++;
  }
  if (*s == '\0') {
    return s;
  }

  head = s;
  char *available = ++s;
  if (*s == '\0') {
    return head;
  }

  while (*s != '\0') {
    if (*s != ' ' || *(s - 1) != ' ') {
      *available = *s;
      available++;
    }
    s++;
  }

  *available = '\0';
  if (*(available - 1) == ' ') {
    *(available - 1) = '\0';
    available--;
  }

  char *left = head;
  char *right = available - 1;
  while (left < right) {
    char temp = *left;
    *left = *right;
    *right = temp;
    left++;
    right--;
  }

  char *p = head;
  while (*p != '\0') {
    left = p;
    while (*p != '\0' && *p != ' ') {
      p++;
    }
    right = p - 1;

    while (left < right) {
      char temp = *left;
      *left = *right;
      *right = temp;
      left++;
      right--;
    }

    if (*p != '\0') {
      p++;
    }
  }

  return head;
}
