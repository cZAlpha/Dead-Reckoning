class Object:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update_position(self, time):
        self.x += self.velocity_x * time
        self.y += self.velocity_y * time

def main():
    # Initial object parameters
    initial_x = 0  # Initial x-coordinate
    initial_y = 0  # Initial y-coordinate
    velocity_x = 5  # Initial velocity in x-direction
    velocity_y = 3  # Initial velocity in y-direction

    # Time interval
    time = 2  # Time interval for estimation

    # Create object
    obj = Object(initial_x, initial_y, velocity_x, velocity_y)

    # Print initial position
    print("Initial position: ({}, {})".format(obj.x, obj.y))

    # Update position using dead reckoning
    obj.update_position(time)

    # Print estimated position
    print("Estimated position after {} seconds: ({}, {})".format(time, obj.x, obj.y))

if __name__ == "__main__":
    main()
