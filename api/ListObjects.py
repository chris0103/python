from tencentcloud.common import credential
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
import json

secret_id = "xxx"
secret_key = "xxx"
assume_role = "qcs::cam::uin/100019001611:roleName/COS_OPProd_eSignature_RW"
region = "ap-shanghai"
bucket_name = "sanofi-apac-prod-op-esignature-1305705473"
path = "doctors-esign/"

proxies = {
    'http': 'http://127.0.0.1:9000',
    'https': 'http://127.0.0.1:9000',
}

try:
    cred = credential.STSAssumeRoleCredential(secret_id,secret_key,assume_role,"firsttest")
    tmp_secret_id = cred.secretId
    tmp_secret_key = cred.secretKey
    token = cred.token
    scheme = 'https'
    config = CosConfig(Region=region, SecretId=tmp_secret_id, SecretKey=tmp_secret_key, Token=token, Scheme=scheme, Proxies=proxies)
    client = CosS3Client(config)
    response = client.list_objects(Bucket=bucket_name, Prefix=path)
    # print(response)

    truncated = response['IsTruncated']
    next_marker = response['NextMarker']
    for content in response['Contents']:
        print(content['Key'])

    while truncated == 'true':
        response = client.list_objects(Bucket=bucket_name, Prefix=path, Marker=next_marker)
        truncated = response['IsTruncated']
        next_marker = response['NextMarker']
        for content in response['Contents']:
            print(content['Key'])

except Exception as e:
    print(e)