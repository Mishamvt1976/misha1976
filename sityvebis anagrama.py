def is_anagram(str1, str2):
    
    def clean_string(text):
        return sorted([char.lower() for char in text if char.isalpha()])
    
    return clean_string(str1) == clean_string(str2)

# მომხმარებელთან ინტერაქცია
word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")

if is_anagram(word1, word2):
    print("შედეგი: სიტყვები ერთმანეთის ანაგრამაა.")
else:
    print("შედეგი: სიტყვები არ არის ანაგრამა.")
