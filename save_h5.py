import boto3

def main():
	print("Running Main()")
	print("Initializing Boto3 Client")

	s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
	bucket_name = ''
	file_name = 'test.h5'
	object_key = 'Dev/BotName/' + file_name

	print("Uploading File to S3")

	response = s3.put_object(
		Body=file_name,
		Bucket=bucket_name,
		Key=object_key,
		ServerSideEncryption='AES256'
	)

	print("Exiting Main()")

if __name__ == '__main__':
	main()