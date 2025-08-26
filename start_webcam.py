import cv2
import numpy as np
from color_blind_app import apply_simulation, modes
from closest_color_name import closest_color_name

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    modes = ["Protanopia", "Deuteranopia", "Tritanopia"]
    mode_index = 0  
    pointer_on_left = True
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Mirror image
        mode_name = modes[mode_index]  # mode_name is like "Protanopia"
        simulated = apply_simulation(frame.copy(), mode_name)

        height, width = frame.shape[:2]
        half_width = width // 2

        # Merge views side-by-side
        separator_thickness = 10  # You can adjust this
        separator_color = (0, 0, 0)  # Black line
        height = frame.shape[0]

# Create the vertical separator
        separator = np.full((height, separator_thickness, 3), separator_color, dtype=np.uint8)

# Combine the images with separator in between
        combined = np.hstack((frame, separator, simulated))

        # Pointer coordinates (center)
        x, y = width // 2, height // 2

        # Color from each view
        if pointer_on_left:
            pixel_normal = frame[y, x]
            pixel_sim = simulated[y, x]
        else:
            pixel_sim = simulated[y, x]
            pixel_normal = frame[y, x]

        # Get color names
        normal_name = closest_color_name(pixel_normal[::-1])
        sim_name = closest_color_name(pixel_sim[::-1])

        # Draw pointer
        pointer_color = (255, 255, 255)
        # Display current mode name
        cv2.putText(combined, f"Mode: {modes[mode_index]}", (10, 90), font, 0.6, (255, 255, 255), 2)

        cv2.circle(combined, (x, y), 5, pointer_color, 2)
        cv2.putText(combined, f"Normal: {normal_name}", (10, 30), font, 0.6, (255, 255, 255), 2)
        cv2.putText(combined, f"Simulated: {sim_name}", (10, 60), font, 0.6, (255, 255, 255), 2)
        cv2.putText(combined, f"Mode: {modes[mode_index]}", (10, 90), font, 0.6, (255, 255, 255), 2)

        cv2.imshow("Color Blindness Simulator", combined)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' or ESC to exit
            break
        elif key == ord('m'):
             mode_index = (mode_index + 1) % len(modes)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
