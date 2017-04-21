from Tkinter import *
import random

root = Tk()
root.title("RANDOM LEAGUE TEAM GENERATOR")

def Button1():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('lol_char.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('lol_char.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('lol_char.txt'))))
 listbox.insert(END, 'SUP: ' + random.choice(list(open('lol_char.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('lol_char.txt'))))
 listbox.insert(END, '')
def Button2():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('Ass.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('Ass.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('Ass.txt'))))
 listbox.insert(END, 'SUP: ' + random.choice(list(open('Ass.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('Ass.txt'))))
 listbox.insert(END, '')
def Button3():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('Mage.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('Mage.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('Mage.txt'))))
 listbox.insert(END, 'SUP: ' + random.choice(list(open('Mage.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('Mage.txt'))))
 listbox.insert(END, '')
def Button4():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'SUP: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, '')
def Button5():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'SUP:' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('Marks.txt'))))
 listbox.insert(END, '')
def Button6():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('Sup.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('Sup.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('Sup.txt'))))
 listbox.insert(END, 'SUP: ' + random.choice(list(open('Sup.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('Sup.txt'))))
 listbox.insert(END, '')
def Button7():
 listbox.insert(END, 'TOP: ' + random.choice(list(open('Tank.txt'))))
 listbox.insert(END, 'MID: ' + random.choice(list(open('Tank.txt'))))
 listbox.insert(END, 'ADC: ' + random.choice(list(open('Tank.txt'))))
 listbox.insert(END, 'SUP: ' + random.choice(list(open('Tank.txt'))))
 listbox.insert(END, 'JG: ' + random.choice(list(open('Tank.txt'))))
 listbox.insert(END, '')

def trng():
 tt.delete(0, END)  
 tt.insert(END, "Random")
def tass():
 tt.delete(0, END)   
 tt.insert(END, "Assasin")
def tfight():
 tt.delete(0, END)   
 tt.insert(END, "Fighter")
def tmag():
 tt.delete(0, END)   
 tt.insert(END, "Mage")
def tmark():
 tt.delete(0, END)   
 tt.insert(END, "Marksman")
def tsup():
 tt.delete(0, END)   
 tt.insert(END, "Support")
def ttank():
 tt.delete(0, END)   
 tt.insert(END, "Tank")

def mrng():
 mt.delete(0, END)  
 mt.insert(END, "Random")
def mass():
 mt.delete(0, END)   
 mt.insert(END, "Assasin")
def mfight():
 mt.delete(0, END)   
 mt.insert(END, "Fighter")
def mmag():
 mt.delete(0, END)   
 mt.insert(END, "Mage")
def mmark():
 mt.delete(0, END)   
 mt.insert(END, "Marksman")
def msup():
 mt.delete(0, END)   
 mt.insert(END, "Support")
def mtank():
 mt.delete(0, END)   
 mt.insert(END, "Tank")

def arng():
 at.delete(0, END)  
 at.insert(END, "Random")
def aass():
 at.delete(0, END)   
 at.insert(END, "Assasin")
def afight():
 at.delete(0, END)   
 at.insert(END, "Fighter")
def amag():
 at.delete(0, END)   
 at.insert(END, "Mage")
def amark():
 at.delete(0, END)   
 at.insert(END, "Marksman")
def asup():
 at.delete(0, END)   
 at.insert(END, "Support")
def atank():
 at.delete(0, END)   
 at.insert(END, "Tank")

def srng():
 st.delete(0, END)  
 st.insert(END, "Random")
def sass():
 st.delete(0, END)   
 st.insert(END, "Assasin")
def sfight():
 st.delete(0, END)   
 st.insert(END, "Fighter")
def smag():
 st.delete(0, END)   
 st.insert(END, "Mage")
def smark():
 st.delete(0, END)   
 st.insert(END, "Marksman")
def ssup():
 st.delete(0, END)   
 st.insert(END, "Support")
def stank():
 st.delete(0, END)   
 st.insert(END, "Tank")

def jrng():
 jt.delete(0, END)  
 jt.insert(END, "Random")
def jass():
 jt.delete(0, END)   
 jt.insert(END, "Assasin")
def jfight():
 jt.delete(0, END)   
 jt.insert(END, "Fighter")
def jmag():
 jt.delete(0, END)   
 jt.insert(END, "Mage")
def jmark():
 jt.delete(0, END)   
 jt.insert(END, "Marksman")
def jsup():
 jt.delete(0, END)   
 jt.insert(END, "Support")
def jtank():
 jt.delete(0, END)   
 jt.insert(END, "Tank")


def done():
    tc = tt.get()
    mc = mt.get()
    ac = at.get()
    sc = st.get()
    jc = jt.get()
     
    if tc=="Random":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('lol_char.txt'))))
    elif tc=="Assasin":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('Ass.txt'))))
    elif tc=="Fighter":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('Sup.txt'))))
    elif tc=="Mage":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('Sup.txt'))))    
    elif tc=="Marksman":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('Sup.txt'))))
    elif tc=="Support":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('Sup.txt'))))
    elif tc=="Tank":
        ttop=listbox.insert(END, 'TOP: ' + random.choice(list(open('Sup.txt'))))

    if mc=="Random":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('lol_char.txt'))))
    elif mc=="Assasin":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('Ass.txt'))))
    elif mc=="Fighter":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('Sup.txt'))))
    elif mc=="Mage":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('Sup.txt'))))    
    elif mc=="Marksman":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('Sup.txt'))))
    elif mc=="Support":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('Sup.txt'))))
    elif mc=="Tank":
        mmid=listbox.insert(END, 'MID: ' + random.choice(list(open('Sup.txt'))))

    if sc=="Random":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('lol_char.txt'))))
    elif sc=="Assasin":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('Ass.txt'))))
    elif sc=="Fighter":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('Sup.txt'))))
    elif sc=="Mage":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('Sup.txt'))))    
    elif sc=="Marksman":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('Sup.txt'))))
    elif sc=="Support":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('Sup.txt'))))
    elif sc=="Tank":
        ssup=listbox.insert(END, 'SUP: ' + random.choice(list(open('Sup.txt'))))
    
    if ac=="Random":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('lol_char.txt'))))
    elif ac=="Assasin":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('Ass.txt'))))
    elif ac=="Fighter":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('Sup.txt'))))
    elif ac=="Mage":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('Sup.txt'))))    
    elif ac=="Marksman":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('Sup.txt'))))
    elif ac=="Support":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('Sup.txt'))))
    elif ac=="Tank":
        aadc=listbox.insert(END, 'ADC: ' + random.choice(list(open('Sup.txt'))))

    if jc=="Random":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('lol_char.txt'))))
    elif jc=="Assasin":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('Ass.txt'))))
    elif jc=="Fighter":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('Sup.txt'))))
    elif jc=="Mage":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('Sup.txt'))))    
    elif jc=="Marksman":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('Sup.txt'))))
    elif jc=="Support":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('Sup.txt'))))
    elif jc=="Tank":
        jjg=listbox.insert(END, 'JG: ' + random.choice(list(open('Sup.txt'))))        

    else:
        ttop
        mmid
        aadc
        ssup
        jjg

 
