
def calculator():
    try:
        
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        operator = input("შეიყვანეთ არითმეტიკული ოპერატორი (+, -, *, /): ")
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

        if operator == '+':
            result = num1 + num2
            print(f"შედეგი: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"შედეგი: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"შედეგი: {num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("შეცდომა: ნულზე გაყოფა შეუძლებელია!")
            else:
                result = num1 / num2
                print(f"შედეგი: {num1} / {num2} = {result}")
        else:
            print("შეცდომა: არასწორი ოპერატორი! გთხოვთ შეიყვანეთ +, -, * ან /")

    except ValueError:
        print("შეცდომა: გთხოვთ შეიყვანეთ მხოლოდ რიცხვები.")

calculator()
