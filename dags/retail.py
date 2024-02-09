from __future__ import annotations

from datetime import datetime

from airflow.decorators import dag
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)


@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["retail"],
)
def retail():
    LocalFilesystemToGCSOperator(
        task_id="upload_to_gcs",
        src="/usr/local/airflow/include/dataset/online_retail.csv",
        dst="input/online_retail.csv",
        bucket="retail_pipeline_bucket",
        gcp_conn_id="gcp",
        mime_type="text/csv",
    )


retail()
