# MISW4406-misoliticos
Módulo seedwork del proyecto para los microservicios de la universidad de los Alpes

## Integrantes

* Santiago Cortés Fernández [s.cortes@uniandes.edu.co](mailto:s.cortes@uniandes.edu.co)

## Estructura del código

El proyecto sigue los líneamiento de creación de DDD, facilitando la implementación de un lenguaje ublicuo dentro del código de la aplicación. Ademas, cada microservicio sigue una división por capas, a continucación se explica la estructura de carpetas de src:
```bash 

📦seedwork
 ┣--- 📂application
 ┃    ┣--- 📜__init__.py
 ┃    ┣--- 📜commands.py
 ┃    ┣--- 📜dtos.py
 ┃    ┣--- 📜handlers.py
 ┃    ┣--- 📜queries.py
 ┃    ┗--- 📜services.py
 ┣--- 📂domain
 ┃    ┣--- 📜__init__.py
 ┃    ┣--- 📜entities.py
 ┃    ┣--- 📜events.py
 ┃    ┣--- 📜exceptions.py
 ┃    ┣--- 📜factories.py
 ┃    ┣--- 📜mixins.py
 ┃    ┣--- 📜repositories.py
 ┃    ┣--- 📜rules.py
 ┃    ┣--- 📜services.py
 ┃    ┗--- 📜value_object.py
 ┣--- 📂infrastructure
 ┃    ┣--- 📂schema
 ┃    ┃    ┣--- 📂v1
 ┃    ┃    ┃    ┣--- 📜__init__.py
 ┃    ┃    ┃    ┣--- 📜commands.py
 ┃    ┃    ┃    ┣--- 📜events.py
 ┃    ┃    ┃    ┣--- 📜mappers.py
 ┃    ┃    ┃    ┗--- 📜messages.py
 ┃    ┃    ┗--- 📜__init__.py
 ┃    ┣--- 📜__init__.py
 ┃    ┣--- 📜dispatchers.py
 ┃    ┣--- 📜uow.py
 ┃    ┗--- 📜utils.py
 ┣--- 📂presentation
 ┃    ┣--- 📜__init__.py
 ┃    ┗--- 📜api.py
 ┣--- 📜README.md
 ┗--- 📜__init__.py
```
