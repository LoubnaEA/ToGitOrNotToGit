# 🎭 Feature : Creators Dataset Validation

Ensures integrity, consistency, semantic richness of `creators.csv`

### Scenario : Every author entry should have a non-empty name
Given the creators dataset is loaded  
Then each row must contain a valid value in the `Author` column

### Scenario : Valid birth and death years
Given the creators dataset is loaded  
Then Birth must be between 1400-1700  
And Death must be between 1450-1750

### Scenario : Period values
Given the creators dataset is loaded  
Then Period must be one of Elizabethan, Jacobean, Caroline
