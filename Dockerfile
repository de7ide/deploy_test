FROM python:3.11-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /deploy_test
COPY requirements.txt .
RUN pip install --no-cache -r /deploy_test/requirements.txt
COPY bot /deploy_test/bot
CMD ["python", "-m", "bot"]