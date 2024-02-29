result = []
with open('playlistId.txt', 'r') as songs:
    result = [line.strip() for line in songs.readlines()]


print(result)