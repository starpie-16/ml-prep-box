
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

### 🚀 Roadmap & Current Progress
| Feature | Status |
| :--- | :---: |
| Metadata-driven architecture & Plugin System | ✅ |
| `setup()` function with feature filtering | ✅ |
| Intelligent inference (Skewness & IQR) | ✅ |
| Modular core logic (`utils.py`) | ✅ |
| **`apply_transform()` for automated execution** | 🔄 *Next Step* |

---

### 📅 Technical Log
* **Current Focus:** Building the transformation engine to map metadata actions to Scikit-Learn transformers.
* **Last Update:** 2026-01-29

---
