# Regularized Linear Regression: US County Health Analysis

[![Codespaces Prebuilds](https://github.com/4GeeksAcademy/gperdrizet-regularized-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-regularized-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds)

A comprehensive machine learning project demonstrating regularized linear regression techniques using real-world US county-level health data. This project applies Ridge and Lasso regression to predict morbidity rates based on sociodemographic and healthcare access features.

## Project Overview

This project analyzes **US county-level sociodemographic and health resource data (2018-2019)** to predict morbidity prevalence at the county level. The dataset provides hands-on experience with:

- Advanced feature engineering and polynomial features
- Data preprocessing and standardization
- Linear regression with L1 (Lasso) and L2 (Ridge) regularization
- Model evaluation and overfitting prevention
- Hyperparameter tuning and cross-validation
- Residual analysis and model diagnostics

The target variable is defined as the **number of people with any reported medical condition per 100 people in the county**.

## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - 4Geeks students: set 4GeeksAcademy as the owner - 4Geeks pays for your codespace usage. All others, set yourself as the owner
   - Give the fork a descriptive name. 4Geeks students: I recommend including your GitHub username to help in finding the fork if you lose the link
   - Click "Create fork"
   - 4Geeks students: bookmark or otherwise save the link to your fork

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main"
   - If the "Create codespace on main" option is grayed out - go to your codespaces list from the three-bar menu at the upper left and delete an old codespace
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/mvp.ipynb` in the Jupyter interface
   - Follow the step-by-step instructions in the notebook

### Option 2: Local Development

1. **Prerequisites**
   - Git
   - Python >= 3.10

2. **Fork the repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - Optional: give the fork a new name and/or description
   - Click "Create fork"

3. **Clone the repository**
   - From your fork of the repository, click the green "Code" button at the upper right
   - From the "Local" tab, select HTTPS and copy the link
   - Run the following commands on your machine, replacing `<LINK>` and `<REPO_NAME>`

   ```bash
   git clone <LINK>
   cd <REPO_NAME>
   ```

4. **Set Up Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Launch Jupyter & start the notebook**
   ```bash
   jupyter notebook notebooks/mvp.ipynb
   ```

## Project Structure

```
├── .devcontainer/           # Development container configuration
├── data/                    # Data directory
├── models/                  # Trained model storage
├── notebooks/               # Jupyter notebook directory
│   ├── helper_functions.py  # Utility functions for analysis
│   ├── mvp.ipynb            # Assignment notebook
│   └── solution.ipynb       # Solution notebook
│
├── .gitignore               # Files/directories not tracked by git
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Dataset

The dataset contains US county-level data with comprehensive sociodemographic and health resource information including:

### Features Categories:
- **Age Demographics**: Population percentages across age groups (0-9, 10-19, ..., 80+)
- **Ethnicity**: Racial and ethnic composition percentages
- **Population Metrics**: Total population, population estimates, birth/death rates
- **Education**: Educational attainment levels (high school, college, bachelor's degree)
- **Employment**: Labor force statistics, unemployment rates, median household income
- **Healthcare Access**: Physician availability, hospital counts, specialist ratios per 100k population
- **Geographic**: County and state identifiers

### Target Variable:
- **Morbidity Rate**: Number of people with any reported medical condition per 100 people in the county

**Note**: This dataset was obtained from official US health and census sources for educational purposes.

## Learning Objectives

1. **Feature Engineering**: Manual feature selection and polynomial interaction terms
2. **Data Preprocessing**: Standardization and encoding of categorical variables
3. **Regularization Techniques**: 
   - L1 Regularization (Lasso) for feature selection
   - L2 Regularization (Ridge) for coefficient shrinkage
4. **Model Evaluation**: R-squared, RMSE, and residual analysis
5. **Hyperparameter Tuning**: Grid search for optimal penalty parameters
6. **Overfitting Detection**: Comparing training vs testing performance
7. **Model Interpretation**: Understanding regularization effects on model complexity

## Key Machine Learning Concepts

### Regularization Methods
- **Linear Regression**: Baseline model without regularization
- **Ridge Regression (L2)**: Shrinks coefficients to prevent overfitting
- **Lasso Regression (L1)**: Performs feature selection by zeroing coefficients

### Model Evaluation Metrics
- **R-squared**: Coefficient of determination
- **RMSE**: Root Mean Squared Error
- **Residual Analysis**: Model diagnostic plots

### Feature Engineering
- **Polynomial Features**: Second-degree interaction terms
- **Standard Scaling**: Feature normalization for regularization convergence

## Technologies Used

- **Python 3.11**: Core programming language
- **Pandas 2.3.1**: Data manipulation and analysis
- **NumPy 2.3.2**: Numerical computing
- **Scikit-learn 1.7.1**: Machine learning algorithms and preprocessing
- **Matplotlib 3.10.3**: Data visualization
- **Seaborn 0.13.2**: Statistical data visualization
- **Jupyter 1.1.1**: Interactive development environment

## Key Results

The project demonstrates:
- How polynomial features can lead to overfitting in high-dimensional datasets
- The effectiveness of regularization in reducing model complexity
- Trade-offs between model performance and interpretability
- Optimal hyperparameter selection through systematic evaluation

## Contributing

This is an educational project. Contributions for improving the analysis or adding new insights are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
