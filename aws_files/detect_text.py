import boto3
from upload_to_bucket import *

"""
Detects the texts in the file named photo from the S3 Bucket bucket and store the result of recognition as a file named file_name to the local location pointed by path.

params:
* photo: The name of the image shown on S3 bucket.
* bucket: The name of the bucket to get the image. (Only have one bucket 'su20' at this point).
* file_name: The name of the file to store the result of recognition. If file_name doesn't exist, a new file called file_name will be created. Otherwise, the origin file will be overwritten by the result. (The file_name has to end with .txt)
* des_path: The local path to store the result of recognition.
"""

def detect_text(photo, bucket, file_name, des_path):  # functions assumes that path finishes with a '/'

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    if textDetections != None:
        path_filename = des_path + file_name
        target_file = open(path_filename, "w")
        for text in textDetections:
            if text['Type'] == 'LINE':
                 target_file.write(text['DetectedText'])
                 
        target_file.close()
    return len(textDetections)

def main():

    bucket='su20'
    photo='testing3.jpg'
    upload_img("../imgs/testing2.jpg", "testing3.jpg")
    text_count=detect_text(photo, bucket, "aws_doc.txt", "../recognition_result/")
    print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()