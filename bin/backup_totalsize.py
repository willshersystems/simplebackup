#!/usr/bin/python
import boto
import os

s3 = boto.connect_s3()
bucket = s3.lookup(os.environ['BUCKET_NAME'])
total_bytes = 0
for key in bucket:
    total_bytes += key.size
print str(total_bytes/(1024*1024)) + "MB"
