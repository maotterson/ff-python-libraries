import pandas as pd
import matplotlib.pyplot as plt

playerFile = pd.read_csv('sample-players.csv')
print(playerFile.to_string())

playerFile.plot(kind = 'bar', x = 'LastName', y = 'Rnk')
plt.show()