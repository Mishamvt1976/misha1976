import random

original_list = [random.randint(-50, 50) for _ in range(20)]

even_list = [num for num in original_list if num % 2 == 0]

print("პირვანდელი სია:", original_list)

print("ლუწი რიცხვების სია:", even_list)