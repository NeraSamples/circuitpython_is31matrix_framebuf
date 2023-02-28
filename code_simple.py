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
from adafruit_is31fl3741 import PREFER_BUFFER
from is31matrixqt_framebuf import IS31FrameBuffer

# i2c = board.I2C()
i2c = board.STEMMA_I2C()
is31 = Adafruit_RGBMatrixQT(i2c, allocate=PREFER_BUFFER)
fbuff = IS31FrameBuffer(is31)

def scroll(text, color):
    for x in range(-13, 7 * len(text)):
        is31.fill(0)
        fbuff.text(text, -x, 1, color)
        is31.show()

def scroll_bis(text, color):
    for c in range(len(text)):
        # first substring scrolls longer, others scroll by 1 char
        if c == 0:
            start = 13
        else:
            start = 0
        end = -6
        # print(c, chars, start, end)
        for x in range(start, end, -1):
            is31.fill(0)
            fbuff.text(text[c:c+4], x, 1, color)
            is31.show()

while True:
    scroll("Hello world!", 0x00FF80)
    scroll_bis("Hello world!", 0xFF0080)
