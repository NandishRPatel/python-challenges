def special_number(number):
    numbers = [int(n) < 6 for n in str(number)]
    if all(numbers):return "Special!!"
    else: return "NOT!!"