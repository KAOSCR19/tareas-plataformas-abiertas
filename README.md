# 🎓 Práctica #2 - Desarrollo de Plataformas Abiertas

## 📋 Descripción del proyecto

Este proyecto consiste en el desarrollo de una API de estudiantes utilizando **Python y Flask**.

La API cuenta con tres endpoints que permiten mostrar un mensaje de bienvenida, saludar a un estudiante y consultar su información básica.

## 🛠️ Tecnologías utilizadas

- 🐍 Python
- 🌐 Flask
- 📮 Postman
- 🐙 Git y GitHub
- 💻 Visual Studio Code

## 🚀 Endpoints de la API

### 👋 1. Hola

**Método:** `GET`

**URL:**
`http://127.0.0.1:5000/estudiantes/api/v1/hola`

**Descripción:** Muestra un mensaje de bienvenida.

**Respuesta:**
```json
{
  "mensaje": "Bienvenido a la API de estudiantes"
}
```

### 🙋 2. Saludo

**Método:** `GET`

**URL:**
`http://127.0.0.1:5000/estudiantes/api/v1/saludo`

**Descripción:** Recibe el nombre de un estudiante mediante un JSON y devuelve un saludo personalizado.

**Ejemplo de solicitud (Body JSON):**
```json
{
  "nombre": "Kevin"
}
```

**Respuesta:**
```json
{
  "mensaje": "Hola Kevin"
}
```

**⚠️ Validación:** Si no se proporciona un nombre, la API devuelve:

```json
{
  "mensaje": "Debe de ingresar el nombre del estudiante."
}
```

### 📚 3. Información del estudiante

**Método:** `GET`

**URL:**
`http://127.0.0.1:5000/estudiantes/api/v1/informacion`

**Descripción:** Permite consultar información básica del estudiante enviando su nombre y carrera mediante parámetros en la URL.

**Ejemplo:**
`?nombre=Kevin&carrera=Ingenieria%20Informatica`

**Respuesta:**
```json
{
  "nombre": "Kevin",
  "carrera": "Ingenieria Informatica",
  "estado": "Activo",
  "mensaje": "Información del estudiante consultada correctamente."
}
```

**⚠️ Validación:** Si falta el nombre o la carrera, devuelve:

```json
{
  "mensaje": "Debe ingresar el nombre y la carrera del estudiante."
}
```

**Nota:** El estado "Activo" es un valor de ejemplo y no se consulta desde una base de datos.

## ⚙️ Instalación y ejecución

**1. 📂 Crear el entorno virtual**

```powershell
python -m venv .venv
```

**2. 🔧 Activar el entorno virtual**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. 📦 Instalar las dependencias**

```powershell
python -m pip install -r requirements.txt
```

**4. ▶️ Ejecutar la API**

```powershell
python app.py
```

**5. 🌐 Probar la API**

Una vez iniciada la aplicación, se puede acceder desde:

`http://127.0.0.1:5000`

Las solicitudes se pueden probar utilizando Postman.

## 🧪 Pruebas realizadas

Se realizaron pruebas con Postman para comprobar el funcionamiento de los tres endpoints.

- ✅ Endpoint `hola`: muestra correctamente el mensaje de bienvenida.
- ✅ Endpoint `saludo`: devuelve el saludo personalizado.
- ✅ Endpoint `saludo`: valida cuando no se proporciona un nombre.
- ✅ Endpoint `informacion`: devuelve los datos del estudiante.
- ✅ Endpoint `informacion`: valida cuando falta el nombre o la carrera.

## 📁 Estructura del proyecto

```text
tareas-plataformas-abiertas/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .venv/ 
```

La carpeta `.venv` se utiliza localmente y no se incluye en el repositorio de GitHub.

## 📝 Conclusión

Con esta práctica se logró desarrollar una API sencilla utilizando Python y Flask. Se aprendió a crear endpoints, utilizar el método GET, recibir parámetros, validar información y devolver respuestas en formato JSON.

También se utilizó Postman para comprobar que las solicitudes y respuestas funcionaran correctamente.