# MISW4406-misoliticos
Repositorio con la aplicación de Propiedades de los Alpes, creada durante el curso de Aplicaciones no monolíticas

## Integrantes

* Santiago Cortés Fernández [s.cortes@uniandes.edu.co](mailto:s.cortes@uniandes.edu.co)

## Estructura del código

El proyecto sigue los líneamiento de creación de DDD, facilitando la implementación de un lenguaje ublicuo dentro del código de la aplicación. Ademas, cada microservicio sigue una división por capas, a continucación se explica la estructura de carpetas de src:
```bash 

📦propiedades
 ┣--- 📂application
 ┃    ┣--- 📂commands
 ┃    ┃    ┣--- 📜__init__.py
 ┃    ┃    ┣--- 📜base.py
 ┃    ┃    ┗--- 📜create_propiedad.py
 ┃    ┣--- 📂queries
 ┃    ┃    ┣--- 📜__init__.py
 ┃    ┃    ┣--- 📜base.py
 ┃    ┃    ┣--- 📜get_propiedad.py
 ┃    ┃    ┣    📜get_propiedades.py
 ┃    ┣--- 📜__init__.py
 ┃    ┣--- 📜dtos.py
 ┃    ┣--- 📜handlers.py
 ┃    ┗--- 📜mappers.py
 ┣--- 📂domain
 ┃    ┣--- 📜__init__.py
 ┃    ┣--- 📜entities.py
 ┃    ┣--- 📜events.py
 ┃    ┣--- 📜exceptions.py
 ┃    ┣--- 📜factories.py
 ┃    ┣--- 📜repositories.py
 ┃    ┣--- 📜rules.py
 ┃    ┗--- 📜value_objects.py
 ┣--- 📂infrastructure
 ┃    ┣--- 📂schema
 ┃    ┃    ┣--- 📂v1
 ┃    ┃    ┃    ┣--- 📜__init__.py
 ┃    ┃    ┃    ┣--- 📜commands.py
 ┃    ┃    ┃    ┣--- 📜events.py
 ┃    ┃    ┃    ┗--- 📜mappers.py
 ┃    ┃    ┗--- 📜__init__.py
 ┃    ┣--- 📜__init__.py
 ┃    ┣--- 📜consumers.py
 ┃    ┣--- 📜dispartchers.py
 ┃    ┣--- 📜dtos.py
 ┃    ┣--- 📜exceptions.py
 ┃    ┣--- 📜factories.py
 ┃    ┣--- 📜mappers.py
 ┃    ┗--- 📜repositories.py
 ┣--- 📂presentation
 ┃    ┣--- 📜__init__.py
 ┃    ┗--- 📜api.py
 ┗--- 📜README.md
```

## Build & Deployment | Docker Compose

```bash
$ # Primero, clone el repositorio con el comando
$ git clone https://github.com/s-cortes/misw4406-misoliticos.git
$ cd misw4406-misoliticos
$
$ # Use Docker Compose CLI para correr el microservicio
$ docker compose up --build -d broker-standalone
$ docker compose up --build -d propiedades-api
$
$ # Acceda a la interfaz desde postman: http://127.0.0.1:3001/
$
$ # Cuando termina remueva los contenedores, imagenes y volumenes
$ docker compose down -v --rmi local
$
```

<br />

## Interfaces

Cada uno de los endpoints puede ser usado empleando los siguientes cURLs

```bash
# Crear inmueble
curl --location 'http://127.0.0.1/:5000/catastrales/inmueble' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fecha_creacion": "2024-01-01T13:11:00Z",
    "entidad": "Minorista",
    "tipo_construccion": "Comercial",
    "fotografias": [
        {
            "contenido": "1234131514214132412",
            "tipo": "JPEG",
            "descripcion": "pruebassss",
            "nombre": "principal"
        }
    ]
}'

# Obtener inmueble
curl --location 'http://127.0.0.1/:3001/propiedades/<id>' \
```