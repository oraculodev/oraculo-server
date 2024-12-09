FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# set display port to avoid crash
ENV DISPLAY=:99

# install dependences
RUN pip install --upgrade pip

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

EXPOSE 8000
CMD ["./run-server.sh"]
