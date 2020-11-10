import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

data = pd.read_csv('student-mat.csv', sep=";")
#print(data.head())
data = data[["G1","G2","G3","studytime","failures","absences"]]
#print(data.head())

predict = "G3"
# our features
X = np.array(data.drop([predict], 1))
# our target/labels
y = np.array(data[predict])
X_train,X_test,y_train,y_test = sklearn.model_selection.train_test_split(X,y,test_size=0.1)
"""
best = 0
for _ in range(30):
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(X_train,y_train)
    acc = linear.score(X_test,y_test)
    print(acc)
    if acc > best:
        best = acc
        with open("studentmodel.pickle","wb") as f:
            pickle.dump(linear,f)
"""
"""
# We can save learning process and load it later
linear = linear_model.LinearRegression()
linear.fit(X_train,y_train)
acc = linear.score(X_test,y_test)
print(acc)
# Na postawie naszych atrybutow mozemy przewidziec z 80 % pewnoscia jaka ocene otrzyma na koniec ziomek
# wb it is write as bites
with open("studentmodel.pickle","wb") as f:
    pickle.dump(linear,f)
"""
pickle_in = open("studentmodel.pickle","rb")
linear = pickle.load(pickle_in)

print("Co" , linear.coef_)
# Tyle ile mamy atrybutow tyle bedzie wspolczynnikow bo to po X idzie
print("Intercept:" , linear.intercept_)

predictions = linear.predict(X_test)

for x in range(len(predictions)):
    print(predictions[x],X_test[x],y_test[x])
p="studytime"
style.use("ggplot")
plt.scatter(data[p],data[predict])
plt.xlabel(p)
plt.ylabel("Final Grade")
plt.show()