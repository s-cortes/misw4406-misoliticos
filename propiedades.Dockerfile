FROM python:3.9

EXPOSE 3001/tcp

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel

RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy

COPY . .

CMD [ "flask", "--app", "./src/propiedades/api/propiedades", "run", "--host=0.0.0.0", "-p", "3001"]
