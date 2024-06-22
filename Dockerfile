FROM python:3.9-slim
# 更新 apt
RUN apt-get update
RUN apt-get -y install net-tools

# 更新pip
RUN pip install --upgrade pip -i https://pypi.doubanio.com/simple

# 安装pipenv
RUN pip install pipenv -i https://pypi.doubanio.com/simple
WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH="/app"
CMD ["python", "spider.py"]