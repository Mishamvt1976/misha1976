# მომხმარებლისგან წამების შემოტანა
total_seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

# საათების, წუთების და დარჩენილი წამების გამოთვლა მათემატიკური ფორმულებით
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# შედეგის დაბეჭდვა
print(f"{total_seconds} წამი არის {hours} საათი, {minutes} წუთი, {seconds} წამი.")
