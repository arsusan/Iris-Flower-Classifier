FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN python train_model.py

EXPOSE 5000
CMD ["python", "app.py"]
