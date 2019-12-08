import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dataframe
df = pd.read_csv('q6CarData.csv', index_col = 'hidden layers')

ax = df['avg'].plot()
ax.set_ylabel('avg accuracy')
ax.set_title('Accuracy v. Hidden Layers -- CarData')
plt.show()

# create dataframe
df = pd.read_csv('q6PenData.csv', index_col = 'hidden layers')

ax = df['avg'].plot()
ax.set_ylabel('avg accuracy')
ax.set_title('Accuracy v. Hidden Layers -- PenData')
plt.show()
