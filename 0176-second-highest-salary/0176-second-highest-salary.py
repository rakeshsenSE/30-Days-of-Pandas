import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_sal = employee.salary.unique()

    if(len(unique_sal) < 2):
        return pd.DataFrame([np.NaN] , columns = ['SecondHighestSalary'])

    else:
        salary = sorted(unique_sal , reverse = True)[1]
        return pd.DataFrame([salary] , columns = ['SecondHighestSalary'])