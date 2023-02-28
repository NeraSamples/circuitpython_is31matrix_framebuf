# SPDX-FileCopyrightText: 2023 Neradoc https://neradoc.me
# SPDX-License-Identifier: MIT
"""
A scroller for the hacky scrolling on the IS31FL3741 13x9 Matrix
https://www.adafruit.com/product/5201
"""
import time
from adafruit_ticks import ticks_ms, ticks_less

class Scroller:
    def __init__(self, buff, text, color, delay):
        self.buff = buff
        self.text = text
        self.color = color
        self.delay = delay * 1000 # ms
        self.last_update = 0
        self.char = 0
        self.step = 0
        self._start()
    def _start(self):
        if self.char == 0:
            self.step = 13
        else:
            self.step = 0
    def update(self):
        if ticks_less(ticks_ms(), self.last_update):
            return True
        self.last_update = ticks_ms() + self.delay
        if self.char == len(self.text):
            self.char = 0
            self._start()
            return False
        end = -6
        if self.step <= end:
            self.char += 1
            self._start()
        self.buff.buf.is31.fill(0)
        self.buff.text(
            self.text[self.char:self.char+4],
            self.step, 1, self.color
        )
        self.buff.buf.is31.show()
        self.step -= 1
        return True
