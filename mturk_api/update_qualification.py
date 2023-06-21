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
# %% TAU-ARG audio-text matching test

with open("mturk_task/xml/custom_qualification_test.xml", "r", encoding="utf-8") as test_xml, \
        open("mturk_task/xml/custom_qualification_answer.xml", "r", encoding="utf-8") as answer_xml:
    custom_qualification_test = test_xml.read()
    custom_qualification_answer = answer_xml.read()

response = client.update_qualification_type(
    QualificationTypeId="",
    Description="This is a qualification test of matching audio segments with their content descriptions. In order to "
                "accept TAU-ARG HITs, you should pass this test and obtain the qualification.",
    QualificationTypeStatus="Active",
    RetryDelayInSeconds=60 * 60 * 24 * 365,
    Test=custom_qualification_test,
    AnswerKey=custom_qualification_answer,
    TestDurationInSeconds=1200
)

qualification = response["QualificationType"]

print("Id:", qualification["QualificationTypeId"],
      "Creation Time:", qualification["CreationTime"],
      "Name:", qualification["Name"],
      "Status:", qualification["QualificationTypeStatus"],
      "Requestable:", qualification["IsRequestable"])
