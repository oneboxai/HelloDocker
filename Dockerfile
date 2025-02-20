# 1. 使用官方 Python 作为基础镜像
FROM python:3.10
# 2. 设置工作目录
WORKDIR /app
# 3. 复制当前目录到容器中
COPY . /app
# 4. 安装依赖
RUN pip install -r requirements.txt
# 5. 运行程序
CMD ["python", "Hello.py"]
