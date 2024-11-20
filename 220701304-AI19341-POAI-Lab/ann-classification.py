from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

X_train, y_train = make_circles(n_samples=700, noise=0.05)
X_test, y_test = make_circles(n_samples=300, noise=0.05)


sns.scatterplot(X_train[:,0], X_train[:,1], hue=y_train)
plt.title("Train Data")
plt.show()

clf = MLPClassifier(max_iter=1000)
clf.fit(X_train, y_train)


print(f"R2 Score for Training Data = {clf.score(X_train, y_train)}")
print(f"R2 Score for Test Data = {clf.score(X_test, y_test)}")


y_pred = clf.predict(X_test)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
sns.scatterplot(X_test[:,0], X_test[:,1], hue=y_pred, ax=ax[0])
ax[0].title.set_text("Predicted Data")
sns.scatterplot(X_test[:,0], X_test[:,1], hue=y_test, ax=ax[1])
ax[1].title.set_text("Test Data")
plt.show()
