from __future__ import annotations

from datetime import datetime

from airflow.decorators import dag
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
)
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)
from astro import sql as aql
from astro.constants import FileType
from astro.dataframes.load_options import PandasLoadOptions
from astro.files import File
from astro.sql.table import Metadata
from astro.sql.table import Table


@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["retail"],
)
def retail():
    upload_to_gcs = LocalFilesystemToGCSOperator(
        task_id="upload_to_gcs",
        src="/usr/local/airflow/include/dataset/online_retail.csv",
        dst="input/online_retail.csv",
        bucket="retail_pipeline_bucket",
        gcp_conn_id="gcp",
        mime_type="text/csv",
    )

    create_bigquery_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="create_bigquery_dataset",
        dataset_id="retail",
        gcp_conn_id="gcp",
    )

    gcs_to_bigquery = aql.load_file(
        task_id="gcs_to_bigquery",
        input_file=File(
            "gs://retail_pipeline_bucket/input/online_retail.csv",
            conn_id="gcp",
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name="raw_invoices",
            conn_id="gcp",
            metadata=Metadata(schema="retail"),
        ),
        use_native_support=False,
        load_options=[
            PandasLoadOptions(encoding="utf_16", kwargs={"encoding_errors": "ignore"}),
        ],
    )

    # Tasks Execution Order
    upload_to_gcs >> create_bigquery_dataset >> gcs_to_bigquery


retail()
