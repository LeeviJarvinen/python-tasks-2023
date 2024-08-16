
#
# https://youtu.be/DpD9Fq50Sy8
# https://youtu.be/DpD9Fq50Sy8
# https://youtu.be/DpD9Fq50Sy8
#

# template
import tkinter as tk
import winsound
import time
import random
import math
import threading

ikkuna=tk.Tk()
ikkuna.title("Exercise 8")
ikkuna.geometry("700x700")
ikkuna.configure(bg="lightblue")
ikkuna.grid_rowconfigure(1, weight=1)
# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)

point_button=[]

for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(5*(i)),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    points_mod=int(amount_of_points/5)
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1) 
    point_button[0].configure(bg='green')   
    for i in range(points_mod):
        point_button[i+1].configure(bg='green')
        winsound.Beep(440+i*100,500)
# example ...

islands = set()
cont = tk.IntVar()
x = tk.IntVar()
x.set(1)

monkey_count = tk.IntVar()
monkey_count.set(10)

island_count = 0
labels = []
mlabels = []
monkeys = []

min_padding = 150

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_island():
    global island_label, island_count, north_pier, east_pier, south_pier, west_pier
    cont.set(0)
    num = x.get()
    monkeys = add_monkeys()
    check = cont.get()

    if num > 10:
        print("island capacity of 10 has been reached")
        return
    
    while True:
        xrand = random.randint(50, 600)
        yrand = random.randint(100, 600)
        valid_position = True

        for (x1, y1) in islands:
            distance = calculate_distance(xrand, yrand, x1, y1)
            if distance < min_padding:
                valid_position = False
                break

        if valid_position:
            add_monkeys()
            break

    if island_count == 0:
        xrand = 315
        yrand = 315

        north_pier = tk.Label(ikkuna, text="| |", bg="lightblue")
        north_pier.place(x=xrand + 32, y=yrand - 20)
        
        east_pier = tk.Label(ikkuna, text="==", bg="lightblue")
        east_pier.place(x=xrand + 80, y=yrand + 30)
        
        south_pier = tk.Label(ikkuna, text="| |", bg="lightblue")
        south_pier.place(x=xrand + 32, y=yrand + 80)
        
        west_pier = tk.Label(ikkuna, text="==", bg="lightblue")
        west_pier.place(x=xrand - 25, y=yrand + 30)

    island_label = tk.Label(ikkuna, text=f"island: {num} \n monkeys: {monkeys}", bg="yellow", width=10, height=5)
    island_label.place(x=xrand, y=yrand)

    # island_label.bind("<Button-1>", lambda event, island_number=num: threading.Thread(target=swimming, args=(island_number)).start())
    
    labels.append(island_label)
    islands.add((xrand, yrand))
    x.set(num + 1)
    island_count += 1
    island_number = num
    
    while check != 1:
        threading.Thread(target=lambda: sound("alive")).start()
        time.sleep(5)
        laughter()
        threading.Thread(target=lambda: swimming(1)).start()
        check = cont.get()

def add_monkeys():
    monkey_amount = 10
    monkeys.append(monkey_amount)
    return monkey_amount

def laughter():
    for j in range(island_count):
        laugh = random.randint(0, 10)
        if laugh == 1 and monkeys[j] != 0:
            print(f"A monkey died of laughter on island {j+1}")
            monkeys[j] -= 1
            island = j + 1
            labels[j].config(bg="red")
            time.sleep(0.3)
            labels[j].config(text=f"island: {island} \n monkeys: {monkeys[j]}", bg="yellow")
            sound("death")
        elif laugh == 1 and monkeys[j] == 0:
            island = j + 1
            print(f"No more monkeys left on island: {island}")

pier_positions = {
    "north_pier": (315, 295),
    "east_pier": (395, 375),
    "south_pier": (315, 455),
    "west_pier": (235, 375)
}

