from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image,ImageChops

(left, upper, right, lower) = (90, 90, 170, 120)
rectangular_position = (left, upper, right, lower)

#get base image to differentiate obstacles
image1 = Image.open("base_image.png").convert("L")
im_crop = image1.crop(rectangular_position)

driver_path = "D:/main programs/coding/geckodriver.exe"
site_url = "https://trex-runner.com/"

#lunch driver to use firefox
driver = webdriver.Firefox(executable_path=driver_path)
driver.get(site_url)
sleep(3)

#get whole page which accecpt keys not canvas
play_board = driver.find_element(By.TAG_NAME,'body')
play_canvas = driver.find_element(By.XPATH,"/html/body/header/div/canvas")

sleep(1)
#start game
play_board.send_keys(Keys.UP)
sleep(1)
ones = 0
zeros = 0

while True:
    sleep(0.09)
    play_canvas.screenshot("position.png")

    image2 = Image.open("position.png").convert("L")
    im_crop2 = image2.crop(rectangular_position)


    diff = ImageChops.difference(im_crop, im_crop2)

    #----2nd solution----------#
    #if color in that spot of screen shot not white means ones not zero
    #also means values of 1,0 is changed

    # zeros = 0
    # for lists in diff.getprojection():
    #     for num in lists:
    #         if int(num) == 0:
    #             zeros += 1
    # print(f"{zeros}")
    # if zeros != 110:
    #     play_board.send_keys(Keys.UP)

    if diff.getbbox():
        play_board.send_keys(Keys.UP)
