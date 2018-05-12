FROM python:3

WORKDIR /usr/src/web

COPY requirements.txt .

COPY requirements requirements

RUN pip install -r requirements.txt

COPY . .

RUN groupadd -r python && useradd --no-log-init -r -g python python
RUN chown -R python /usr/src/web

USER python