#!/usr/bin/env python
# coding: utf-8

# # 作業
# 
# 思考一下我們前面有提到圖片是矩陣，但維度可能會不一樣
# 例如灰階圖只有兩個維度，RGB 彩圖則有 3 個維度
# 
# 假如今天我們把 RGB 3 個維度拆開來看會有甚麼不同的效果呢？

# In[ ]:


import cv2

#data資料夾要跟程式放一起
img_path = 'data/lena.png'

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

#如果只要只有某一channel，其他channel要設為0
#[:,:,012]=[width,height ,bgr]
b=img.copy()
b[:,:,1]=0 #代表紅色通道[1]，長寬像素都為0
b[:,:,2]=0

g=img.copy()
g[:,:,0]=0
g[:,:,2]=0

r=img.copy()
r[:,:,0]=0
r[:,:,1]=0

# 為了要不斷顯示圖片，所以使用一個迴圈(按叉叉關不掉的意思)
while True:
    # 顯示彩圖
    cv2.imshow('bgr', img)
    cv2.imshow('bgr_b', b)
    cv2.imshow('bgr_g', g)
    cv2.imshow('bgr_r', r)


    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
