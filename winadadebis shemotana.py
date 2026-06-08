
text = input("შეიყვანეთ წინადადება: ")

old_text = input("შეიყვანეთ სიტყვა, რომლის ჩანაცვლებაც გსურთ: ")

new_text = input("შეიყვანეთ ახალი სიტყვა: ")

updated_text = text.replace(old_text, new_text)

print("\nგანახლებული წინადადება:")
print(updated_text)
