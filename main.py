import numpy as np
import cv2
import matplotlib.pyplot as plt
from Mozaik import *

# reads image
img_BGR = cv2.imread('Images/fruts.jpg')
img_RGB = img_BGR[:, :, ::-1] #reverse BGR to RGB

# extract channels
b, g, r = cv2.split(img_BGR)
zer = np.zeros(b.shape, dtype=b.dtype)

r_m, g_m, b_m = mozaik(r, g, b)
r_r, g_r, b_r = restore_chanels_RGB(r_m, g_m, b_m)

plt.figure(figsize=[20, 5])
# Каналы оригинального изоброжения
plt.subplot(341)
plt.imshow(cv2.merge((r, zer, zer)), )
plt.title("Red Channel")
plt.subplot(342)
plt.imshow(cv2.merge((zer, g, zer)))
plt.title("Green Channel")
plt.subplot(343)
plt.imshow(cv2.merge((zer, zer, b)))
plt.title("Blue Channel")
# Собираем по 3м каналам
plt.subplot(344)
imgMerged = cv2.merge((r, g, b))
plt.imshow(imgMerged)
plt.title("Merged Output")

# RAW каналы
plt.subplot(345)
plt.imshow(cv2.merge((r_m, zer, zer)), )
plt.subplot(346)
plt.imshow(cv2.merge((zer, g_m, zer)))
plt.subplot(347)
plt.imshow(cv2.merge((zer, zer, b_m)))
# Собираем по 3м каналам
plt.subplot(348)
imgMerged_m = cv2.merge((r_m, g_m, b_m))
plt.imshow(imgMerged_m)


# Востановленные каналы
plt.subplot(349)
plt.imshow(cv2.merge((r_r, zer, zer)), )
plt.subplot(3,4,10)
plt.imshow(cv2.merge((zer, g_r, zer)))
plt.subplot(3,4,11)
plt.imshow(cv2.merge((zer, zer, b_r)))
# Собираем по 3м каналам
plt.subplot(3,4,12)
imgMerged_r = cv2.merge((r_r, g_r, b_r))
plt.imshow(imgMerged_r)


plt.show()
