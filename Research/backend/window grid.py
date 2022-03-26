for y in range(height):
    for x in range(width):
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(window, color, rect)