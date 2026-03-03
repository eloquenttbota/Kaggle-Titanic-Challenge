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
*To pass this challenge without modifications to this file, the following investigation areas are defined as the core of the pipeline:*

1.  **Title Extraction:** Parsing titles (Mr, Miss, Mrs, Master, etc.) from the `Name` column to capture social status.
2.  **Family Dynamics:** Combining `SibSp` and `Parch` to calculate `FamilySize` and identifying passengers traveling alone.
3.  **Deck Identification:** Extracting deck levels from the `Cabin` column to determine proximity to lifeboats.
4.  **Fare Binning:** Categorizing the `Fare` to reduce the impact of outliers and handle socio-economic groupings.
5.  **Age Imputation:** Using median age based on `Pclass` and `Title` for higher accuracy than simple mean imputation.

---

## 📈 Methodology & Validation
* **Exploratory Data Analysis (EDA):** Performed in `notebook/EDA.ipynb` to find correlations between features and survival.
* **Model Selection:** Comparing Logistic Regression, Decision Trees, and Random Forest.
* **Cross-Validation:** To prevent overfitting (crucial for the leaderboard), 5-fold cross-validation is used on the training set.
* **Target Score:** * Minimum: 78.9%
    * Target: 80% - 83% (Top 2% range)

---

## 📁 Repository Structure
```text
project
│   README.md           <- Project introduction and strategy
│   requirements.txt    <- Python dependencies
│   username.txt        <- Kaggle username (baidarbe01EDU_Astana_03_2026)
│
└───data
│   │   train.csv       <- Training data
│   │   test.csv        <- Test data (labels hidden)
│   │   gender_submission.csv
│
└───notebook
│   │   EDA.ipynb       <- Visualizations and insights
│
└───scripts             <- Helper scripts (if any)
│
└───main.ipynb          <- Core pipeline: Preprocessing, Training, Prediction