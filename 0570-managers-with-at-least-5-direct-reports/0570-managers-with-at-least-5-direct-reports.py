import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['managerId'].value_counts()
    df_maneger = df[df >= 5].index
    return employee[employee['id'].isin(df_maneger)][['name']]