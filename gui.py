from tkinter import *
import trivia
import html
import threading
import random

root = Tk()
root.geometry("1366x768")
root.iconbitmap("icon.ico")
root.title("Trivia Party!")
root.config(bg="#4dc4ff")
root.attributes("-fullscreen", True)

logo = PhotoImage(file="logo.png")
# main screen
frame = Frame(root, bg="#4dc4ff")

# about screen
about = Frame(root)

start_frame_container = Frame(root, bg="#4dc4ff")
start_frame_container.pack(expand=YES, fill=BOTH)

questions_asked = 0
answered_correctly = 0

def clear_about_screen():
    about.pack_forget()
    start_frame_container.pack()


Label(about, font=("Arial", 15), text="Created by Jacob Fabb (2020), \n Github repo: ").pack()
return_button = Button(about, text="return", command=clear_about_screen)


def about_screen():
    start_frame_container.pack_forget()
    about.pack(expand=YES, fill=BOTH)
    about.tkraise(start_frame_container)
    return_button.pack()


def start_game():
    frame.pack(fill=BOTH, expand=YES)
    start_frame_container.pack_forget()

# Homescreen Buttons: play, about and exit
Label(start_frame_container, bg="#4dc4ff", image=logo).pack()
Button(start_frame_container, text="PLAY", command=start_game, font=("Arial", 18), width=35, height=4).pack()
Button(start_frame_container, text="ABOUT", command=about_screen, font=("Arial", 18), width=35, height=4).pack(pady=20)
Button(start_frame_container, text="EXIT", command=root.destroy, font=("Arial", 18), width=35, height=4).pack()

incorrect_taunts = ["Better luck next time!", "Nice try! :)", "That one was easy :)", "Bad luck", "Have another go!"]
correct_taunts = ["Well done smarty pants!", "I bet you guessed!", "I knew that ;)", "That one was easy!"]


def refresh(text):
    global answered_correctly, questions_asked
    questions_asked += 1
    for widget in frame.winfo_children():
        widget.destroy()

    if text == html.unescape(t.return_correct_answer()):
        answered_correctly += 1
        label = Label(frame, text="Correct!", font=("Arial", 30), background="#7CFC00", width=20, height=2)
        correct_taunt = Label(frame, text=random.choice(correct_taunts), font=("Arial", 30), background="#00abff",
                              width=20)
        label.pack(pady=200)
        correct_taunt.pack()
        threading.Timer(2.0, correct_taunt.destroy).start()

    else:
        label = Label(frame, text="incorrect!", font=("Arial", 30), background="#ff6347", width=20, height=2)
        incorrect_taunt = Label(frame, text=random.choice(incorrect_taunts), font=("Arial", 30), background="#00abff")
        correct_answer = Label(frame, text=("The correct answer was " + t.return_correct_answer()),
                               font=("Helvetica", 18), background="#FFFF66")

        label.pack(pady=200)
        incorrect_taunt.pack()
        correct_answer.pack(pady=25)

        threading.Timer(2.0, correct_answer.destroy).start()
        threading.Timer(2.0, incorrect_taunt.destroy).start()

    threading.Timer(2.0, label.destroy).start()
    threading.Timer(1.25, make_buttons).start()


def homescreen():
    frame.pack_forget()
    start_frame_container.pack(expand=YES, fill=BOTH, pady=150)


def make_buttons():
    global t, questions_asked
    t = trivia.Trivia()
    question_label = Label(frame, text=html.unescape(t.return_question()), height=5, font=("Helvetica", 25),
                           bg="#00abff")
    question_label.pack(fill=X)

    Button(question_label, text="Exit", font=("Helvetica", 15), highlightbackground="#ff6347", height=3, width=6,
           command=homescreen).pack(side=LEFT)

    for i in t.return_all_answers():
        button = Button(frame, text=html.unescape(i), font=("Arial", 30), wraplength=250,
                        command=lambda x=i: refresh(x))
        button.pack(side=LEFT, expand=YES)

    Label(question_label, text=("Score: " + str(answered_correctly) + "/" + str(questions_asked)),
          background="#0EBFE9", font=("Arial", 25)).pack(side=LEFT, fill=Y)
    frame.update()


make_buttons()
root.mainloop()
