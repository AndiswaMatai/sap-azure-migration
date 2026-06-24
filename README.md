# 🏥 Healthcare Data Migration Platform

![Sector](https://img.shields.io/badge/Sector-Healthcare-005EB8?style=flat)
![Cloud](https://img.shields.io/badge/Azure-Cloud-blue?style=flat)
![Processing](https://img.shields.io/badge/Engine-PySpark-orange?style=flat)
![Architecture](https://img.shields.io/badge/Architecture-Medallion-green?style=flat)

---

## 🚀 Overview

A production-style healthcare data migration platform that demonstrates how enterprise healthcare systems migrate from SAP-based environments into a modern Azure Lakehouse architecture.

The system implements a Medallion Architecture (Bronze → Silver → Gold) using Apache Spark principles, simulating real-world data engineering migration patterns used in enterprise healthcare organisations.

---

## 🧠 Business Problem

Healthcare organisations face significant challenges when modernising legacy SAP systems:

- Large volumes of structured and semi-structured clinical data
- Inconsistent or duplicated patient records
- Regulatory and compliance constraints
- Zero tolerance for data loss
- Complex downstream reporting requirements

This project demonstrates how these challenges are addressed using scalable data engineering patterns.

---

## 🏗️ Architecture

The platform follows a layered Medallion Architecture:

- **Bronze Layer** → Raw ingestion from SAP extracts
- **Silver Layer** → Data cleansing and standardisation
- **Gold Layer** → Analytics-ready datasets for reporting

---

## ⚙️ Key Features (Foundation Level)

### 🔹 Data Ingestion
- Simulated SAP extract ingestion
- Raw CSV-based staging layer

### 🔹 Data Transformation
- Patient data standardisation
- Duplicate handling
- Null value cleaning

### 🔹 Medallion Structure
- Bronze → Silver → Gold progression
- Clear separation of data layers

---

## 🧱 Tech Stack

- Python
- PySpark (design patterns)
- Azure Data Lake (architecture simulation)
- Delta Lake (conceptual design)
- GitHub (version control)

---

## 📂 Project Structure

Structured using enterprise-grade data engineering principles:

- ingestion
- bronze
- silver
- gold
- quality
- reconciliation
- orchestration
- infrastructure

---

## ▶️ How to Run

```bash
python src/orchestration/pipeline.py
