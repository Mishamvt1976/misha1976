frozenset = frozenset({})
from faker import Faker
from typing import Dict, List

# ვასხამთ ფეიკერს, რომლის მეშვეობითაც დავაგენერირებთ სახელებსა და გვარებს
fake = Faker()


def generate_student(student_id: int) -> Dict:
    """აგენერირებს ერთი სტუდენტის მონაცემებს გადაცემული ID-ის მიხედვით."""
    return {
        "ID": student_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": fake.random_int(min=18, max=80)
    }

def generate_students(count: int) -> List[Dict]:
    """აგენერირებს სტუდენტების სიას მითითებული რაოდენობით."""
    # ვიყენებთ List Comprehension-ს, სადაც ID იწყება 1-დან და ავტომატურად იზრდება
    return [generate_student(i) for i in range(1, count + 1)]

#  5 სტუდენტის გენერირება:
students_list = generate_students(5)

for student in students_list:
    print(student)
