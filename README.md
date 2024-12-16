# Intrusion Detection: Few-Shot Learning vs. Traditional Techniques

This repository presents a comparative analysis of intrusion detection methodologies, focusing on few-shot learning approaches versus the classic naive-bayes model. The study utilizes a subset of the CIC-IDS-2017 dataset to evaluate and contrast the performance of these methods.

## Repository Structure

- **Data_Cleaning.ipynb**: A Jupyter Notebook detailing the data preprocessing steps applied to the CIC-IDS-2017 subset.
- **create_binary_label.py**: A Python script that generates binary labels for the dataset, distinguishing between normal and intrusive network traffic.
- **traditional_method.ipynb**: A Jupyter Notebook implementing a traditional intrusion detection technique, such as Hidden Naive Bayes, and evaluating its performance on the preprocessed dataset.
- **few-shot-learning/**: Directory containing implementations related to few-shot learning approaches for intrusion detection.
- **CIC-IDS-2017_Subset.xlsx**: Excel file containing the subset of the CIC-IDS-2017 dataset used in this analysis.
- **cleaned_dataset.csv**: CSV file of the dataset after preprocessing steps.
- **Modified_dataset.csv**: CSV file of the dataset after applying modifications, such as feature engineering or label creation.

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

Open and execute the cells in `few-shot-learning/FSL-model-IDS.ipynb` and `traditional_method.ipynb` to reproduce the results.

## Data Preprocessing

The `Data_Cleaning.ipynb` notebook outlines the following steps:

- **Loading Data**: Importing the dataset from `CIC-IDS-2017_Subset.xlsx`.
- **Data Cleaning**: Handling missing values, duplicates, and irrelevant features.
- **Feature Engineering**: Creating new features or transforming existing ones to enhance model performance.
- **Label Encoding**: Converting categorical labels into binary labels using `create_binary_label.py`.

## Traditional Intrusion Detection Method

The `traditional_method.ipynb` notebook demonstrates:

- **Model Selection**: Implementing a traditional machine learning model, such as Hidden Naive Bayes.
- **Training**: Fitting the model on the preprocessed dataset.
- **Evaluation**: Assessing model performance using metrics like accuracy, precision, recall, and F1-score.

## Few-Shot Learning Approach

The `few-shot-learning/` directory includes:

- **Model Implementation**: Scripts and notebooks related to few-shot learning models tailored for intrusion detection.
- **Training and Evaluation**: Procedures to train and assess the few-shot learning models on the dataset.

## Results and Discussion

The repository provides insights into the effectiveness of few-shot learning compared to traditional methods in intrusion detection tasks. Detailed results, including performance metrics and analysis, are documented within the notebooks.

## Contributors

- **Anuttara Rajasinghe**
- **Jathusharini Basker**
- **Amandi Wijesuriya**
- **Tharani Dissanayake**

