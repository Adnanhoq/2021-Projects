import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
#imported from pynput

delay = 0.01 #delay of 1/100th of a second
button = Button.left #Uses left click
start_stop_key = KeyCode(char='[')  #Start/stop key set to [
exit_key = KeyCode(char=']')  #Exit key set to ]


class ClickMouse(threading.Thread) :
    def __init__(self, delay, button) :
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        #Automated delay and reclick of button
        self.running = False
        self.program_running = True
        #If key to start hasn't been clicked, program can still run in the background

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()



def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop
#try with capital L without line below

with Listener(on_press=on_press) as listener:
    listener.join()