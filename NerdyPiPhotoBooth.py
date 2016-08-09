from os import system
import picamera
from picamera import Color
import time
from gpiozero import Button
import random
from datetime import datetime



camera = picamera.PiCamera()
button = Button(18)


camera.start_preview()
camera.annotate_text_size = 160
camera.annotate_text='Ready!'

while True:
    try:
        button.wait_for_press()
        filename="photo_strip%s.jpg"%datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
   
    
        camera.annotate_text_size = 160
        camera.annotate_foreground = Color('black')
        camera.annotate_text='5'
        time.sleep(1)
        camera.annotate_text='4'
        time.sleep(1)
        camera.annotate_text='3'
        time.sleep(1)
        camera.annotate_text='2'
        time.sleep(1)
        camera.annotate_text='1'
        time.sleep(1)
        camera.annotate_text=' '
        camera.capture("aaa.jpg")
        
        camera.annotate_text='3'
        time.sleep(1)
        camera.annotate_text='2'
        time.sleep(1)
        camera.annotate_text='1'
        time.sleep(1)
        camera.annotate_text=' '
        camera.capture("bbb.jpg")
        
        camera.annotate_text='3'
        time.sleep(1)
        camera.annotate_text='2'
        time.sleep(1)
        camera.annotate_text='1'
        time.sleep(1)
        camera.annotate_text=' '
        camera.capture("ccc.jpg")
        camera.annotate_text='Processing'
        
        system("convert aaa.jpg -resize x400 -gravity center -crop 400x400+0+0 =repage aaa_crop.jpg")
        
        system("convert bbb.jpg -resize x400 -gravity center -crop 400x400+0+0 =repage bbb_crop.jpg")
        
        system("convert ccc.jpg -resize x400 -gravity center -crop 400x400+0+0 =repage ccc_crop.jpg")
        
        system("convert aaa_crop.jpg -extent 1200x1800-100-100 photo_strip.jpg")
        
        system("composite -compose atop -geometry +700+100 aaa_crop.jpg photo_strip.jpg photo_strip.jpg")
       
        system("composite -compose atop -geometry +100+700 bbb_crop.jpg photo_strip.jpg photo_strip.jpg")
        
        system("composite -compose atop -geometry +700+700 bbb_crop.jpg photo_strip.jpg photo_strip.jpg")
        
        system("composite -compose atop -geometry +100+1300 ccc_crop.jpg photo_strip.jpg photo_strip.jpg")
        
        system("composite -compose atop -geometry +700+1300 ccc_crop.jpg photo_strip.jpg photo_strip.jpg")
        
        system("cp photo_strip.jpg %s" % filename)
        
        system ("dropbox_uploader upload %s 'Nerdy Booth'/" % filename)
        
    
        
        camera.annotate_text='Done!'
        time.sleep(3)
        camera.annotate_text='Ready!'

    except KeyboardInterrupt:
        camera.stop_preview()
        break 
