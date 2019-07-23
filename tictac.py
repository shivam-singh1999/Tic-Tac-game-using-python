from tkinter import *
from tkinter import messagebox
game = Tk()
game.title("Tic Tac Toe")
bclick = True

def tictac(button):
    global bclick
    if button['text']=='' and bclick==True:
        button['text']="X"

        bclick = False
    if button['text'] == '' and bclick == False:
        button['text'] = "O"
        bclick = True

    #FOR X WINNER
    if (btn1['text']=="X" and btn2['text']=="X" and btn3['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()

    if (btn4['text']=="X" and btn5['text']=="X" and btn6['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()

    if (btn7['text']=="X" and btn8['text']=="X" and btn9['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()
    if (btn1['text']=="X" and btn4['text']=="X" and btn7['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()
    if (btn2['text']=="X" and btn5['text']=="X" and btn8['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()
    if (btn3['text']=="X" and btn6['text']=="X" and btn9['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()
    if (btn1['text']=="X" and btn5['text']=="X" and btn9['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()
    if (btn3['text']=="X" and btn5['text']=="X" and btn7['text']=="X"):
        messagebox.showinfo("message","X is winner")
        exit()


    #FOR O WINNWER

    if (btn1['text'] == "O" and btn2['text'] == "O" and btn3['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()

    if (btn4['text'] == "O" and btn5['text'] == "O" and btn6['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()

    if (btn7['text'] == "O" and btn8['text'] == "O" and btn9['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()
    if (btn1['text'] == "O" and btn4['text'] == "O" and btn7['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()
    if (btn2['text'] == "O" and btn5['text'] == "O" and btn8['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()
    if (btn3['text'] == "O" and btn6['text'] == "O" and btn9['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()
    if (btn1['text'] == "O" and btn5['text'] == "O" and btn9['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()
    if (btn3['text'] == "O" and btn5['text'] == "O" and btn7['text'] == "O"):
        messagebox.showinfo("message","O is winner")
        exit()




btn1 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn1))
btn1.grid(row=0,column=0,sticky=S+N+W+E)

btn2 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn2))
btn2.grid(row=0,column=1,sticky=S+N+W+E)

btn3 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn3))
btn3.grid(row=0,column=2,sticky=S+N+W+E)

btn4 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn4))
btn4.grid(row=1,column=0,sticky=S+N+W+E)

btn5 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn5))
btn5.grid(row=1,column=1,sticky=S+N+W+E)

btn6 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn6))
btn6.grid(row=1,column=2,sticky=S+N+W+E)

btn7 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn7))
btn7.grid(row=2,column=0,sticky=S+N+W+E)

btn8 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn8))
btn8.grid(row=2,column=1,sticky=S+N+W+E)

btn9 = Button(game,text='',font=('Arial 20 bold'),height=4,width=8,command=lambda :tictac(btn9))
btn9.grid(row=2,column=2,sticky=S+N+W+E)

game.mainloop()