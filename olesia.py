import pandas as pd


def create_csv_file(path):
    data = {'Data': [], 'Goal': [], 'Number of time(goal)': [], 'Number of time(reality)': [
    ], 'Success': [], 'Failure': []}
    df = pd.DataFrame(data, columns=[
                      'Data', 'Goal', 'Number of time(goal)', 'Number of time(reality)', 'Success', 'Failure'])
    return df
