
def is_prime(num):
    prime_flag = 0
    for i in range(2, (num//2)+1):
        if num % i == 0:
            prime_flag += 1
    if prime_flag >= 1:
        return False
    else:
        return True


print(is_prime(4))
print(is_prime(73))
print(is_prime(75))
# 75 should be False, 73 should be True
