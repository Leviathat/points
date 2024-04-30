FROM python:3.11.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --ignore-installed six watson-developer-cloud

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
