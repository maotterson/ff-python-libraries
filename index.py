import pandas

playerFile = pandas.read_csv('sample-players.csv')
print(playerFile.to_string())