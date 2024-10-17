# DIVP project 数字图像与视频处理 

## setup 
1. 使用docker image 为lxn_d2l:1.0，Dockerfile为[Dockerfile](./Dockerfile)
可以在dockerfile的基础上继续定制image，构建更合适的镜像

2. 默认使用ALL GPU， 文件挂载点为该项目根目录，挂载位置为`/root/DIVP_project` 

3. 容器GUI窗口可视化，获取宿主机IP地址为`host_ip` , 在容器设置以下环境变量，（若为WSL+dockerdesktop需要在window启动xlaunch，即xserver）
```shell
export DISPLAY=<host_ip>:0.0
```
使用x11-apps中的xeyes进行测试
```shell
apt-get update
apt-get install x11-apps
xeyes
```
## dependencies
**python pkg** 
```shell
pip install opencv-python
pip install opencv-python-headless
```
**apt pkg**
```shell
apt-get install libgtk2.0-dev pkg-config -y
apt-get install ffmpeg libsm6 libxext6  -y
apt-get install libgl1 -y
# for export ipynb file to PDF formate
apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic -y
```

## 其他
附上一张数字图像处理经典图像

![lena](./project02/proj02-images/lena_std.bmp)

> 这张图给人有种迷离的感觉
