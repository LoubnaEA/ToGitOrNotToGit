# 🎭 Feature : Creators Dataset Validation

# Ensures integrity, consistency, semantic richness of `creators_raw_dataset.csv`
# Reference Notebooks (no outputs):
#   - notebooks/eda_creators.ipynb

Feature: Validate Creators Dataset
  As a QA/Data engineer
  I want the creators dataset to follow defined integrity and semantic rules
  So that downstream modules (Fate Engine, analytics, visualizations) can rely on consistent, clean data

# Tags :
#   @creators_dataset
#   @eda-informed

### Basic Integrity Scenarios
Scenario: Every author entry should have a non-empty name
    Given the creators dataset is loaded  
    Then each row must contain a valid value in the `Author` column

Scenario: Valid birth and death years
    Given the creators dataset is loaded  
    Then Birth must be between 1400-1700  
    And Death must be between 1450-1750

Scenario: Period values
    Given the creators dataset is loaded  
    Then Period must be one of Elizabethan, Jacobean, Caroline

Scenario: Author name uniqueness
    Given the creators dataset is loaded  
    Then each Author value must be unique

# Notes :
# Scenarios are informed by EDA to define realistic validation thresholds
# Future expansions can include completeness checks, cross-field consistency, derived features
# Tags like @eda-informed indicate grounding in prior analysis

