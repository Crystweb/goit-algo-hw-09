# Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:
# Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві,
# і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад,
# для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати
# найбільш доступні номінали монет.
# Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, але
# використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування
# цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми
# найефективнішим способом. Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}

import time

# Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}

    for coin in coins:
        coin_count[coin] = amount // coin
        amount %= coin

    return coin_count

# Функція динамічного програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Побудова словника з кількістю монет кожного номіналу
    coin_count = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i >= coin and dp[i] == dp[i - coin] + 1:
                coin_count[coin] = coin_count.get(coin, 0) + 1
                i -= coin
                break

    return coin_count

# Порівняння ефективності
# Створення випадкової великої суми для тестування
large_amount = 10**6

start_time = time.time()
greedy_result = find_coins_greedy(large_amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(large_amount)
dp_time = time.time() - start_time

print("Жадібний алгоритм:", greedy_result)
print("Час виконання (жадібний алгоритм):", greedy_time)

print("\nАлгоритм динамічного програмування:", dp_result)
print("Час виконання (алгоритм динамічного програмування):", dp_time)
