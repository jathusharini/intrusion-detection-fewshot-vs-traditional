# Intrusion Detection: Few-Shot Learning vs. Traditional Techniques

This repository presents a comparative analysis of intrusion detection methodologies, focusing on few-shot learning approaches versus the classic naive-bayes model. The study utilizes a subset of the CIC-IDS-2017 dataset to evaluate and contrast the performance of these methods.

---

## Repository Structure

- **CIC-IDS-2017_Subset.xlsx**: Subset of the CIC-IDS-2017 dataset used for this analysis.
- **Data_Cleaning.ipynb**: Jupyter Notebook for preprocessing the dataset (handling missing values, duplicates, and feature engineering).
- **create_binary_label.py**: Script to add binary labels to the dataset (normal vs. intrusive traffic).
- **cleaned_dataset.csv**: Preprocessed version of the dataset.
- **Modified_dataset.csv**: Dataset after feature modifications.
- **README.md**: Current documentation for the project.

### Model Implementations
- **Hidden_Naive_Bayes/**:
  - **Hidden_Naive_Bayes_Classifier.ipynb**: Implements the Hidden Naive Bayes model with cross-validation.
- **few-shot-learning/**:
  - **FSL-model-IDS.ipynb**: Few-shot learning model for intrusion detection.
  - **visualizations_test5_oversampling_issue.pth**: Finalized few-shot learning model.

---

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jathusharini/intrusion-detection-fewshot-vs-traditional.git
   cd intrusion-detection-fewshot-vs-traditional
   ```

2. **Set Up the Environment**:

Ensure you have Python installed. It's recommended to use a virtual environment.

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. ### Run Jupyter Notebooks:

Launch Jupyter Notebook to explore the data cleaning and model implementation steps.

```bash
jupyter notebook
```
Open the following notebooks to reproduce the results:

- `Data_Cleaning.ipynb`
- `Hidden_Naive_Bayes/Hidden_Naive_Bayes_Classifier.ipynb`
- `few-shot-learning/FSL-model-IDS.ipynb`

---

## Data Preprocessing

The `Data_Cleaning.ipynb` notebook outlines the following steps:

- **Loading Data**: Importing the dataset from `CIC-IDS-2017_Subset.xlsx`.
- **Data Cleaning**: Handling missing values, duplicates, and irrelevant features.
- **Feature Engineering**: Creating new features or transforming existing ones to enhance model performance.
- **Label Encoding**: Converting categorical labels into binary labels using `create_binary_label.py`.

---

## Traditional Intrusion Detection Method

The **`Hidden_Naive_Bayes/Hidden_Naive_Bayes_Classifier.ipynb`** notebook includes:

- **Model Selection**: Hidden Naive Bayes classifier.
- **Cross-Validation**: Ensures model robustness with validation folds.
- **Evaluation**: Accuracy, Precision, Recall, and F1-Score.

---

## Few-Shot Learning Approach

The **`few-shot-learning/`** folder includes:

- **FSL-model-IDS.ipynb**: Few-shot learning implementation to handle limited labeled data.
- **visualizations_test5_oversampling_issue.pth**: Finalized model file.

---

## Results and Discussion

The project provides a detailed comparison of:

- Hidden Naive Bayes (traditional approach)  
- Few-shot learning (modern approach)  

Performance metrics such as accuracy, precision, and recall are evaluated and compared. Results, discussions, and visualizations can be found in their respective notebooks.

---

## Contributors

- **Anuttara Rajasinghe**
- **Jathusharini Basker**
- **Amandi Wijesuriya**
- **Tharani Dissanayake**

