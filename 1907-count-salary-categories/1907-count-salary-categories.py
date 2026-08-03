import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame({
        'category' : ['Low Salary','Average Salary','High Salary'],
        'accounts_count' : [
            len(accounts[accounts['income'] < 20000]),
            len(accounts[(accounts["income"] >= 20000)& (accounts["income"] <= 50000)]),
            len(accounts[accounts['income'] > 50000])
        ]
    })

    return df