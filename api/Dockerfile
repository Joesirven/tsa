FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py

# Copy all of the subdirectories in your service's directory
# Modify these instructions to do that
# COPY queries queries
# COPY routers routers

RUN python -m pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port 80
