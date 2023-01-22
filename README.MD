## Proyecto básico de inventarios generado con ChatGPT

**_Instalación ambiente local por terminal_**

1. Instalar ambiente local

    ```
    pip3 install virtualenv
    virtualenv venv
    ```

2. Activar ambiente virtual

    ```
    venv\Scripts\activate.bat ---> Windows
    venv/bin/activate ---> macOs / linux
    ```

3. Instalar los requerimientos

    ```
    pip3 install -r requirements.txt
    ```


**_Ejecución de scripts**

1. Ejecuta el siguiente comando para crear un csv con datos falsos de un inventario:

    ```
    py .\src\faker\__init__.py
    ```

2. Configura la variable `db_url` del archivo `src/__init__.py` para conectarte a una base de datos postgresql

    - La estructura de la conexión a la base de datos es la siguiente:
    `postgresql://username:password@host:port/database`

3. Ejecuta el siguiente comando para guardar los productos del inventario csv en la base de datos:

    ```
    py .\src\__init__.py
    ```


