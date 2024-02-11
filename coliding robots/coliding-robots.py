import random

n = 4
healths = []
directions = []
for i in range(n):
    healths.append(random.randint(10, 50))
    directions.append(random.randint(0, 1))

robots = [[health, direction] for health, direction in zip(healths, directions)]


print(robots)

def solve(n, robots):
    survivors = []
    for i, robot in enumerate(robots):
        if robot[1] == 0 and robot[0] > 0:
            if i > 0:
                if robots[i-1][1] == 1 and robots[i-1][0] > 0:
                    h1 = robot[0]
                    h2 = robots[i-1][0]
                    robot[0] = h1 - h2
                    robots[i-1][0] = h2 - h1
        if robot[1] == 1 and robot[0] > 0:
            if i < n-2:
                if robots[i+1][1] == 0 and robots[i+1][0] > 0:
                    h1 = robot[0]
                    h2 = robots[i+1][0]
                    robot[0] = h1 - h2
                    robots[i+1][0] = h2 - h1
    for robot in robots:
        if robot[0] >= 0:
            survivors.append(robot)
    return survivors


print(solve(n, robots))
