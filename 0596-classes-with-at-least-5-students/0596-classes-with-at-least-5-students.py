import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].nunique().reset_index()
    res = df[df['student'] >= 5][['class']]
    return res