import random

alll = input("All: 0 = Random 1 = Assasin 2 = Fighter 3 = Mage 4 = Marksman 5 = Support 6 = Tank 7 = Options: ")
if alll==0:
    print('TOP:' + random.choice(list(open('lol_char.txt'))))
    print('MID:' + random.choice(list(open('lol_char.txt'))))
    print('ADC:' + random.choice(list(open('lol_char.txt'))))
    print('SUP:' + random.choice(list(open('lol_char.txt'))))
    print('JG:' + random.choice(list(open('lol_char.txt'))))
elif alll==1:
    print('TOP:' + random.choice(list(open('Ass.txt'))))
    print('MID:' + random.choice(list(open('Ass.txt'))))
    print('ADC:' + random.choice(list(open('Ass.txt'))))
    print('SUP:' + random.choice(list(open('Ass.txt'))))
    print('JG:' + random.choice(list(open('Ass.txt'))))
elif alll==2:
    print('TOP:' + random.choice(list(open('Fight.txt'))))
    print('MID:' + random.choice(list(open('Fight.txt'))))
    print('ADC:' + random.choice(list(open('Fight.txt'))))
    print('SUP:' + random.choice(list(open('Fight.txt'))))
    print('JG:' + random.choice(list(open('Fight.txt'))))
elif alll==3:
    print('TOP:' + random.choice(list(open('Mage.txt'))))
    print('MID:' + random.choice(list(open('Mage.txt'))))
    print('ADC:' + random.choice(list(open('Mage.txt'))))
    print('SUP:' + random.choice(list(open('Mage.txt'))))
    print('JG:' + random.choice(list(open('Mage.txt'))))
elif alll==4:
    print('TOP:' + random.choice(list(open('Marks.txt'))))
    print('MID:' + random.choice(list(open('Marks.txt'))))
    print('ADC:' + random.choice(list(open('Marks.txt'))))
    print('SUP:' + random.choice(list(open('Marks.txt'))))
    print('JG:' + random.choice(list(open('Marks.txt'))))
elif alll==5:
    print('TOP:' + random.choice(list(open('Sup.txt'))))
    print('MID:' + random.choice(list(open('Sup.txt'))))
    print('ADC:' + random.choice(list(open('Sup.txt'))))
    print('SUP:' + random.choice(list(open('Sup.txt'))))
    print('JG:' + random.choice(list(open('Sup.txt'))))
elif alll==6:
    print('TOP:' + random.choice(list(open('Tank.txt'))))
    print('MID:' + random.choice(list(open('Tank.txt'))))
    print('ADC:' + random.choice(list(open('Tank.txt'))))
    print('SUP:' + random.choice(list(open('Tank.txt'))))
    print('JG:' + random.choice(list(open('Tank.txt'))))
elif alll==7:
    top = input("TOP: 0 = Random 1 = Assasin 2 = Fighter 3 = Mage 4 = Marksman 5 = Support 6 = Tank: ")
    if top==0:
        toop=('TOP:' + random.choice(list(open('lol_char.txt'))))
    elif top==1:
        toop=('TOP:' + random.choice(list(open('Ass.txt'))))
    elif top==2:
        toop=('TOP:' + random.choice(list(open('Fight.txt'))))
    elif top==3:
        toop=('TOP:' + random.choice(list(open('Mage.txt'))))
    elif top==4:
        toop=('TOP:' + random.choice(list(open('Marks.txt'))))
    elif top==5:
        toop=('TOP:' + random.choice(list(open('Sup.txt'))))
    elif top==6:
        toop=('TOP:' + random.choice(list(open('Tank.txt'))))
    mid = input("MID: 0 = Random 1 = Assasin 2 = Fighter 3 = Mage 4 = Marksman 5 = Support 6 = Tank: ")
    if mid==0:
        miid=('MID:' + random.choice(list(open('lol_char.txt'))))
    elif mid==1:
        miid=('MID:' + random.choice(list(open('Ass.txt'))))
    elif mid==2:
        miid=('MID:' + random.choice(list(open('Fight.txt'))))
    elif mid==3:
        miid=('MID:' + random.choice(list(open('Mage.txt'))))
    elif mid==4:
        miid=('MID:' + random.choice(list(open('Marks.txt'))))
    elif mid==5:
        miid=('MID:' + random.choice(list(open('Sup.txt'))))
    elif mid==6:
        miid=('TOP:' + random.choice(list(open('Tank.txt'))))
    adc = input("ADC: 0 = Random 1 = Assasin 2 = Fighter 3 = Mage 4 = Marksman 5 = Support 6 = Tank: ")
    if adc==0:
        adcc=('ADC:' + random.choice(list(open('lol_char.txt'))))
    elif adc==1:
        adcc=('ADC:' + random.choice(list(open('Ass.txt'))))
    elif adc==2:
        adcc=('ADC:' + random.choice(list(open('Fight.txt'))))
    elif adc==3:
        adcc=('ADC:' + random.choice(list(open('Mage.txt'))))
    elif adc==4:
        adcc=('ADC:' + random.choice(list(open('Marks.txt'))))
    elif adc==5:
        adcc=('ADC:' + random.choice(list(open('Sup.txt'))))
    elif adc==6:
        adcc=('ADC:' + random.choice(list(open('Tank.txt'))))
    sup = input("SUP: 0 = Random 1 = Assasin 2 = Fighter 3 = Mage 4 = Marksman 5 = Support 6 = Tank: ")
    if sup==0:
        supp=('SUP:' + random.choice(list(open('lol_char.txt'))))
    elif sup==1:
        supp=('SUP:' + random.choice(list(open('Ass.txt'))))
    elif sup==2:
        supp=('SUP:' + random.choice(list(open('Fight.txt'))))
    elif sup==3:
        supp=('SUP:' + random.choice(list(open('Mage.txt'))))
    elif sup==4:
        supp=('SUP:' + random.choice(list(open('Marks.txt'))))
    elif sup==5:
        supp=('SUP:' + random.choice(list(open('Sup.txt'))))
    elif sup==6:
        supp=('TOP:' + random.choice(list(open('Tank.txt'))))
    jg = input("JG: 0 = Random 1 = Assasin 2 = Fighter 3 = Mage 4 = Marksman 5 = Support 6 = Tank: ")
    if jg==0:
        jgg=('JG:' + random.choice(list(open('lol_char.txt'))))
    elif jg==1:
        jgg=('JG:' + random.choice(list(open('Ass.txt'))))
    elif jg==2:
        jgg=('JG:' + random.choice(list(open('Fight.txt'))))
    elif jg==3:
        jgg=('JG:' + random.choice(list(open('Mage.txt'))))
    elif jg==4:
        jgg=('JG:' + random.choice(list(open('Marks.txt'))))
    elif jg==5:
        jgg=('JG:' + random.choice(list(open('Sup.txt'))))
    elif jg==6:
        jgg=('JG:' + random.choice(list(open('Tank.txt'))))

print toop
print miid
print adcc
print supp
print jgg
	
    


