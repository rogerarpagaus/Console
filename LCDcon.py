import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

import socket

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
font = ImageFont.load_default(10)
draw.text ((1,20), "IP adr:", font=font)
#draw.text ((1,30), ip, font=fontSmall)
draw.text ((1,30), ip, font=font)

d.image(image)
d.display()
