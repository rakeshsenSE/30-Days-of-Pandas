import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_c = company[company['name'] == 'RED']['com_id']

    red_sales = orders[orders['com_id'].isin(red_c)]['sales_id']

    result = sales_person[~sales_person['sales_id'].isin(red_sales)][['name']]

    return result