def swimming(island_number):
    index = island_number - 1
    if monkeys[index] > 0:
        monkeys[index] -= 1
        labels[index].config(text=f"island: {island_number}\nmonkeys: {monkeys[index]}", bg="yellow")
        direction = random.choice(["north", "east", "south", "west"])
        
        dx, dy = 0, 0

        if direction == "north":
            xrand, yrand = north_pier.winfo_x(), north_pier.winfo_y()
            dy = -5
        elif direction == "east":
            xrand, yrand = east_pier.winfo_x(), east_pier.winfo_y()
            dx = 5
        elif direction == "south":
            xrand, yrand = south_pier.winfo_x(), south_pier.winfo_y()
            dy = 5
        elif direction == "west":
            xrand, yrand = west_pier.winfo_x(), west_pier.winfo_y()
            dx = -5

        monkey_label = tk.Label(ikkuna, text="■", bg="lightblue", fg="brown")
        monkey_label.place(x=xrand, y=yrand)

        monkey_thread = threading.Thread(target=eaten, args=(monkey_label, island_number)) # huomasi että teit esimerkeissäsi threadeja näin joten käytit tätä tapaa itsekkin tässä kohdassa
        monkey_thread.start()

        while xrand >= 0 and xrand <= 700 and yrand >= 0 and yrand <= 700:
            xrand += dx
            yrand += dy
            monkey_label.place(x=xrand, y=yrand)
            ikkuna.update()
            time.sleep(0.5)

        # monkey_label.destroy()
        # print(f"Monkey from island {island_number} started swimming {direction}")

    elif monkeys[index] <= 0:
        print(f"No monkeys left on island {island_number} to swim")

def eaten(monkey_label, island_number):
    while True:
        eaten = random.randint(1, 10)
        time.sleep(1)
        if eaten == 1:
            monkey_label.destroy()
            print("monkey was eaten while swimming")
            sound("death")
            break
        ikkuna.update()
        time.sleep(0.1)
        
def sound(x):
    if x == "alive":
        hz = random.randint(200, 1000)
        winsound.Beep(hz, 100)
    elif x == "death":
        winsound.Beep(100, 100)

def reset():
    laughter()
    cont.set(1)
    x.set(1)
    islands.clear()
    monkeys.clear()
    for label in labels:
        label.destroy()
    for monkey in mlabels:
        monkey.destroy()

island_button = tk.Button(ikkuna, text="New island", command=lambda: threading.Thread(target=create_island).start())
island_button.grid(row=2, column=1, sticky="sw")

reset_button = tk.Button(ikkuna, text="Reset", command=reset)
reset_button.grid(row=3, column=1, sticky="sw")

i_suppose_i_have_earned_so_much_points(15)
ikkuna.mainloop()

#Tässä on 5 ja 10 pisteen toteutuksen koodi.

# # template
# import tkinter as tk
# import winsound
# import time
# import random
# import math
# import threading

# ikkuna=tk.Tk()
# ikkuna.title("Exercise 8")
# ikkuna.geometry("700x700")
# ikkuna.configure(bg="lightblue")
# ikkuna.grid_rowconfigure(1, weight=1)
# # add five buttons to the top line of the window
# koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)

# point_button=[]

# for i in range(5):
#     button_temp=tk.Button(ikkuna,text="Points: "+str(5*(i)),padx=40)
#     button_temp.grid(row=0,column=i+1)
#     point_button.append(button_temp)
# def i_suppose_i_have_earned_so_much_points(amount_of_points):
#     points_mod=int(amount_of_points/5)
#     for i in range(5):
#         point_button[i].configure(bg='gray')
#     time.sleep(1) 
#     point_button[0].configure(bg='green')   
#     for i in range(points_mod):
#         point_button[i+1].configure(bg='green')
#         winsound.Beep(440+i*100,500)
# # example ...

# islands = set()
# cont = tk.IntVar()
# x = tk.IntVar()
# x.set(1)

# monkey_count = tk.IntVar()
# monkey_count.set(10)

# island_count = 0
# labels = []
# mlabels = []
# monkeys = []

# min_padding = 150

# def calculate_distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# def create_island():
#     global island_label, island_count
#     cont.set(0)
#     num = x.get()
#     monkeys = add_monkeys()
#     check = cont.get()

#     if num > 10:
#         print("island capacity of 10 has been reached")
#         return
    
