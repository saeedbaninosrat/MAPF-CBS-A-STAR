import plotly.express as px
import random

def create_maze(maze_size, zeros_number):
    # Create a random maze with maze size and number of blocks got from main function 
    new_maze = [[5] * maze_size for _ in range(maze_size)]
    zeros_generated = 0
    while zeros_generated < zeros_number:
        x = random.randint(0, maze_size - 1)
        y = random.randint(0, maze_size - 1)
        if new_maze[x][y] == 5:
            new_maze[x][y] = 0
            zeros_generated += 1
    maze = []
    for row in new_maze:
        maze.append(row)
        
        
    # Todo: Uncomment the following lines to generate the maze manually
    # Note that the fives are allowed paths and zeros are blocks    
    # maze = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5],
    #         [5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5],
    #         [5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5],
    #         [5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5],
    #         [5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5],
    #         [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5],
    #         [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #         [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
    
    return maze

class Node():
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self) -> str:
        return f"{self.position}"


class Agent:
    def __init__(self, start_position, end_position):
        self.start_node = Node(None, start_position)
        self.end_node = Node(None, end_position)
        self.current_node = Node(None, start_position)
        self.open_list = []
        self.close_list = []
        self.path = []
        
def generate_agents(number_of_agents, maze_size, maze):
    # Agents get randomly generated in this function
    agents = []
    list_of_random_points = []
    for _ in range(number_of_agents):
        start, end = generate_random_points(maze_size, maze, list_of_random_points)
        agent = Agent(start, end)
        agents.append(agent)
        
    # Todo: Uncomment these lines and change numbers to generate agents manually
    # Todo: You should set agents respect the number of agents we define in main function
    # agents[0] = Agent((2, 0) ,(12, 5))   
    # agents[1] = Agent((6, 0) ,(6, 14))
    # agents[2] = Agent((0, 0) ,(12, 6))
    # agents[3] = Agent((4, 4) ,(0, 12))
    # agents[4] = Agent((0, 4) ,(4, 0))
    # agents[5] = Agent((1, 4) ,(4, 1))
    
    for agent in agents:
        print("start and end positions of agent ",agents.index(agent) + 1,"is: ",agent.start_node.position, agent.end_node.position)
    
    # We check if start and end positions of agents are different and not on blocks
    counter = 0
    for agent in agents:
        counter += 1
        if(agent.start_node.position == agent.end_node.position):
            raise Exception("Start and End positions of Agent " + str(counter) +" are same")
        if(maze[agent.start_node.position[0]][agent.start_node.position[1]] == 0): 
            raise Exception("Start position of Agent "+str(counter)+ " is on Block in the position: " )
        if(maze[agent.end_node.position[0]][agent.end_node.position[1]] == 0): 
            raise Exception("End position of Agent "+str(counter)+" is on Block in the position: ")
    return agents

# Random points for start and end nodes of agents are randomly generated from this function
def generate_random_points(maze_size, maze, list_of_random_points):
    while True:
        start_x = random.randint(0, maze_size - 1)
        start_y = random.randint(0, maze_size - 1)
        end_x = random.randint(0, maze_size - 1)
        end_y = random.randint(0, maze_size - 1)
        if (start_x, start_y) != (end_x, end_y) and maze[start_x][start_y] != 0 and maze[end_x][end_y] != 0 and (start_x, start_y) not in list_of_random_points and (end_x, end_y) not in list_of_random_points  :
            list_of_random_points.append((start_x, start_y))
            list_of_random_points.append((end_x, end_y))
            return (start_x, start_y), (end_x, end_y)
        
# Check if all agents arrived to their end nodes
def reach_final(agents):
    for agent in agents:
        if agent.current_node != agent.end_node:
            return(False)
    return(True)

