FROM python:3.10.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn" , "main:app", "--host", "0.0.0.0", "--port", "8000" ]