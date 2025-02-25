
Crear entorno virtual:
```PYTHON
python -m venv .venv
```

Activar entorno virtual (linux):
```PYTHON
source .venv/bin/activate
```
Instalar requerimientos:
```PYTHON
pip install -r requirements.txt
```
Ejecutar migraciones:
```PYTHON
python manage.py migrate
```
Crear superusuario:
```PYTHON
python manage.py createsuperuser
```
Correr proyecto:
```PYTHON
python manage.py runserver
```
Poblar Base de Datos:

```PYTHON
python manage.py loaddata fixtures/services.json
```

