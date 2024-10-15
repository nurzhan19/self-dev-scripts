FROM python:3.12

WORKDIR /app

COPY randomSeed.py .

ENTRYPOINT ["python", "randomSeed.py"]
