from prefect_aws import S3Bucket
from prefect_aws import AwsCredentials

aws_credentials_block = AwsCredentials.load("my-aws-creds")

def create_s3_bucket_block():
    
    my_s3_bucket_obj = S3Bucket(
        bucket_name="nyc-duration-prediction-hal4zhou ", credentials=aws_credentials_block 
    )
    my_s3_bucket_obj.save(name="s3-bucket-score-output", overwrite=True)


if __name__ == "__main__":
    create_s3_bucket_block()