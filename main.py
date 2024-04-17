import numpy as np

class Object:
    def __init__(self, position, velocity):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def update_position(self, time):
        self.position += self.velocity * time

def main():
    # Initial object parameters
    initial_position = [0, 0]  # Initial position [x, y]
    velocity = [5, 3]  # Initial velocity [vx, vy]

    # Time interval
    time = 2  # Time interval for estimation

    # Create object
    obj = Object(initial_position, velocity)

    # Print initial position
    print("Initial position:", obj.position)

    # Update position using dead reckoning
    obj.update_position(time)

    # Print estimated position
    print("Estimated position after {} seconds:".format(time), obj.position)

if __name__ == "__main__":
    main()
