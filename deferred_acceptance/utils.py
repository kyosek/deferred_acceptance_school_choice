from random import randint
from typing import Tuple

import numpy as np
import pandas as pd


def strict_preference_check(
    students_list: list,
    students_preferences: dict,
) -> None:
    """
    Check the strict order of student's preference over schools
    If a student's preference is not strict, it will raise an error

    Args:
        students_list: list of students
        students_preferences: students' preference dictionary
    """
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

    Args:
        students_list: list of students
        students_preferences: students' preference dictionary
        schools_list: list of schools
        schools_preferences: schools' preference dictionary
    Return:
        tuple contains students_df and schools_df
    """
    strict_preference_check(students_list, students_preferences)

    students_df = pd.DataFrame(students_preferences)
    students_df.index = schools_list
    students_df = students_df.transpose()
    schools_df = pd.DataFrame(schools_preferences)
    schools_df.index = students_list

    return students_df, schools_df


def tie_break(schools_df: pd.DataFrame) -> pd.DataFrame:
    """
    This function randomly breaks the indifferent schools' preference over students
    and make their preference strict.

    Iterations:
    0. Iterate through each school's preference
    1. Create a subset that contains the same ranked students
    2. Randomly order students in the same rank until all the students get the unique rank
    3. Merge all of students with new order and assign new rank to them
    4. Merge all the schools' preferences

    Args:
        schools_df: schools' dataframe
    Return:
        new schools_df with strict preferences over students
    """
    new_schools_df = pd.DataFrame()
    # 0. Iterate through each school's preference
    for school in schools_df.columns:
        new_rank = pd.Series(dtype="int32")

        # 1. Create a subset that contains the same ranked students
        for rank in sorted(schools_df[school].unique()):
            allocated_ranks = []
            sub_df = schools_df.loc[schools_df[school] == rank, school]

            # 2. Randomly order students in the same rank until all the students get the unique rank
            for student in sub_df.index:
                lottery = randint(1, len(sub_df))
                while lottery in allocated_ranks:
                    lottery = randint(1, len(sub_df))
                sub_df.loc[[student]] = lottery
                allocated_ranks.append(lottery)

            # 3. Merge all of students with new order and assign new rank to them
            new_rank = pd.concat([new_rank, sub_df.sort_values()])

        # 4. Merge all the schools' preferences
        new_rank_df = pd.DataFrame(new_rank, columns=[school])
        new_rank_df[school] = np.arange(len(new_rank))
        new_schools_df[school] = new_rank_df[school]

    return new_schools_df
