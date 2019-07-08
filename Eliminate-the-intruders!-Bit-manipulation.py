def eliminate_set_bits(number):
    return 2 ** number.count("1") - 1

print(eliminate_set_bits("1000000"))