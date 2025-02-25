import cv2
import mediapipe as mp

""" Notas del Script:
    - Reconoce y dice el porcentaje de confianza en cada dedo que se extiende:
    - No reconoce de manera adecuada el pulgar
    - 
    """
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

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

    if finger_tip_id == 4:  
        if is_right_hand:
            return tip_x < pip_x  
        else:
            return tip_x > pip_x  
    else:
        return tip_y < pip_y  

def calculate_confidence(tip_y, pip_y):
    """
    Calcula el porcentaje de confianza de que un dedo esté extendido.
    """
    return max(0, min(1, (pip_y - tip_y) / 0.1))  

def main():
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.85,  
        min_tracking_confidence=0.85    
    )

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("No se puede acceder a la cámara.")
            break

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_label = handedness.classification[0].label  
                is_right_hand = hand_label == "Right"
                fingers_status = []  
                fingers_confidence = []
                finger_tips_ids = [4, 8, 12, 16, 20] 
                finger_pip_ids = [2, 6, 10, 14, 18]   

                for tip_id, pip_id in zip(finger_tips_ids, finger_pip_ids):
                    tip_y = hand_landmarks.landmark[tip_id].y
                    pip_y = hand_landmarks.landmark[pip_id].y
                    extended = is_finger_extended(hand_landmarks, tip_id, pip_id, is_right_hand)
                    fingers_status.append(1 if extended else 0)
                    confidence = calculate_confidence(tip_y, pip_y)
                    fingers_confidence.append(confidence)

                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                status_text = f"Dedos: {fingers_status}"
                cv2.putText(image, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

                for i, confidence in enumerate(fingers_confidence):
                    confidence_text = f"Dedo {i}: {int(confidence * 100)}%"
                    cv2.putText(image, confidence_text, (10, image.shape[0] - 30 - i * 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Modo Espejo con Detección de Dedos', image)
        if cv2.waitKey(5) & 0xFF == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
