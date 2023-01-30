# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: 2023 Neradoc https://neradoc.me
# SPDX-License-Identifier: MIT
"""
A somewhat hacky attempt at scrolling text on the IS31FL3741 13x9 Matrix
https://www.adafruit.com/product/5201
"""
import time
import board
from rainbowio import colorwheel
from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT
import adafruit_is31fl3741
from is31matrixqt_framebuf import IS31FrameBuffer

# i2c = board.I2C()
i2c = board.STEMMA_I2C()

is31 = Adafruit_RGBMatrixQT(i2c, allocate=adafruit_is31fl3741.PREFER_BUFFER)
is31.set_led_scaling(0xFF)
is31.global_current = 0xFF
is31.enable = True

fbuff = IS31FrameBuffer(is31)

def scroll(text, color):
    for x in range(-13, 7 * len(text)):
        is31.fill(0)
        fbuff.text(text, -x, 1, color)
        is31.show()

while True:
    scroll("Hello world!", 0x00FF80)
