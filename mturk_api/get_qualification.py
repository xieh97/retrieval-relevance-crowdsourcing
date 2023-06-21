import boto3

region_name = "us-east-1"
aws_access_key_id = ""
aws_secret_access_key = ""

endpoint_url = "https://mturk-requester-sandbox.us-east-1.amazonaws.com"

# Uncomment this line to use in production
# endpoint_url = "https://mturk-requester.us-east-1.amazonaws.com"

client = boto3.client(
    service_name="mturk",
    region_name=region_name,
    endpoint_url=endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

#
# %% GetQualificationType

response = client.get_qualification_type(
    QualificationTypeId=""
)

qualification = response["QualificationType"]

print("Id:", qualification["QualificationTypeId"],
      "Creation Time:", qualification["CreationTime"],
      "Name:", qualification["Name"],
      "Status:", qualification["QualificationTypeStatus"],
      "Requestable:", qualification["IsRequestable"])
