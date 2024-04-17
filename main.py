import numpy as np
import matplotlib.pyplot as plt

class Object:
    def __init__(self, position, velocity):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def update_position(self, time):
        self.position += self.velocity * time  # Update position based on time

def main():
    # Initial object parameters
    initial_position = [0, 0]  # Initial position [x, y]
    velocity = [5, 3]  # Initial velocity [vx, vy]

    # Time intervals
    time_intervals = [1, 2, 3]  # List of time intervals for estimation

    # Create object
    obj = Object(initial_position, velocity)

    # Store initial position
    estimated_positions = [initial_position]

    # Update positions for each time interval and store them
    for time in time_intervals:
        obj.update_position(time)
        estimated_positions.append(obj.position.copy())  # Append a copy of the current position

    # Plotting
    plt.figure()
    estimated_positions = np.array(estimated_positions)  # Convert to numpy array for indexing
    plt.plot(estimated_positions[:, 0], estimated_positions[:, 1], 'bo--', label='Estimated Positions')
    for i, pos in enumerate(estimated_positions[1:], start=1):  # Start from index 1 to match time_intervals
        plt.text(pos[0], pos[1], f't={time_intervals[i-1]}', verticalalignment='bottom', horizontalalignment='right')
    plt.plot(initial_position[0], initial_position[1], 'ro', label='Initial Position')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Dead Reckoning: Initial and Estimated Positions')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print initial and estimated positions
    print("Initial position:", initial_position)
    for i, pos in enumerate(estimated_positions[1:], start=1):
        print("Estimated position after {} seconds: {}".format(time_intervals[i-1], pos))

if __name__ == "__main__":
    main()
