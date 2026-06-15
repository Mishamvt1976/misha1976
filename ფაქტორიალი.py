# მომხმარებელს შევყავით რიცხვი
num = int(input("შეიყვანეთ რიცხვი: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}-ის ფაქტორიალი არის: {factorial}")
