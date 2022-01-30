import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from datetime import datetime
from create_dataset import create_random_dataset

def check_set(given_set, set_label):
    print("checking label '%s':" %(set_label))
    x = np.isnan(given_set)
    if np.any(np.isnan(given_set)):
        print(x)
        #np.argwhere(np.isnan(given_set))
        file_name = set_label + "_nan.csv"
        export_set(given_set, file_name)
    if not np.any(np.isfinite(given_set)):
        print("found inf")
        file_name = set_label + "_inf.csv"
        export_set(given_set, file_name)

def export_set(given_set, file_name):
    df = pd.DataFrame(given_set)
    df.to_csv(file_name)

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
csv_data_file = "diceroll_reduced_rnd.csv"#create_random_dataset(10, file_path, file_name)
print_current_time("data created.")
#read data
print_current_time("loading file '%s'" %(csv_data_file))
dices_dataframe = pd.read_csv(csv_data_file)
#currently we have problems with some bitmap data - nan values occur, which have to be eliminated
dices_dataframe = dices_dataframe.interpolate()
print_current_time("files loaded.")

#process data
max_columns = 100000
dices_features = []
for i in range(0, max_columns - 1):
    dices_features += [str(i)]
X = dices_dataframe[dices_features]
y = dices_dataframe.value
print_current_time("csv read.")

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
check_set(train_X, "train_X")
check_set(val_X, "val_X")
check_set(train_y, "train_y")
check_set(val_y, "val_y")
print_current_time("model trained.")
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

print_current_time("finished.")