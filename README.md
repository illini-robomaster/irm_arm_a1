# Introduction
This library is used for the communication between PC and the motor control board, so that the user can control the motors by PC. This library includes Linux and Windows version, where the Linux version also support ROS. And we offer the usage examples of C, C++ and Python.

# Dependencies
* [CMake](http://www.cmake.org) (version 2.8.3 or higher)
  
# Files
## /lib
Including the library files of Linux and Windows separately. If you wish to use the SDK under ARM32/64, please modify the CMakeList manually to select the correst `.so` file.
## /include
Including the header files. Where ```LSerial.h``` contains the declarations of serial port operation functions. The ```motor_msg.h``` contains the command structure for motor communication. The ```motor_ctrl.h``` contains the encoding and decoding functions.
## /src
Including the example source files of C and C++. The example can control motors to run under desired command for desired time, and then stop. Please watch out that only the check.c is the full control example with all functions. check.cpp and also the Python example do not contain some comments and important tutorials.
## /script
Including the example source files of Python. This example's function is same with the C/C++ example. The ```typedef.py``` declares the data structure of all library functions and structures in Python style, so that the ```check.py``` can call the library correctly.
## /unitree_motor_ctrl
It is a package of ROS and the library file is just the library file of Linux.

# Usage
## C/C++ under Liunx
### Build
```
mkdir -p build
cd build
cmake ..
make
```
### Run
- Have appropriate permissions
- Ubuntu: `sudo usermod -aG dialout $USER`
- Arch: `sudo usermod -aG uucp`
```
cd ../dist
./check_c
```
and
```
cd ../dist
./check_cpp
```
## Python under Linux
```
python3 scripts/check.py
```

## C/C++ under ROS
### Build
Under the catkin workspace, run:
```
catkin_make
```
### Run
As we cannot use ```sudo rosrun```, please run as follows:

First, at a terminal, run:
```
roscore
```
In another terminal, run:
```
sudo su
source devel/setup.bash
rosrun unitree_motor_ctrl unitree_motor_ctrl_node
```
## Python under ROS
First, at a terminal, run:
```
roscore
```
In another terminal, run:
```
sudo su
source devel/setup.bash
rosrun unitree_motor_ctrl check.py
```
## C/C++ under Windows
### Build
We take MinGW as an example. First, select the "MinGW Makefiles" in CMake GUI and generate the makefiles to ```build``` directory. Then open the cmd.exe, run:
```
cd build
mingw32-make.exe
```
### Run
Put the generated .exe file(/bin) and the .dll file(/lib) to same directory, and double click the .exe file to run.
## Python under Windows
Open the cmd.exe, then:
```
cd script
check.py
```
