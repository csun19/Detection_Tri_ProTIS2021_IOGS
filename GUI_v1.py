# Graphical User Interface of Color&Shape dectection
# ~~~~~~~~~~~~~~~~ Version 1 ~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~ Chenyu SUN ~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~ 1 April 2021 ~~~~~~~~~~~~~~~~

import tkinter as tk
import os
from Mod_detect import mod_detect
try:
    import RPi.GPIO as GPIO
except:
    print("Error: import RPi.GPIO")
from time import sleep

window = tk.Tk()

window.title('GUI test')
window.geometry('500x300')

# notice
notice = tk.Label(window, text = "Veuillez cliquer sur 'detect' pour démarrer la détection \n"\
                  "de la couleur et de la forme")
notice.pack()

# Detection live view
def callback_test():
    mod_detect()
    
button_test = tk.Button(window, text='detect', width=5, height=1, command=callback_test)
button_test.place(x=200,y=60,anchor='nw')


# test of actuator

def callback_R():
    print('Rouge')
    # test the actuator of red by producing a pulse at pin15
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(15, GPIO.LOW)
    GPIO.cleanup()
def callback_G():
    print('Vert')
    # test the actuator of green by producing a pulse at pin16
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()
def callback_B():
    print('Bleu')
    # test the actuator of blue by producing a pulse at pin18
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()
testlab = tk.Label(window, text="Actionneur\ntest")
button_R = tk.Button(window, text='Rouge', width = 5, height = 1, command = callback_R)
button_G = tk.Button(window, text='Vert', width = 5, height = 1, command = callback_G)
button_B = tk.Button(window, text='Bleu', width = 5, height = 1, command = callback_B)
testlab.place(x=20,y=60,anchor='nw')
button_R.place(x=20,y=110,anchor='nw')
button_G.place(x=20,y=160,anchor='nw')
button_B.place(x=20,y=210,anchor='nw')

window.mainloop()
