FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Add user (see link for how to do so )
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

COPY ./ ./ 

CMD ["python", "main.py"]
