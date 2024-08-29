def is_prime(num):
    if num / num == 1 and num / 1 == num:
        return True
    else:
        return False


print(is_prime(75))
print(is_prime(73))
# 75 should be False, 73 should be True