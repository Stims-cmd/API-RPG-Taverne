FROM python:3.9
WORKDIR /RPG

COPY requirements.txt .
COPY main.py .
COPY sitev3.html .
COPY static ./static/
RUN pip install -r requirements.txt

COPY ./BDD/sql_quest.sql /sql/sql_quest.sql
COPY ./BDD/BDD.sql.sha256 /sql/BDD.sql.sha256
RUN sha256sum -c /sql/BDD.sql.sha256


EXPOSE 5000
CMD ["python", "main.py"]
