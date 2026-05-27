# Configuración del entorno de desarrollo

Este documento explica cómo configurar el entorno de desarrollo del proyecto en cualquier máquina (Linux o Windows), incluyendo soporte para **Jupyter Notebook** y la organización del repositorio.

---

## Estructura del proyecto

El repositorio sigue esta organización:

```

proyecto/
│
├── venv/              # Entorno virtual (NO subir al repositorio)
├── notebooks/         # Notebooks Jupyter
├── src/               # Código Python del proyecto
├── data/              # Conjuntos de datos
├── docs/              # Documentación e informe de la práctica
│   ├── plantilla/     # Plantilla oficial del informe
│   └── trabajo/       # Documentos en desarrollo
│
├── requirements.txt   # Dependencias del proyecto
├── .gitignore
└── README.md

```

---

## Carpeta `docs/`

Esta carpeta contiene toda la documentación del proyecto:

- **plantilla/**: plantilla base del informe final (proporcionada por la asignatura)
- **trabajo/**: documentos en los que se va trabajando durante la práctica

**Aquí se irá elaborando progresivamente el informe final que habrá que entregar.**

**Importante:**

- Toda la redacción del trabajo debe centralizarse aquí
- Evitar duplicar documentos en otras carpetas
- Usar nombres de archivo claros y versiones organizadas

---

## Requisitos previos

Asegúrate de tener instalado:

- Python 3.10 o superior
- Git

```bash
python3 --version
git --version
```

---

## 1. Clonar el repositorio

```bash
git clone git@github.com:usuario/repositorio.git
cd repositorio
```

---

## 2. Crear entorno virtual

### 🔹 Linux / macOS

```bash
python3 -m venv venv
```

### 🔹 Windows

```bash
python -m venv venv
```

---

## 3. Activar entorno virtual

### 🔹 Linux / macOS

```bash
source venv/bin/activate
```

### 🔹 Windows (PowerShell)

```powershell
venv\Scripts\activate
```

---

## 4. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5. Soporte para Jupyter Notebook

Instalar Jupyter:

```bash
pip install notebook ipykernel
```

Registrar entorno:

```bash
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

---

## 6. Ejecutar Jupyter

```bash
jupyter notebook
```

(Opcional):

```bash
pip install jupyterlab
jupyter lab
```

Seleccionar kernel:

```
Python (venv)
```

---

## 7. Verificar instalación

```python
import networkx
import sklearn

print("Entorno configurado correctamente ")
```

---

## 8. Actualizar dependencias

```bash
pip install nueva_libreria
pip freeze > requirements.txt
```

---

## 9. Desactivar entorno

```bash
deactivate
```

---

## Notas importantes

- ❌ No subir la carpeta `venv/`
- ✅ Usar siempre `requirements.txt`
- ✅ Cada sistema (Linux/Windows) usa su propio entorno virtual
- ✅ Documentación centralizada en `docs/`

---

## Listo

El entorno está preparado para:

- Desarrollo en Python
- Uso de NetworkX y Scikit-learn
- Ejecución de notebooks Jupyter
- Redacción del informe en `docs/` 🎉

```

```
