# def max_profit(prices: list[int]) -> int:
#     largest = 0
#     for i in range(len(prices) - 1):
#         for j in range(i + 1, len(prices)):
#             largest = max(largest, prices[j] - prices[i])
#
#     return largest
import sys


def max_profit(prices: list[int]) -> int:
    min_price = sys.maxsize
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
