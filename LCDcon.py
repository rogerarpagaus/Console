import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFront
import time

spiSettings = SPI.SpiDev(0,0 max-speed_hz=4000000)
d = LCD.PCD8544(23, 24, spiSettings)

d.begin(contrast060)
d.clear()
d.display ()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHIGHT))
draw = ImageDraw(image)
draw.rectangle((0.0.84,84), outline=255, fill=255)

draw.ellipse((2,2,27,22), outline=0, fill=255)
draw.rectangle((35,2,54,22), outline=0, fill=255)
draw.polygon([](63,33), (73,2), (83,22)], outline=0, fill=255)

font = ImageFont.load_default()
draw.text ((8,30), 'Hello World', font=font)

d.image(image)
d.display()
