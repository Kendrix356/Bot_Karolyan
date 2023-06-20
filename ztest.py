import random
import asyncio

async def print_array(array):
    for row in array:
        print(row)
    print()

async def update_array(array):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        array[row][col] = 1
        await print_array(array)
        await asyncio.sleep(random.randint(3, 10))
        array[row][col] = 0
        await print_array(array)

# Создание двумерного массива 5x5 и заполнение нулями
array = [[0] * 5 for _ in range(5)]

print("Исходный массив:")

# Запуск асинхронной функции в основной программе
asyncio.run(print_array(array))

# Запуск обновления массива
asyncio.run(update_array(array))
