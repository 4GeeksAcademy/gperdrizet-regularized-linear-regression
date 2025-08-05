# Regularized Linear Regression: US County-Level Sociodemographic and Health Resource Data (2018-2019)

This repository contains a data science bootcamp assignment focused on regularized linear regression using real-world US county-level data. Students will learn to:

- Apply regularization techniques (Lasso regression) to linear models
- Perform feature selection using Recursive Feature Elimination (RFE)
- Handle mixed data types (categorical and numerical features)
- Evaluate model performance and prevent overfitting
- Compare baseline, linear, and regularized model performance

## Dataset

The assignment uses US county-level sociodemographic and health resource data from 2018-2019. The target variable is `anycondition_number` - the number of people with any health condition in each county. Features include demographic information, economic indicators, and healthcare resource availability.

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
2. **Exploratory Data Analysis (EDA)** - Analyze target variable and feature distributions
3. **Feature Selection** - Use RFE to identify most relevant features
4. **Linear Model Training** - Build baseline linear regression model
5. **Model Regularization** - Apply Lasso regression with different penalty values
6. **Hyperparameter Optimization** - Find optimal regularization strength
7. **Final Evaluation** - Compare all models and analyze results

### Key Concepts Covered

- **Overfitting vs. Underfitting**: Understanding the bias-variance tradeoff
- **Regularization**: L1 penalty (Lasso) for feature selection and overfitting prevention
- **Cross-validation**: Proper model evaluation techniques
- **Feature Engineering**: Handling categorical variables and feature scaling

## Working on the Assignment

- Complete the sections marked with `# Your code here...`
- Run cells sequentially to maintain proper data flow
- Experiment with different hyperparameters
- Document your observations and findings

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all packages from `requirements.txt` are installed
2. **Kernel Issues**: Restart the kernel if variables seem undefined
3. **Memory Issues**: The dataset is manageable, but restart kernel if needed

### Getting Help

- Review the instructor solution in `notebooks/solution.ipynb` if you're stuck
- Check the scikit-learn documentation for specific functions

## Additional Resources

- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [Understanding Regularization](https://scikit-learn.org/stable/modules/linear_model.html#regularization)
- [Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)
