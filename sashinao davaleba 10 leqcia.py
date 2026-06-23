# პირველი დავალება

# def sum_user_inputs(count=5):
#     total_sum = 0
#     for i in range(count):
#         while True:
#             try:
#                 number = float(input(f"შეიყვანეთ რიცხვი ({i + 1}/{count}): "))
#                 total_sum += number
#                 break
#             except ValueError:
#                 print("გთხოვთ, შეიყვანოთ ვალიდური რიცხვი!")
#     return total_sum
# result = sum_user_inputs()
# print(f"საბოლოო ჯამი: {result}")

# result = sum_user_inputs(3)
# print(f"საბოლოო ჯამი: {result}")

    

# მეორე დავალება

# def classify_numbers(*args):
#     odd_numbers = []
#     even_numbers = []
    
#     for num in args:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
            
#     return odd_numbers, even_numbers

# even, odd = classify_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print("კენტი:", even)
# print("ლუწი:", odd)


# მესამე დავალება

# import re

# def count_words(sentence):
    
#     lower_sentence = sentence.lower()

#     words = re.findall(r'\b\w+\b', lower_sentence)

#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1

#     return word_count

# example = "This is a test. This test is fun."
# print(count_words(example))


# მეოთხე დავალება

# from functools import reduce

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]

# filtered_products = list(filter(lambda x: x["price"] < 100, products))
# print("ფასი 100-ზე ნაკლებია:", filtered_products)

# mapped_products = list(map(lambda x: f"{x['name']}: {x['price']}$", products))
# print("სახელი და ფასი:", mapped_products)

# sorted_products = sorted(products, key=lambda x: x["price"])
# print("დასორტირებული ფასით:", sorted_products)

# total_price = reduce(lambda acc, x: acc + x["price"], products, 0)
# print("ფასების ჯამი:", total_price)


# მეხუთე დავალება

def factorial(n):
    # Base Case (საბაზისო პირობა)
    if n == 0 or n == 1:
        return 1
    # Recursive Case (რეკურსიული ნაწილი)
    else:
        return n * factorial(n - 1)

print(factorial(5))