from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/VSCode/Gitrepo/GCP_Storage_Bucket_Handling_With_Python/cloudquicklabs-93d1e8c6ac6a.json'

# define function that uploads a file from the bucket
def upload_cs_file(bucket_name, source_file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return 




upload_cs_file('bucket-test-demo', 'C:/VSCode/Gitrepo/bk_upload/cloudquicklabs-93d1e8c6ac6a.json', 'json/test.json')