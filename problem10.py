from util import verifica_se_eh_primo 
limit = 2000000
sum = 0 
for i in range(2, limit):
    if verifica_se_eh_primo(i):
        sum = sum + i

print sum

