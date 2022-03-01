import numpy as np
import tkinter
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg='black', height=500, width=500)
sz = 45
population = np.random.randint(0, 2, (10, 10))
lol = False
def kek():
    population = np.random.randint(0, 2, (10, 10))
    print(population)
    return
kek()
def key_pressed(event):
    global population
    global lol
    if event.keysym == "m" or lol:
        render(sz)
        nums_render(sz)
        print(lol)
        if not lol:
            lol = True
            print("Нажмите любую клавишу чтобы начать ввод")
            return
        else:
            lol = False
        x = int(input("Какую клетку вы хотите изменить?\n"))
        for i in range(len(population)):
            for j in range(len(population[i])):
                x -= 1
                if x == 0:
                    if population[j, i] == 0:
                        population[j, i] = 1
                    else:
                        population[j, i] = 0
            render(sz)
    else:
        population = next_population(population)
    render(sz)
    canvas.pack()

def next_population(population):
    k = 0
    for i in population.reshape(100, 1):
        if i == 0:
            k += 1
    if k >= 100:
        population = np.random.randint(0, 2, (10, 10))
        render(sz)
    neighbors = sum([
        np.roll(np.roll(population, -1, 1), 1, 0),
        np.roll(np.roll(population, 1, 1), -1, 0),
        np.roll(np.roll(population, 1, 1), 1, 0),
        np.roll(np.roll(population, -1, 1), -1, 0),
        np.roll(population, 1, 1),
        np.roll(population, -1, 1),
        np.roll(population, 1, 0),
        np.roll(population, -1, 0)
    ])
    return (neighbors == 3) | (population & (neighbors == 2))

def nums_render(size):
    p = 0
    for j in range(len(population)):
        for i in range(len(population[j])):
            p += 1
            canvas.create_text(i * size + size / 2, j * size + size / 2, text=str(p), fill="grey")

def render(size):
    global population
    canvas.delete("all")
    canvas.delete("all")
    for i in range(len(population)):
        for j in range(len(population[i])):
            if population[i, j] == 1:
                col = "green"
            else:
                col = "black"
            canvas.create_rectangle(
                (i * size, j * size), (i * size + size, j * size + size), fill=col)


canvas.pack()
window.bind("<KeyPress>", key_pressed)
window.mainloop()
