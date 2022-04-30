from random import randrange
from typing import Tuple

import numpy as np
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


def tie_break(schools_df: pd.DataFrame) -> pd.DataFrame:
    """
    This function randomly breaks the indifferent preference over students
    and make the schools' preference strict.

    Iterations:
    0. iterate through each school's preference
    1. create a subset that contains the same ranked students
    2. randomly order students in the same rank
    3. continue till all the students get the unique rank
    4. merge all of students with new order
    5. assign new rank to all the student in order
    6. merge all the schools' preferences

    :param schools_df:
    :return:
    """
    new_schools_df = pd.DataFrame()
    # 0.
    for school in schools_df.columns:
        new_rank = pd.Series(dtype="int32")

        # 1.
        for rank in sorted(schools_df[school].unique()):
            allocated_ranks = []
            sub_df = schools_df.loc[schools_df[school] == rank, school]

            # 2. 3.
            for student in sub_df.index:
                lottery = randrange(len(sub_df))
                while lottery in allocated_ranks:
                    lottery = randrange(len(sub_df))
                sub_df.loc[[student]] = lottery
                allocated_ranks.append(lottery)
            # 4.
            new_rank = pd.concat([new_rank, sub_df.sort_values()])

        # 5.
        new_rank_df = pd.DataFrame(new_rank, columns=[school])
        new_rank_df[school] = np.arange(len(new_rank))
        new_schools_df[school] = new_rank_df[school]

    return new_schools_df
