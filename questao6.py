positivos = [float(input("digite os valores: ")) for _6 in range (6)]

totalpositivos = 0 
somadosposit = 0 

for r in positivos:
    if r > 0:
        totalpositivos += 1
        somadosposit += r

print('{} valores positivos' .format(totalpositivos))
print('{:.if}'.format(somadosposit/totalpositivos))