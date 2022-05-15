from collections import Counter
from copy import copy
from typing import Optional

import pandas as pd


def deferred_acceptance(
    students_df: pd.DataFrame,
    schools_df: pd.DataFrame,
    schools_quota: dict,
    verbose: Optional[int] = 0,
) -> dict:
    """
    The deferred acceptance algorithm implementation.
    The process would be following:
    1. Create the initial environments for matching
    2. Start matching
    3. Count applications in school

    Args:
        students_df: students dataframe
        schools_df: schools dataframe
        schools_quota: students quota in each schools
        verbose: verbose=0 (silent), else shows the number of iterations
    Return:
        dictionary of student - school matches
    """

    # Create the initial environments for matching
    available_school = {
        student: list(students_df.columns.values)
        for student in list(students_df.index.values)
    }
    students_stack = []
    matches = {}
    itr_count = 0

    # Start matching
    while len(students_stack) < len(students_df):
        for student in students_df.index:
            if student not in students_stack:
                school = available_school[student]
                best_choice = students_df.loc[student][
                    students_df.loc[student].index.isin(school)
                ].idxmin()
                matches[(student, best_choice)] = (
                    students_df.loc[student][best_choice],
                    schools_df.loc[student][best_choice],
                )

        # Count applications in school
        schools_applications = Counter([key[1] for key in matches.keys()])

        for school in schools_applications.keys():
            if schools_applications[school] > schools_quota[school]:
                pairs_to_drop = sorted(
                    {
                        pair: matches[pair] for pair in matches.keys() if school in pair
                    }.items(),
                    key=lambda x: x[1][1],
                )[1:]

                for p_to_drop in pairs_to_drop:
                    del matches[p_to_drop[0]]
                    _school = copy(available_school[p_to_drop[0][0]])
                    _school.remove(p_to_drop[0][1])
                    available_school[p_to_drop[0][0]] = _school

        students_stack = [student[0] for student in matches.keys()]
        itr_count += 1

    if verbose != 0:
        print(f"Number of iterations: {itr_count}")

    return matches


def stable_improvement_cycle(
    matches: dict,
    students_df: pd.DataFrame,
    schools_df: pd.DataFrame,
    schools_quota: dict,
) -> dict:
    """
    Stable improvement cycle implementation.

    Process:
    1. Iterate through each students
    2. Check the rank of student and if it's not the highest possible ranked school
    3. If not, refer that school's preference list against the student's and other matched students'
    4. If the student's rank is higher than at least one of the matched students, trade the school
    5. When there's no student who would be better off by trading, this iteration will be terminated

    students_df: students dataframe
    schools_df: schools dataframe
    schools_quota: students quota in each schools
    """
    matched = {}
    new_matches = {}

    # 1.
    for i in range(len(students_df) - 1):
        student = list(matches)[i][0]
        # 2. 3.
        # if matches[list(matches)[i]][0] != 1:
        # # Here, get the student's best school
        #     best_school =

    return {}
