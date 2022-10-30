FROM python:3.10

RUN apt update && apt -y install gettext-base

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

EXPOSE 8080

CMD ["python", "./main.py"]