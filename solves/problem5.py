number = 20
while True:
    is_him = True
    
    for div in range(1,21):
        is_him = is_him and (number%div) == 0
    
    if is_him:
        break

    number+=20

print(number)
