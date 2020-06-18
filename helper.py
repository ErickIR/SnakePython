def calculate_distance(P, Q):
    X = (Q[0] - P[0]) ** 2
    Y = (Q[1] - P[1]) ** 2
    return (X + Y) ** 0.5

def is_wall_colliding(pos, WIDTH, HEIGHT):
        return pos[0] >= (WIDTH) or pos[0] <= 0 or pos[1] >= (HEIGHT) or pos[1] <= 0
    
def are_blocks_colliding(block, other):
    return block[0] == other[0] and block[1] == other[1]
    
def is_snake_colliding(blocks):
    for i in range(0, len(blocks)):
        for j in range(0, len(blocks)):
            if i == j:
                continue
            if are_blocks_colliding(blocks[i], blocks[j]):
                return True
    return False