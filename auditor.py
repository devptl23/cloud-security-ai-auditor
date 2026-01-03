import boto3
import json

s3 = boto3.client('s3')
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')


def do_audit():
    print("Checking buckets...")
    buckets = s3.list_buckets()['Buckets']
    results = []

    for b in buckets:
        if "dev-patel" in b['Name']:
            bucket_name = b['Name']
            security_info = {
                "name": bucket_name,
                "status": "Found",
                "security_checks": {}
            }

            try:
                # Check encryption
                encryption = s3.get_bucket_encryption(Bucket=bucket_name)
                security_info["security_checks"]["encryption"] = "ENABLED"
            except:
                security_info["security_checks"]["encryption"] = "DISABLED (Risk!)"

            try:
                # Check public access
                public_access = s3.get_public_access_block(Bucket=bucket_name)
                is_blocked = public_access['PublicAccessBlockConfiguration']['BlockPublicAcls']
                security_info["security_checks"]["public_access_blocked"] = is_blocked
            except:
                security_info["security_checks"]["public_access_blocked"] = False

            try:
                # Check versioning
                versioning = s3.get_bucket_versioning(Bucket=bucket_name)
                security_info["security_checks"]["versioning"] = versioning.get(
                    'Status', 'Disabled')
            except:
                security_info["security_checks"]["versioning"] = "Unknown"

            try:
                # Check logging
                logging = s3.get_bucket_logging(Bucket=bucket_name)
                has_logging = 'LoggingEnabled' in logging
                security_info["security_checks"]["logging_enabled"] = has_logging
            except:
                security_info["security_checks"]["logging_enabled"] = False

            results.append(security_info)

    return results


def ask_ai(data):
    # We are adding very specific instructions to stop the AI from giving a dictionary definition
    prompt = f"""
    You are a Cloud Infrastructure Security Expert. 
    
    SECURITY AUDIT DATA:
    {data}
    
    Provide a security analysis with:
    1. Identified Security Issues (list any risks found)
    2. Compliance Status (is it production-ready?)
    3. 3 Specific Security Recommendations
    
    Be technical and specific. Focus on actual security findings."""

    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 300,
            "stopSequences": [],
            "temperature": 0,  # Setting temperature to 0 makes it more factual and less "creative"
            "topP": 0.9
        }
    })

    response = bedrock.invoke_model(
        body=body, modelId="amazon.titan-text-express-v1")
    response_body = json.loads(response.get('body').read())
    return response_body.get('results')[0].get('outputText')


if __name__ == "__main__":
    found_data = do_audit()

    # Format the security data nicely for the AI
    formatted_data = "AWS S3 BUCKET SECURITY SCAN RESULTS:\n"
    for bucket in found_data:
        formatted_data += f"\nBucket: {bucket['name']}\n"
        for check, result in bucket['security_checks'].items():
            formatted_data += f"  - {check}: {result}\n"

    report = ask_ai(formatted_data)
    print("\n" + "="*60)
    print("🔐 AI-POWERED CLOUD SECURITY AUDIT REPORT")
    print("="*60)
    print(report)
    print("="*60 + "\n")
