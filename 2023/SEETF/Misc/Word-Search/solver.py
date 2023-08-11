def search_word(puzzle, word):
    rows = len(puzzle)
    cols = len(puzzle[0])

    # Define directions (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == word[0]:
                for direction in directions:
                    dx, dy = direction
                    found = True
                    for k in range(1, len(word)):
                        x = i + k * dx
                        y = j + k * dy
                        if x < 0 or x >= rows or y < 0 or y >= cols or puzzle[x][y] != word[k]:
                            found = False
                            break
                    if found:
                        return (i, j), (x, y)

    return None

# Open the wordsearch.txt file
with open("wordsearch1.txt", "r") as file:
    lines = file.readlines()

# Remove newline characters and create the puzzle grid
puzzle = [list(line.strip()) for line in lines]

# List of words to search for
words = ["SEE", "CTF", "_", "}"]

# Search for each word in the puzzle
for word in words:
    result = search_word(puzzle, word)
    if result:
        start, end = result
        print(f"Found {word} at ({start[0]}, {start[1]}) to ({end[0]}, {end[1]})")
    else:
        print(f"{word} not found in the puzzle.")

# Close the file
file.close()
