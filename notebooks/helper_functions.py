'''Helper functions for notebooks.'''

import matplotlib.pyplot as plt

def residual_plot(training_predictions, training_labels, testing_predictions, testing_labels) -> None:
    """
    Plot residuals for training and testing predictions.
    
    Args:
        training_predictions (array-like): Predictions for the training set.
        training_labels (array-like): True labels for the training set.
        testing_predictions (array-like): Predictions for the testing set.
        testing_labels (array-like): True labels for the testing set.
    """
    fig, axs = plt.subplots(2, 2, figsize=(7, 7), sharex='col', sharey='col')
    axs = axs.flatten()

    # Training predicted vs Actual plot
    axs[0].scatter(training_labels, training_predictions, color='black', alpha=0.6, s=30)
    axs[0].plot([min(training_labels), max(training_labels)], [min(training_labels), max(training_labels)], 
                'r--', linewidth=2, label='Perfect prediction')
    axs[0].set_xlabel('Actual morbidity')
    axs[0].set_ylabel('Predicted morbidity')
    axs[0].set_title(f'Training data: predicted vs actual morbidity')
    axs[0].legend()
    axs[0].grid(alpha=0.3)

    # Training residuals plot
    residuals = training_predictions - training_labels
    axs[1].scatter(training_predictions, residuals, color='black', alpha=0.6, s=30)
    axs[1].axhline(y=0, color='black', linestyle='-', linewidth=1)
    axs[1].set_xlabel('Predicted morbidity')
    axs[1].set_ylabel('Predicted - actual morbidity')
    axs[1].set_title(f'Training data: residuals vs predicted')
    axs[1].grid(alpha=0.3)

    # Testing predicted vs Actual plot
    axs[2].scatter(testing_labels, testing_predictions, color='black', alpha=0.6, s=30)
    axs[2].plot([min(testing_labels), max(testing_labels)], [min(testing_labels), max(testing_labels)], 
                'r--', linewidth=2, label='Perfect prediction')
    axs[2].set_xlabel('Actual morbidity')
    axs[2].set_ylabel('Predicted morbidity')
    axs[2].set_title(f'Testing data: predicted vs actual morbidity')
    axs[2].legend()
    axs[2].grid(alpha=0.3)

    # testing residuals plot
    residuals = testing_predictions - testing_labels
    axs[3].scatter(testing_predictions, residuals, color='black', alpha=0.6, s=30)
    axs[3].axhline(y=0, color='black', linestyle='-', linewidth=1)
    axs[3].set_xlabel('Predicted morbidity')
    axs[3].set_ylabel('Predicted - actual morbidity')
    axs[3].set_title(f'Testing data: residuals vs predicted')
    axs[3].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()