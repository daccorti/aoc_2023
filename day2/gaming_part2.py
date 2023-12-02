# only 12 red cubes, 13 green cubes, and 14 blue cubes
import numpy

f = open("part_a.txt",'r')
contents = f.readlines()
data = [line.strip("\n") for line in contents]

def fewest_colors(games):
    max_counts = {}
    for game in games:
        game_name, attempts = game.split(': ')
        max_counts[game_name] = {'red': 0, 'green': 0, 'blue': 0}

        # Process each attempt
        for attempt in attempts.split('; '):
            for color_count in attempt.split(', '):
                count, color = color_count.split(' ')
                count = int(count)
                # Update max count if current count is higher
                if count > max_counts[game_name][color]:
                    max_counts[game_name][color] = count

    return max_counts

# Apply the function to get max count per color per game
max_counts_per_game = fewest_colors(data)

# print(max_counts_per_game["Game 1"]["red"])

answer = []

for game in max_counts_per_game:
    res = []
    for vals in max_counts_per_game[game].items():
        res.append(vals[1])
    answer.append(numpy.prod(res))

print(sum(answer))
