# Configuración del Entorno Virtual

Para aislar las dependencias del proyecto, cree y active un entorno virtual en Python ejecutando:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows
```

Para reproducir este entorno en otra máquina e instalar todas las dependencias requeridas, ejecute:

```bash
pip install -r requirements.txt
```