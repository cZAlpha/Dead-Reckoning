import numpy as np
import matplotlib.pyplot as plt

class Object:
    def __init__(self, position, velocity=None, acceleration=None):
        self.position = np.array(position)
        self.velocity = np.array(velocity) if velocity is not None else None
        self.acceleration = np.array(acceleration) if acceleration is not None else None

    def update_position(self, time):
        if self.velocity is not None:
            self.position += self.velocity * time
        if self.acceleration is not None:
            # Update velocity with acceleration for this time step
            self.velocity += self.acceleration * time
            # Update position using updated velocity
            self.position += self.velocity * time
            print("Acceleration:", self.acceleration)
            print("Velocity:", self.velocity)


def rabbit(ax):
    # Define parameters
    r = 0.1  # growth rate
    K = 1000  # carrying capacity
    dt = 0.1  # time step size
    num_steps = 1000  # number of time steps

    # Initialize array to store population sizes
    N_values = np.zeros(num_steps + 1)
    N_values[0] = 10  # initial population size

    # Iterate over time steps to compute population sizes
    for n in range(num_steps):
        N_values[n + 1] = N_values[n] + r * dt * N_values[n] * (1 - N_values[n] / K)

    # Plot population size over time
    ax.plot(np.arange(num_steps + 1) * dt, N_values, label='Population Size')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population size')
    ax.set_title('Rabbit Population Growth (Difference Equation)')
    ax.grid(True)

    # Highlight the sequence of population sizes
    for n in range(num_steps):
        ax.plot([n * dt, (n + 1) * dt], [N_values[n], N_values[n + 1]], 'w--')  # Make the line dashed

    ax.legend()


def linear(ax):
    # Initial object parameters
    initial_position = [0, 0]  # Initial position [x, y]
    initial_velocity = [5, 3]  # Initial velocity [vx, vy]
    acceleration = [0, 0]  # Acceleration [ax, ay]

    # Time intervals
    time_intervals = [1, 2, 3]  # List of time intervals for estimation

    # Create object
    obj = Object(initial_position, initial_velocity, acceleration)

    # Store initial position
    estimated_positions = [initial_position]

    # Update positions for each time interval and store them
    for time in time_intervals:
        obj.update_position(time)
        estimated_positions.append(obj.position.copy())  # Append a copy of the current position

    # Plotting
    estimated_positions = np.array(estimated_positions)  # Convert to numpy array for indexing
    ax.plot(estimated_positions[:, 0], estimated_positions[:, 1], 'bo--', label='Estimated Positions')
    for i, pos in enumerate(estimated_positions[1:], start=1):  # Start from index 1 to match time_intervals
        ax.text(pos[0], pos[1], f't={time_intervals[i-1]}', verticalalignment='bottom', horizontalalignment='right')
    ax.plot(initial_position[0], initial_position[1], 'ro', label='Initial Position')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Dead Reckoning | First Order')
    ax.legend()
    ax.grid(True)


def second_order(ax):
    # Initial object parameters
    initial_position = [0, 0]  # Initial position [x, y]
    initial_velocity = [2, 2]  # Initial velocity [vx, vy]
    acceleration = [2, 1]  # Acceleration [ax, ay]

    # Time intervals
    time_intervals = [10, 20, 30]  # List of time intervals for estimation

    # Create object
    obj = Object(initial_position, initial_velocity, acceleration)

    # Store initial position
    estimated_positions = [initial_position]

    # Update positions for each time interval and store them
    for time in time_intervals:
        obj.update_position(time)
        estimated_positions.append(obj.position.copy())  # Append a copy of the current position

    # Plotting
    estimated_positions = np.array(estimated_positions)  # Convert to numpy array for indexing
    ax.plot(estimated_positions[:, 0], estimated_positions[:, 1], 'bo--', label='Estimated Positions')
    for i, pos in enumerate(estimated_positions[1:], start=1):  # Start from index 1 to match time_intervals
        ax.text(pos[0], pos[1], f't={time_intervals[i-1]}', verticalalignment='bottom', horizontalalignment='right')
    ax.plot(initial_position[0], initial_position[1], 'ro', label='Initial Position')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Dead Reckoning | Second Order')
    ax.legend()
    ax.grid(True)


