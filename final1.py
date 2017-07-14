import cv2

img = cv2.imread('aggregate.png')
res = cv2.imread('aggregate.png')
x,y,z = img.shape
val = 0
n=y/4
for i in range(x):
	chk = img[:,:y/2]
	t = chk[:i,:]
	res[x-i:x,n:y/2+n] = t
	cv2.imwrite("/home/pravar/opencvpics/"+str(val).zfill(3)+".jpeg",res)
	val = val + 1