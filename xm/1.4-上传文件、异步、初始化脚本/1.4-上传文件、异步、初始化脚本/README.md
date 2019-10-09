# Swiper

### 项目初始化

```shell

# github.com 新建项目，公开，选择 .gitignore 文件，license 选 MIT

# clone 代码下来
git clone ...

# 进入目录
cd swiper

# 新建虚拟环境
# 1. virtualenv .venv
# 2. python -m http.venv .venv

# 激活虚拟环境
source .venv/bin/activate

# 安装 django 和相关库
pip install django==1.11.22 gunicorn gevent redis==2.10.6 celery ipython

# 冻结安装版本
pip freeze > requirements.txt

# 新建 django 项目
django-admin startproject swiper ./

# 新建 django app
django-admin startapp user



``


### 本地已有代码的项目，与远程仓库建立关联
```shell
# 进入本地源码目录
cd source_path

# 新建本地仓库
git init

# 添加远程地址
git remote add origin https://github.com/bj-py-2019/1903.git

# 将本地 master 分支与远端 master 建立关联
git branch --set-upstream-to=origin/master master

# 添加用户名和邮件
git config --global user.email "yuzebin@gmail.com"
git config --global user.name "yuzebin"

# 将远端文件拉取下来（忽略无关的文件历史）
git pull origin master --allow-unrelated-histories

# 本地修改了文件
git add .
git commit -m "some changes."

# 第一次将本地分支 master 推送到远端 master 分支
git push --set-upstream origin master

# 以后就可以直接 push 了
git push

```
