from typing import Tuple

import pandas as pd


def strict_preference_check(
    students_list: list,
    students_preferences: dict,
) -> None:
    # Check the strict order of student's preference over schools
    hash_table = []

    for student in students_list:
        for preference in students_preferences[student]:
            if preference not in hash_table:
                hash_table.append(preference)
            else:
                raise ValueError("The student's preference must be strictly ordered")

        hash_table = []


def create_dataframes(
    students_list: list,
    students_preferences: dict,
    schools_list: list,
    schools_preferences: dict,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Create students and schools dataframes

    :param students_list: list of students
    :param students_preferences: students' preference dictionary
    :param schools_list: list of schools
    :param schools_preferences: schools' preference dictionary
    :return:
    """
    strict_preference_check(students_list, students_preferences)

    students_df = pd.DataFrame(students_preferences)
    students_df.index = schools_list
    students_df = students_df.transpose()
    schools_df = pd.DataFrame(schools_preferences)
    schools_df.index = students_list

    return students_df, schools_df
