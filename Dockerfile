FROM python:3.10
EXPOSE 5001
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
