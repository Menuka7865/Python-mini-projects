import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.axis("off")
fig.set_facecolor("black")

# Heart shape function
def heart_shape(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Generate the heart shape points
t = np.linspace(0, 2 * np.pi, 100)
x, y = heart_shape(t)

# Fill the heart shape with an initial red color
heart_fill = ax.fill(x, y, color="red", alpha=0.5)[0]

# Set the limits for the plot
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Blinking effect function
def update(frame):
    # Calculate intensity for blinking effect
    intensity = 0.5 + 0.5 * np.sin(frame * 0.3)
    
    # Update the color intensity and transparency for the heart fill
    heart_fill.set_facecolor((1, intensity, intensity))
    heart_fill.set_alpha(0.3 + 0.7 * intensity)  # Adjust transparency for blinking effect

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50)

# Display the animation
plt.show()
