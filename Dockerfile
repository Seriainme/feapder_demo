# 使用官方 Python 运行时作为基础镜像
FROM python:3.9-slim

# 更新 apt
RUN apt-get update && apt-get -y install net-tools

# 更新 pip
RUN pip install --upgrade pip -i https://pypi.doubanio.com/simple

# 安装 pipenv
RUN pip install pipenv -i https://pypi.doubanio.com/simple

# 设置工作目录
WORKDIR /app

# 复制 Pipfile 和 Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# 安装依赖
RUN pipenv install --system --deploy --ignore-pipfile -vv

# 复制项目文件
COPY . /app

# 设置 PYTHONPATH
ENV PYTHONPATH="/app"

# 运行爬虫脚本
CMD ["python", "spider.py"]
