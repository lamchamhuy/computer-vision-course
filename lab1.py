import cv2
import os

# đọc ảnh
img = cv2.imread(os.path.join('.', 'img_data', 'anhchim2.png'))

#Truy cập và chỉnh sửa giá trị pixel.
px = img[100,100]
print(px)

# accessing only red pixel
red = img[100,100,2]
print(red)

# sửa đổi giá trị pixel
img[100,100] = [255,255,255]
print("màu trắng",img[100,100])

#Truy cập thuộc tính hình ảnh
print("số hàng, số cột , kênh màu",img.shape)

# Total number of pixels is accessed by img.size:
print(img.size)

#Kiểu dữ liệu hình ảnh
print(img.dtype)

#Vùng quan tâm hình ảnh (Image ROI)
head = img[108:267, 502:687]
img[120:279, 150:335] = head

# Tách và ghép các kênh hình ảnh
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# ===== TẠO VIỀN =====
replicate = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255,0,0])  # viền xanh dương

# ===== HIỂN THỊ =====
cv2.imshow('original', img)
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)
# show ảnh
# cv2.imshow('anh dep', img)
# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('red', r)
cv2.waitKey(0)