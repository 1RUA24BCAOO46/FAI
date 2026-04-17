def dfs_maze_3d(maze, start, goal):
    # Dimensions of maze
    depth = len(maze)          # number of layers (Z axis)
    rows = len(maze[0])        # X axis
    cols = len(maze[0][0])     # Y axis

    # Stack stores: (current_position, path_so_far)
    stack = [(start, [start])]

    # Track visited cells to avoid loops
    visited = set()

    # DFS loop continues until stack is empty
    while stack:
        (z, x, y), path = stack.pop()

        # If goal reached, return the path
        if (z, x, y) == goal:
            return path

        # Process only if not visited
        if (z, x, y) not in visited:
            visited.add((z, x, y))

            # Possible 3D movements:
            # Up/Down layer + 4 directions on same layer
            moves = [
                (0, -1, 0),   # move up (row)
                (0, 1, 0),    # move down
                (0, 0, -1),   # move left
                (0, 0, 1),    # move right
                (-1, 0, 0),   # move to lower layer
                (1, 0, 0)     # move to upper layer
            ]

            # Explore all neighbors
            for dz, dx, dy in moves:
                nz, nx, ny = z + dz, x + dx, y + dy

                # Check boundaries, wall, and visited condition
                if (0 <= nz < depth and
                    0 <= nx < rows and
                    0 <= ny < cols and
                    maze[nz][nx][ny] != 1 and
                    (nz, nx, ny) not in visited):
  # Add new position with updated path
                    stack.append(((nz, nx, ny), path + [(nz, nx, ny)]))

    # If no path found
    return None
maze = [
    [['S', 0, 1, 0],
     [0, 0, 1, 0],
     [1, 0, 0, 0],
     [1, 1, 0, 0]],
    
    [[1, 0, 1, 0],
     [0, 0, 1, 0],
     [1, 0, 0, 0],
     [1, 1, 0, 'G']]]

start = (0, 0, 0)
goal = (1, 3, 3)

solution = dfs_maze_3d(maze, start, goal)

if solution:
    print("Path Found:")
    print(solution)
else:
    print("No path found.")
