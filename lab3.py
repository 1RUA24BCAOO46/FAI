from collections import deque

def bfs_maze(maze, start, goal):
    
    # Get dimensions of the maze for boundary checking later
    rows = len(maze)
    cols = len(maze[0])

    # Track visited cells to avoid revisiting them and prevent infinite loops
    visited = set()
    visited.add(start)

    # Initialization of the queue with the starting position
    queue = deque([(start, [start])])

    # Continue searching as long as there are positions left to explore
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny =  x + dx, y + dy
\
            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] != 1 and
                (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None
maze = [
    ['S', 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 'G']
]

start = (0, 0)
goal = (3, 3)

solution = bfs_maze(maze, start, goal)

if solution:
    print("Path found:")
    print(solution)
else:
    print("No path found.")
