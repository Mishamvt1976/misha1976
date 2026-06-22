# პირველი დავალება

# def count_and_convert_to_upper(text):
#     # დიდი ასოების დათვლა
#     upper_count = sum(1 for char in text if char.isupper())
    
#     # ტექსტის გადაყვანა მაღალ რეგისტრში
#     upper_text = text.upper()
    
#     return upper_count, upper_text

# # მაგალითი:
# user_input = "Hello woRld"
# count, result = count_and_convert_to_upper(user_input)

# print(f"დიდი ასოების რაოდენობა: {count}")
# print(f"შედეგი: {result}")


# მეორე დავალება

def camel_to_snake(text):
    result = []
    for char in text:
        if char.isupper():
            result.append('_' + char.lower())
        else:
            result.append(char)
    return ''.join(result)
