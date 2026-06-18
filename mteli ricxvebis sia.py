  # ვქმნით 5 ელემენტიან სიას
numbers = [14, 27, 42, 53, 74]

#ჯამის გამოთვლა
total_sum = 0
for num in numbers:
    total_sum += num

#  ელემენტების რაოდენობის განსაზღვრა და საშუალოს გამოთვლა
count = 0
for _ in numbers:
    count += 1

average = total_sum / count

print("ჯამი:", total_sum)
print("საშუალო:", average) 