# Portfolio Nathaly Buenaño

Portfolio profesional de Nathaly Buenaño — Content Manager & Estrategia Digital.

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd porfolio_nataly

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Crear base de datos
python manage.py migrate

# Cargar datos iniciales (servicios y habilidades)
python manage.py seed

# Crear usuario administrador
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Uso

- **Sitio**: http://localhost:8000
- **Admin**: http://localhost:8000/admin/

### Agregar proyectos

1. Ir al admin de Django
2. Click en "Proyectos" > "Agregar proyecto"
3. Llenar título, descripción, subir imagen, seleccionar categoría
4. Marcar "Destacado" para que aparezca más grande en el portfolio
5. Usar el campo "Orden" para controlar el orden de aparición

## Estructura

```
portfolio_nathaly/    # Configuración Django
core/                 # App principal (modelos, vistas, admin)
templates/            # HTML templates
static/               # CSS, JS, imágenes
media/                # Uploads desde el admin
```

## Despliegue

Preparado para Railway, Render o cualquier PaaS:

- WhiteNoise para servir archivos estáticos
- Gunicorn como servidor WSGI
- Variables de entorno con python-decouple

```bash
# Recolectar estáticos para producción
python manage.py collectstatic --noinput
```

## Contacto

Nathaly Buenaño — nathalybuenano@gmail.com
