import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from datetime import datetime

def print_current_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time is ", current_time)

print_current_time()
dices_data = pd.read_csv('./diceroll_slim_short.csv')
print_current_time()
print('file loaded.')
dices_features = []
for i in range(0, 25):
    dices_features += [str(i)]
X = dices_data[dices_features]
y = dices_data.value
dices_model = DecisionTreeRegressor(random_state=1)
dices_model.fit(X, y)

print("making predictions")
print(X.head())
print("the predictions are")
print(dices_model.predict(X.head()))
print('end.')