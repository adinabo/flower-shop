import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from django.conf import settings
from unittest import TestCase

class TestS3BucketSettings(TestCase):

    def test_bucket_exists(self):
        """Test if the configured S3 bucket exists and is accessible."""
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        try:
            response = s3.head_bucket(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
            self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)
        except NoCredentialsError:
            self.fail("AWS credentials not configured correctly.")
        except PartialCredentialsError:
            self.fail("AWS credentials are incomplete.")
        except Exception as e:
            self.fail(f"Failed to access bucket: {e}")
