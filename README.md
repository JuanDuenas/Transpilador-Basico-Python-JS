# Transpilador-Basico-Python-JS

Este es un ejemplo de un transpilador básico de Python a JavaScript.

## Antes de empezar

Antes de empezar, asegúrate de tener instalados los siguientes paquetes:

- Python 3.10
- pip
- antlr4-python3-runtime

## Instalación

Para instalar los paquetes necesarios, ejecuta el siguiente comando en una terminal:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el transpilador, ejecuta el siguiente comando en una terminal:

```bash
python main.py
```

Este comando parsea el archivo `ejemplo.py` y llama a los métodos `run_listener` y `run_visitor` de los archivos `listener.py` y `visitor.py`, respectivamente.
