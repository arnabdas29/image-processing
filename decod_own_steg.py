# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:50:12 2020

@author: cgpra
"""

import PIL.Image as Image
im = Image.open('changedImg.png', 'r')
width, height = im.size
pix_val = list(im.getdata())
pix = list(im.getdata())
def binaryToDecimal(n): 
    num = n; 
    dec_value = 0;
    base = 1;  
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value
i=0
bin_ext=0
temp = 'x'
fin_str = ''
while(temp!='~'):
    for j in range(0,8):
        if pix[i][0]%2 == 0:
            bin_ext = bin_ext*10
        else:
            bin_ext = bin_ext*10 + 1
        i+=1
    x=binaryToDecimal(bin_ext)
    temp = chr(x)
    bin_ext = 0
    if temp != '~':
        fin_str = fin_str + temp
print(fin_str)
    
    