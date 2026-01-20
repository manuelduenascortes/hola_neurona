# 🧠 Hola Neurona

Aplicación interactiva de Streamlit que demuestra el funcionamiento de neuronas artificiales con diferentes configuraciones de entradas y pesos.

## 📋 Características

- **Visualización de neurona**: Imagen ilustrativa de una neurona biológica
- **3 modos interactivos**:
  - 1 entrada con peso ajustable
  - 2 entradas con pesos ajustables
  - 3 entradas con pesos ajustables + sesgo
- **Cálculos en tiempo real**: Visualiza la suma ponderada y la función de activación sigmoid
- **Gráficos interactivos**: Diagramas visuales de la neurona con Plotly

## 🚀 Ejecución Local

### Requisitos
- Python 3.11 o superior
- pip

### Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
```

La aplicación estará disponible en `http://localhost:8501`

## 🐳 Ejecución con Docker

### Opción 1: Docker Compose (Recomendado)

```bash
# Construir y ejecutar
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d

# Detener
docker-compose down
```

### Opción 2: Docker manual

```bash
# Construir la imagen
docker build -t hola_neurona .

# Ejecutar el contenedor
docker run -p 8501:8501 hola_neurona
```

La aplicación estará disponible en `http://localhost:8501`

## 📚 Cómo Funciona

Cada neurona artificial realiza los siguientes pasos:

1. **Recibe entradas** (x₁, x₂, x₃, ...)
2. **Multiplica cada entrada por su peso** (w₁, w₂, w₃, ...)
3. **Suma todos los productos** más el sesgo (b)
4. **Aplica una función de activación** (sigmoid) para obtener la salida

### Fórmula

```
z = w₁·x₁ + w₂·x₂ + w₃·x₃ + b
salida = σ(z) = 1 / (1 + e^(-z))
```

## 🎨 Tecnologías

- **Streamlit**: Framework para aplicaciones web interactivas
- **NumPy**: Cálculos numéricos
- **Plotly**: Visualizaciones interactivas
- **Docker**: Contenedorización

## 📝 Estructura del Proyecto

```
hola_neurona/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias Python
├── Dockerfile         # Configuración Docker
├── .dockerignore      # Archivos excluidos de Docker
├── assets/
│   └── neurona.jpg    # Imagen de neurona
└── README.md          # Este archivo
```

## 🎯 Uso

1. Selecciona una de las tres pestañas según el número de entradas que quieras explorar
2. Ajusta los sliders para cambiar los valores de entrada y pesos
3. Observa cómo cambian los cálculos y la visualización en tiempo real
4. Experimenta con diferentes combinaciones para entender cómo funcionan las neuronas

---

Creado con ❤️ usando Streamlit
