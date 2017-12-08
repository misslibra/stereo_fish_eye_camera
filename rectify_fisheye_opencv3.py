import os,cv2
## 
import cv2.calibration
import numpy as np
import xml.dom.minidom

##########    fisheyes example
# img_l = cv2.imread('/cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/imgs/left1.jpg')

# Camera_Matrix_left = np.zeros((3,3))
# Camera_Matrix_left[0] = [2.2750890078043116e+02, 0., 4.7238736249088845e+02]
# Camera_Matrix_left[1] = [0.,2.2702663646882499e+02, 3.0739903020948299e+02]
# Camera_Matrix_left[2] = [0,0,1]
# # Distortion_Coefficients_left = np.zeros((4,1))
# # Distortion_Coefficients_left[:,0] = (1.2861344366039267e-02, 2.6453453373951994e-03, -5.8473922029335891e-03, 1.2480849549148254e-03)

# Distortion_Coefficients_left = np.zeros(4)
# Distortion_Coefficients_left[:] = (1.2861344366039267e-02, 2.6453453373951994e-03, -5.8473922029335891e-03, 1.2480849549148254e-03)

# ###   undistort with Camera_Matrix and Distortion_Coefficients
# undistort_frame_left = img_l.copy()
# h, w = undistort_frame_left.shape[:2]  
# newcameramtx, roi = cv2.getOptimalNewCameraMatrix(Camera_Matrix_left,Distortion_Coefficients_left,(w,h),1,(w,h))  #### add
# # undistort_frame_left = cv2.undistort(img_l,Camera_Matrix_left, Distortion_Coefficients_left )
# undistort_frame_left = cv2.undistort(img_l,Camera_Matrix_left, Distortion_Coefficients_left,None,newcameramtx)
# # roi_image = undistort_frame_left[:,:]
# print "rectify ok !"
# cv2.imwrite('/cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/result/left1.bmp',undistort_frame_left)



assert float(cv2.__version__.rsplit('.', 1)[0]) >= 3, 'OpenCV version 3 or newer required.'
####  example
# K = np.array([[  2.2750890078043116e+02, 0., 4.7238736249088845e+02],
#               [    0.  ,   2.2702663646882499e+02, 3.0739903020948299e+02],
#               [    0.  ,     0.  ,     1.  ]])

# # zero distortion coefficients work well for this image
# D = np.array([1.2861344366039267e-02, 2.6453453373951994e-03, -5.8473922029335891e-03, 1.2480849549148254e-03])

# ######  donghua_1 param
# K = np.array([[  7.2512703456484553e+02, 0., 1.3084379859812832e+03],
#               [    0.  ,   7.2444418376279964e+02, 9.5961031123063265e+02],
#               [    0.  ,     0.  ,     1.  ]])

# # zero distortion coefficients work well for this image
# D = np.array([-2.9814828361951921e-02, -4.7684884926221327e-03,-1.2196199537986071e-03, 1.1378548557740654e-04])

######  donghua_2 param
K = np.array([[  7.2512703456484553e+02, 0., 1.3084379859812832e+03],
              [    0.  ,   7.2444418376279964e+02, 9.5961031123063265e+02],
              [    0.  ,     0.  ,     1.  ]])

# zero distortion coefficients work well for this image
D = np.array([-2.9814828361951921e-02, -4.7684884926221327e-03,-1.2196199537986071e-03, 1.1378548557740654e-04])

# use Knew to scale the output
Knew = K.copy()
Knew[(0,1), (0,1)] = 0.4 * Knew[(0,1), (0,1)]


# img = cv2.imread('C:/Users/lenovo/Desktop/fisheye-stereo-calibration-master/DongHuaFisheyecamera/left9.jpg')
img = cv2.imread('/cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/DongHuaFisheyecamera/left2.jpg')

img_undistorted = cv2.fisheye.undistortImage(img, K, D=D, Knew=Knew)
# img_undistorted = cv.fisheye.undistortImage(img, K, D=D, Knew=Knew)

row = img_undistorted.shape[0]
col = img_undistorted.shape[1]

clip_img = img_undistorted[int(0.25*row):int(0.75*row),int(0.25*col):int(0.75*col),:]

# cv2.imwrite('C:/Users/lenovo/Desktop/fisheye-stereo-calibration-master/result/left9_clip_1.bmp', clip_img)
cv2.imwrite('/cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/result/left9___clip_1.bmp', clip_img)

#cv2.imshow('undistorted', img_undistorted)
#cv2.waitKey()
