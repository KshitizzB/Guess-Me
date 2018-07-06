
from tkinter import *
import random


root = Tk()
root.title("Guess Me!")
root.geometry("700x600")
root.resizable(False, False)
app = Frame(root)
app.grid()
l = Label(app, text="Welcome to GUESS ME!\n")
m = Label(app, text="Computer will generate a random number from 1 to 10. \nYou have to guess the number in maximum THREE chances. \n\nLet's see if you have a good Sixth Sense..\n\n\nClick below to begin !!\n\n")
l.config(font=("Century Gothic", 44))
m.config(font=("Century Gothic", 14))
l.grid()
m.grid()


def start():
    l.destroy()
    m.destroy()
    ex.destroy()
    sb.destroy()
    k = random.randrange(10) + 1
    ll = Label(app, text="Computer has picked the number!(1 - 10)\n\nEnter your guess below..\n\n")
    ll.config(font=("Century Gothic", 23))
    ll.grid(column=1)
    cl = Label(app, text="Chances Left: 3")
    cl.config(font=("Century Gothic", 20))
    cl.grid(column=1)
    t = Entry()
    t.config(font=("Century Gothic", 18))
    t.grid()
    llll = Label(app, text="\n")
    llll.grid()

    def submit():
        if t.get() == str(k):
            ll.destroy()
            t.destroy()
            bt.destroy()
            lllll = Label(app, text="               Congratulations!\n")
            lllll.config(font=("Century Gothic", 25))
            lllll.grid(column=1)
            cl.configure(text="       YOU WON!!")
            cl.config(font=("Century Gothic", 50))
            th4 = Label(app, text="                    Thanks for playing..\n\n                      For more updates please follow\n")
            th4.config(font=("Century Gothic", 20))
            th4.grid(column=1)
            th3 = Label(app, text="          @kshitizz420")
            th3.config(font=("Century Gothic", 30))
            th3.grid(column=1)
        else:
            if cl.cget("text") == "Chances Left: 1":
                ll.destroy()
                t.destroy()
                bt.destroy()
                cl.configure(text="   BETTER LUCK NEXT TIME!!")
                cl.config(font=("Century Gothic", 40))
                th = Label(app, text="  Thanks for playing..\n\n  For more updates please follow\n")
                th.config(font=("Century Gothic", 20))
                th.grid(column=1)
                th2 = Label(app, text="  @kshitizz420")
                th2.config(font=("Century Gothic", 30))
                th2.grid(column=1)
            if cl.cget("text") == "Chances Left: 2":
                cl.configure(text="Chances Left: 1")
            if cl.cget("text") == "Chances Left: 3":
                cl.configure(text="Chances Left: 2")

    bt = Button(app, text="Check!", command=submit)
    bt.config(font=("Century Gothic", 25))
    bt.grid(column=1)
    llll = Label(app, text="\n")
    llll.grid()


sb = Button(app, text="START THE GAME!", command=start)
sb.config(font=("Century Gothic", 25))
sb.grid()
lll = Label(app, text="\n\n")
lll.grid()
ex = Button(app, text="EXIT", command=root.destroy)
ex.config(font=("Century Gothic", 25))
ex.grid()

root.mainloop()

