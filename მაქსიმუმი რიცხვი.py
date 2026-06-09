# შევიტანოთ 3 რიცხვი
num1 = (input("შეიყვანეთ პირველი რიცხვი: "))
num2 = (input("შეიყვანეთ მეორე რიცხვი: "))
num3 = (input("შეიყვანეთ მესამე რიცხვი: "))

# ვამოწმებთ, რომ რიცხვები არ უდრიდეს ერთმანეთს
if num1 == num2 or num1 == num3 or num2 == num3:
    print("შეიყვანეთ განსხვავებული რიცხვები!")
else:
    # ვპოულობთ ყველაზე დიდ რიცხვს max ფუნქციის გარეშე
    if num1 > num2 and num1 > num3:
        largenumber = num1
    elif num2 > num1 and num2 > num3:
        largenumber = num2
    else:
        largenumber = num3
        
    print(f"ყველაზე დიდი რიცხვი არის: {largenumber}")
