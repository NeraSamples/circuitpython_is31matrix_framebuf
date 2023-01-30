# SPDX-FileCopyrightText: 2023 Neradoc https://neradoc.me
# SPDX-License-Identifier: MIT
"""
"""
import adafruit_framebuf
from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT

def rgb_matrix_qt_mapping():
    mapping = [0] * (13*9*3)
    i = 0
    for y in range(9):
        for x in range(13):
            (b, g, r) = Adafruit_RGBMatrixQT.pixel_addrs(x,y)
            for z in (r, g, b):
                mapping[i] = z
                i = i + 1
    return mapping

class IS31Buffer:
    def __init__(self, is31, mapping):
        self.is31 = is31
        self.mapping = mapping

    def __len__(self):
        return len(self.is31)

    def __setitem__(self, index, val):
        if isinstance(index, slice):
            start, stop, step = index.indices(13*9*3)
            for val_i, in_i in enumerate(range(start, stop, step)):
                self.is31[self.mapping[in_i]] = val[val_i]
        else:
            self.is31[self.mapping[index]] = val

def IS31FrameBuffer(is31):
    is31_buffer = IS31Buffer(is31, rgb_matrix_qt_mapping())
    return adafruit_framebuf.FrameBuffer(
        is31_buffer, 13, 9,
        adafruit_framebuf.RGB888
    )
