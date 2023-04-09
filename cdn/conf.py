# import os
# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_ACCESS_KEY_ID="DO00AVAJP38WZ9WT62NC"
AWS_SECRET_ACCESS_KEY="oPp42Sqd5vuukv0lTLUO8VQTQga2u6dteDlapznZYS0"

AWS_STORAGE_BUCKET_NAME = "phoenixvanz"
AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
     "ACL": "public-read"
}
AWS_LOCATION = "https://phoenixvanz.fra1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'cdn.backends.StaticRootS3BotoStorage'
