import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f'getNthHighestSalary({N})'

    unique = employee['salary'].drop_duplicates()

    if N <= 0 or len(unique) < N:
        return pd.DataFrame({col : [None]})
   
    Nth = unique.sort_values(ascending=False).iloc[N - 1]
    return pd.DataFrame({col:[Nth]})
