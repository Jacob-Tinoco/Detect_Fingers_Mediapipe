# Proyecto: Reconocimiento de Dedos y Gestos con MediaPipe
## Autores

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)

## Bienvenida
¡Hola! 👋 Bienvenido al proyecto **Detect_Fingers_Mediapipe**. Este proyecto utiliza la biblioteca MediaPipe para detectar y reconocer la extensión de dedos en tiempo real.

## Sobre la V1.0.1
Caracteristicas de esta versión:
- Determina si un dedo está extendido basado en la posición de sus landmarks.
- Un dedo está extendido si la punta (tip) está por encima de la articulación (pip).
- Reconoce y dice el porcentaje de confianza en cada dedo que se extiende:
- No reconoce de manera adecuada el pulgar
- Para el pulgar (dedo 0), se usa tanto la coordenada X, al igual que la Y.
- Para los dedos 1 al 4: usa la distancia vertical (Y) entre la punta y la articulación (PIP).
- Para el pulgar: usa la distancia horizontal (Y) entre la punta y la articulación (PIP).
- También considera la distancia entre la punta del dedo y la muñeca.
- Calcula el porcentaje de confianza de que un dedo esté extendido.


## ¿Qué es?
Este proyecto es una aplicación que utiliza la cámara web para capturar imágenes en tiempo real, detectar manos y reconocer la extensión de dedos utilizando MediaPipe. Se han desarrollado varias versiones del script para mejorar la precisión y funcionalidad.

## ¿Qué hace?
- Captura de video en tiempo real desde la cámara web.
- Detecta y sigue los movimientos de la mano.
- Reconoce la extensión de dedos y muestra la información en pantalla.
- Calcula el nivel de confianza para cada dedo extendido.

## Versiones del Proyecto

### Versión 1.0.1 (`fingers_extentionV1.0.1.py`)
- **Funcionalidad**: Detecta la extensión de los dedos (excepto el pulgar) y muestra el nivel de confianza en pantalla.
- **Características**:
  - Reconoce los dedos índice, medio, anular y meñique.
  - Muestra el porcentaje de confianza para cada dedo extendido.
  - No detecta correctamente el pulgar.

### Versión 1.0.2 (`fingers_extentionV1.0.2.py`)
- **Funcionalidad**: Detecta la extensión del pulgar y muestra el nivel de confianza en pantalla.
- **Características**:
  - Reconoce el pulgar y calcula su nivel de confianza.
  - Solo funciona para el pulgar.

### Versión 1.2.0 (`fingers_extentionV1.2.0.py`)
- **Funcionalidad**: Combina las funcionalidades de las versiones anteriores y mejora la detección de todos los dedos, incluyendo el pulgar.
- **Características**:
  - Detecta la extensión de todos los dedos, incluyendo el pulgar.
  - Muestra el estado de los dedos (extendido o no) y el nivel de confianza en pantalla.
  - Mejora la precisión al usar la distancia entre la punta del dedo y la muñeca.

## Herramientas Integradas
- **OpenCV**: Para la captura y el procesamiento de imágenes.
- **MediaPipe**: Para la detección y el reconocimiento de manos y dedos.
- **NumPy**: Para operaciones numéricas y de matrices.

## Potenciales Usos
- Interacción sin contacto en aplicaciones y dispositivos.
- Sistemas de control basados en gestos.
- Proyectos educativos y de investigación en el campo de la visión por computadora.

## Nivel de Uso
**Intermedio**: Este proyecto requiere conocimientos básicos de Python y bibliotecas como OpenCV y MediaPipe.

## Opciones de Ejecución y Uso

### 1. **Instalar Dependencias**
Asegúrate de tener Python instalado y luego instala las bibliotecas necesarias utilizando pip:
```bash
pip install -r requirements.txt
```

## Autores

- **Jacob Tinoco** - *Reposiotorio de edcuación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)

## Historial de Versiones - 1.0.1 - Reposiotorio de edcuación 
#02 Licencia Este proyecto está licenciado bajo la Licencia GPL V.2 - consulta el archivo [LICENSE](LICENSE) para para más detalles.

## Contacto

Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jacob-t-329675258/) o en [Instagram](https://www.instagram.com/jknc.0/).
