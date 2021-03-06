import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


#Quickly run green across display a pixel at a time.
def colorGreen(strip, color = Color(0, 200, 0), wait_ms=5):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000)

#flash strip red
def flashRed(strip, color = Color(200, 0, 0)):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(.5)
    clearLED(strip)
    time.sleep(.5)

#flash strip green
def flashGreen(strip, color = Color(0, 200, 0)):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(.5)
    clearLED(strip)

def clearLED(strip, color = Color(0, 0, 0)):
    #Clear LED
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    try:
        while True:
            print("Testing LEDs")
            for i in range(3):
                flashRed(strip)
            flashGreen(strip)

            colorGreen(strip)
            time.sleep(1)
            clearLED(strip)

    except KeyboardInterrupt:
        print("Game stopped by User")
        clearLED(strip)

