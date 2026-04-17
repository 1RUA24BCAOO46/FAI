def dfs_maze(maze, start, goal):
    # Dimensions of the Maze i.e., Rows and columns
    rows = len(maze)
    cols = len(maze[0])

    # Stack has the position in the form of (current_node, path_travelled)
    stack = [(start, [start])]

    # This helps us to create a record of the visited nodes
    visited = set()

    # Continue until there is no path to explore more
    while stack:
        # Pop Out the last position as DFS uses LIFO
        (x, y), path = stack.pop()

        # If the goal is reached, the path is return
        if (x, y) == goal:
            return path
        
        # If this position hasn't been visited yet
        if (x, y) not in visited:
            visited.add((x, y)) # Mark it as visited

            # Possible moves: Up, Down, Left, Right
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            # Explore each possible moves
            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                # Checking if it is within the boundaries, walls (maze[nx][ny] != 1), and visited status
                if (0 <= nx < rows and 
                    0 <= ny < cols and 
                    maze[nx][ny] != 1 and 
                    (nx, ny) not in visited):

                    # Add new position and updated path to the stack
                    stack.append(((nx ny), path + [(nx, ny)]))

    # If there is no path, None is returned as the value
    return None

maze = [['S', 0, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 'G']]

start = (0, 0)
goal = (3, 3)

solution = dfs_maze(maze, start, goal)

if solution:
    print("Path Found:")
    print(solution)
else:
    print("No path found.")
Path Found:
[(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)]
Q1. 3 Different maze combinations.

maze = [['S', 1, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 'G']]

start = (0, 0)
goal = (3, 3)

solution = dfs_maze(maze, start, goal)

if solution:
    print("Path Found:")
 print(solution)
else:
    print("No path found.")
No path found.
maze = [['S', 0, 0, 0],
        [0, 0, 'G', 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0]]

start = (0, 0)
goal = (1, 2)

solution = dfs_maze(maze, start, goal)

if solution:
    print("Path Found:")
    print(solution)
else:
    print("No path found.")
Path Found:
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2)]
maze = [['S', 'G', 0, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1]]

start = (0, 0)
goal = (0, 1)

solution = dfs_maze(maze, start, goal)

if solution:
    print("Path Found:")
    print(solution)
else:
    print("No path found.")
Path Found:
[(0, 0), (0, 1)]
