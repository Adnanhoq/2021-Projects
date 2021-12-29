import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
#imported from pynput

delay = 0.01 #delay of 1/100th of a second
button = Button.left #Uses left click
start_stop_key = KeyCode(char='[')  #Start/stop key set to [
exit_key = KeyCode(char=']')  #Exit key set to ]


class ClickMouse(threading.Thread) : #new class called ClickMouse - object of executing the clicking - inheriting threading attributes
    def __init__(self, delay, button) : #init = initialisation
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        #Automated delay and reclick of button
        self.running = False
        self.program_running = True
        #Program is on, but is not running (hence why running if false and program_running is true) - Will be switched around once the program is running

    def start_clicking(self):
        self.running = True
#Sets running to be true when key is clicked

    def stop_clicking(self):
        self.running = False
#Sets running to be false when key is clicked the second time

    def exit(self):
        self.stop_clicking()
        self.program_running = False
#Turns off the program when the exit key is clicked

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
#While the program is running and clicking, the left mouse button will automatically be clicked and sleep for the delay set


mouse = Controller() #Mouse has been defined as a controller
click_thread = ClickMouse(delay, button) #Delay and button passed onto the ClickMouse
click_thread.start()


def on_press(key):
    if key == start_stop_key:  #If the start/stop key is pressed, stop/start the program
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key: #If the exit key is pressed, exit the program
        click_thread.exit()
        listener.stop #In the threading library which has been imported
        
with Listener(on_press=on_press) as listener:
    listener.join()
