
data_list = {
    ('Kelly', 'Simpson'): 26,
    ('Erika', 'Stephens'): 24,
    ('Cheryl', 'Dunn'): 30,
    ('Amy', 'Larsen'): 49,
    ('Christine', 'Gordon'): 23,
    ('Monica', 'Huff'): 38,
    ('David', 'Nixon'): 36,
    ('Cindy', 'Escobar'): 41,
    ('Cindy', 'White'): 33, 
    ('Joel', 'Hall'): 43,
    ('Steven', 'Winters'): 28,
    ('Alex', 'Cole'): 68,
    ('Alex', 'Smith'): 32,
    ('Alex', 'White'): 42,
    ('Brittany', 'Thompson'): 18,
    ('Ernest', 'Young'): 43,
    ('Traci', 'Wells'): 38,
    ('Andrew', 'Flores'): 61,
    ('Christopher', 'Lewis'): 29,
    ('Kevin', 'Willis'): 57,
    ('Kayla', 'Lucas'): 28,
    ('Michelle', 'Rush'): 43,
    ('Thomas', 'Mason'): 37
}

while True:
    # მომხმარებელს ვეკითხებით სახელს
    name = input("შეიყვანეთ სახელი (ან 'stop' გასაჩერებლად): ").strip()
    
    # ციკლის გაჩერება
    if name.lower() == "stop":
        print("პროგრამა გაჩერდა.")
        break
        
    # ვამოწმებთ, არის თუ არა სახელი სიაში (ვამოწმებთ თითოეული ჩანაწერის პირველ ელემენტს)
    if name not in [key[0] for key in data_list.keys()]:
        print("სახელი არ არის მოცემული სიაში.")
        continue  # ვუბრუნებთ ციკლის დასაწყისს (გვარს აღარ ვეკითხებით)
        
    # თუ სახელი მოიძებნა, ვეკითხებით გვარს
    surname = input("შეიყვანეთ გვარი: ").strip()
    
    # ვამოწმებთ, არის თუ არა სახელი და გვარი ერთად სიაში
    full_name = (name, surname)
    if full_name not in data_list:
        print("გვარი არ არის მოცემული სიაში.")
        continue  # ვუბრუნებთ ციკლის დასაწყისს
        
    # თუ ორივე მოიძებნა, ვბეჭდავთ ასაკს
    age = data_list[full_name]
    print(f"ასაკი: {age}")
