# Engineering Log

## Date: 17 June 2026

### Project: Customer Segmentation System

### Session: 1 - Project Setup & Data Loading

#### Objective

Initialize project structure and verify dataset loading.

#### Work Done

- Created project folder structure.
- Added requirements.txt and .gitignore.
- Added Mall Customers dataset.
- Implemented data_loader.py.
- Created main.py.
- Loaded dataset successfully and displayed basic information.

#### Observations

- Dataset contains 200 customer records.
- Columns include CustomerID, Gender, Age, Annual Income, and Spending Score.
- Data loaded without issues.

#### Challenges

- None.

#### Next Step

Implement preprocessing layer and prepare features for clustering.

### Session 2: Preprocessing

#### objective

Prepare the customer dataset for clustering by validating data quality and removing non-informative features.

#### Work Done

- Created preprocessor.py.
- Checked dataset shape.
- Verified column structure.
- Checked for missing values across all columns.
- Checked for duplicate records.
- Removed CustomerID column from the dataset.
- Returned cleaned DataFrame to main.py.
- Verified successful pipeline execution.
- Displayed processed dataset preview.

#### Observations

- Dataset contains 200 customer records and 5 columns.
- No missing values were found.
- No duplicate rows were found.
- CustomerID is an identifier and does not contain behavioral information useful for clustering.
- After removing CustomerID, the dataset contains only customer attributes relevant to segmentation.

#### Changes Made

- Implemented preprocess_data() function.
- Added missing value validation.
- Added duplicate row validation.
- Added CustomerID removal step.
- Updated main.py to include preprocessing stage.

#### Challenges

- Initially loaded the Sales Forecasting dataset by mistake.
- Encountered a CustomerID column error because the wrong dataset schema was being used.
- Verified dataset columns and corrected the dataset source.
- Re-ran the pipeline successfully using the Mall Customers dataset.

#### Key Learning

- Data preprocessing is the bridge between raw data and machine learning.
- Identifiers should generally be removed before training ML models.
- Validating dataset schema is an important debugging step.
- Many apparent code errors are actually data input issues.

#### Next Step

- Create feature_engineering.py.
- Encode Gender column into numerical values.
- Apply feature scaling using StandardScaler.
- Generate a clustering-ready feature matrix for K-Means.

### Session 3 – Feature Engineering and Feature Scaling

#### Objective

Transform customer data into a numerical and standardized feature set suitable for K-Means clustering.

#### Work Done

- Created feature_engineering.py.
- Encoded Gender values:  
    Male → 0
    Female → 1
- Selected clustering features after preprocessing.
- Created scaler.py.
- Implemented feature scaling using StandardScaler.
- Updated main.py to integrate feature engineering and scaling stages.
- Generated scaled feature matrix.
- Verified successful pipeline execution.

#### Observations

- After preprocessing, the dataset contained:  
    Gender  
    Age  
    Annual Income (k$)  
    Spending Score (1-100)  

- CustomerID was successfully removed before feature engineering.
- Feature matrix shape after scaling:
    (200, 4)

- All features were converted into a numerical format suitable for machine learning algorithms.

#### Changes Made

- Implemented prepare_features() function.
- Added Gender encoding logic.
- Implemented scale_feature() function using StandardScaler.
- Connected preprocessing, feature engineering, and scaling stages in the pipeline.

#### Challenges

- Initially passed cleaned_df directly into StandardScaler.
- Encountered error:

    ValueError: could not convert string to     float: 'Male'

- Investigated the issue and identified that the Gender column was still categorical.
- Corrected the pipeline flow by passing feature_df (encoded data) into the scaler instead of cleaned_df.
- Re-ran the pipeline successfully.

#### Key Learning

- StandardScaler can only process numerical values.
- Categorical features must be encoded before scaling.
- The order of stages in an ML pipeline is important:

```

    Raw Data
        ↓
    Preprocessing
        ↓
    Feature Engineering
        ↓
    Scaling
        ↓
    Machine Learning Model

```

- Distance-based algorithms such as K-Means depend heavily on properly scaled features.

Next Step:

- Create clustering.py.
- Implement K-Means clustering.
- Determine optimal number of clusters.
- Generate cluster labels.
- Analyze customer segments and cluster characteristics.


### Session 4 – K-Means Clustering

#### Objective:
Implement K-Means clustering and assign customers to behavioral segments.

#### Work Done:
- Created clustering.py.
- Imported KMeans from scikit-learn.
- Configured model with:  
    n_clusters=5  
    random_state=42  
    n_init=10  
- Applied fit_predict() on scaled customer features.
- Generated cluster labels for all customers.
- Added Cluster column to the dataset.
- Displayed sample cluster assignments.

#### Observations:
- K-Means successfully assigned every customer to a cluster.
- Dataset shape used for clustering:  
    (200, 4)
- Cluster labels were generated without errors.
- Customers with similar characteristics were grouped together.

#### Changes Made:

- Implemented create_clusters() function.
- Added clustering stage to the pipeline.
- Added Cluster column to feature dataset.

#### Challenges:

- None.
- Previous feature engineering and scaling stages worked correctly, allowing clustering to run successfully.

#### Key Learning:

- K-Means is an unsupervised learning algorithm.
- Cluster labels are created by the algorithm and are not provided by the dataset.
- Clustering groups customers based on feature similarity.
- Scaled features are essential because K-Means relies on distance calculations.

#### Next Step:

- Create analyzer.py.
- Analyze cluster statistics.
- Calculate average age, income, and spending score for each cluster.
- Interpret customer segments.
