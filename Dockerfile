FROM python:3.10-slim

WORKDIR /app

COPY mtcars.csv train_model.py app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN python train_model.py

EXPOSE 8080

CMD ["python", "app.py"]