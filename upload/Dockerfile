FROM python:3.9-slim
WORKDIR /api
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8080 run:app