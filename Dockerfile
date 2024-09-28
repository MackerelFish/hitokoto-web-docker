# 使用Python 3.10作为基础镜像 
FROM python:3.10
RUN pip install --upgrade pip
WORKDIR /hitokoto
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
