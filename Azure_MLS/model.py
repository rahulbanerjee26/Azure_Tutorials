import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib
import pickle

data = load_iris()
df = pd.DataFrame(data.data , columns = data.feature_names)
print("Loaded Data Frame")
scaler = MinMaxScaler()
df = scaler.fit_transform(df)
X_train , X_test, y_train, y_test = train_test_split(df , data.target , test_size = 0.2)
print("Created Train/Test Split")

# Update value for n_neighbors
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(X_train , y_train)

print ( model.predict(scaler.fit_transform([[0.9,0.1,0.1,0.9]]))[0])


# To dump
f = 'model/knn.pkl'
with open(f, 'wb') as file:
    pickle.dump(model, file)

# To load
loaded_model = joblib.load(f)

print (
    loaded_model.predict(scaler.fit_transform( [[2,0,2,10]]))[0]
)