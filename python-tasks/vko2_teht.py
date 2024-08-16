r = 1.5 #vaihdetaan 2.9
x = 0.1 #vaihdetaan 0.5
for i in range(100):
    x = r*x*(1-x)
    print(i, x)

Teht 2.

"""
Ratkaistaan liikeyhtälöt jousesta roikkuvalle massalle käyttäen Eulerin menetelmää.
"""

import matplotlib.pyplot as plt

# Määritellään fysikaaliset vakiot
g = 10
k = 1
m = 1
L = 0
b = 0.25

# Alkuarvot paikalle ja nopeudelle
x_0 = 1
v_0 = 0

# Aikaan liittyvät muuttujat
t_0 = 0
t_max = 20
dt = 0.01

# Alustetaan muuttujat
x = x_0
v = v_0
t = t_0

# Taulukot muuttujille
x_array = [x_0]
v_array = [v_0]
t_array = [t_0]

# Iteroidaan aikaa eteenpäin
while t < t_max:
    # Lasketaan uudet arvot
    x_new = x + dt * v
    v_new = v + dt * (g - k/m * (x - L)- (b/m) * v)
    t_new = t + dt

    # Päivitetään
    x = x_new
    v = v_new
    t = t_new

    # Lisätään taulukkoon
    x_array.append(x)
    v_array.append(v)
    t_array.append(t)


# Luodaan kuvaaja liikkeestä
fig, ax = plt.subplots()
ax.scatter(t_array, x_array)
plt.show()