# Kaggle Titanic - Machine Learning from Disaster 🚢

## 👤 Participant Information
* **Kaggle Username:** baidarbe01EDU_Astana_03_2026
* **Project Goal:** Predict passenger survival with at least 78.9% accuracy.
* **Platform:** [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)

---

## 📋 Project Overview
This project is part of the Astana Hub / 01 Education module. The objective is to build a predictive model to determine which sorts of people were more likely to survive the RMS Titanic shipwreck using passenger data (age, gender, socio-economic class, etc.).

---

## 🛠️ Feature Engineering Strategy
*To pass this challenge, the following investigation areas are defined as the core of the pipeline:*

1.  **Title Extraction:** Parsing titles (Mr, Miss, Mrs, Master, etc.) from the `Name` column to capture social status.
2.  **Family Dynamics:** Combining `SibSp` and `Parch` to calculate `FamilySize` and identifying passengers traveling alone.
3.  **Deck Identification:** Extracting deck levels from the `Cabin` column to determine proximity to lifeboats.
4.  **Fare Binning:** Categorizing the `Fare` to reduce the impact of outliers and handle socio-economic groupings.
5.  **Age Imputation:** Using median age based on `Title` for higher accuracy than simple mean imputation.

---

## 📈 Methodology & Validation
* **Exploratory Data Analysis (EDA):** Performed in `notebook/EDA.ipynb` to find correlations between features and survival.
* **Model Selection:** Using **Random Forest Classifier** as the primary estimator.
* **Cross-Validation:** To prevent overfitting, 5-fold cross-validation is used on the training set.
* **Performance:** Surpassed the required 78.9% threshold.

---

## 📁 Repository Structure
```text
project
│   README.md           <- Project introduction and strategy
│   requirements.txt    <- Python dependencies
│   username.txt        <- Kaggle username
│   .gitignore          <- Excluded environment and temporary files
│
└───data
│   │   train.csv       <- Training data
│   │   test.csv        <- Test data
│
└───notebook
│   │   EDA.ipynb       <- Visualizations and insights
│
└───scripts             
│   │   preprocessing.py <- Modular Python scripts for data processing
│
└───main.ipynb          <- Core pipeline: Preprocessing, Training, Prediction


```
ℹ️ Additional Project Information
Note: This section contains supplemental details and does not override the mandatory project structure.

🛡️ Version Control & Cleanup
.gitignore: Added to ensure that environment files (tomorrow/, venv/), temporary Python cache (__pycache__/), and Jupyter checkpoints do not clutter the version history.

Modular Code: Core logic moved to scripts/preprocessing.py to maintain a clean and professional notebook structure.

🏆 Final Competition Results
Model: RandomForestClassifier (optimized depth).

Advanced Feature Engineering: Implemented a complex Group Survival logic based on family names and ticket IDs. This feature significantly boosted the model's ability to identify survivors within families and groups.

Kaggle Score: 0.80143

Ranking: Successfully surpassed the project's target threshold of 78.9%.