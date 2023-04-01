import random
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('700x800')
root.config(bg='#000000')

paper = ImageTk.PhotoImage(Image.open("C:/Users/Admin/Pictures/paper-500.jpg").resize((350,350)))
rock = ImageTk.PhotoImage(Image.open("C:/Users/Admin/Pictures/rock.jpg").resize((320,320)))
scissors = ImageTk.PhotoImage(Image.open("C:/Users/Admin/Pictures/-scissors-500.jpg").resize((300,300)))

possible_actions = [rock, paper, scissors]

u = 0 #user score
c = 0 #computer score

def f_computer_action(action):
    y = 0
    x = 0
    if action==paper:
        y = 70
        x = 30
    elif action==rock:
        y = 70
        x = 70
    else:
        y = 100
        x = 60
    computer_action = Label(root,image=action,borderwidth=0)
    computer_action.place(x=x,y=y)
    return action 

def f_paper():
    global u,c,user_action

    user_action = Label(root,image=paper,borderwidth=0)
    user_action.place(x=320,y=70)
    action = f_computer_action(random.choice(possible_actions))
    
    if action == paper:
        massage.set(f"Both selected paper. It's a tie!")
    elif action == rock:
        massage.set("Paper covers rock! You win!")
        u +=1
    else:
        massage.set("Scissors cuts paper! You lose.")
        c +=1
    user_score.set(u)
    computer_score.set(c)

def f_scissors():
    global u,c,user_action

    user_action = Label(root,image=scissors,borderwidth=0)
    user_action.place(x=340,y=100)
    action = f_computer_action(random.choice(possible_actions))
    
    if action == scissors:
        massage.set(f"Both selected scissors. It's a tie!")
    elif action == paper:
        massage.set("Scissors cuts paper! You win!")
        u+=1
    else:
        massage.set("Rock smashes scissors! You lose.")
        c+=1
    user_score.set(u)
    computer_score.set(c)

def f_rock():
    global u,c,user_action

    user_action = Label(root,image=rock,borderwidth=0)
    user_action.place(x=330,y=70)
    action = f_computer_action(random.choice(possible_actions))
    
    if action==rock:
        massage.set(f"Both selected rock. It's a tie!") 
    elif action == scissors:
        massage.set("Rock smashes scissors! You win!")
        u+=1
    else:
        massage.set("Paper covers rock! You lose.")
        c+=1
    user_score.set(u)
    computer_score.set(c)    

def restart():
    global u, c

    u = 0
    c = 0
    user_score.set(u)
    computer_score.set(c)  
    Frame(root,bg="#000000",width=665,height=282).place(x=0,y=100)
    massage.set(" ")

massage = StringVar()
user_score = StringVar()
computer_score = StringVar()

Frame(root,bg="#FFFFFF",width=567,height=185).place(x=65,y=550)
Frame(root,bg="#000000",width=565,height=182).place(x=66,y=552)

Label(root,textvariable=massage,font=('Times New Romer',25),bg='#000000',fg='#41b2f0').place(x=70,y=570)

Label(root,text='Your score:',font=('Times New Romer',20),bg='#000000',fg='#e34fc5').place(x=70,y=630)
Label(root,textvariable=user_score,font=('Times New Romer',20),bg='#000000',fg='#e34fc5').place(x=300,y=630)    
Label(root,text='Computer score:',font=('Times New Romer',20),bg='#000000',fg='#e6bc32').place(x=70,y=680)
Label(root,textvariable=computer_score,font=('Times New Romer',20),bg='#000000',fg='#e6bc32').place(x=300,y=680)    

Label(root,text='ROCK',font=('Times New Romer',30),bg='black',fg='#e34fc5').place(x=110,y=30)
Label(root,text='PAPER',font=('Times New Romer',30),bg='black',fg='#41b2f0').place(x=240,y=30)
Label(root,text='SCISSORS',font=('Times New Romer',30),bg='black',fg='#e6bc32').place(x=390,y=30)

Button(root,text='rock',font=('Times New Romer',20),width=10,height=2,bg='#e34fc5',fg='black',borderwidth=0,command=f_rock).place(x=65,y=440)
Button(root,text='paper',font=('Times New Romer',20),width=10,height=2,bg='#41b2f0',fg='black',borderwidth=0,command=f_paper).place(x=265,y=440)
Button(root,text='scissors',font=('Times New Romer',20),width=10,height=2,bg='#e6bc32',fg='black',borderwidth=0,command=f_scissors).place(x=465,y=440)
Button(root,text='restart',font=('Times New Romer',20),width=9,height=1,bg='#ffffff',fg='black',borderwidth=0,command=restart).place(x=445,y=640)

mainloop()