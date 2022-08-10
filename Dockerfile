FROM python:3.9.4

RUN mkdir -p /root/k8s-web
WORKDIR /root/k8s-web
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 5000
CMD python main.py

