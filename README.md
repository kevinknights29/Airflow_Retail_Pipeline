# Airflow_Retail_Pipeline

This project is inspired by the video: Data Engineer Project: An end-to-end Airflow data pipeline with BigQuery, Dbt, Soda, and more!

## Prerequisites

- [ ] Have Docker installed

    To install check: [Docker Dekstop Install](https://www.docker.com/products/docker-desktop/)

- [ ] Have Astro CLI installed

    If you use brew, you can run: `brew install astro`

    For other systems, please refer to: [Install Astro CLI](https://docs.astronomer.io/astro/cli/install-cli)

- [ ] Have a Soda account

    You can get a 45-day free trial: [Soda](https://www.soda.io/)

- [ ] Have a Google Cloud account

    You can create your account here: [Google Cloud](cloud.google.com)

## Getting Started

1. Run `astro dev init` to create the necessary files for your environment.

2. Run `astro dev start` to start the airflow service with docker.

3. Download dataset from [Kaggle - Online Retail](https://www.kaggle.com/datasets/tunguz/online-retail?resource=download)

    - Create a folder `dataset` inside the `include` directory and add your CSV file there.

4. Create a Google Cloud Bucket.

5. Create a Service Account.

    - Grant access to Cloud Storage as "Storage Admin".

    - Grant access to BigQuery as "BigQuery Admin".

6. Create a JSON key for the Service Account.

    - Create a folder `gcp` inside the `include` directory and add your JSON key there.
