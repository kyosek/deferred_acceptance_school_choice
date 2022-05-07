from deferred_acceptance.deferred_acceptance import deferred_acceptance
from deferred_acceptance.utils import create_dataframes, tie_break


def tie_break_school_choice() -> None:
    """
    This example shows how the deferred acceptance algorithm works with the random tie-breaking mechanism.
    """
    # Prepare the dataframes
    students_list = ["a", "b", "c", "d"]
    schools_list = ["A", "B", "C"]
    students_preferences = {
        "a": [1, 2, 3],
        "b": [2, 3, 1],
        "c": [3, 2, 1],
        "d": [2, 1, 3],
    }
    schools_preferences = {"A": [1, 1, 1, 4], "B": [1, 3, 3, 1], "C": [2, 2, 2, 2]}

    students_df, schools_df = create_dataframes(
        students_list=students_list,
        students_preferences=students_preferences,
        schools_list=schools_list,
        schools_preferences=schools_preferences,
    )

    # Break the "tie" and make the schools' preference strict
    strict_school_df = tie_break(schools_df)

    # Run the algorithm
    schools_quota = {"A": 1, "B": 2, "C": 1}
    matches = deferred_acceptance(
        students_df=students_df,
        schools_df=strict_school_df,
        schools_quota=schools_quota,
    )

    print(matches)


if __name__ == "__main__":
    tie_break_school_choice()
