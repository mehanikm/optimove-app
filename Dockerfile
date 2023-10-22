FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["/usr/local/bin/python3"]
CMD ["main.py"]

EXPOSE 8080
