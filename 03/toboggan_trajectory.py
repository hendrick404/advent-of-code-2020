file_obj = open('input', 'r')

terrain = []

for line in file_obj:
    terrain.append(line)

def count_trees(terrain, dX, dY):
    treeCount = 0
    posX = 0
    posY = 0
    width = len(terrain[0]) - 1 

    while posY < len(terrain) - dY:
        posX += dX
        posX %= width
        posY += dY
        if terrain[posY][posX] == '#':
            treeCount += 1

    return treeCount

prod = 1
for (x,y) in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    prod *= count_trees(terrain=terrain, dX=x, dY=y)

print('Product of encountered trees: ' + str(prod))