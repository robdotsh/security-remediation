import boto3

iam = boto3.client("iam")

for user in iam.list_users()["Users"]:
    print(f"User: {user['UserName']}")
    mfa = iam.list_mfa_devices(UserName=user["UserName"])
    if not mfa["MFADevices"]:
        print("MFA NOT ENABLED")
