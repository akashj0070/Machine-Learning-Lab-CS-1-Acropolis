from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from PIL import Image , ImageTk
chatbot=ChatBot('cis')

conversation = [
    "Good morning",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name",
    "My name is cisco",
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
'''
a=input()
response = chatbot.get_response(a)
print(response)


print("talk to bot")
while True:
  query=input()
  if query=='exit':
    break
  response = chatbot.get_response(query)
  print(response)
'''




def getval():
    con=text.get()
    res=chatbot.get_response(con)
    box.insert(END,"You :"+con)
    box.insert(END,"Cisco :"+ str(res))
    texte.delete(0,END)
    


#a=getval()
tk=Tk()
tk.title("CHATBOT")
tk.geometry("550x650")
tk.minsize(500,600)
tk.configure(background='grey')
'''
get=Label(tk,text="CHATBOT")
get.pack()
'''

img=Image.open("aa.jpg")
imge=ImageTk.PhotoImage(img)
img_label=Label(image=imge)
img_label.pack()


frame=Frame(tk, width=100, height=100,)
sc=Scrollbar(frame)
'''
Main = Canvas(FrameBIG,height = 1200,width =1500,scrollregion=Main.bbox("all"))
scroll = Scrollbar(frame ,orient="vertical", command=Main.yview)
scroll.pack(side="right", fill="y")
Main.pack(side = BOTTOM, anchor = NW,fill="x")
frame.pack(anchor = W, fill = "x")

'''



box=Listbox(frame, width=50, height=20)
sc.pack(side=RIGHT, fill=Y)
box.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()


text=StringVar()
texte=Entry(tk,textvariable=text)
texte.pack(pady=10)
'''

text = Entry(tk, font=("Verdana", 16))
text.pack(pady=10)
'''
btn=Button(tk,text="ASK",command=getval)
btn.pack()

tk.mainloop()
