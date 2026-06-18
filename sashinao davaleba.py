
# პირველი დავალება
# დაწერეთ პროგრამა, რომელიც შექმნის დიქტს, რომელშიც key-ები იქნება 1-დან 10-ის ჩათვლით რიცხვები, ხოლო value-ები key-ს შესაბამისი
# კვადრატები


# squares_dict = {x: x**2 for x in range(1, 11)}

# print(squares_dict)


#მეორე დავალება
# ა. დაბეჭდეთ ყველა პროდუქტის დასახელება
# ბ. გამოითვალეთ ყველა პროდუქტის ღირებულების ჯამი(ანუ პროდუქტის ფასი უნდა გაამრავლოთ რაოდენობაზე და დააჯამოთ)


# 2. მოცემულია პროდუქტების ლისტი:

products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]
print("პროდუქტების დასახელებები:")
for product in products:
    for name in product.keys():
        print(name)
print(products)
total_sum = 0
for product in products:
    for info in product.values():
        total_sum += info["price"] * info["quantity"]

print(f"\nყველა პროდუქტის ღირებულების ჯამი: {total_sum}")


 
# მესამე დავალება:
# დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი


# fruits_count = {}

# while True:
#     fruit = input("შეიყვანეთ ხილის სახელი (დასასრულებლად ჩაწერეთ 'stop'): ").strip().lower()
    
#     if fruit == 'stop':
#         break
        
#     if fruit == '':
#         continue
        
#     fruits_count[fruit] = fruits_count.get(fruit, 0) + 1

# print(fruits_count)
