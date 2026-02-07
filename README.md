
# 📊 ML-Prep-Box
**Simplify data cleaning with automated strategies mapped to your data types.**

---

### 📝 Project Overview
An automated, **metadata-driven** data preparation toolbox designed to streamline preprocessing workflows by analyzing data characteristics. 

> **Focus:** Currently optimized for **basic tabular data**.

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

### ⚙️ Phase 2: Preprocessing (Processors) - [85%]
- [x] Automated Imputation (Median/Most Frequent)
- [x] Scaling (Standard/Robust)
- [x] One-Hot Encoding with state management
- [ ] Label Encoding for high cardinality features
- [ ] Target Leakage detection report

### 🧪 Phase 3: Model Training & Evaluation - [Coming Soon]
- [ ] Automated model selection
- [ ] Hyperparameter tuning

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

## 📅 Updated Technical Log

**Current Focus:** Building the transformation engine to map metadata actions to [Scikit-Learn](https://scikit-learn.org) transformers.

**Latest Milestone:** Completed the core `processors.py` module (Scaling, Imputation, One-Hot Encoding) and integrated state management into `apply_transform`.

**Upcoming Roadmap:**
*   Testing the pipeline against real-world datasets ([PyCaret](https://pycaret.org), [UCI](https://archive.ics.uci.edu), [Kaggle](https://www.kaggle.com)) to ensure robustness.
*   Official public release as a structured library once benchmarking is complete.

**Last Update:** `2026-02-07`


---
