FROM python:3.10

WORKDIR /app

ADD ./src ./src
COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel

RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy

ENV FLASK_APP=./src/propiedades/api/__init__.py

EXPOSE 5000/tcp

CMD [ "flask","--app", "src/propiedades/api", "run", "-h", "0.0.0.0", "-p", "5000" ]
