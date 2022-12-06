def floodFill(image, sr, sc, newColor):
    starting_num = image[sr][sc]
    max_row = len(image)
    max_col = len(image[0])
    if starting_num == newColor:
        return image

    def fill(r, c):
        if image[r][c] == starting_num:
            image[r][c] = newColor
            if r >= 1:
                fill(r-1, c)
            if r+1 < max_row:
                fill(r+1, c)

            if c >= 1:
                fill(r, c-1)
            if c+1 < max_col:
                fill(r, c+1)

    fill(sr, sc)
    return image


image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
newColor = 2

print(floodFill(image, sr, sc, newColor))
