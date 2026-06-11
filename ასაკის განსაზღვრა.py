try:

    age_input = input("გთხოვთ, შეიყვანოთ თქვენი ასაკი: ")

    age_input = input

    age = int (age_input)

    if age < 0:

       raise ValueError ("ასაკი არ შეიძლება იყოს უარყოფითი")

    if age < 18:

         print("თქვენ ხართ არასრულწლოვანი.")
    else:
         print("თქვენ ხართ სრულწლოვანი.")
   
except ValueError as e:
   
    if not age_input.isdigit():
            print("შეიყვანეთ მხოლოდ რიცხვი!")
    else:
        
        print(f"შეცდომა: {e}")