import random
kotak = []

rdm = random.randint(2,4)
for i in range(rdm):
    a = "sin","cos","cot","tan"
    ardm = random.choice(a)
    b ="30","45","60","90"
    brdm = random.choice(b)
    opr = "+","-","*"
    ordm = random.choice(opr)
    
    latex = "\\"+ardm+" \SI{"+brdm+"}{\degree}"+ordm
    kotak.append(latex)


for i in kotak:
    print(i)
    