def varying_velocity(ax):
    # Initial object parameters
    initial_position = [0, 0]  # Initial position [x, y]
    initial_velocity = [5, 3]  # Initial velocity [vx, vy]

    # Velocity changes over time
    velocities = [[5, 3], [6, 4], [7, 2], [1, 2], [5, 5], [3, 8], [9, 0], [17, 2], [1, 1], [0, 1]]  # List of velocity vectors for each time interval
    time_intervals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List of time intervals for estimation

    # Create object with initial position and velocity
    obj = Object(initial_position, initial_velocity)

    # Store initial position
    estimated_positions = [initial_position]

    # Update positions for each time interval and store them
    for i, time in enumerate(time_intervals):
        # Update velocity if within bounds of velocity list
        if i < len(velocities):
            obj.velocity = velocities[i]
        # Update position using element-wise multiplication with a NumPy array
        obj.position += np.array(obj.velocity) * time
        estimated_positions.append(obj.position.copy())  # Append a copy of the current position

    # Plotting
    estimated_positions = np.array(estimated_positions)  # Convert to numpy array for indexing
    ax.plot(estimated_positions[:, 0], estimated_positions[:, 1], 'bo--', label='Estimated Positions')
    for i, pos in enumerate(estimated_positions[1:], start=1):  # Start from index 1 to match time_intervals
        ax.text(pos[0], pos[1], f't={time_intervals[i - 1]}', verticalalignment='bottom',
                 horizontalalignment='right')
    ax.plot(initial_position[0], initial_position[1], 'ro', label='Initial Position')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Dead Reckoning | Varying Velocities')
    ax.legend()
    ax.grid(True)


def random_velocity(ax, num_changes):
    # Initial object parameters
    initial_position = [0, 0]  # Initial position [x, y]
    initial_velocity = [5, 3]  # Initial velocity [vx, vy]

    # Random velocities
    velocities = [[np.random.randint(0, 21), np.random.randint(-16, 16)] for _ in range(num_changes)]

    # Time intervals
    time_intervals = list(range(1, num_changes + 1))

    # Create object with initial position and velocity
    obj = Object(initial_position, initial_velocity)

    # Store initial position
    estimated_positions = [initial_position]

    # Update positions for each time interval and store them
    for i, time in enumerate(time_intervals):
        # Update velocity if within bounds of velocity list
        if i < len(velocities):
            obj.velocity = velocities[i]
        # Update position using element-wise multiplication with a NumPy array
        obj.position += np.array(obj.velocity) * time
        estimated_positions.append(obj.position.copy())  # Append a copy of the current position

    # Plotting
    estimated_positions = np.array(estimated_positions)  # Convert to numpy array for indexing
    ax.plot(estimated_positions[:, 0], estimated_positions[:, 1], 'bo--', label='Estimated Positions')
    for i, pos in enumerate(estimated_positions[1:], start=1):  # Start from index 1 to match time_intervals
        if num_changes < 15:  # Gets rid of time interval labels if there are too many steps (looks cluttered)
            ax.text(pos[0], pos[1], f't={time_intervals[i - 1]}', verticalalignment='bottom',
                    horizontalalignment='right')
    ax.plot(initial_position[0], initial_position[1], 'ro', label='Initial Position')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Dead Reckoning | Random Velocities')
    ax.legend()
    ax.grid(True)


if __name__ == "__main__":
    fig, axs = plt.subplots(3, 2, figsize=(14, 12))

    rabbit(axs[0, 0])
    linear(axs[0, 1])
    second_order(axs[1, 0])
    varying_velocity(axs[1, 1])
    random_velocity(axs[2, 0], 10)
    random_velocity(axs[2, 1], 30)

    plt.tight_layout()
    plt.show()
