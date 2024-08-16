#
# Videon linkki: https://youtu.be/Kjg7YNh0gr0
#
# template
import random
import tkinter as tk
import winsound
import time
import threading

ikkuna=tk.Tk()
ikkuna.title("Exercise 5")
ikkuna.geometry("700x700")
ikkuna.configure(bg="lightblue")
# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)
point_button=[]
for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(i+1),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)    
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100,500)

words = ["olemme", "pulassa", "saarella", "tarvitsemme", "apua", "saarelle"]

def createIslands():
    global emessage, kmessage, win, ernesti, kernesti, emonkeys, kmonkeys
    emessage = words[:3]
    kmessage = words[3:]
    win = False
    emonkeys = 0
    kmonkeys = 0

    ikkuna.grid_rowconfigure(2, weight=1)
    island = tk.Label(ikkuna, text="Island", bg='green', fg='white', width=15, height=25)
    island.grid(row=2, column=1)
    
    continent = tk.Label(ikkuna, text="Continent", bg='gray', fg='white', width=15, height=25)
    continent.grid(row=2, column=5)

    ernesti = tk.Label(ikkuna, text="Ernesti", bg='red', fg='white', width=7, height=5)
    ernesti.place(x=50, y=200)

    kernesti = tk.Label(ikkuna, text="Kernesti", bg='orange', fg='white', width=7, height=5)
    kernesti.place(x=50, y=400)

    points(1)


def sendRescue(y_position):
    global win
    if not win:
        win = True
        rescue_ship = tk.Label(ikkuna, text="Rescue", bg='blue', fg='white', width=7, height=5)
        rescue_ship.place(x=50, y=y_position)
        for step in range(1,101):
            winsound.Beep(500, 100)
            x_position = 550 - (step * 5)
            rescue_ship.place(x=x_position,y=y_position)
            ikkuna.update()
            if step == 100:
                winner(y_position)
                time.sleep(5)
                ernesti.destroy()
                kernesti.destroy()
                for step in range(1, 101):
                    movement = step + 10
                    x_position = movement * 5
                    rescue_ship.place(x=x_position, y=y_position)
                    ikkuna.update()
                    winsound.Beep(500, 100)
                    if step == 100:
                        eruoka = emonkeys * 4
                        kruoka = kmonkeys * 4
                        print(f"Ernestin apinoista riitti syötävää {eruoka} henkilölle perunoiden kera \n")
                        print(f"Kernestin apinoista riitti syötävää {kruoka} henkilölle perunoiden kera \n")
                        if emonkeys > kmonkeys:
                            print("Ernestin apinoista apinoista saatiin järkättyä suuremmat juhlat \n")
                        elif emonkeys < kmonkeys:
                            print("Kernestin apinoista apinoista saatiin järkättyä suuremmat juhlat \n")
                        else:
                            print("Kummankin apinoista saatiin järkättyä yhtä suuret juhlat")
                        points(5)
                break

def sendMonkey(monkey_type, message, y_position):
    if monkey_type == "Ernesti":
        y_position = 200
    elif monkey_type == "Kernesti":
        y_position = 400

    monkey_label = tk.Label(ikkuna, text=f"{monkey_type} \n{message}", bg='brown', fg='white', width=7, height=5)
    monkey_label.place(x=50, y=y_position)

    for step in range(1, 101):
        movement = step + 10
        x_position = movement * 5
        monkey_label.place(x=x_position, y=y_position)
        ikkuna.update()
        winsound.Beep(800, 100)

        if random.randint(1, 150) == 1:
            monkey_label.destroy()
            winsound.Beep(300, 100)
            break

        if step == 100:
            monkeycount(monkey_type)
            if message in emessage and monkey_type == "E_monkey":
                emessage.remove(message)
            if message in kmessage and monkey_type == "K_monkey":
                kmessage.remove(message)
            winsound.Beep(1000, 500)
            if monkey_type == "E_monkey" and not emessage or monkey_type == "K_monkey" and not kmessage:
                sendRescue(y_position)
                continue
    return

def winner(pos):
    points(4)
    if pos == 200:
        print("Ernesti voitti!!!")

    else:
        print("Kernesti voitti!!!")
    
def monkeycount(x):
    global emonkeys, kmonkeys
    if x == "E_monkey":
        emonkeys += 1
        print(f"Ernestis monkeys {emonkeys} \n")
    elif x == "K_monkey":
        kmonkeys += 1
        print(f"Kernestis monkeys {kmonkeys} \n")
    else:
        return

def monkeyMessage(x):
    def send_emonkey(): #tähän on varmasti helpompi tapa mutta tämä on nyt mitä on.
        if not emessage:
            return
        else:
            rand_element = random.choice(emessage)
            threading.Thread(target=lambda: sendMonkey("E_monkey", rand_element, 200)).start()

    def send_kmonkey():
        if not kmessage:
            return
        else:
            rand_element = random.choice(kmessage)
            threading.Thread(target=lambda: sendMonkey("K_monkey", rand_element, 400)).start()

    match x:
        case 1:
            for i in range(10):
                delay = i * 3000
                ikkuna.after(delay, lambda i=i: (send_kmonkey(),send_emonkey()))
            points(3)
        case 2:
            send_emonkey()
            points(2)
        case 3:
            send_kmonkey()
            points(2)

def points(x):
    match x:
        case 1:
            i_suppose_i_have_earned_so_much_points(1)
        case 2:
            i_suppose_i_have_earned_so_much_points(2)
        case 3:
            i_suppose_i_have_earned_so_much_points(3)
        case 4:
            i_suppose_i_have_earned_so_much_points(4)
        case 5:
            i_suppose_i_have_earned_so_much_points(5)


send_button = tk.Button(ikkuna, text="Send 10 monkeys", padx=40, command=lambda: monkeyMessage(1))
send_button.grid(row=5, column=1, columnspan=5)

ernesti_button = tk.Button(ikkuna, text="Send e_monkey", padx=40, command=lambda: monkeyMessage(2))
ernesti_button.grid(row=3, column=1, columnspan=5)

kernesti_button = tk.Button(ikkuna, text="Send k_monkey", padx=40, command=lambda: monkeyMessage(3))
kernesti_button.grid(row=4, column=1, columnspan=5,)

# example ...
createIslands()
ikkuna.mainloop()