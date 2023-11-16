text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

nList = list(map(len, ["How", "I", "want", "a", "drink", "alcoholic", "of", "course", "after", "the", "heavy", "chapters", "involving",
"quantum", "mechanics", "All", "of", "thy", "geometry", "Herr Planck", "is", "fairly", "hard",]))
print(nList)

n = int("".join(map(str, nList)))
print(n)
