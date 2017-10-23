#!/usr/bin/env python


class Rover:
    """Class to define rover and the actions performed
    by the rover.
    """

    def __init__(self, current_position_x, current_position_y, current_direction, upper_bound_x, upper_bound_y):
        self.x = current_position_x
        self.y = current_position_y
        self.direction = current_direction
        self.upper_bound_x = upper_bound_x
        self.upper_bound_y = upper_bound_y

    def rotate(self, command):
        """This method rotates the rover 90deg based on it's
        current direction and command given.

        :param command:
            Command to rotate the rover.
        """
        if (self.direction == 'N' and command == 'L') or (self.direction == 'S' and command == 'R'):
            self.direction = 'W'
        elif (self.direction == 'N' and command == 'R') or (self.direction == 'S' and command == 'L'):
            self.direction = 'E'
        elif (self.direction == 'W' and command == 'L') or (self.direction == 'E' and command == 'R'):
            self.direction = 'S'
        else:
            self.direction = 'N'

    def move(self):
        """This method moves the rover in current direction."""
        if self.direction == 'N' and ((self.y + 1) <= self.upper_bound_y):
            self.y += 1
        elif self.direction == 'S' and ((self.y - 1) >= 0):
            self.y -= 1
        elif self.direction == 'W' and ((self.x - 1) >= 0):
            self.x -= 1
        elif self.direction == 'E' and ((self.x + 1) <= self.upper_bound_x):
            self.x += 1

    def process_command(self, commands):
        """This method processes the commands given to the rover.

        :param commands:
            Commands given to the rover in form of a string.
        """
        for command in commands:
            if command in ['L', 'R']:
                self.rotate(command)
            else:
                self.move()

    def current_location(self):
        print '%d %d %s' % (self.x, self.y, self.direction)


def main():
    # Taking input of upper bound and mapping it to int
    upper_bound_x, upper_bound_y = map(int, raw_input().split())
    # Assuming two rovers
    rover_count = 2
    while rover_count:
        rover_count -= 1

        # Taking input of rover position and direction and mapping it to appropriate type
        current_position_x, current_position_y, current_direction = raw_input().split()
        current_position_x, current_position_y = map(int, [current_position_x, current_position_y])

        # Taking input for commands
        commands = raw_input()

        # Instantiating Rover
        rover = Rover(
            current_position_x, current_position_y, current_direction,
            upper_bound_x, upper_bound_y
        )

        # Processing the commands given to rover
        rover.process_command(commands)
        # Printing the current location after processing commands
        rover.current_location()


if __name__ == '__main__':
    main()

