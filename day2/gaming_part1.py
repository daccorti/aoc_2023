# only 12 red cubes, 13 green cubes, and 14 blue cubes
from itertools import groupby
import re

f = open("part_a.txt",'r')
contents = f.readlines()
data = [line.strip("\n") for line in contents]

def parse_and_filter(games):
    filtered_games = []
    for game in games:
        game_name, attempts = game.split(': ')
        all_attempts_pass = True  # Flag to check if all attempts pass the filter

        
        # Process each attempt separately
        for attempt in attempts.split('; '):
            # Initializing a dictionary to hold the counts for this attempt
            attempt_counts = {}
            for color_count in attempt.split(', '):
                count, color = color_count.split(' ')
                attempt_counts[color] = int(count)
                
           # Check if this attempt passes the filtering criteria
            if not (attempt_counts.get('red', 0) <= 12 and
                    attempt_counts.get('green', 0) <= 13 and
                    attempt_counts.get('blue', 0) <= 14):
                all_attempts_pass = False
                break  # If one attempt fails, the game does not pass

        if all_attempts_pass:
            filtered_games.append(game_name)

    return filtered_games

# Apply the modified function to the games list
filtered_games = parse_and_filter(data)
answer = [int(re.sub("[^0-9]", "",i)) for i in filtered_games]

print(sum(answer))

