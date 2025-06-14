# 使用Python 3.10作为基础镜像 
FROM python:3.10.17-slim-bookworm
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip
WORKDIR /hitokoto
COPY ./ /hitokoto
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
