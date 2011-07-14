from util import verifica_se_eh_primo

num = 2
primos = [2] 
while len(primos) < 10002:
    if verifica_se_eh_primo(num):
        print num,"---",len(primos)
        primos.append(num)
    num = num + 1

print "O numero esperado eh %d" % primos[-1]
