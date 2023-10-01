FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY ./app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]