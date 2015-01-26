#!/usr/local/bin/python
# coding : utf-8 -*-
# file name : PSD2Cocos.py
# author : Albin
# created at : Wed Sep  3 13:56:17 2014
# Copyright (c) iuixi.com

import os, sys, getopt
from PIL import Image, ImageChops
from psd_tools import PSDImage, Group, Layer
from Sprite import *
import tenjin
from tenjin.helpers import *
from tenjin.html import *

class PSD2Cocos():
    def __init__(self, psd, pname = 'demo', mode='-auto'):
        self.mode = mode
        self.projectName = pname
        self.children = []
        self.psd = psd;
        self.width = psd.header.width
        self.height = psd.header.height
        self.parsePsd(self.psd)

    def getString(self):
        engine = tenjin.Engine()
        return  engine.render('json/ui.json', {
            "height" : self.height, 
            "width" : self.width,
            "children" : self.children
            })

    def bbox2Pos(self, bbox):
        w, h = bbox[2] - bbox[0], bbox[3]- bbox[1]
        x, y = bbox[0] + w / 2, self.height - bbox[1]
        y = y - h / 2
        return x, y, w, h

    def addChild(self, parent, name, cc_type, box):
        sp = Sprite()
        sp.setTexture(name + '.png')
        sp.setRect(box)
        self.children.append(sp)

    def parsePsd(self, psd, parent = None):
        if isinstance(psd, Layer):
            names = psd.name.split(':')
            name = ''
            cc_type = 'Sprite'
            if len(names) == 2:
                name = names[0]
                cc_type = names[1]
            else:
                name = names[0]
            image = psd.as_PIL()
            image.save(self.projectName + "/Resources/" + name+'.png')

            self.addChild(parent, name, cc_type,  self.bbox2Pos(psd.bbox))

        elif isinstance(psd, Group):
            for i in psd.layers[::-1]:
                self.parsePsd(i, name)

        else:
            for i in psd.layers[::-1]:
                self.parsePsd(i, parent)


if __name__ == '__main__':
    args = sys.argv[1:]
    projectName = args[0].split('.')[0]
    psd = PSDImage.load(args[0])
    if(not os.path.isdir(projectName)):
        os.mkdir(projectName)
    if(not os.path.isdir(projectName + "/Resources")):
        os.mkdir(os.path.abspath(projectName + "/Resources"))
    if(not os.path.isdir(projectName + "/Json")):
        os.mkdir(os.path.abspath(projectName + "/Json"))
    tool = PSD2Cocos(psd, projectName, '-auto')

    f = open(projectName + "/Json/" + projectName + "_1.json", 'w')
    f.write(tool.getString())
    f.close()

    engine = tenjin.Engine()
    ui = engine.render('json/project.xml', {
        "height" : tool.height, 
        "width" : tool.width,
        "project_name" : projectName,
        "work_space" : os.path.abspath(os.getcwd() + '/' + projectName)
        })

    f = open(projectName + "/" + projectName + '.xml.ui', 'w')
    f.write(ui)
    f.close()
