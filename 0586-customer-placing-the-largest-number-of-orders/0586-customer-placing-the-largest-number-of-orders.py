import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
   df =  orders.groupby('customer_number').size().reset_index()
   df = df.sort_values(by = 0 , ascending = False)
   return pd.DataFrame(
    {'customer_number' : df['customer_number'].head(1)}
   )