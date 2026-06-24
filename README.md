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

## 📊 Analytics & Power BI Layer

The Gold layer is designed to directly feed Power BI dashboards used by healthcare operations teams.

### Key Metrics Available:

- Total Active Patients
- Patient Demographics (Gender / Age Distribution)
- Appointment Volume Trends
- Billing Summary
- Claims Processing Status

### Data Output Format:

- Delta Lake Gold Tables
- Aggregated fact tables
- Star schema ready datasets
  
---

## 🧠 Engineering Decisions

| Decision | Rationale |
|----------|----------|
| Medallion Architecture | Ensures structured data refinement from raw to analytics-ready datasets |
| Databricks + Spark | Enables distributed processing of large healthcare datasets |
| Delta Lake | Provides ACID transactions and supports schema evolution |
| ADF Orchestration | Handles scheduled and event-driven SAP extraction workflows |
| Key Vault Integration | Ensures secure handling of credentials and secrets |
| GitHub Actions | Enables automated validation and CI/CD workflows |
| Terraform | Ensures reproducible Azure infrastructure provisioning |
| Power BI Gold Layer | Provides business-ready reporting datasets |

---

## ▶️ How to Run

```bash
python src/orchestration/pipeline.py
