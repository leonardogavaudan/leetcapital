#include <stdio.h>
#include <stdlib.h>

struct HashItem {
  int key;
  int value;
};

struct HashTable {
  int size;
  int maxSize;
  struct HashItem *items;
};

struct HashTable *createHashTable(int maxSize) {
  struct HashTable *table = malloc(sizeof(struct HashTable));
  table->maxSize = maxSize;
  table->size = 0;

  table->items = malloc(maxSize * sizeof(struct HashItem));

  for (int i = 0; i < maxSize; i++) {
    table->items[i].key = -1;
  }

  return table;
}

int hash(int key, int maxSize) { return (key % maxSize + maxSize) % maxSize; }

int insertInHashMap(struct HashTable *table, int key, int value) {
  if (table->size == table->maxSize) {
    return 0;
  }

  int index = hash(key, table->maxSize);

  while (table->items[index].key != -1) {
    index = (index + 1) % table->maxSize;
  }

  table->items[index].key = key;
  table->items[index].value = value;

  return 1;
}

int freeHashTable(struct HashTable *table) {
  free(table->items);
  free(table);

  return 1;
}

int searchHashTable(struct HashTable *table, int key, int *value) {
  int index = hash(key, table->maxSize);
  int initialIndex = index;

  while (table->items[index].key != -1) {
    if (table->items[index].key == key) {
      *value = table->items[index].value;
      return 1;
    }

    index = (index + 1) % table->maxSize;

    if (index == initialIndex) {
      return 0;
    }
  }

  return 0;
}

int *twoSum(int *nums, int numSize, int target, int *returnSize) {
  struct HashTable *table = createHashTable(numSize * 2);
  int *result = malloc(sizeof(int) * 2);

  for (int i = 0; i < numSize; i++) {
    int complement = target - nums[i];
    int value;

    int searchResult = searchHashTable(table, complement, &value);
    if (searchResult) {
      *result = value;
      *(result + 1) = i;
      *returnSize = 2;
      freeHashTable(table);
      return result;
    }

    insertInHashMap(table, nums[i], i);
  }

  freeHashTable(table);
  *returnSize = 0;
  return NULL;
}

int main() {
  int nums[] = {3, 5, 1, 4, 9};
  int numSize = 5;
  int target = 10;
  int returnSize = 0;

  int *res = twoSum(nums, numSize, target, &returnSize);

  if (res != NULL) {
    for (int i = 0; i < returnSize; i++) {
      printf("Index %d: %d\n", res[i], nums[res[i]]);
    }
    free(res);
  } else {
    printf("No match found\n");
  }

  return 0;
}