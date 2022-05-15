from school_choice.school_choice import deferred_acceptance
from school_choice.utils import create_dataframes


def simple_school_choice() -> None:
    """
    Here is a minimalistic example of deferred acceptance algorithm for school choice.
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
    schools_preferences = {"A": [1, 2, 3, 4], "B": [1, 3, 2, 4], "C": [2, 3, 4, 1]}

    students_df, schools_df = create_dataframes(
        students_list=students_list,
        students_preferences=students_preferences,
        schools_list=schools_list,
        schools_preferences=schools_preferences,
    )

    # Run the algorithm
    schools_quota = {"A": 1, "B": 2, "C": 1}
    matches = deferred_acceptance(
        students_df=students_df, schools_df=schools_df, schools_quota=schools_quota
    )

    print(matches)


if __name__ == "__main__":
    simple_school_choice()
