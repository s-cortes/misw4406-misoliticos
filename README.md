# MISW4406-misoliticos
Repositorio con la aplicación de Propiedades de los Alpes, creada durante el curso de Aplicaciones no monolíticas

## Integrantes

* Santiago Cortés Fernández [s.cortes@uniandes.edu.co](mailto:s.cortes@uniandes.edu.co)
* Daniela Báez Rincon [m.castros@uniandes.edu.co](mailto:d.baezr@uniandes.edu.co)
* Ivan Mateo Bohorquez Perez [i.bohorquezp@uniandes.edu.co](mailto:i.bohorquezp@uniandes.edu.co)
* Lara Simonetti [l.simonetti@uniandes.edu.co](mailto:l.simonetti@uniandes.edu.co)

## Estructura del código

El proyecto sigue los líneamiento de creación de DDD, facilitando la implementación de un lenguaje ublicuo dentro del código de la aplicación. Ademas, cada microservicio sigue una división por capas, a continucación se explica la estructura de carpetas de src:
```bash
📦MISW4406-misoliticos
 ┣-- 📂api -> Carpeta donde se almacenan las API Gateway de los microservicios
 ┃   ┃   ┣-- 📜__init__.py
 ┃   ┃   ┣-- 📜catastrales.py
 ┃   ┃
 ┃   📂config -> Carpeta donde se guardan los archivos de configuración de base de datos y la unidad de trabajo
 ┃   ┃   ┣ 📜__init__.py
 ┃   ┃   ┣ 📜db.py
 ┃   ┃   ┗ 📜uwo.py
 ┃   ┃
 ┃   📂modules -> Carpeta con la lógica dividida en modulos
 ┃   ┣   📂catastrales
 ┃   ┃   ┣   📂application -> Carpeta de la capa aplicación
 ┃   ┃   ┃   ┣   📂commands -> Carpeta de los comandos
 ┃   ┃   ┃   ┃   ┣ 📜__init__.py
 ┃   ┃   ┃   ┃   ┣ 📜base.py
 ┃   ┃   ┃   ┃   ┗ 📜crear_inmueble.py
 ┃   ┃   ┃   ┣   📂queries -> Carpeta de las consultas
 ┃   ┃   ┃   ┃   ┣ 📜__init__.py
 ┃   ┃   ┃   ┃   ┣ 📜base.py
 ┃   ┃   ┃   ┃   ┗ 📜obtener_inmueble.py
 ┃   ┃   ┃   ┣ 📜__init__.py
 ┃   ┃   ┃   ┣ 📜dtos.py
 ┃   ┃   ┃   ┣ 📜hadlers.py
 ┃   ┃   ┃   ┣ 📜mappers.py
 ┃   ┃   ┃   ┗ 📜services.py
 ┃   ┃   ┣   📂domain -> Carpeta de la capa de dominio
 ┃   ┃   ┃   ┣ 📜__init__.py
 ┃   ┃   ┃   ┣ 📜entities.py
 ┃   ┃   ┃   ┣ 📜events.py
 ┃   ┃   ┃   ┣ 📜exceptions.py
 ┃   ┃   ┃   ┣ 📜factories.py
 ┃   ┃   ┃   ┣ 📜repositories.py
 ┃   ┃   ┃   ┣ 📜rules.py
 ┃   ┃   ┃   ┗ 📜value_objects.py
 ┃   ┃   ┣   📂infrastructure -> Carpeta de la capa de infraestructura
 ┃   ┃   ┃   ┣ 📜__init__.py
 ┃   ┃   ┃   ┣ 📜dto.py
 ┃   ┃   ┃   ┣ 📜mappers.py
 ┃   ┃   ┃   ┣ 📜exceptions.py
 ┃   ┃   ┃   ┣ 📜factories.py
 ┃   ┃   ┃   ┗ 📜repositories.py
 ┃   ┃   ┗   📜__init__.py
 ┃   ┃
 ┃   📂seedwork -> Carpeta que contiene clases abstractas que se usan en varias partes del código
```

## Build & Deployment | Docker Compose

```bash
$ # Primero, clone el repositorio con el comando
$ git clone https://github.com/s-cortes/misw4406-misoliticos.git
$ cd misw4406-misoliticos
$
$ # Use Docker Compose CLI para correr el microservicio
$ docker compose up --build -d propiedades
$
$ # Acceda a la interfaz desde postman: http://127.0.0.1:5000/
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
  "piso":[{"oficinas":[{"area":{"valor":5.5, "unidad":"n2"},"ubicacion":{"nombre":"ubi","nombre_visible":"otra cosa","telefono":"str"}}]}]
}

# Obtener inmueble
curl --location 'http://127.0.0.1/:5000/inmueble/<id>' \
```