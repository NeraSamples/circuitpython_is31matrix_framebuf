# SPDX-FileCopyrightText: 2023 Neradoc https://neradoc.me
# SPDX-License-Identifier: MIT
"""
A somewhat hacky attempt at scrolling text on the IS31FL3741 13x9 Matrix
https://www.adafruit.com/product/5201
"""
import time
import board
from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT
from adafruit_is31fl3741 import PREFER_BUFFER
from is31matrixqt_framebuf import IS31FrameBuffer
from is31_scroller import Scroller

# i2c = board.I2C()
i2c = board.STEMMA_I2C()
# setup the display and buffer
is31 = Adafruit_RGBMatrixQT(i2c, allocate=PREFER_BUFFER)
# setup the buffer
fbuff = IS31FrameBuffer(is31)

hello = "Hello World! \x03\x04\x05\x06"
scroller = Scroller(fbuff, hello, 0xFF8000, 0)
scroller2 = Scroller(fbuff, hello, 0xFF0080, 0)

while True:
    try:
        while scroller.update():
            pass
        while scroller2.update():
            pass
    except OSError:
        print("Error")
