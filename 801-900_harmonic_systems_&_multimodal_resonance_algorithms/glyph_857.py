# glyph_857 – KALMAN_1D_CONST_VELOCITY
# 1D Kalman filter tracking position with constant velocity model.

import numpy as np

class glyph_857:
    def __init__(self, dt=1.0, process_var=1e-2, meas_var=1e-1):
        """
        State: [position, velocity]^T
        """
        self.dt = dt
        self.F = np.array([[1, dt],[0, 1]], dtype=float)
        self.H = np.array([[1, 0]], dtype=float)
        self.Q = process_var * np.array([[dt**4/4, dt**3/2],[dt**3/2, dt**2]])
        self.R = np.array([[meas_var]])
        self.x = np.zeros((2,1))
        self.P = np.eye(2)

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        z = np.array([[float(z)]])
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        I = np.eye(2)
        self.P = (I - K @ self.H) @ self.P

    def state(self):
        return float(self.x[0,0]), float(self.x[1,0])
