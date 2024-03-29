FROM python:3.10
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python3", "app.py"]
