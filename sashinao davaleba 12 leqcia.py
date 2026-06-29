# def transaction_decorator(func):
#     def wrapper(balance, amount):
#         commission = 1
#         total_needed = amount + commission
#
#         if balance < total_needed:
#             return "შეცდომა: ანგარიშზე არ არის საკმარისი თანხა (გადასახდელი + 1 ლარი საკომისიო)."
#
#         # ვაბრუნებთ ორიგინალი ფუნქციის შედეგს, სადაც ბალანსს აკლდება თანხა და საკომისიო
#         return func(balance - total_needed, amount)
#
#     return wrapper
#
#
# @transaction_decorator
# def process_transaction(balance, amount):
#     return f"ტრანზაქცია წარმატებით შესრულდა! თქვენი ახალი ბალანსია: {balance} ლარი."
#
#
# # ტესტირება 1: როცა თანხა საკმარისია
# print(process_transaction(balance=20, amount=10))
#
# # ტესტირება 2: როცა თანხა არ არის საკმარისი
# print(process_transaction(balance=10, amount=10))


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"ფუნქცია '{func.__name__}' გამოიძახეს {wrapper.calls}-ჯერ")
        return func(*args, **kwargs)

    wrapper.calls = 0  # საწყისი მნიშვნელობის მინიჭება
    return wrapper
@count_calls
def say_hello(name):
    return f"გამარჯობა, {name}!"

# ფუნქციის გამოძახება რამდენჯერმე
say_hello("გიორგი")
say_hello("ანი")
say_hello("ლუკა")


