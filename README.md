
# 📊 ML-Prep-Box
**Simplify data cleaning with automated strategies mapped to your data types.**

---

### 📝 Project Overview
An automated, **metadata-driven** data preparation toolbox designed to streamline preprocessing workflows by analyzing data characteristics. 

> **Focus:** Currently benchmarked and optimized for **basic tabular data**.

The project features:
* **Automated Type Inference:** Detecting numeric, categorical, and datetime features.
* **Statistical Intelligence:** Integrated skewness and outlier detection (IQR method).
* **Smart Strategy Mapping:** Automated selection of Imputation, Scaling (Standard vs. Robust), and Encoding based on data distribution.

---

### 🛠 System Architecture
The toolbox follows a modular, hybrid architecture:
* **Core Engine:** A wrapper class for seamless user interaction.
* **Utility Layer:** Decoupled functional logic in `utils.py` for high-performance statistical calculations.
* **Plugin System:** Extensible registry for custom transformation modules.

---

## 🚀 Project Progress

### 🏗 Phase 1: Data Analysis (Utils) - [100%]
- [x] Auto infer feature types (Numeric, Categorical, Constant)
- [x] Outlier detection & Skewness calculation
- [x] Missing values & Cardinality statistics
- [x] Target class imbalance check

### ⚙️ Phase 2: Preprocessing (Processors) - [100%]
- [x] Automated Imputation (Median/Most Frequent)
- [x] Scaling (Standard/Robust)
- [x] One-Hot Encoding with state management
- [x] Label Encoding for high cardinality features
- [x] Package distribution & setup.py integration
- [x] Verification with real-world datasets (Titanic Demo)

### 🧪 Phase 3: Model Training & Evaluation - [Coming Soon]
- [ ] Automated model selection
- [ ] Hyperparameter tuning

---


## 📊 Datasets

This project uses the following datasets for testing and demonstration:

| Dataset | Source | Description | Path |
| :--- | :--- | :--- | :--- |
| **Titanic** | [Kaggle](https://www.kaggle.com/c/titanic) | Binary classification for survival prediction. | `data/raw/titanic.csv` |

> **Note:** All raw datasets are stored in `dataset/raw/`. The processed versions after running the `toolbox` will be saved in `dataset/processed/`.


---


## 🧪 Validation & Demo
We verified the DataWise engine using the Titanic dataset. The engine successfully generated optimal preprocessing strategies for mixed data types:
  Scaling: Applied to PassengerId, Age, Fare.
  Encoding: Automatically mapped for Name, Sex, Ticket, Embarked.
  Status: Zero errors found in the final transformation pipeline.

---

## 🧪 Benchmarking & Validation Framework

To ensure the stability, reliability, and precision of the automated pipeline, the toolbox undergoes continuous "stress testing" using diverse real-world datasets.

### 1. Data Sources & Provenance
We benchmark the pipeline against high-variance datasets to ensure cross-domain compatibility:
* **PyCaret Dataset Library:** Standardized sets such as `juice` (mixed types), `diabetes` (numeric), and `credit` (imbalanced classes).
* **UCI Machine Learning Repository:** Classic classification and regression benchmarks (e.g., Adult Census, Wine Quality).
* **Open-source Raw Data (Kaggle):** Testing against uncurated data with high noise levels, complex formatting, and inconsistent schemas.

### 2. Performance Key Results (KPIs)
A transformation is considered successful only if it meets the following criteria:
* **Data Integrity:** Zero unintended row loss; row counts must remain constant unless explicit 'drop' actions are triggered.
* **Schema Accuracy:** One-hot encoded columns must strictly match the unique categories identified during the analysis phase.
* **Null-Value Clearance:** 100% elimination of `NaN` values post-imputation across all features.
* **Production Readiness:** Transformer objects (Scalers, Encoders) must be state-managed to handle "Unseen Data" during inference without crashing or schema mismatch.

### 3. Bug Tracking & Versioning Strategy
Every edge case or failure identified during testing follows a strict resolution cycle:
1. **Detection:** Log the specific traceback and the dataset characteristics that triggered the fault.
2. **Patching:** Refactor logic within `processors.py` or `utils.py` to handle the exception gracefully.
3. **Regression Testing:** Re-running previous successful benchmarks to ensure new patches do not break existing functionality.
4. **Versioning:** Incremental versioning (e.g., `v0.1.0` → `v0.1.1`) documented via a comprehensive Changelog.

---

## 🚀 Installation (Developer Mode)

To use **DataWise** in your local projects while staying synchronized with the source code:

```bash
git clone [https://github.com/starpie-16/ml-prep-box.git](https://github.com/starpie-16/ml-prep-box.git)
cd ml-prep-box
pip install -e .
```

---

## 📅 Updated Technical Log

**Current Focus:** Finalizing the Python package distribution and creating the first official GitHub Release.

**Latest Milestone:** Successfully restructured the project into the datawise package.

**Upcoming Roadmap:**
*   Testing the pipeline against real-world datasets ([PyCaret](https://pycaret.org), [UCI](https://archive.ics.uci.edu), [Kaggle](https://www.kaggle.com)) to ensure robustness.
*   Official public release as a structured library once benchmarking is complete.
*   Adding support for automated model selection.

**Last Update:** `2026-02-19`


---
