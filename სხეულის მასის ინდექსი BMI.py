# მომხმარებელს ვთხოვთ შეიყვანოს წონა და სიმაღლე
weight = float(input("შეიყვანეთ წონა (კგ): "))
height = float(input("შეიყვანეთ სიმაღლე (მ): "))

# ვიანგარიშებთ BMI-ს ფორმულით: წონა / (სიმაღლე)^2
bmi = weight / (height ** 2)

# ვბეჭდავთ მიღებულ შედეგს
print(f"თქვენი BMI არის: {bmi:.2f}")

# ვამოწმებთ პირობებს და გამოგვაქვს შესაბამისი შეტყობინება
if bmi < 19:
    print("Underweight")
elif 19 <= bmi <= 25:
    print("Normalweight")
else:
    print("Overweight")
               