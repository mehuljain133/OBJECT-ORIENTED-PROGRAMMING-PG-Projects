# Unit-V Visualization using 2D and 3D graphics: Visualization using graphical objects like point, line, histogram, 3D objects, animation.

pip install matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# --- 2D Visualization: Points and Lines ---
def plot_2d_points_and_line():
    # Plotting points and a line
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(6, 4))
    
    # Plotting points (scatter)
    plt.scatter(x, y, color='blue', label='Points')
    
    # Plotting line
    plt.plot(x, y, color='red', label='Sine Curve')
    
    plt.title("2D Points and Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

# --- 2D Visualization: Histogram ---
def plot_2d_histogram():
    # Creating a random dataset
    data = np.random.randn(1000)
    
    plt.figure(figsize=(6, 4))
    
    # Plotting a histogram
    plt.hist(data, bins=30, color='purple', edgecolor='black')
    
    plt.title("2D Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# --- 3D Visualization: 3D Surface Plot ---
def plot_3d_surface():
    # Generating data for 3D surface plot
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # 3D surface plot
    ax.plot_surface(x, y, z, cmap='viridis')
    
    ax.set_title("3D Surface Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    plt.show()

# --- 3D Visualization: 3D Scatter Plot ---
def plot_3d_scatter():
    # Generating random 3D data
    x = np.random.randn(100)
    y = np.random.randn(100)
    z = np.random.randn(100)
    
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # 3D scatter plot
    ax.scatter(x, y, z, color='red')
    
    ax.set_title("3D Scatter Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    plt.show()

# --- Animation: Sine Wave Animation ---
def animate_sine_wave():
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(0, 10, 100)
    line, = ax.plot([], [], lw=2)

    def init():
        ax.set_xlim(0, 10)
        ax.set_ylim(-1, 1)
        return line,

    def update(frame):
        y = np.sin(x + frame / 10.0)
        line.set_data(x, y)
        return line,

    ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
    plt.title("Sine Wave Animation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# --- Main Program ---
def main():
    # 2D Visualization
    plot_2d_points_and_line()
    plot_2d_histogram()
    
    # 3D Visualization
    plot_3d_surface()
    plot_3d_scatter()
    
    # Animation
    animate_sine_wave()

if __name__ == "__main__":
    main()
