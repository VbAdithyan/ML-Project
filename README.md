# ❤️ Cardiovascular Disease Prediction Using Machine Learning

This project aims to predict the likelihood of heart disease (cardiovascular disease) using various patient health indicators and supervised machine learning algorithms. It includes data preprocessing, exploratory data analysis, visualization, model comparison, and accuracy evaluation.

---

## 📌 Problem Statement

Cardiovascular diseases are one of the leading causes of death worldwide. Early detection can save lives and reduce the burden on healthcare systems. This project uses machine learning to predict whether a patient is likely to have heart disease based on clinical attributes.

---

## 📊 Dataset

- **Name**: Cardio Train Dataset
- **Source**: [Kaggle/UCI/Custom Dataset]
- **Records**: 70,000+
- **Features**:
  - Age (in days → converted to years)
  - Gender
  - Height, Weight
  - Blood pressure (systolic and diastolic)
  - Cholesterol, Glucose levels
  - Lifestyle indicators: Smoking, Alcohol intake, Physical activity
  - Target variable: `cardio` (1 = disease, 0 = healthy)

---

## ⚙️ Technologies Used

- Python 3.8+
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn

---

## 📈 Exploratory Data Analysis

- Age distribution
- Heart disease vs gender
- Cholesterol vs heart disease
- Blood pressure distribution
- Correlation matrix of all features

---

## 🧠 Machine Learning Models Tested

| Model                | Description                        |
|---------------------|------------------------------------|
| Logistic Regression | Baseline binary classification     |
| Decision Tree       | Rule-based classification          |
| Random Forest       | Ensemble of decision trees         |
| K-Nearest Neighbors | Distance-based classification      |
| SVM (Support Vector Machine) | Maximal margin classification |

---

## 🧪 Evaluation Metrics

- Accuracy
- Confusion Matrix
- Precision, Recall, F1-score
- Cross-validation (if applied)

---

## 🏆 Best Model

> **Random Forest Classifier** showed the highest accuracy and robustness in prediction.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/VbAdithyan/ML-Project.git
   cd ML-Project

ML-Project/
├── cardio_train.csv
├── heart_disease_visualization.py
├── model_training.py
├── README.md
└── requirements.txt
