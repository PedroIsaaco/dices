import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from datetime import datetime

def print_current_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time is ", current_time)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

csv_data_file = './diceroll_reduced_new.csv'

print_current_time()
dices_data = pd.read_csv(csv_data_file)
print_current_time()
print('file loaded.')
dices_features = []
for i in range(0, 10000):
    dices_features += [str(i)]
X = dices_data[dices_features]
y = dices_data.value

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))