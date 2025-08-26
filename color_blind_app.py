import numpy as np

def simulate_color_blind(image_bgr, matrix):
    flat = image_bgr.reshape(-1, 3).astype(np.float32) / 255.0
    simulated = np.dot(flat, matrix.T)
    simulated = np.clip(simulated, 0, 1) * 255
    return simulated.reshape(image_bgr.shape).astype(np.uint8)

def simulate_protanopia(image_bgr):
    matrix = np.array([
        [0.56667, 0.43333, 0],
        [0.55833, 0.44167, 0],
        [0, 0.24167, 0.75833]
    ])
    return simulate_color_blind(image_bgr, matrix)

def simulate_deuteranopia(image_bgr):
    matrix = np.array([
        [0.625, 0.375, 0],
        [0.7, 0.3, 0],
        [0, 0.3, 0.7]
    ])
    return simulate_color_blind(image_bgr, matrix)

def simulate_tritanopia(image_bgr):
    matrix = np.array([
        [0.95, 0.05, 0],
        [0, 0.43333, 0.56667],
        [0, 0.475, 0.525]
    ])
    return simulate_color_blind(image_bgr, matrix)

# Dictionary of modes
modes = {
    "Protanopia": simulate_protanopia,
    "Deuteranopia": simulate_deuteranopia,
    "Tritanopia": simulate_tritanopia
}

def apply_simulation(frame, mode_name):
    mode_function = modes[mode_name]  # Get the function using the name
    return mode_function(frame)       # Now call it
