import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from datetime import datetime
from process_image import create_random_dataset

def print_current_time(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("current time: %s - %s" %(current_time, message))

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

file_path = "./Images/target_output/*.*"
file_name = "diceroll_reduced"
#csv: https://realpython.com/python-csv/
print_current_time("starting ...")
#create data
csv_data_file = create_random_dataset(100, file_path, file_name)
print_current_time("data created.")
#read data
dices_data = pd.read_csv(csv_data_file)
print_current_time("files loaded.")

#process data
max_columns = 10000
dices_features = []
for i in range(0, max_columns - 1):
    dices_features += [str(i)]
X = dices_data[dices_features]
y = dices_data.value
print_current_time("csv read.")

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
print_current_time("model trained.")
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

print_current_time("finished.")