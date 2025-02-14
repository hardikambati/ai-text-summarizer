FROM python:3.10.12-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]