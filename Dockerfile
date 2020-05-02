FROM python:3.5.2

RUN mkdir -r /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python3", "Engine.py"]
# Haven't finished Dockerfile yet