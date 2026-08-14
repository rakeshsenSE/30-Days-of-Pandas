import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    df = students.merge(subjects, how="cross")

    counts = (
        examinations.groupby(["student_id", "subject_name"])
        .size()
        .reset_index(name="attended_exams")
    )

    df = df.merge(counts, on=["student_id", "subject_name"], how="left")
    df["attended_exams"] = df["attended_exams"].fillna(0)
    return df.sort_values(by=["student_id", "subject_name"])