#include <stdio.h>

int maxProfit(int *prices, int pricesSize) {
  if (pricesSize == 1) {
    return 0;
  }

  int maximumProfit = 0;
  int lowest_price = prices[0];

  for (int i = 1; i < pricesSize; i++) {
    if (prices[i] < lowest_price) {
      lowest_price = prices[i];
      continue;
    }

    int currentProfit = prices[i] - lowest_price;
    if (currentProfit > maximumProfit) {
      maximumProfit = currentProfit;
    }
  }

  return maximumProfit;
}

int main() {
  int pricesSize = 10;
  int prices[10] = {5, 3, 8, 3, 7, 2, 9, 4, 10};
  int maximumProfit = maxProfit(prices, pricesSize);

  printf("maximumProfit is: %d", maximumProfit);
}
