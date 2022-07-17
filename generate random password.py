from tkinter import *
import random
root=Tk()
root.geometry("400x400")
root.title("generate a strong password")


label1=Label(root,text="")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)

label2=Label(root,text="")
label2.place(relx=0.5, rely=0.7, anchor=CENTER)

inputbox=Entry(root,)
inputbox.place(relx=0.5, rely=0.3, anchor=CENTER)


arrays3d = [[[1,2,3,4,5,6],["piano","scissor","xyz"],["a","b","c","d","e","f","g","h","i","s","j"]]]


def generatepass():
    
    randomnum1 = random.randint(0,5)
    randomnum2 = random.randint(0,2)
    randomnum3 = random.randint(0,10)
    letter1=str(arrays3d[0][0][randomnum1])
    letter2=(arrays3d[0][1][randomnum2])
    letter3=(arrays3d[0][2][randomnum3])
    label1["text"]=letter1+letter2+letter3
   
    guessPASSWORD=inputbox.get()
    generatedpassword =letter1+letter2+letter3
    if(guessPASSWORD==generatedpassword):
        label2["text"]="guessPASSWORD is correct!"
    else:
        label2["text"]="guessPASSWORD is wrong!"
        
button1=Button(root, text="generate password", command=generatepass)
button1.place(relx= 0.5, rely=0.8, anchor= CENTER)






root.mainloop()