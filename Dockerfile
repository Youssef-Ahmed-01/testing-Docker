FROM youssefahmed01/alpask:v1.0

WORKDIR /home/hello

RUN python3 -m venv venv

COPY requirements.txt .

RUN ./venv/bin/pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["./venv/bin/python3", "app.py"]

