# API de List a de Tareas

Esta es una API RESTful creada con Django y Django Rest Framework, para el desarrollo de una aplicación de lista de tareas.

## Requisitos

- Python 3.8 o superior
- Poetry(Opcional)
- Docker
- Docker Compose

## Instalación

Clonar el repositorio.
Dentro del la carpeta src/ del proyecto ejecutar:

```bash
poetry install
```

Si no tienes Poetry instalado, puedes instalarlo con el siguiente comando:

```bash
pip install poetry
```

También puedes instalar las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Levantar el servidor

Para levantar el servidor localmente sin docker, ejecutar el siguiente comando en la raiz del proyecto:

```bash
make runserver
```

Para levantar el servidor con docker, ejecutar el siguiente comando:

```bash
make up
```

## Pruebas

Para ejecutar las pruebas unitarias, ejecutar el siguiente comando:

```bash
make pytest
```

## Swagger

La documentación de la API se puede acceder a través de Swagger, en la ruta `http://localhost:8000/swagger/`.
