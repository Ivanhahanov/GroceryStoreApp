FROM python:3.8-alpine
MAINTAINER Ivan Hahanov 'hahanov.i@explabs.ru'
RUN pip install fastapi uvicorn
EXPOSE 80
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app /api
CMD ["uvicorn", "api.app.server:app", "--host", "0.0.0.0", "--port", "80", "--reload"]