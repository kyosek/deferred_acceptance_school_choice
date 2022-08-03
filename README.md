# Deferred Acceptance algorithm for school choice
Python implementation of Deferred Acceptance algorithm (Gale and Shapley, 1962) for school choice.

The medium blog about this repo can be found [here](https://medium).
## Introduction
The study of matching investigates matching between people, institutes, and goods. Starting with Gale and Shapley (1962)'s deferred acceptance (DA) algorithm, this has been successfully utilised in the real world, especially in the world of the school choice since early 2000s. This repo is a python implementation of the algorithm.

This repo covers (so far):
- DA algorithm for school choice (student optimal)
- DA algorithm with random tie-break lotteries
- Examples of above algorithms usage

## Usage
### [Simple DA algorithm](/examples/simple_school_choice.py)
After input student and school's preference and schools' quota,
```python
from deferred_acceptance.deferred_acceptance import deferred_acceptance
from deferred_acceptance.utils import create_dataframes


students_df, schools_df = create_dataframes(
        students_list=students_list,
        students_preferences=students_preferences,
        schools_list=schools_list,
        schools_preferences=schools_preferences,
    )
matches = deferred_acceptance(
        students_df=students_df, schools_df=schools_df, schools_quota=schools_quota
    )
```

### [DA algorithm with random tie-break lotteries](/examples/tie_break_school_choice.py)
```python
from deferred_acceptance.deferred_acceptance import deferred_acceptance
from deferred_acceptance.utils import create_dataframes, tie_break


students_df, schools_df = create_dataframes(
        students_list=students_list,
        students_preferences=students_preferences,
        schools_list=schools_list,
        schools_preferences=schools_preferences,
    )

strict_school_df = tie_break(schools_df)
matches = deferred_acceptance(
    students_df=students_df,
    schools_df=strict_school_df,
    schools_quota=schools_quota,
)
```