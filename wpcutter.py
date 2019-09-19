#!/usr/bin/env python3

import sys
from PIL import Image, ImageFilter

monitors = [{"width":1680, "height":1050}, {"width":2560, "height":1080}, {"width":1920, "height":1080}]

global fullMonitorWidth
fullMonitorWidth = 0
for monitor in monitors:
    fullMonitorWidth += monitor["width"]

global maxMonitorHeight
maxMonitorHeight = 0
for monitor in monitors:
    if maxMonitorHeight < monitor["height"]:
        maxMonitorHeight = monitor["height"]

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        paddingWidth = 0
        paddingHeight = 0
        if(len(sys.argv) == 3):
            paddingWidth = int(sys.argv[2])
        if(len(sys.argv) == 4):
            paddingHeight = int(sys.argv[3])

        imgpath = sys.argv[1]
        im = Image.open(imgpath)
        fullImgWidth, fullImgHeight = im.size
        if fullImgHeight >= maxMonitorHeight:
            if fullMonitorWidth <= fullImgWidth:
                widthMargin = fullImgWidth - fullMonitorWidth

                leftMargin = widthMargin / 2 - paddingWidth
                rightMargin = widthMargin / 2 + paddingWidth

                heightMargin = fullImgHeight - maxMonitorHeight
                topMargin = heightMargin / 2 - paddingHeight
                botMargin = heightMargin / 2 + paddingHeight

                print("Left Width Margin: " + str(leftMargin))
                print("Right Width Margin: " + str(rightMargin))
                print("Top Height Margin: " + str(topMargin))
                print("Bottom Height Margin: " + str(botMargin))

                box = (leftMargin, topMargin, fullImgWidth - rightMargin, fullImgHeight - botMargin)
                croppedImg = im.crop(box)
                croppedImg.save(imgpath.split(".")[0] + "_cropped.png")

            else:
                print("Image width too small")
        else:
            print("Image height too small")
