FROM python:3.9
WORKDIR /RPG

COPY requirements.txt .
COPY main.py .
COPY index.html .
COPY style.css .

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]
