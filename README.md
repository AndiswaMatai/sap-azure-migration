# 🏥 Healthcare Data Migration Platform

![Azure](https://img.shields.io/badge/Azure-Databricks-blue)
![Architecture](https://img.shields.io/badge/Lakehouse-Medallion-green)
![Pipeline](https://img.shields.io/badge/Data%20Engineering-Spark-orange)
![CI/CD](https://img.shields.io/badge/Automation-GitHub%20Actions-purple)

---

## 🚀 Executive Summary

This project simulates a real-world enterprise healthcare data migration program where legacy SAP systems are modernised into an Azure Lakehouse architecture using Databricks and Delta Lake.

The platform demonstrates how large-scale clinical and operational datasets are:

- Extracted from SAP systems
- Validated and standardised
- Transformed using Spark-based Medallion architecture
- Loaded into Delta Lake
- Served to Power BI for analytics and reporting

It reflects how data engineering teams design **secure, scalable, and auditable migration pipelines in regulated industries like healthcare.**

---

## 🧠 Business Context

Healthcare organisations face increasing pressure to modernise legacy systems while maintaining:

- Regulatory compliance (HIPAA/GDPR-style constraints)
- Zero data loss tolerance
- Historical data integrity
- Accurate patient and billing records

This platform demonstrates how a structured migration approach solves these challenges using cloud-native engineering patterns.

---

## 🏗️ Architecture

🏢 Business Layer
SAP ECC + Clinical Systems + Billing Systems
            ↓
☁️ Migration Layer
Azure Data Factory + Databricks Jobs
            ↓
🥉 Bronze Layer (Raw SAP Extracts)
            ↓
🥈 Silver Layer (Cleaned + Standardised Data)
            ↓
🥇 Gold Layer (Analytics + KPIs)
            ↓
📊 Consumption Layer
Power BI / Reporting / Analytics
---

This architecture ensures:

- Full traceability from SAP source to analytics output
- Zero-loss migration with validation checkpoints
- Scalable processing using Spark
- Separation of raw, clean, and business-ready data
- Cloud-native orchestration and monitoring

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
