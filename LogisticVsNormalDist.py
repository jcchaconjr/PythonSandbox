from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(random.normal(scale=2, size=1000), label="normal")
sns.histplot(random.logistic(size=1000), label="logistic")

plt.show()