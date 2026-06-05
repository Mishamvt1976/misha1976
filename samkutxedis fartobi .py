import math

a = int(input("შეიყვანეთ პირველი კათეტის სიგრძე: "))
b = int(input("შეიყვანეთ მეორე კათეტის სიგრძე: "))

if a > 0 and b > 0:
    hypotenuse = math.sqrt(a**2 + b**2)
    area = (a * b) / 2
    
    print(f"ჰიპოთენუზა: {hypotenuse:.2f}")
    print(f"ფართობი: {area:.2f}")
else:
    print("გთხოვთ შეიყვანოთ დადებითი მთელი რიცხვები.")