FROM python:3.8-slim
WORKDIR /app
# RUN apk add --no-cache build-base

# COPY app.py .
# COPY gendocx.py .
# COPY requirements.txt .
COPY . .

RUN python -m pip install --upgrade pip
# RUN pip install lxml
RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn app:app --host 0.0.0.0 