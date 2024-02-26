FROM python:3.10

ADD ./src ./src
COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel

RUN pip install --no-cache-dir -r pipenv
RUN pipenv install --system --deploy


EXPOSE 5000/tcp

ENTRYPOINT [ "flask" ]
CMD [ "--app", "src/propiedades", "run", "-h", "0.0.0.0", "-p", "5000" ]
