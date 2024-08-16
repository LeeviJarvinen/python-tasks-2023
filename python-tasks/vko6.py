#
# Demovideo: https://youtu.be/Uiw9LhT9BVQ
#

import tkinter as tk
import numpy as np
import winsound
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

def init():
    global ernesti_label, kernesti_label

    ernesti_label = create_label("E", "red", 250, 500)
    kernesti_label = create_label("K", "orange", 450, 500)

def create_label(text, bg_color, x, y):
    label = tk.Label(ikkuna, text=text, bg=bg_color, fg='white', width=2, height=1)
    label.place(x=x, y=y)
    return label
    
def start_digging(amount):
    def send_monkey(monkey_type):
        A_e = 1
        B_e = 100
        pos = random.randint(A_e, B_e) - 1
        xpos = 240 if monkey_type == "E_M" else 440
        monkey_label = create_label(monkey_type, 'brown', xpos, 155 + pos * 2)
        threading.Thread(target=dig_monkey, args=(monkey_type, monkey_label, pos, xpos)).start()

    def send_mul_monkey(monkey_type, pos):
        xpos = 240 if monkey_type == "E_M" else 440
        monkey_label = create_label(monkey_type, 'brown', xpos, 155 + pos * 2)
        threading.Thread(target=dig_monkey, args=(monkey_type, monkey_label, pos, xpos)).start()

    match amount:
        case 1:
            send_monkey("E_M")
        case 2:
            send_monkey("K_M")
        case 3:
            positions = spaced_indexes[:10]
            for i in range(10):
                delay = i * 1000
                ikkuna.after(delay, lambda i=i: (send_mul_monkey("E_M", positions[i])))
        case 4:
            positions = spaced_indexes[:10]
            for i in range(10):
                delay = i * 1000
                ikkuna.after(delay, lambda i=i: (send_mul_monkey("K_M", positions[i])))

def generate_spaced_indexes(type):
    global spaced_indexes
    random_index = random.randint(0, 99)
    print("Random_index: ", random_index)
    spaced_indexes = []
    
    step = 10
    
    for i in range(99, random_index, -step):
        spaced_indexes.append(i)
    
    spaced_indexes.append(random_index)
    
    for i in range(random_index - step, 0, -step):
        spaced_indexes.append(i)

    if type == "E_M":
        start_digging(3)
    else:
        start_digging(4)

def dig_monkey(monkey_type, monkey_label, monkey_pos, monkey_xpos):
    while monkey_pos >= 0:
        if monkey_type == "E_M" and eoja[monkey_pos] > 0:
            eoja[monkey_pos] -= 1
            ewater(monkey_type, 0)
            refresh(monkey_type)
        elif monkey_type == "K_M" and koja[monkey_pos] > 0:
            koja[monkey_pos] -= 1
            kwater(monkey_type, 0)
            refresh(monkey_type)
        else:
            monkey_label.destroy()
            refresh(monkey_type)
        update_monkey_position(monkey_label, monkey_xpos, 155 + monkey_pos * 2)
        monkey_pos -= 1
        winsound.Beep(500, 500)
        ikkuna.update()
        if monkey_pos == -1:
            monkey_label.destroy()
            refresh(monkey_type)
            if monkey_type == "E_M":
                ewater(monkey_type, 0)
            else:
                kwater(monkey_type, 0)

elastpos = 0
klastpos = 0
labels = []

def ewater(water_type, x):
    global elastpos

    if x == 1:
        elastpos = 0
        lastwpos = 0
        wpos = 0
    
    wpos = elastpos
    while wpos <= 99:
        lastwpos = wpos
        water_label = create_label(water_type, 'blue', 265, 155 + lastwpos * 2)
        labels.append(water_label)
        if eoja[wpos] == 1:
            break
        else:
            wpos += 1
            winsound.Beep(300, 100)
            ikkuna.update()
            if wpos == 99:
                win(water_type)
    elastpos = wpos

def kwater(water_type, x):
    global klastpos

    if x == 1:
        klastpos = 0
        lastwpos = 0
        wpos = 0
    
    wpos = klastpos
    while wpos <= 99:
        lastwpos = wpos
        water_label = create_label(water_type, 'blue', 465, 155 + lastwpos * 2)
        labels.append(water_label)
        if koja[wpos] == 1:
            break
        else:
            wpos += 1
            winsound.Beep(300, 100)
            ikkuna.update()
            if wpos == 99:
                win(water_type)
    klastpos = wpos

winner = 0

