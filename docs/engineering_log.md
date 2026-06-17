# Engineering Log

## Date: 17 June 2026

### Project: Customer Segmentation System

### Session: 1 - Project Setup & Data Loading

#### Objective:

Initialize project structure and verify dataset loading.

#### Work Done

- Created project folder structure.
- Added requirements.txt and .gitignore.
- Added Mall Customers dataset.
- Implemented data_loader.py.
- Created main.py.
- Loaded dataset successfully and displayed basic information.

#### Observations:

- Dataset contains 200 customer records.
- Columns include CustomerID, Gender, Age, Annual Income, and Spending Score.
- Data loaded without issues.

#### Challenges:

- None.

#### Next Step:

Implement preprocessing layer and prepare features for clustering.


### Session 2: Preprocessing

#### objective:
Prepare the customer dataset for clustering by validating data quality and removing non-informative features.

#### Work Done:
- Created preprocessor.py.
- Checked dataset shape.
- Verified column structure.
- Checked for missing values across all columns.
- Checked for duplicate records.
- Removed CustomerID column from the dataset.
- Returned cleaned DataFrame to main.py.
- Verified successful pipeline execution.
- Displayed processed dataset preview.

#### Observations:
- Dataset contains 200 customer records and 5 columns.
- No missing values were found.
- No duplicate rows were found.
- CustomerID is an identifier and does not contain behavioral information useful for clustering.
- After removing CustomerID, the dataset contains only customer attributes relevant to segmentation.

#### Changes Made:
- Implemented preprocess_data() function.
- Added missing value validation.
- Added duplicate row validation.
- Added CustomerID removal step.
- Updated main.py to include preprocessing stage.

#### Challenges:
- Initially loaded the Sales Forecasting dataset by mistake.
- Encountered a CustomerID column error because the wrong dataset schema was being used.
- Verified dataset columns and corrected the dataset source.
- Re-ran the pipeline successfully using the Mall Customers dataset.

#### Key Learning:
- Data preprocessing is the bridge between raw data and machine learning.
- Identifiers should generally be removed before training ML models.
- Validating dataset schema is an important debugging step.
- Many apparent code errors are actually data input issues.

#### Next Step:
- Create feature_engineering.py.
- Encode Gender column into numerical values.
- Apply feature scaling using StandardScaler.
- Generate a clustering-ready feature matrix for K-Means.
