FROM python:3.9.13

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y sudo

WORKDIR /simulator

#kopiranje svih fajlova i foldera
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./Program.py"]