textframe1 = LabelFrame(root, labelanchor=N, text="ALL LANE", padx=10, pady=5)
textframe2 = LabelFrame(root, labelanchor=N, text="TOP LANE", padx=10, pady=5)
textframe3 = LabelFrame(root, labelanchor=N, text="MID LANE", padx=10, pady=5)
textframe4 = LabelFrame(root, labelanchor=N, text="ADC", padx=10, pady=5)
textframe5 = LabelFrame(root, labelanchor=N, text="SUPPORT", padx=10, pady=5)
textframe6 = LabelFrame(root, labelanchor=N, text="JUNGLE", padx=10, pady=5)
textframe7 = LabelFrame(root, labelanchor=N, text="DONE?", padx=10, pady=5)
listframe = Frame(root)


button1 = Button(textframe1, text="All RNG", command = Button1)
button2 = Button(textframe1, text="All Assasin", command = Button2)
button3 = Button(textframe1, text="All Fighter", command = Button3)
button4 = Button(textframe1, text="All Mage", command = Button4)
button5 = Button(textframe1, text="All Marksman", command = Button5)
button6 = Button(textframe1, text="All Support", command = Button6)
button7 = Button(textframe1, text="All Tank", command = Button7)

t1 = Button(textframe2, text="TOP RNG", command = trng)
t2 = Button(textframe2, text="TOP Assasin", command = tass)
t3 = Button(textframe2, text="TOP Fighter", command = tfight)
t4 = Button(textframe2, text="TOP Mage", command = tmag)
t5 = Button(textframe2, text="TOP Marksman", command = tmark)
t6 = Button(textframe2, text="TOP Support", command = tsup)
t7 = Button(textframe2, text="TOP Tank", command = ttank)

