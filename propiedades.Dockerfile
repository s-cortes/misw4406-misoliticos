FROM python:3.10

EXPOSE 3000/tcp

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel

RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy

COPY . .

CMD [ "flask", "--app", "./src/propiedades/api", "run", "--host=0.0.0.0", "--port=3000"]
