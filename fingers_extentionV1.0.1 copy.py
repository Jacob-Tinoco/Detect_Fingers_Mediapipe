import cv2
import mediapipe as mp

# Configuración de MediaPipe Hands 
""" Notas del Script:
    - Reconoce y dice el porcentaje de confianza en cada dedo que se extiende:
    - No reconoce de manera adecuada el pulgar
    - 
    """
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Umbral de confianza para considerar un dedo extendido
FINGER_EXTENDED_THRESHOLD = 0.85

def is_finger_extended(hand_landmarks, finger_tip_id, finger_pip_id, is_right_hand):
    """
    Determina si un dedo está extendido basado en la posición de sus landmarks.
    Para el pulgar (dedo 0), se usa tanto la coordenada x como la y.
    """
    tip_x = hand_landmarks.landmark[finger_tip_id].x
    tip_y = hand_landmarks.landmark[finger_tip_id].y
    pip_x = hand_landmarks.landmark[finger_pip_id].x
    pip_y = hand_landmarks.landmark[finger_pip_id].y

    if finger_tip_id == 4:  # Solo para el pulgar
        if is_right_hand:
            return tip_x < pip_x  # Para la mano derecha, el pulgar está a la izquierda
        else:
            return tip_x > pip_x  # Para la mano izquierda, el pulgar está a la derecha
    else:
        return tip_y < pip_y  # Para los otros dedos, usamos la coordenada y

def calculate_confidence(tip_y, pip_y):
    """
    Calcula el porcentaje de confianza de que un dedo esté extendido.
    """
    return max(0, min(1, (pip_y - tip_y) / 0.1))  # Normalizado entre 0 y 1

def main():
    # Inicializa MediaPipe Hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.85,  # 85% de confianza para detectar una mano
        min_tracking_confidence=0.85    # 85% de confianza para rastrear una mano
    )

    # Captura de video desde la cámara web
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("No se puede acceder a la cámara.")
            break

        # Voltea la imagen para que se vea como un espejo
        image = cv2.flip(image, 1)

        # Convierte la imagen de BGR a RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Procesa la imagen para detectar manos
        results = hands.process(image_rgb)

        # Si se detectan manos, dibuja las anotaciones y muestra la información
        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_label = handedness.classification[0].label  # 'Left' o 'Right'
                is_right_hand = hand_label == "Right"

                # Identifica si los dedos están extendidos y calcula la confianza
                fingers_status = []  # Lista para almacenar el estado de los dedos (0 o 1)
                fingers_confidence = []  # Lista para almacenar la confianza de cada dedo

                # Landmarks para las puntas y articulaciones de los dedos
                finger_tips_ids = [4, 8, 12, 16, 20]  # Pulgar, índice, medio, anular, meñique
                finger_pip_ids = [2, 6, 10, 14, 18]   # Articulaciones de los dedos

                for tip_id, pip_id in zip(finger_tips_ids, finger_pip_ids):
                    tip_y = hand_landmarks.landmark[tip_id].y
                    pip_y = hand_landmarks.landmark[pip_id].y

                    # Determina si el dedo está extendido
                    extended = is_finger_extended(hand_landmarks, tip_id, pip_id, is_right_hand)
                    fingers_status.append(1 if extended else 0)

                    # Calcula la confianza de que el dedo esté extendido
                    confidence = calculate_confidence(tip_y, pip_y)
                    fingers_confidence.append(confidence)

                # Dibuja las manos
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Muestra el estado de los dedos (0 o 1) en la parte superior
                status_text = f"Dedos: {fingers_status}"
                cv2.putText(image, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

                # Muestra el porcentaje de confianza en la parte inferior
                for i, confidence in enumerate(fingers_confidence):
                    confidence_text = f"Dedo {i}: {int(confidence * 100)}%"
                    cv2.putText(image, confidence_text, (10, image.shape[0] - 30 - i * 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        # Muestra la imagen con las anotaciones
        cv2.imshow('Modo Espejo con Detección de Dedos', image)
        if cv2.waitKey(5) & 0xFF == 27:  # Presiona ESC para salir
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()