#import pandas as pd
#data = pd.read_csv("C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv")

#x = data["genres"]
#y=data["content_rating"]

#print(x,y)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies_2.xlsx")
print(data)
pivot=data.groupby(['Fresh']).mean()
fresh_movie=pivot.loc[:,"movie_title(Mine)":"tomatometer_status(Units)"]
fresh_movie.plot(kind='bar')
plt.show()