#     while True:
#         xrand = random.randint(50, 600)
#         yrand = random.randint(100, 600)
#         valid_position = True

#         for (x1, y1) in islands:
#             distance = calculate_distance(xrand, yrand, x1, y1)
#             if distance < min_padding:
#                 valid_position = False
#                 break

#         if valid_position:
#             add_monkeys()
#             break

#     island_label = tk.Label(ikkuna, text=f"island: {num} \n monkeys: {monkeys}", bg="yellow", width=10, height=5)
#     island_label.place(x=xrand, y=yrand)

#     island_label.bind("<Button-1>", lambda event, island_number=num: threading.Thread(target=swimming, args=(island_number,)).start())
    
#     labels.append(island_label)
#     islands.add((xrand, yrand))
#     x.set(num + 1)
#     island_count += 1
    
#     while check != 1:
#         threading.Thread(target=lambda: sound("alive")).start()
#         time.sleep(10)
#         laughter()
#         check = cont.get()

# def add_monkeys():
#     monkey_amount = 10
#     monkeys.append(monkey_amount)
#     return monkey_amount

# def laughter():
#     for j in range(island_count):
#         laugh = random.randint(0, 50)
#         if laugh == 1 and monkeys[j] != 0:
#             print(f"A monkey died of laughter on island {j+1}")
#             monkeys[j] -= 1
#             island = j + 1
#             labels[j].config(bg="red")
#             time.sleep(0.3)
#             labels[j].config(text=f"island: {island} \n monkeys: {monkeys[j]}", bg="yellow")
#             sound("death")
#         elif laugh == 1 and monkeys[j] == 0:
#             island = j + 1
#             print(f"No more monkeys left on island: {island}")

# def swimming(island_number):
#     index = island_number - 1
#     ypos = random.randint(0, 50)
#     xpos = random.randint(80, 120)
    
#     if monkeys[index] > 0:
#         monkeys[index] -= 1
#         labels[index].config(text=f"island: {island_number} \n monkeys: {monkeys[index]}", bg="yellow")
        
#         monkey_label = tk.Label(ikkuna, text="■", bg="lightblue", fg="brown")
#         xrand, yrand = labels[index].winfo_x(), labels[index].winfo_y()
#         monkey_label.place(x=xrand + xpos, y=yrand + ypos)
        
#         monkey_thread = threading.Thread(target=eaten, args=(monkey_label, island_number)) # huomasi että teit esimerkeissäsi threadeja näin joten käytit tätä tapaa itsekkin tässä kohdassa
#         monkey_thread.start()

#     elif monkeys[index] <= 0:
#         print(f"No monkeys left on island {island_number} to swim")

# def eaten(monkey_label, island_number):
#     print(f"monkey went swimming on island {island_number}")
#     while True:
#         eaten = random.randint(1, 10)
#         time.sleep(1)
#         if eaten == 1:
#             monkey_label.destroy()
#             print("monkey was eaten while swimming")
#             sound("death")
#             break

#         dx = random.randint(-5, 5)
#         dy = random.randint(-5, 5)

#         x, y = monkey_label.winfo_x(), monkey_label.winfo_y()
#         monkey_label.place(x=x + dx, y=y + dy)
#         ikkuna.update
#         time.sleep(.1) 
        
# def sound(x):
#     if x == "alive":
#         hz = random.randint(200, 1000)
#         winsound.Beep(hz, 100)
#     elif x == "death":
#         winsound.Beep(100, 100)

# def reset():
#     laughter()
#     cont.set(1)
#     x.set(1)
#     islands.clear()
#     monkeys.clear()
#     for label in labels:
#         label.destroy()
#     for monkey in mlabels:
#         monkey.destroy()

# island_button = tk.Button(ikkuna, text="New island", command=lambda: threading.Thread(target=create_island).start())
# island_button.grid(row=2, column=1, sticky="sw")

# reset_button = tk.Button(ikkuna, text="Reset", command=reset)
# reset_button.grid(row=3, column=1, sticky="sw")

# i_suppose_i_have_earned_so_much_points(10)
# ikkuna.mainloop()