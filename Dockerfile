FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY ./app /app
WORKDIR /app
RUN pip instal poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

EXPOSE 80
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]