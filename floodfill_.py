def floodfill(image, sr, sc, newColor):
    first_num = image[sr][sc]
    max_row = len(image)
    max_col = len(image[0])
    if first_num == newColor:
        return image

    def fill(sr, sc):
        if image[sr][sc] == first_num:
            image[sr][sc] = newColor
            if sr-1 >= 0:
                fill(sr-1, sc)
            if sr+1 < max_row:
                fill(sr+1, sc)
            if sc-1 >= 0:
                fill( sr, sc-1)
            if sc+1 < max_col:
                fill(sr, sc+1)

    fill(sr, sc)
    return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

print(floodfill(image, sr, sc, newColor))

# SOLUTION
# class Solution(object):
#     def floodFill(self, image, sr, sc, newColor):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type newColor: int
#         :rtype: List[List[int]]
#         """
#         starting_num = image[sr][sc]
#         max_row = len(image)
#         max_col = len(image[0])
#         if starting_num == newColor:
#             return image

#         def fill(r, c):
#             if image[r][c] == starting_num:
#                 image[r][c] = newColor
#                 if r >= 1:
#                     fill(r-1, c)
#                 if r+1 < max_row:
#                     fill(r+1, c)

#                 if c >= 1:
#                     fill(r, c-1)
#                 if c+1 < max_col:
#                     fill(r, c+1)

#         fill(sr, sc)
#         return image
