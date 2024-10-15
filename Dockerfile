FROM python:3.12

WORKDIR /app

COPY randomSeed.py .

CMD ["python", "randomSeed.py", "1000", "100"]
