# Walking Robot Simulation
# A robot on an infinite XY-plane starts at point (0, 0) and faces north.
# The robot can receive one of three possible types of commands:

# -2: turn left 90 degrees,
# -1: turn right 90 degrees, or
# 1 <= k <= 9: move forward k units.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi).

# If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)
# Return the maximum Euclidean distance that the robot will be from the origin squared (i.e. if the distance is 5, return 25).

# Note:

# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.

# Failed

class Solution:

    # Not original but almost same method as mine
    # 99.19%
    def robotSim2(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Put obstacles into a set
        os = set(map(tuple, obstacles))
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        index = 0
        x = y = 0
        maximum = 0
        for c in commands:
            # Turn Right
            if c == -1:
                index += 1
            # Turn Left
            elif c == -2:
                index -= 1
            else:
                index %= 4
                for i in range(c):
                    if (x + dx[index], y + dy[index]) not in os:
                        x += dx[index]
                        y += dy[index]
                maximum = max(maximum, x ** 2 + y ** 2)
        return maximum

    # Original
    # Failed
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        directions = (0, 1, 2, 3)
        # North = 0 or -4 West = 1 or -3 South = 2 or -2 East = 3 or -1
        direction_index = 0
        coordinate = [0, 0]
        maximum = 0
        for command in commands:
            if command == -1:
                direction_index -= 1
            elif command == -2:
                direction_index += 1
            else:
                if direction_index >= 4:
                    direction_index %= 4
                elif direction_index <= -5:
                    direction_index = -(abs(direction_index) % 4)
                direction = directions[direction_index]
                if direction == 0:
                    start = coordinate[1]
                    coordinate[1] += command
                    for obstacle in obstacles:
                        if obstacle[0] == coordinate[0] and obstacle[1] > start:
                            coordinate[1] = obstacle[1] - 1
                elif direction == 1:
                    start = coordinate[0]
                    coordinate[0] -= command
                    for obstacle in obstacles:
                        if obstacle[1] == coordinate[1] and obstacle[0] < start:
                            coordinate[0] = obstacle[0] + 1
                elif direction == 2:
                    start = coordinate[1]
                    coordinate[1] -= command
                    for obstacle in obstacles:
                        if obstacle[0] == coordinate[0] and obstacle[1] < start:
                            coordinate[1] = obstacle[1] + 1
                elif direction == 3:
                    start = coordinate[0]
                    coordinate[0] += command
                    for obstacle in obstacles:
                        if obstacle[1] == coordinate[1] and obstacle[0] > start:
                            coordinate[0] = obstacle[0] - 1
                maximum = max(maximum, coordinate[0] ** 2 + coordinate[1] ** 2)
        return maximum


if __name__ == "__main__":
    print(Solution().robotSim([4, -1, 3], []) == 25)
    print(Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]) == 65)
    print("Method2")
    print(Solution().robotSim2([4, -1, 3], []) == 25)
    print(Solution().robotSim2([4, -1, 4, -2, 4], [[2, 4]]) == 65)
