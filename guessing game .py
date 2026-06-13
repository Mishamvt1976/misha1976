import random

def play_game():
    secret_number = random.randint(1, 100)
    lives = 5
    
    print("თამაში დაიწყო! გამოიცანით რიცხვი 1-დან 100-მდე.")
    print("თქვენ გაქვთ 5 სიცოცხლე.")

    while lives > 0:
        try:
            guess = int(input("\nშეიყვანეთ თქვენი ვარაუდი: "))
        except ValueError:
            print("გთხოვთ შეიყვანოთ მხოლოდ მთელი რიცხვი.")
            continue

        if guess == secret_number:
            print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი ({secret_number}) და მოიგეთ!")
            break
        elif guess > secret_number:
            lives -= 1
            print(f"არასწორია. საიდუმლო რიცხვი **ნაკლებია** თქვენს მიერ შეყვანილ რიცხვზე.")
        else:
            lives -= 1
            print(f"არასწორია. საიდუმლო რიცხვი **მეტია** თქვენს მიერ შეყვანილ რიცხვზე.")
        
        if lives > 0:
            print(f"დარჩენილი სიცოცხლეების რაოდენობა: {lives}")
        else:
            print(f"\nსამწუხაროდ, თქვენ ამოწურეთ ყველა სიცოცხლე. თამაში დასრულდა. საიდუმლო რიცხვი იყო: {secret_number}")

play_game()
