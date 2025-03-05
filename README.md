# Proyecto FastAPI

Este es un proyecto de API RESTful utilizando FastAPI con autenticación, encriptación de contraseñas y acceso a bases de datos.

## Requisitos

Para ejecutar este proyecto, necesitas instalar las dependencias necesarias en tu entorno de desarrollo.

## Instalación

Sigue estos pasos para instalar las dependencias:

1. Actualiza `pip` a la última versión:

    ```bash
    python.exe -m pip install --upgrade pip
    ```

2. Instala SQLAlchemy:

    ```bash
    pip install sqlalchemy
    ```

3. Instala la versión más reciente de `passlib` y `bcrypt`:

    ```bash
    pip install --upgrade passlib bcrypt
    ```

4. Instala `bcrypt`:

    ```bash
    pip install bcrypt
    ```

5. Instala `python-jose` para manejar la autenticación JWT:

    ```bash
    pip install python-jose
    ```

6. Instala `passlib` para la encriptación de contraseñas:

    ```bash
    pip install passlib
    ```

7. Instala `sqlalchemy` y `psycopg2-binary` para conectar con bases de datos PostgreSQL:

    ```bash
    pip install sqlalchemy psycopg2-binary
    ```

8. Instala todas las dependencias recomendadas de FastAPI:

    ```bash
    pip install "fastapi[all]"
    ```

## Uso

1. Clona el repositorio o descarga el proyecto.
2. Instala las dependencias mencionadas anteriormente.
3. Ejecuta la aplicación FastAPI con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

La aplicación estará disponible en `http://127.0.0.1:8000` por defecto.

## Contribución

Si deseas contribuir al proyecto, por favor abre un *pull request* con tus cambios. Asegúrate de que todas las pruebas pasen antes de enviarlo.

## Licencia

Este proyecto está bajo la licencia MIT.
