import pandas as pd
from typing import Tuple


def create_dataframes(
        students_list: list,
        students_preferences: dict,
        schools_list: list,
        schools_preferences: dict
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Create students and schools dataframes

    :param students_list: list of students
    :param students_preferences: students' preference dictionary
    :param schools_list: list of schools
    :param schools_preferences: schools' preference dictionary
    :return:
    """
    students_df = pd.DataFrame(students_preferences)
    students_df.index = schools_list
    students_df = students_df.transpose()
    schools_df = pd.DataFrame(schools_preferences)
    schools_df.index = students_list

    return students_df, schools_df