m1 = Button(textframe3, text="MID RNG", command = mrng)
m2 = Button(textframe3, text="MID Assasin", command = mass)
m3 = Button(textframe3, text="MID Fighter", command = mfight)
m4 = Button(textframe3, text="MID Mage", command = mmag)
m5 = Button(textframe3, text="MID Marksman", command = mmark)
m6 = Button(textframe3, text="MID Support", command = msup)
m7 = Button(textframe3, text="MID Tank", command = mtank)

a1 = Button(textframe4, text="ADC RNG", command = arng)
a2 = Button(textframe4, text="ADC Assasin", command = aass)
a3 = Button(textframe4, text="ADC Fighter", command = afight)
a4 = Button(textframe4, text="ADC Mage", command = amag)
a5 = Button(textframe4, text="ADC Marksman", command = amark)
a6 = Button(textframe4, text="ADC Support", command = asup)
a7 = Button(textframe4, text="ADC Tank", command = atank)

s1 = Button(textframe5, text="SUP RNG", command = srng)
s2 = Button(textframe5, text="SUP Assasin", command = sass)
s3 = Button(textframe5, text="SUP Fighter", command = sfight)
s4 = Button(textframe5, text="SUP Mage", command = smag)
s5 = Button(textframe5, text="SUP Marksman", command = smark)
s6 = Button(textframe5, text="SUP Support", command = ssup)
s7 = Button(textframe5, text="SUP Tank", command = stank)

j1 = Button(textframe6, text="JG RNG", command = jrng)
j2 = Button(textframe6, text="JG Assasin", command = jass)
j3 = Button(textframe6, text="JG Fighter", command = jfight)
j4 = Button(textframe6, text="JG Mage", command = jmag)
j5 = Button(textframe6, text="JG Marksman", command = jmark)
j6 = Button(textframe6, text="JG Support", command = jsup)
j7 = Button(textframe6, text="JG Tank", command = jtank)

done = Button(textframe7, text="I AM DONE!!!", command = done)

scrollbar = Scrollbar(listframe, orient=VERTICAL)
listbox = Listbox(listframe, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)
tt = Entry(textframe2)
mt = Entry(textframe3)
at = Entry(textframe4)
st = Entry(textframe5)
jt = Entry(textframe6)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)


t1.pack(side=TOP)
t2.pack(side=TOP)
t3.pack(side=TOP)
t4.pack(side=TOP)
t5.pack(side=TOP)
t6.pack(side=TOP)
t7.pack(side=TOP)
tt.pack(side=BOTTOM)

m1.pack(side=TOP)
m2.pack(side=TOP)
m3.pack(side=TOP)
m4.pack(side=TOP)
m5.pack(side=TOP)
m6.pack(side=TOP)
m7.pack(side=TOP)
mt.pack(side=BOTTOM)

a1.pack(side=TOP)
a2.pack(side=TOP)
a3.pack(side=TOP)
a4.pack(side=TOP)
a5.pack(side=TOP)
a6.pack(side=TOP)
a7.pack(side=TOP)
at.pack(side=BOTTOM)

s1.pack(side=TOP)
s2.pack(side=TOP)
s3.pack(side=TOP)
s4.pack(side=TOP)
s5.pack(side=TOP)
s6.pack(side=TOP)
s7.pack(side=TOP)
st.pack(side=BOTTOM)

j1.pack(side=TOP)
j2.pack(side=TOP)
j3.pack(side=TOP)
j4.pack(side=TOP)
j5.pack(side=TOP)
j6.pack(side=TOP)
j7.pack(side=TOP)
jt.pack(side=BOTTOM)

done.pack(side=RIGHT)

listbox.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)

textframe1.pack(side=TOP, fill=X)
textframe2.pack(side=LEFT, fill=Y, pady=5, padx=5)
textframe3.pack(side=LEFT, fill=Y, pady=5, padx=5)
textframe4.pack(side=LEFT, fill=Y, pady=5, padx=5)
textframe5.pack(side=LEFT, fill=Y, pady=5, padx=5)
textframe6.pack(side=LEFT, fill=Y, pady=5, padx=5)
textframe7.pack(side=BOTTOM, fill=X, pady=5, padx=5)
listframe.pack(fill=BOTH, expand=1)
root.geometry("1200x600")

root.mainloop()
    


