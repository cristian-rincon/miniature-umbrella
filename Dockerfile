FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY . /
WORKDIR /
RUN pip install -r app/requirements.txt

EXPOSE 80
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]