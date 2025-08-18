# Жадный алгоритм выбирает наибольшую возможную монету на каждом шаге
# (работает не для всех систем монет!).

def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1