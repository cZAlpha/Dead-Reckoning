import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

class Object3D:
    def __init__(self, position, velocity=None):
        self.position = np.array(position)
        self.velocity = np.array(velocity) if velocity is not None else None

    def update_position(self, time):
        if self.velocity is not None:
            self.position += self.velocity * time

def threedeeDeadReckoning(num_changes):
    # Initial object parameters
    initial_position = [0, 0, 0] # Initial position [x, y, z]
    initial_velocity = [5, 3, 2] # Initial velocity [vx, vy, vz]

    # Create object with initial position and velocity
    obj = Object3D(initial_position, initial_velocity)

    # Store initial position
    estimated_positions = [initial_position]

    # Generate random velocities within the range of -15 to 15 for each component
    # Ensure each iteration of velocity generation does not differ from the last velocity by more than 5
    last_velocity = initial_velocity
    velocities = []
    for _ in range(num_changes):
        new_velocity = [random.uniform(max(last_velocity[i] - 5, -15), min(last_velocity[i] + 5, 15)) for i in range(3)]
        velocities.append(new_velocity)
        last_velocity = new_velocity

    # Time intervals for each velocity change
    time_intervals = [i+1 for i in range(num_changes)]  # Incrementing time intervals by 1

    # Update positions for each time interval and store them
    for i, time in enumerate(time_intervals):
        # Update velocity with a random velocity within the specified range
        obj.velocity = velocities[i]
        # Update position using element-wise multiplication with a NumPy array
        obj.position = obj.position.astype(float)
        obj.position += np.array(obj.velocity) * time
        estimated_positions.append(obj.position.copy()) # Append a copy of the current position


    # Printing velocities to the console for further information gathering
    for givenVelocity in velocities:
        print("Velocity: " + str(givenVelocity))

    # Plotting
    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(111, projection='3d')

    estimated_positions = np.array(estimated_positions) # Convert to numpy array for indexing
    ax.plot(estimated_positions[:, 0], estimated_positions[:, 1], estimated_positions[:, 2], 'bo--', label='Estimated Positions')
    for i, pos in enumerate(estimated_positions[1:], start=1): # Start from index 1 to match time_intervals
        ax.text(pos[0], pos[1], pos[2], f't={time_intervals[i - 1]}', verticalalignment='bottom',
                 horizontalalignment='right')
    ax.plot(initial_position[0], initial_position[1], initial_position[2], 'ro', label='Initial Position')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Dead Reckoning | Random Velocities (3D)')
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    threedeeDeadReckoning(num_changes=5) # Specify the number of velocity changes
