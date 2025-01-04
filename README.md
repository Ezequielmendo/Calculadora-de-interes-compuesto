# **Calculadora de Interés Compuesto**
Una aplicación web que permite a los usuarios calcular el interés compuesto basado en un capital inicial, una tasa de interés anual, un periodo en años y un aporte mensual. También genera una tabla con los resultados por año.

# **Características**
-Cálculo del capital final usando interés compuesto.
-Determinación de la ganancia total y el monto invertido.
-Generación de una tabla con resultados anuales.
-Interfaz web intuitiva y fácil de usar.

# **Requisitos**
Para ejecutar este proyecto necesitas tener instalado:
```
-Python 3.8 o superior.
-Un entorno virtual (opcional, pero recomendado).
-Las librerías incluidas en requirements.txt

# **Instalación**
Clona este repositorio:
```bash
git clone https://github.com/Ezequielmendo/Calculadora-de-inter-s-compuesto.
```
Navega al directorio del proyecto:
```bash
cd calculadora-interes-compuesto
```
(Opcional) Crea un entorno virtual y actívalo
```bash
python -m venv venv
```
Instala las dependencias:
```bash
pip install -r requirements.txt
```

# **Uso**
Inicia el servidor Flask:
```bash
python main.py
```
Abre tu navegador web y accede a:
http://127.0.0.1:5000
Ingresa los datos requeridos en el formulario y haz clic en "Calcular". Verás los resultados directamente en la página.

# **Estructura del Proyecto**
```
app/
│
├── static/  
│    │
│    ├── images/
│    │   └── image.jpeg   # Imagen utilizada en el proyecto
│    │
│    ├── css/
│    │   └── style.css    # Estilos CSS para la aplicación
│    │
│    ├── js/
│    │   └── mensajes.js  # Script JavaScript para alertas y funciones dinámicas
│
├── templates/
│    └── index.html       # Plantilla HTML para la página principal
│
├── __init__.py           # Archivo de inicialización del paquete `app`
├── funciones.py          # Funciones auxiliares del proyecto
├── routes.py             # Definición de rutas para la aplicación Flask
├── calculadora.py        # Archivo principal para la lógica de la calculadora
├── config.py             # Configuración de la aplicación
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias necesarias para el proyecto
└── .gitignore            # Archivos y carpetas a ignorar por Git

```

# **Licencia**
Este proyecto se distribuye bajo la licencia MIT.

# **Sobre Mí**
Este proyecto fue desarrollado por Ezequiel Mendoza. Si tienes dudas o sugerencias, ¡no dudes en contactarme!