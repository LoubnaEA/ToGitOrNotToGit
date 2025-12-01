from pytest_bdd import scenarios, given, then
import pandas as pd

scenarios("../features/creators_scenarios.md")

@given("the creators dataset is loaded")
def creators_df():
    return pd.read_csv("data/creators.csv")

@then("each row must contain a valid value in the Author column")
def test_non_empty_authors(creators_df):
    assert creators_df["Author"].notna().all()

@then("Birth must be between 1400-1700")
def test_birth_years(creators_df):
    assert creators_df["Birth"].between(1400, 1700).all()

@then("Death must be between 1450-1750")
def test_death_years(creators_df):
    assert creators_df["Death"].between(1450, 1750).all()

@then("Period must be one of Elizabethan, Jacobean, Caroline")
def test_period(creators_df):
    valid_periods = ["Elizabethan","Jacobean","Caroline"]
    assert creators_df["Period"].dropna().apply(lambda x: all(p.strip() in valid_periods for p in x.split(","))).all()
