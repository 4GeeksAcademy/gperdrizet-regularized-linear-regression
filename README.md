# Regularized Linear Regression: US County-Level Sociodemographic and Health Resource Data (2018-2019)

[![Codespace Prebuild](https://github.com/4GeeksAcademy/gperdrizet-regularized-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-regularized-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds)

This repository contains a data science bootcamp assignment focused on regularized linear regression using real-world US county-level data. Students will learn to:

- Apply regularization techniques (Lasso and Ridge regression) to linear models
- Perform manual feature selection and engineering
- Create polynomial interaction features to intentionally induce overfitting
- Handle mixed data types (categorical and numerical features)
- Evaluate model performance and prevent overfitting using regularization
- Compare baseline, linear, and regularized model performance

## Dataset

The assignment uses US county-level sociodemographic and health resource data from 2018-2019. The target variable is `morbidity` - the calculated rate of any health condition per 100 people in each county (derived from `anycondition_number` and `TOT_POP`). Features include demographic information (age, ethnicity), economic indicators (employment, income, education), and healthcare resource availability.

## Repository Structure

- `notebooks/mvp.ipynb`: The main assignment notebook for students to complete.
- `notebooks/solution.ipynb`: The instructor's full solution for reference.
- `data/`: Contains raw, interim, and processed data folders (ignored by git).
- `models/`: Directory for saving trained models (ignored by git).
- `requirements.txt`: List of required Python packages.

## Getting Started

To complete this assignment, you can choose between two options: using GitHub Codespaces (recommended) or setting up a local development environment. Both methods will allow you to run the Jupyter notebook and complete the assignment.

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the [GitHub repository page](https://github.com/4GeeksAcademy/gperdrizet-regularized-linear-regression)
   - This creates your own copy under your GitHub account

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main" 
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/mvp.ipynb` in the Jupyter interface
   - Follow the step-by-step instructions in the notebook

### Option 2: Local Development

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/gperdrizet-regularized-linear-regression.git
   cd gperdrizet-regularized-linear-regression
   ```

2. **Set Up Environment**
   ```bash
   # Create virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Launch Jupyter**
   ```bash
   jupyter notebook notebooks/mvp.ipynb
   ```

## Assignment Overview

The `mvp.ipynb` notebook guides you through:

1. **Data Loading & Inspection** - Load and explore the county-level dataset
2. **Initial Feature Selection** - Manually select relevant features from different categories (age, ethnicity, population, education, employment, healthcare)
3. **Exploratory Data Analysis (EDA)** - Analyze target variable and feature distributions, examine feature-label correlations
4. **Data Preparation** - Train-test split, categorical encoding, and polynomial feature generation
5. **Linear Model Training** - Build baseline and linear regression models
6. **Model Regularization** - Apply both Lasso and Ridge regression with different penalty values
7. **Hyperparameter Optimization** - Find optimal regularization strength using penalty sweeps
8. **Final Evaluation** - Compare all models and analyze results with residual plots

### Key Concepts Covered

- **Overfitting vs. Underfitting**: Understanding the bias-variance tradeoff through polynomial features
- **Regularization**: Both L1 penalty (Lasso) and L2 penalty (Ridge) for overfitting prevention
- **Feature Engineering**: Manual feature selection, polynomial interaction features, and categorical encoding
- **Model Evaluation**: RMSE, R-squared metrics, and residual analysis

## Working on the Assignment

- Complete the sections marked with code comments like `# Investigate the distribution...`, `# Take a look at the descriptive statistics...`, etc.
- Run cells sequentially to maintain proper data flow
- Experiment with different regularization penalties
- Analyze the overfitting behavior in the linear model and how regularization addresses it
- Document your observations about the penalty optimization plots

## Additional Resources

- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [Understanding Regularization](https://scikit-learn.org/stable/modules/linear_model.html#regularization)
- [Polynomial Features Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
- [Lasso Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
- [Ridge Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
