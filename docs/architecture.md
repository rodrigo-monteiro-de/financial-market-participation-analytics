# Financial Market Participation Analytics

## Business Problem

This project aims to analyze how financial market participation evolves across countries and demographic groups over time.

The initial version focuses on comparing population and investor participation indicators using a modern Data Engineering architecture based on Medallion principles.

---

## Objectives

* Build an end-to-end Data Engineering project.
* Apply dimensional modeling concepts.
* Implement Bronze, Silver, and Gold layers.
* Demonstrate analytical SQL techniques.
* Create business-oriented data marts.
* Deliver data ready for BI consumption.

---

## Architecture

Data Source
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer
↓
Dashboard

---

## Bronze Layer

Stores raw data exactly as received from source systems.

Examples:

* Population datasets
* Investor datasets
* Demographic datasets

---

## Silver Layer

Stores cleansed and standardized datasets.

Transformations include:

* Data type corrections
* Null handling
* Deduplication
* Standardization of values

---

## Gold Layer

Stores business-ready analytical models.

Examples:

* Dimensions
* Fact tables
* Analytical marts

---

## Dimensional Model

### Dimensions

* dim_country
* dim_time
* dim_gender
* dim_age_group

### Fact

* fact_market_participation

### Grain

One row represents:

Country + Year + Gender + Age Group

---

## Future Improvements

* dbt implementation
* DuckDB integration
* Automated ingestion pipelines
* Dashboard publication
* Additional countries
* Additional demographic dimensions
