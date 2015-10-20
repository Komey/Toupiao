—————————————————————————————————————————————

Django的一个运行容器
使用Nginx和uWSGI作为运行环境

概念部分就不过多的赘述了，亲们自行度娘即可

—————————————————————————————————————————————

Dockerfile使用方法：

首先请将此Dockerfile clone到本地
git clone https://github.com/Komey/Django-on-Docker.git

构建本地镜像
sudo docker build -t komeydjango .

运行容器
sudo docker run -d komeydjango

—————————————————————————————————————————————

使用现有代码构建镜像

Ptyhon应用的代码文件，请存放在/app文件夹下，并确保manage.py文件在此文件夹下

Github的上的源码中已包含文件夹的目录结构信息，请查看https://github.com/Komey/Django-on-Docker

/app文件夹下默认带有requirements.txt，该文件记录了你的Python应用所须运行库，在构建时会通过PIP安装文件中的依赖


—————————————————————————————————————————————

镜像使用方法

docker pull index.alauda.cn/lmh5257/django-on-docker

docker run -p 80 -d -e MODULE=myapp index.alauda.cn/lmh5257/django-on-docker

使用本地应用

docker run -p 80 -d -e MODULE=myapp -v /home/komey/myapp:/home/docker/code/app index.alauda.cn/lmh5257/django-on-docker

—————————————————————————————————————————————

可选环境变量：

MODULE = Python应用名（默认为website）

ROOT_PASS = root用户密码（默认随机生成，请查看Log）
—————————————————————————————————————————————

更多功能 持续更新ing