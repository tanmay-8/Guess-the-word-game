import random
from tkinter import *
from hints import hints

# start
master = Tk()
master.geometry("1000x500")
master.configure(bg="#b8dff5")


# getting nextword
def init():
    global word,hints,hint,nog,worddisplay,text,text2
    global text4,submit,e1

    #resetting number of guesses 
    nog=0

    # selecting word and hint
    word = random.choice(list(hints.keys()))
    try:
        hint = hints[word]
    except:
        hint = "No hints"
    hints.pop(word)
    word = word.upper()

    # Jumbling letters in word
    list1 = list(word)
    letters = random.sample(list1, len(list1))
    while letters == list1:
        letters = random.sample(list1, len(list1))
    worddisplay = " ".join(letters)
    
    # Resetting labels and input fields
    nexti.configure(state=DISABLED)
    text4.configure(text="")
    text.configure(text=f"Letters are:{worddisplay}")
    text2.configure(text=f"Hint:{hint}")
    submit.configure(state=NORMAL)
    e1.delete(0,END)


def gettext():
    global nog
    global points

    # getting guessed word
    guess = (e1.get()).upper()
    while(guess.find(" ")!=-1):
        guess = guess.replace(" ","")

    if(nog<5):

        # if guessed correct
        if(guess.upper()==word):
            nog = 0 
            points += 1
            text4.configure(text="You Guessed Correct Word")
            text5.configure(text=f"POINTS:{points}") 
            nexti.configure(state=NORMAL)
            submit.configure(state=DISABLED)
            # if guessed all words
            if(points == 2464):
                text5.configure(text="YOUR CHAMPION")
                nexti.configure(state=DISABLED)
                submit.configure(state=DISABLED)
        else:
            nog += 1 
            text4.configure(text=f"You Guessed Wrong Word.Guesses Remaining:{5-nog}")         
    else:
        text4.configure(text = f"You Lost.Your Word is : {word}" )
        submit.configure(state=DISABLED)
        nexti.configure(state=NORMAL)
        nog=0

#show word       
def showw():
    global nog
    text4.configure(text = f"You Lost.Your Word is : {word}" )
    submit.configure(state=DISABLED)
    nexti.configure(state=NORMAL)
    nog=0



# quit  
def end():
    quit()

#main logic
points = 0

#getting first word and hint
word = random.choice(list(hints.keys()))
try:
    hint = hints[word]
except:
    hint = "No hint"
hints.pop(word)
word = word.upper()

# Jumbling letters in word
list1 = list(word)
letters = random.sample(list1, len(list1))
while letters == list1:
    letters = random.sample(list1, len(list1))
worddisplay = " ".join(letters)


nog = 0

#Word label 
text = Label()
text.place(x=0,y=0,width=1000,height=100)
text.configure(font=("",20),bg="#fabbc9",text=f"Letters are:{worddisplay}")

#hint label
text2 = Label(wraplength=1000)
text2.place(x=0,y=100,width=1000,height=120)
text2.configure(font=("",15),bg="#c1f5c4",text=f"Hint:{hint}")

# Jumbled letters label
text3 = Label(master ,text=("Try To Guess A Word:"))
text3.configure(font=("",20),bg="#eaa5f2")
text3.place(x=0,y=220,height=60)

#for guessing word
e1 = Entry(master=master)
e1.configure(font=("",20))
e1.place(x=(text3.winfo_reqwidth()),y=220,width=(1000-text3.winfo_reqwidth()),height=60)

# To show word on aksed
text4 = Label(master,text=(""))
text4.configure(font=("",15),background="#f5d6a9")
text4.place(y=340,x=0,width=1000,height=50)

#Points label 
text5 = Label(master,text=(f"POINTS : {points}"))
text5.configure(font=("",30),background="#eaa5f2")
text5.place(y=390,width=1000,x=0)

#submit button 
submit = Button(master=master, text="OK")
submit.configure(font=("",15),background="#74fc86",command=gettext)
submit.place(x=400,y=290,width=100)

#show word button
show = Button(master=master, text="SHOW")
show.configure(font=("",15),background="#74fc86",command=showw)
show.place(x=500,y=290,width=100)

#quit
quiti = Button(master=master, text="quit")
quiti.configure(font=("",15),background="red",command=end)
quiti.place(x=400,y=450,width=100)

#get next word
nexti = Button(master=master, text="next")
nexti.configure(font=("",15),background="#74fc86",command=init,state=DISABLED)
nexti.place(x=500,y=450,width=100)
master.mainloop()    


  





        

