# 📘 Proyecto con Django – Sistema de Gestión Web

Este proyecto es una **aplicación web desarrollada con Django** que permite administrar tareas, usuarios y diferentes componentes del sistema desde una interfaz sencilla e intuitiva.

Está diseñado como un sistema modular que puede adaptarse fácilmente a entornos escolares, administrativos o de uso personal.

---

## 🧩 ¿Qué hace esta aplicación?

- Permite crear, editar y eliminar tareas o registros.
- Gestiona usuarios y vistas personalizadas.
- Cuenta con migraciones, plantillas, autenticación y navegación.
- Funciona localmente desde cualquier computadora.

---

## 🛠 Requisitos del sistema

Solo necesitas:

- Una computadora con **Windows, Linux o macOS**
- Conexión a internet (para la instalación)
- Tener instalado **Python 3.10 o superior**

---

## 🧭 Guía de instalación paso a paso

### 1️⃣ Instalar Python

1. Visita 👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Descarga la versión más reciente.
3. Durante la instalación, activa la casilla que dice **"Add Python to PATH"**.

---

### 2️⃣ Obtener el proyecto

1. Dirígete al botón verde **`Code`** en esta página.
2. Selecciona la opción **`Download ZIP`**.
3. Extrae el contenido del archivo ZIP en una carpeta de tu computadora.

---

### 3️⃣ Abrir la terminal

- En **Windows**: abre el símbolo del sistema (`cmd`) o PowerShell.
- En **Linux/macOS**: abre la Terminal.

---

### 4️⃣ Navegar a la carpeta del proyecto

En la terminal, escribe el siguiente comando y presiona Enter (reemplaza `ruta/a/tu/carpeta` por la ruta donde extrajiste el proyecto):

```bash
cd ruta/a/tu/carpeta/mi_dashboard
```

---

### 5️⃣ (Opcional pero recomendado) Crear un entorno virtual

En la terminal, ejecuta:

```bash
python -m venv venv
```

Activa el entorno virtual:

- **En Windows**:

```bash
venv\Scripts\activate
```

- **En Linux/Mac**:

```bash
source venv/bin/activate
```

Luego continúa con la instalación de dependencias.

---

### 6️⃣ Instalar las dependencias

Escribe este comando y presiona Enter:

```bash
pip install -r requirements.txt
```

Esto instalará automáticamente los paquetes que requiere Django y otras herramientas del sistema.

---

### 7️⃣ Aplicar las migraciones

Ejecuta el siguiente comando:

```bash
python manage.py migrate
```

Este paso creará las tablas necesarias en la base de datos para que el sistema funcione correctamente.

---

### 8️⃣ Iniciar el servidor local

Inicia el servidor con:

```bash
python manage.py runserver
```

Verás un mensaje en consola indicando que el servidor está corriendo en:

```
http://127.0.0.1:8000/
```

---

### 9️⃣ Acceder a la aplicación

Abre tu navegador (Chrome, Firefox, Edge...) y entra a:

```
http://127.0.0.1:8000/
```

¡Listo! 🎉 Ya puedes comenzar a utilizar tu sistema web desarrollado con Django.

---

## 🙋‍♀️ Autora del proyecto

**Guadalupe Erizeth Mejía**  
Estudiante de Tecnologías de la Información – Área Desarrollo de Software Multiplataforma  
**Universidad Tecnológica del Valle de Toluca**
