
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

### 📅 Technical Log
* **Current Focus:** Building the transformation engine to map metadata actions to Scikit-Learn transformers.
* **Last Update:** 2026-01-29

---
