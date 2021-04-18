# Graphical User Interface of Color&Shape dectection
# ~~~~~~~~~~~~~~~~ Version 0 ~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~ Chenyu SUN ~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~ 1 April 2021 ~~~~~~~~~~~~~~~~

import tkinter as tk
import os
from Mod_detect import mod_detect
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

window = tk.Tk()

window.title('GUI test')
window.geometry('500x300')

# notice
notice = tk.Label(window, text = "Please click 'detect' to detect the color and shape \n"\
                  "and make sure that the piece is in the center area")
notice.pack()

# Detection live view
def callback_test():
    mod_detect()
     #os.system('python Main_Detect.py')
    
button_test = tk.Button(window, text='detect', width=5, height=1, command=callback_test)
button_test.place(x=200,y=60,anchor='nw')


# test of actuator
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


def callback_R():
    print('Rouge')
def callback_G():
    print('Vert')
def callback_B():
    print('Bleu')
testlab = tk.Label(window, text="Actionneur\ntest")
button_R = tk.Button(window, text='Rouge', width = 5, height = 1, command = callback_R)
button_G = tk.Button(window, text='Vert', width = 5, height = 1, command = callback_G)
button_B = tk.Button(window, text='Bleu', width = 5, height = 1, command = callback_B)
testlab.place(x=20,y=60,anchor='nw')
button_R.place(x=20,y=110,anchor='nw')
button_G.place(x=20,y=160,anchor='nw')
button_B.place(x=20,y=210,anchor='nw')

window.mainloop()
