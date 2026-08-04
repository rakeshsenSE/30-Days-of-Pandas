import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    res = employees.groupby(['event_day' , 'emp_id'])['total_time'].sum().reset_index()
    res.rename(columns = {'event_day' : 'day'},inplace = True)

    return res