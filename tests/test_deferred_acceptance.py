import pandas as pd
from deferred_acceptance.deferred_acceptance import deferred_acceptance
from pandas._testing import assert_dict_equal


def test_deferred_acceptance():
    students_df = pd.DataFrame(
        {
            "A": [1, 2, 3, 2],
            "B": [2, 3, 2, 1],
            "C": [3, 1, 1, 3]
        },
        index=["a", "b", "c", "d"]
    )

    schools_df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4],
            "B": [1, 3, 2, 4],
            "C": [2, 3, 4, 1]
        },
        index=["a", "b", "c", "d"]
    )

    schools_quota = {'A': 1, 'B': 2, 'C': 1}

    matches = deferred_acceptance(
        students_df=students_df,
        schools_df=schools_df,
        schools_quota=schools_quota
    )
    print(matches)

    assert_dict_equal(
        matches,
        {('a', 'A'): (1, 1), ('b', 'C'): (1, 3), ('d', 'B'): (1, 4), ('c', 'B'): (2, 2)}
    )
