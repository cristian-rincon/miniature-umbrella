FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY ./app /app
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

EXPOSE 80
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]