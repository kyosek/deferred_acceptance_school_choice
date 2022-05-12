import pandas as pd
from pandas._testing import assert_frame_equal

from deferred_acceptance.utils import (
    create_dataframes,
    strict_preference_check,
    tie_break,
)


def test_strict_preference_check():
    # Won't be able to properly test it as it doesn't return anything
    students_list = ["a", "b", "c", "d"]
    students_preferences = {
        "a": [1, 2, 3],
        "b": [2, 3, 1],
        "c": [3, 2, 1],
        "d": [2, 1, 3],
    }

    strict_preference_check(students_list, students_preferences)


def test_create_dataframes():
    expected_students_df = pd.DataFrame(
        {"A": [1, 2, 3, 2], "B": [2, 3, 2, 1], "C": [3, 1, 1, 3]},
        index=["a", "b", "c", "d"],
    )

    expected_schools_df = pd.DataFrame(
        {"A": [1, 2, 3, 4], "B": [1, 3, 2, 4], "C": [2, 3, 4, 1]},
        index=["a", "b", "c", "d"],
    )

    students_list = ["a", "b", "c", "d"]
    schools_list = ["A", "B", "C"]
    students_preferences = {
        "a": [1, 2, 3],
        "b": [2, 3, 1],
        "c": [3, 2, 1],
        "d": [2, 1, 3],
    }
    schools_preferences = {"A": [1, 2, 3, 4], "B": [1, 3, 2, 4], "C": [2, 3, 4, 1]}

    students_df, schools_df = create_dataframes(
        students_list=students_list,
        students_preferences=students_preferences,
        schools_list=schools_list,
        schools_preferences=schools_preferences,
    )

    assert_frame_equal(students_df, expected_students_df)

    assert_frame_equal(schools_df, expected_schools_df)


def test_tie_break():
    schools_df = pd.DataFrame(
        {
            "A": [1, 1, 2, 2],
            "B": [2, 1, 1, 2],
            "C": [1, 3, 3, 3],
        },
        index=["a", "b", "c", "d"],
    )

    new_schools_df = tie_break(schools_df)

    assert new_schools_df["A"].nunique() == 4
    assert new_schools_df["B"].nunique() == 4
    assert new_schools_df["C"].nunique() == 4
