import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        department,
        left_on = 'departmentId',
        right_on = 'id',
        suffixes = ('_employee' , '_department')
    )

    highst_salary = (df['salary'] == df.groupby('departmentId')['salary'].transform('max'))

    result_df = df[highst_salary]

    result_df = result_df[['name_department' , 'name_employee' , 'salary']]
    result_df.columns = ['Department' , 'Employee','Salary']

    return result_df


    