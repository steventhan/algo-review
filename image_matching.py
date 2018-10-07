def countMatches(grid1, grid2):
    grid1_regions = gen_regions(grid1)
    grid2_regions = gen_regions(grid2)
    count = 0

    for region1 in grid1_regions:
        if region1 in grid2_regions:
            count += 1
    return count


def gen_regions(grid):
    visited = set()
    regions = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1" and (i, j) not in visited:
                regions.add(bfs(i, j, grid, visited))

    return regions


def bfs(i, j, grid, visited):
    q = [(i, j)]
    res = set()
    while q:
        new_q = []
        for i, j in q:
            res.add((i, j))
            visited.add((i, j))
            for neighbor in neighbors(i, j, grid):
                if neighbor not in visited:
                    new_q.append(neighbor)
        q = new_q
    return frozenset(res)


def neighbors(i, j, grid):
    neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
    return [(i, j) for (i, j) in neighbors if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"]

grid1 = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 0]
]
grid2 = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1]
]

grid3 = [
    [0,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,1,1],
]
grid4 = [
    [0,1,0,1],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,1,1],
]
print(countMatches(grid3, grid4))
