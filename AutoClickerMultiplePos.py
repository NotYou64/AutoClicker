# Cole Delong
# Auto clicker
# 4/29/20

# imports
from pynput.mouse import Button, Controller, Listener
import time

# globals
global positions
positions = []

# main function
def main():
    
    # setup
    mouse = Controller()

    # loop
    while True:

        # reset positions array
        global positions
        positions = []

        # Collect new click location
        with Listener(
                on_click=on_click) as listener:
            listener.join()
        
        # position and click each mouse position 100 times
        for i in range(100):
            print(i+1)
            for pos in positions:
                mouse.position = (pos)
                mouse.click(Button.left, 3)

# listeners
def on_click(x, y, button, pressed):
    if pressed and button == button.middle:
        positions.append((x, y))
    if not pressed and button == button.middle:
        print("click {}: ({}, {})".format(len(positions), x, y))
    if not pressed and button == button.right:
        positions.append((x, y))
        print("click {}: ({}, {})".format(len(positions), x, y))
        print("Clicking...")
        return False
     
# run main function
if __name__ == "__main__": main()

 
