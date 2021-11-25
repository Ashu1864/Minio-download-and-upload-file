from mmap import ACCESS_WRITE
from minio import Minio

host = "localhost:9000"
access_key="minioadmin"
secret_key="minioadmin"

minioClient = Minio(host,access_key=access_key,secret_key=secret_key,secure=False)
miniobucket = input('Enter the bucket name you want to create:')
found = minioClient.bucket_exists(miniobucket)
if not found:
    minioClient.make_bucket(miniobucket,location='us-west-1')
else:
    print("Bucket"+miniobucket+"already exists")

buckets =minioClient.list_buckets()
for bucket in buckets:
    print(bucket.name)

data = open('file.txt' , 'w')
data.write('This is first file' +'\n')
data.close()

minioClient.fput_object(miniobucket,'contents/file.txt','file.txt')
'6b8c327f0fc6f470c030a5b6c71154c5'
data = open('file2.txt' , 'w')
data.write('This is second file' +'\n')
data.close()
minioClient.fput_object(miniobucket,'contents/file2.txt','file2.txt')
'6b8c327f0fc6f470c030a5b6c71154c5'

objects = minioClient.list_objects(miniobucket,prefix='contents/',recursive=True)
for obj in objects:
    print(obj.object_name,obj.size)

try:
    object = minioClient.fget_object(miniobucket,'contents/file.txt','C:/Users/Public/Documents/common.txt')
    ob = minioClient.fget_object(miniobucket,'contents/file2.txt','C:/Users/Public/Documents/com.txt')
    print("The data is downloaded successfully")
except:
    print("There was error while downloading file. The file might not exist.")
