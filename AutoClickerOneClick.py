# Cole Delong
# Auto clicker
# 4/29/20

# imports
from pynput.mouse import Button, Controller, Listener

# main function
def main():
    
    # setup
    mouse = Controller()

    # loop
    while True:

        # Collect new click location
        with Listener(
                on_click=on_click) as listener:
            listener.join()
        
        # click the mouse in the position 1000 times
        mouse.click(Button.left, 1000)
        print("Done!")

# listeners
def on_click(x, y, button, pressed):
    if not pressed and button == button.middle:
        print("click: ({}, {})".format(x, y))
        print("Clicking...")
        return False
     
# run main function
if __name__ == "__main__": main()

 
