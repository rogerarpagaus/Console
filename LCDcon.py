import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

import socket

from gpiozero import CPUTemperature, LoadAverage

cpu = CPUTemperature()
print(cpu.temperature)
la = LoadAverage(min_load_average=0, max_load_average=2)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
ip=s.getsockname()[0]
s.close()

spiSettings = SPI.SpiDev(0,0, max_speed_hz=4000000)
d = LCD.PCD8544(23, 24, spi=spiSettings)

d.begin(contrast=60)
d.clear()
d.display ()
#font = ImageFont.truetype("/home/pi/fonts/Railway.ttf",12)
#fontSmall = ImageFont.truetype("/home/pi/fonts/Railway.ttf",9)
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,84,48), outline=255, fill=255)
draw.rectangle((0,0,83,47), outline=0, fill=255)
font = ImageFont.load_default()
while (True):
  draw.rectangle((0,0,83,47), outline=0, fill=255)
  draw.text ((1,10), str(la), font=font)
  draw.text ((1,20), "CPU t= " + str(round(cpu.temperature,1)) +"C", font=font)
  #draw.text ((1,30), ip, font=fontSmall)
  draw.text ((1,30), ip, font=font)
  d.image(image)
  d.display()
  time.sleep(1)
