import pyautogui
import time
import pydirectinput
from PIL import ImageGrab, ImageShow

time.sleep(3)

random_pixel = [(255, 255, 255), (248, 248, 248), (244, 244, 244), (238, 238, 238), (107, 107, 107), (186, 182, 182), (190, 190, 190), (180, 180, 181), (104, 104, 104), (98, 98, 101), (84, 84, 84), (79, 80, 82), (66, 66, 66), (55, 55, 55), (33, 33, 33)]

# my_image = ImageGrab.grab()
# im = my_image.crop((160, 640, 200, 700))
# ImageShow.show(im)
# ImageShow.XVViewer()
# extrema = my_image.convert("L").getextrema()
#
# print(pyautogui.pixel(160, 640))

def is_white_screen(image):
    extrema = image.convert("L").getextrema()
    if extrema == (255, 255):
        return True
    elif extrema == (33, 33):
        return False
    else:
        return "yes"
#
#
def jump_duck(color, screen1, screen2):
    if color in screen1:
        pyautogui.press("space")

    elif color in screen2:
        pydirectinput.keyDown("down")
        time.sleep(0.3)
        pydirectinput.keyUp("down")




while(True):
    my_image = ImageGrab.grab()

    im = my_image.crop((200, 150, 250, 220))
    mi = my_image.crop((350, 680, 730, 700))
    img = my_image.crop((350, 600, 730, 630))
    my_color = (83, 83, 83)
    whiteness = (172, 172, 172)


    screen_colors = [color[1] for color in mi.getcolors()]
    another_colors = [color[1] for color in img.getcolors()]

    if is_white_screen(im) == "yes":

        # for pixel in random_pixel:
        if pyautogui.pixel(160, 640) in screen_colors:
            pyautogui.press("space")
        elif pyautogui.pixel(160, 640) in another_colors:
            pydirectinput.keyDown("down")
            time.sleep(0.3)
            pydirectinput.keyUp("down")

        # another = my_image.crop((350, 680, 800, 700))
        # ImageShow.show(another)
        # ImageShow.XVViewer()




    elif is_white_screen(im):
        jump_duck(my_color, screen_colors, another_colors)
    else:
        jump_duck(whiteness, screen_colors, another_colors)







