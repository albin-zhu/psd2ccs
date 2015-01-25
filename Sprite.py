#!/usr/bin/python
# -*- coding : utf-8 -*-
# file name : ImageOptions.py
# author : albin
# created at : Sun Jan 25 17:40:30 2015
# Copyright (c) iuixi.com

import json
import tenjin
from tenjin.helpers import *
from tenjin.html import *

class Sprite(dict):
    def __init__(self, parent = None):
        self.parent = parent
        self.ax = 0.5
        self.ay = 0.5
        self.height = 0
        self.width = 0
        self.px = 0
        self.py = 0
        self.path = ""
        self.children = []

        if parent:
            parent.children.append(self.data)

    def setTexture(self,  t):
        self.path = t
    
    def getPos(self):
        x = self.x - self.width * self.ax
        y = self.y - self.height * self.ay
        return x, y

    def getGlobalPostion(self):
        sp = self
        x, y = self.getPos()
        while(sp.parent):
            sp  = sp.parent
            x1, y1 = sp.getPos()
            x -= x1
            y -= y1
        return x,  y

    def setRect(self, box):
        x,y,w,h = box
        self.width = w
        self.height = h

        if(self.parent):
            gx, gy = self.parent.getGlobalPostion()
            pw = self.parent.width
            ph = self.parent.height
            self.x = x - gx
            self.y = y - gy
            self.px = float(self.x) / float(pw)
            self.py = float(self.y) / float(ph)
        else:
            self.x, self.y = x,y

    def setAnchorPoint(self, x, y):
        self.ax = x
        self.ay = y

    def getData(self):
        return {
            "height" : self.height, 
            "width" : self.width,
            "ax" : self.ax,
            "ay" : self.ay,
            "px" : self.px,
            "py" : self.py,
            "x" : self.x,
            "y" : self.y,
            "path" :  self.path
        }
