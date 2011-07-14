from math import sqrt

def ehPrimo(num):
    import re
    return re.match(r'^1?$|^(11+?)\1+$', '1' * num) == None
    
def verifica_se_eh_primo(num):
    """ metodo para validar se um numero eh primo """
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num == 5:
        return True
    if num == 7:
        return True

    if num%2 == 0:
        return False
    if num%3 == 0:
        return False
    if num%5 == 0:
        return False
    if num%7 == 0:
        return False
    sqrt_num = int(num**0.5) + 1
    for i in range(11,sqrt_num):
        if  num % i == 0:
            return False
    return True


