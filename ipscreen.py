#######################################################
#
#	This Python Script is for LCD of Nokia 5110 module 
#	from SunFounder. Get it from www.sunfounder.com
#
#######################################################	
import math
import time

import netifaces
import socket
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

SCLK = 17
DIN  = 18
DC   = 27
RST  = 23
CS   = 22

disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

def setup():
	disp.begin(contrast=60)
	disp.clear()
	disp.display()

def ip():
        image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        font = ImageFont.load_default()
        e0=netifaces.ifaddresses("eth0")
        w0=netifaces.ifaddresses("wlan0")
        ips="eth0:\n" + str(e0[2][0]['addr']) 
        try:
            ipsw="\nwlan0:\n" + str(w0[2][0]['addr'])
        except:
            ipsw=''
        if ipsw != '':
            ips = ips+ipsw
        #+"\nwlan0:\n" + str(w0[2][addr]) + "\n"
        x=1
        while True:
            image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
            draw= ImageDraw.Draw(image)
            draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
            draw.text((1,x), ips, font=font)
            disp.image(image)
            disp.display()
            time.sleep(5)
            disp.clear()
            disp.display()
            x=x+5
            if x == 11:
                x=1




def bye():
	disp.clear()
	disp.display()

def main():
        ip()

if __name__ == "__main__":
	setup()
	try:
		main()
	except KeyboardInterrupt:
		bye()