def win(type):
    global winner, winner_label
    if winner == 0 and type == "E_M":
        winner_label = tk.Label(ikkuna, text="Ernesti voitti!!!")
        winner_label.place(x=300, y=200)
        ikkuna.update()
        print("Ernesti voitti!!!!")
        winsound.Beep(300, 10000)
        winner = 1
        pool()
    elif winner == 0 and type == "K_M":
        winner_label = tk.Label(ikkuna, text="Kernesti voitti!!!")
        winner_label.place(x=300, y=200)
        print("Kernesti voitti!!!!")
        winsound.Beep(800, 10000)
        winner = 1
        pool()
    elif type == "RESET":
        winner = 0

def pool():
    for i in range(20):
        allas[i, :] = 0
        refresh("ALLAS")
        ikkuna.update()
        winsound.Beep(400, 200)

def fill():
    pos = 99
    while pos >= 0:
        ernesti_label.place(x=240, y=155 + pos * 2)
        kernesti_label.place(x=440, y=155 + pos * 2)
        koja[pos] = 1
        eoja[pos] = 1
        pos -= 1
        winsound.Beep(300, 10)
        ikkuna.update()
    ernesti_label.destroy()
    kernesti_label.destroy()
    ewater("", 1)
    kwater("", 1)
    win("RESET")
    for label in labels:
        label.destroy()
    init()
    refresh("ALL")

def refresh(type):
    if type == "E_M":
        ax1.matshow(eoja)
        eoja_kanvaasi.draw()
    elif type == "K_M":
        ax2.matshow(koja)
        koja_kanvaasi.draw()
    elif type == "ALLAS":
        ax3.matshow(allas)
        allas_kanvaasi.draw()
    else:
        ax1.matshow(eoja)
        eoja_kanvaasi.draw()
        ax2.matshow(koja)
        koja_kanvaasi.draw()

def update_monkey_position(monkey_label, xpos, ypos):
    monkey_label.place(x=xpos, y=ypos)

ikkuna = tk.Tk()
ikkuna.title("Exercise 6")
ikkuna.geometry("700x700")
ikkuna.configure(bg="#00CDCD")

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

island = tk.Label(ikkuna, bg='yellow', width=50, height=25)
island.place(x=175,y=150)
init()

eoja = np.ones((100, 1))
koja = np.ones((100, 1))
allas = np.ones((20, 60))

fig1, ax1 = plt.subplots(figsize=(0.2, 2.8))
fig1.set_facecolor("#F0F0F0")
ax1.matshow(eoja)
ax1.axis("off")

fig2, ax2 = plt.subplots(figsize=(0.2, 2.8))
fig2.set_facecolor("#F0F0F0")
ax2.matshow(koja)
ax2.axis("off")

fig3, ax3 = plt.subplots(figsize=(2.2, 1))
fig3.set_facecolor("#F0F0F0")
ax3.matshow(allas)
ax3.axis("off")

koja_kanvaasi = FigureCanvasTkAgg(fig2, master=ikkuna)
koja_kanvaasi.get_tk_widget().place(x=450, y=124)

eoja_kanvaasi = FigureCanvasTkAgg(fig1, master=ikkuna)
eoja_kanvaasi.get_tk_widget().place(x=250, y=124)

allas_kanvaasi = FigureCanvasTkAgg(fig3, master=ikkuna)
allas_kanvaasi.get_tk_widget().place(x=250, y=375)

eoja_kanvaasi.draw()
koja_kanvaasi.draw()
allas_kanvaasi.draw

monkey_button1 = tk.Button(ikkuna, text="Kaiva Ernestin ojaa", padx=40, command=lambda: start_digging(1))
monkey_button1.grid(row=1, column=1, columnspan=5)

monkey_button2 = tk.Button(ikkuna, text="Kaiva Kernestin ojaa", padx=40, command=lambda: start_digging(2))
monkey_button2.grid(row=2, column=1, columnspan=5)

fill_button = tk.Button(ikkuna, text="Täytä ojat", padx=40, command=lambda: threading.Thread(target=fill).start())
fill_button.grid(row=3, column=1, columnspan=5)

monkey_button3 = tk.Button(ikkuna, text="Ernesti 10 apinaa", padx=40, command=lambda: generate_spaced_indexes("E_M"))
monkey_button3.grid(row=4, column=1, columnspan=5)

monkey_button4 = tk.Button(ikkuna, text="Kernesti 10 apinaa", padx=40, command=lambda: generate_spaced_indexes("K_M"))
monkey_button4.grid(row=5, column=1, columnspan=5)

i_suppose_i_have_earned_so_much_points(5)
ikkuna.mainloop()
