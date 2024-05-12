FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask pymysql
ENTRYPOINT ["python"]
CMD ["app.py"]