def get_constraint_tree(agents):
    final_paths = []
    for agent in agents:
        final_path = []  
        goal = agent.path[-1]
        while goal is not None:
            final_path.append(goal)
            goal = goal.parent
        final_path = final_path[::-1]
        final_paths.append(final_path)
    constraint_tree = []
    for i, path in enumerate(final_paths):
        for j, other_path in enumerate(final_paths):
            if i < j:
                for k, item in enumerate(path):
                    for p, other_item in enumerate(other_path):
                        if k == p and item == other_item:
                            if item.parent.h < other_item.parent.h:
                                constraint_tree.append((i, k, item.parent))
                            else:
                                constraint_tree.append((j, p, other_item.parent))
    return(constraint_tree, final_paths)


def generate_children(agents, maze):
    maze_x = len(maze)-1
    maze_y = len(maze[0])-1
    for agent in agents:
        if agent.current_node != agent.end_node:
        # Generate children
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0),(-1, -1), (1, 1), (-1, 1), (1, -1)]: # Adjacent squares

                # Get node position
                adjacent_position = (agent.current_node.position[0] + new_position[0], agent.current_node.position[1] + new_position[1])

                # Make sure within range
                if adjacent_position[0] > maze_x or adjacent_position[0] < 0 or adjacent_position[1] > maze_y or adjacent_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if maze[adjacent_position[0]][adjacent_position[1]] == 0:
                    continue

                # Create new node
                new_node = Node(agent.current_node, adjacent_position)

        
                # Child is on the closed list
                if new_node in agent.close_list:
                    continue

                # Create the f, g, and h values
                new_node.g = agent.current_node.g + 1
                new_node.h = ((new_node.position[0] - agent.end_node.position[0]) ** 2) + ((new_node.position[1] - agent.end_node.position[1]) ** 2)
                new_node.f = new_node.g + new_node.h

                # new_node is already in the open list
                if new_node not in agent.close_list:
                    if new_node in agent.open_list:
                        conflicted_agent = agent.open_list.index(new_node)
                        duplicated = agent.open_list[conflicted_agent]
                        if new_node.g < duplicated.g:
                            agent.open_list.append(new_node)
                    else:
                        agent.open_list.append(new_node)
        
        if len(agent.open_list) > 0 and agent.current_node != agent.end_node:
            # Get the agents current node
            agent.current_node = agent.open_list[0]
            for item in agent.open_list:
                if item.f < agent.current_node.f:
                    agent.current_node = item

            # Pop current node off open list, add to closed list
            agent.open_list.remove(agent.current_node)
            agent.path.append(agent.current_node)
            agent.close_list.append(agent.current_node)
            
def cbs_algorithm(maze, agents):
    
    new_maze = maze

    # Add the agents start node
    counter = 0
    for agent in agents:
        counter += 1
        agent.path.append(agent.current_node)
        agent.close_list.append(agent.start_node)

    # Loop until you find the end
    while True:
        # Found the goal
        if reach_final(agents):
            
            constraint_tree, final_paths = get_constraint_tree(agents)

            for l, i, val in constraint_tree:
                final_paths[l].insert(i, val)
            final_path_primes = final_paths

            counter = 2
            for final_path_prime in final_path_primes:
                print("agent ", counter - 1," has the path",final_path_prime) # Print reversed path
                for path_position in final_path_prime:
                    new_maze[path_position.position[0]][path_position.position[1]] = counter * 2
                counter +=1
            
            return(new_maze)
        
        generate_children(agents, maze)


def main():
    # Todo: Set maze size by changing this number
    maze_size = 15
    
    # Todo: Set Number of Blocks by changing this number
    number_of_blocks = 60

    # Todo: Set Number of Agents by changing this number
    number_of_agents = 4
    
    maze = create_maze(maze_size, number_of_blocks)
    agents = generate_agents(number_of_agents, maze_size, maze)
    new_maze = cbs_algorithm(maze, agents)

    fig = px.imshow(new_maze, color_continuous_midpoint=0.0 , range_color= [-(number_of_agents * 2)+2,(number_of_agents * 2)+2], color_continuous_scale = 'Picnic' )
    fig.show()


main()