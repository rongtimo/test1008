Swiper
======

项目初始化

```shell
git clone https://github.com/bj-py1903/swiper.git
cd swiper
python -m venv .venv
source .venv/bin/activate
pip install django==1.11.18 gunicorn gevent redis==2.10.6 celery ipython requests
pip freeze > requirment.txt
django-admin startproject swiper ./
git add ./
git commit -m 'first commit'
git push
```
