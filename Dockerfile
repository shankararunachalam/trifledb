FROM python:3-slim

WORKDIR /trifledb

RUN apt update && apt install -y curl net-tools

COPY requirements.txt /trifledb/requirements.txt

RUN pip3 install --no-cache-dir -r /trifledb/requirements.txt

COPY ./app /trifledb/app

EXPOSE 8000

CMD ["uvicorn", "app.trifledb_server:app", "--host", "0.0.0.0"]
