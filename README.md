# 🏥 Healthcare Data Migration Platform

![SAP](https://img.shields.io/badge/ERP-SAP-blue?logo=sap)
![Azure](https://img.shields.io/badge/Cloud-Azure-blue?logo=microsoftazure)
![Databricks](https://img.shields.io/badge/Platform-Databricks-orange?logo=databricks)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python)
![Delta Lake](https://img.shields.io/badge/Storage-Delta%20Lake-lightblue?logo=deltalake)
![Power BI](https://img.shields.io/badge/BI-Power%20BI-yellow?logo=powerbi)
![Compliance](https://img.shields.io/badge/Domain-Healthcare%20Compliance-red)

---

## 🚀 Executive Summary
This project simulates a real-world enterprise healthcare migration program where legacy **SAP systems** are modernised into an **Azure Lakehouse** using Databricks and Delta Lake.  
It demonstrates how large-scale clinical and operational datasets are:
- Extracted from SAP systems  
- Validated and standardised  
- Transformed using Spark-based Medallion architecture  
- Loaded into Delta Lake  
- Served to Power BI for analytics and reporting  

---

## 🧠 Business Context
Healthcare organisations must modernise legacy systems while ensuring:
- Regulatory compliance (HIPAA/GDPR-style constraints)  
- Zero data loss tolerance  
- Historical data integrity  
- Accurate patient and billing records  

This platform shows how structured migration pipelines solve these challenges.

---

## 🏗️ Architecture
🏢 **Business Layer** → ☁️ **Migration Layer** → 🥉 **Bronze** → 🥈 **Silver** → 🥇 **Gold** → 📊 **Consumption Layer**

- **Business Layer:** SAP ECC + Clinical + Billing systems  
- **Migration Layer:** Azure Data Factory + Databricks jobs  
- **Bronze:** Raw SAP extracts  
- **Silver:** Cleaned + standardised data  
- **Gold:** Analytics-ready KPIs  
- **Consumption:** Power BI dashboards  

---

## ⚙️ Key Features
**🔹 Data Ingestion**  
- Simulated SAP extract ingestion  
- Raw CSV staging  

**🔹 Data Transformation**  
- Patient data standardisation  
- Duplicate handling  
- Null value cleaning  

**🔹 Medallion Structure**  
- Bronze → Silver → Gold progression  
- Clear separation of data layers  

---

## 🛠️ Tech Stack
Python · PySpark · Azure Data Lake · Delta Lake · Databricks · GitHub Actions · Terraform · Power BI  

---

## 📂 Project Structure
```
healthcare-data-migration/
├── ingestion/        # SAP extract ingestion scripts
├── bronze/           # Raw staging datasets
├── silver/           # Cleaned + standardised datasets
├── gold/             # Analytics-ready datasets + KPIs
├── quality/          # Data validation + integrity checks
├── reconciliation/   # Audit + reconciliation logic
├── orchestration/    # Pipeline orchestration scripts
├── infrastructure/   # Terraform + CI/CD configs
├── dashboards/       # Power BI models + reports
├── tests/            # Unit/integration tests
└── README.md         # Documentation
```

---

## 📊 Analytics & Power BI Layer
Gold layer feeds Power BI dashboards with:
- Total Active Patients  
- Demographics (gender/age distribution)  
- Appointment volume trends  
- Billing summaries  
- Claims processing status  

Outputs: Delta Lake Gold tables · Aggregated fact tables · Star schema datasets

---

## 🧠 Engineering Decisions
| Decision | Rationale |
|----------|-----------|
| Medallion Architecture | Structured refinement from raw → analytics-ready |
| Databricks + Spark | Distributed processing of large datasets |
| Delta Lake | ACID transactions + schema evolution |
| ADF Orchestration | Scheduled + event-driven SAP extraction |
| Key Vault | Secure credential handling |
| GitHub Actions | Automated validation + CI/CD |
| Terraform | Reproducible Azure infra provisioning |
| Power BI Gold Layer | Business-ready reporting datasets |

---

## 💡 Business Impact
- **Compliance:** POPIA/HIPAA-aligned design ensures regulatory readiness.  
- **Integrity:** Zero-loss migration with validation checkpoints.  
- **Auditability:** Full reconciliation + traceable transformations.  
- **Performance:** Scalable Spark pipelines handle millions of records efficiently.  
- **Decision Support:** Gold datasets feed Power BI, enabling faster clinical and financial insights.  

---

## ▶️ How to Run
```bash
python src/orchestration/pipeline.py
