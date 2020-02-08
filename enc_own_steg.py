# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:43:44 2020

@author: cgpra
"""
import PIL.Image as Image
import numpy as np
im = Image.open('Adventure.jpeg', 'r')
width, height = im.size
pix_val = list(im.getdata())
pix = list(im.getdata())
tot_w_len = np.floor(len(pix)/8)
def genData(data): 
        dat = []  
        for i in data: 
            dat.append(format(ord(i), '08b')) 
        return dat
dat = genData(input("enter the string to be encoded\nmax size:"+ str(tot_w_len) +"\n") + '~')
act_bin =[]
for i in range(0,len(dat)):
    for j in range(0,8):
        act_bin.append(int(dat[i][j]))

for i in range(0,len(act_bin)):
    if (pix[i][0]%2)!=0 and act_bin[i]==0 :
        y=pix[i][0]
        y &= ~0x01
        pix_val[i] = (y,pix[i][1],pix[i][2])
    elif (pix[i][0]%2)==0 and act_bin[i]==1:
        y=pix[i][0]
        y |= 0x01
        pix_val[i] = (y,pix[i][1],pix[i][2])
img=Image.new(mode = "RGBA",size=(width,height))
img.putdata(pix_val)
img.save("changedImg.png")
img.show()