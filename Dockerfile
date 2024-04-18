FROM python:3.12

COPY . /Start

WORKDIR /Start

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "DjangoStart/manage.py", "runserver", "0.0.0.0:8000"]