## OpenCV C++ Stereo Fisheye Calibration

This contains a source file to calibrate a stereo system comprising of fisheye lenses. It calibrates the extrinsics and the intrinsics of the cameras without any initial guesses. If you are looking for stereo calibration with lenses which follow the pinhole model check [here](https://github.com/sourishg/stereo_calibration).

### Dependencies

- OpenCV
- popt

### Compilation

Compile all the files using the following commands.

```bash
mkdir build && cd build
cmake ..
make
```

Make sure your are in the `build` folder to run the executables.

### Data

Some sample calibration images are stored in the `imgs` folder.

### Running calibration

Run the executable with the following command

```bash
./calibrate -w [board_width] -h [board_height] -s [square_size] -n [num_imgs] -d [img_dir] -l [left_img_prefix] -r [right_img_prefix] -o [calib_file]
```

For example if you use the images in the `imgs` folder run the following command

```bash
# ./calibrate -w 9 -h 6 -s 0.02423 -n 29 -d ../imgs/ -l left -r right -o cam_stereo.yml
./calibrate -w 9 -h 6 -s 0.041 -n 25 -d ../DongHuaFisheyecamera/ -l left -r right -o cam_stereo.yml
注意 要改 -n 25 
../DongHuaFisheyecamera/
./calibrate -w 9 -h 6 -s 0.041 -n 23 -d /cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/2017-12-08_donghua_2/ -l left -r right -o cam_stereo.yml


```

## cindy comment
这个代码比较不灵活，标定图片必须严格准照左图右图在同一个文件夹，并且已left right开头命名，后面必须严格是1 2 3 ...的顺序
这个是双目的标定，暂时用左右相同的图片来做单目的标定，

另外，fisheye模块在opencv2版本中，只有c++版本，没有python版本。想要在python中调fisheye模块只能是下载opencv3


############  debug
westwell@cindy:/cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/build$ ./calibrate -w 9 -h 6 -s 0.041 -n 25 -d /cv/cindy/stereo_vision/calibration_rectify/fisheye-stereo-calibration-master/DongHuaFisheyecamera/  -l left -r right -o cam_stereo.yml
OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor, file /home/westwell/opencv-2.4.13/modules/imgproc/src/color.cpp, line 3739
terminate called after throwing an instance of 'cv::Exception'
  what():  /home/westwell/opencv-2.4.13/modules/imgproc/src/color.cpp:3739: error: (-215) scn == 3 || scn == 4 in function cvtColor

Aborted (core dumped)
----------- 输入图片格式出错。没有后缀的点

OpenCV Error: Assertion failed (svd.w.at<double>(0) / svd.w.at<double>((int)svd.w.total() - 1) < thresh_cond) in CalibrateExtrinsics, file /home/westwell/opencv-2.4.13/modules/calib3d/src/fisheye.cpp, line 1401
terminate called after throwing an instance of 'cv::Exception'
  what():  /home/westwell/opencv-2.4.13/modules/calib3d/src/fisheye.cpp:1401: error: (-215) svd.w.at<double>(0) / svd.w.at<double>((int)svd.w.total() - 1) < thresh_cond in function CalibrateExtrinsics

Aborted (core dumped)
----------图片的长宽比被改变，导致obj.push_back(Point3d(double( (float)j * square_size ), double( (float)i * square_size ), 0));
按照这个公式算的时候找不到点。标定失败。   尝试按照原图长款比缩小图片,重新标定。

###########
[100%] Linking CXX executable calibrate
/usr/bin/ld: cannot find -lopencv_dep_cudart
------ 解决方法：
got rid of the error by adding set(CUDA_USE_STATIC_CUDA_RUNTIME OFF) to my CMakeLists.txt file or running in shell with: 
cmake .. -DCUDA_USE_STATIC_CUDA_RUNTIME=OFF.