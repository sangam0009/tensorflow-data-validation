import pandas as pd
from google.cloud import storage
import logging
import click
import tensorflow_data_validation as tfdv
import os
# from submit import compile_pipeline_json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dev-mlops-exp-batch-vertexai-dw-analytics-d01.json"

def validation():
    
    
    
    df = pd.read_csv('gs://dev_dw_npii_adhoc/sat_analytics/dataproc_testing/tfdv/train.csv')
    
    print('read data')
    
    train_stats = tfdv.generate_statistics_from_dataframe(df)
    
    with open('sample.html','w')  as f:
        f.write(tfdv.get_statistics_html(train_stats))
        
    print('save html file')
    storage_client = storage.Client('dw-analytics-d01')
    bucket = storage_client.get_bucket('dev_dw_npii_adhoc')
    blob = bucket.blob('sat_analytics/dataproc_testing/tfdv/sample.html')
    
    blob.upload_from_filename('sample.html')

    return True

if __name__ == "__main__":
    validation()

        
    
    
    