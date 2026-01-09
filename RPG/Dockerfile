FROM python:3.9
WORKDIR /RPG

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
COPY sitev3.html .
COPY static ./static/


COPY BDD/sql_quest.sql /sql/sql_quest.sql 
COPY BDD/BDD.sql.sha256 /sql/BDD.sql.sha256 
WORKDIR /sql
RUN sha256sum -c BDD.sql.sha256

EXPOSE 5000
CMD ["python", "main.py"]