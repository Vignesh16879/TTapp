import requests

def initiate_verification(account_sid, auth_token, service_sid, phone_number):
    endpoint = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications"
    credentials = (account_sid, auth_token)
    data = {
        "To": phone_number,
        "Channel": "sms",  # You can choose "call" or "sms" based on your preference
    }

    try:
        response = requests.post(endpoint, auth=credentials, json=data)

        if response.status_code in {200, 201}:
            print(f"Verification initiated for {phone_number}.")
            return response.json()["sid"]  # Return verification SID for later use
        else:
            print(f"Failed to initiate verification. Status code: {response.status_code}")
            print(response.text)
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def verify_otp(account_sid, auth_token, service_sid, verification_sid, otp):
    endpoint = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{verification_sid}"
    credentials = (account_sid, auth_token)
    data = {"Code": otp}

    try:
        response = requests.post(endpoint, auth=credentials, json=data)

        if response.status_code == 200:
            print(f"Verification successful for SID {verification_sid}.")
        else:
            print(f"Verification failed. Status code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error: {e}")

# Your Twilio Account SID, Auth Token, and Verification Service SID
account_sid = "ACd5a3b4236c548582b3079c4e4a8219b7"
auth_token = "f7126fb59f26189bd21888869886c972"
service_sid = "VAfc8fd98c51fb2cb3ef5c412bfdf5eda3"

# The phone number to be verified (in E.164 format, e.g., +1234567890)
phone_number_to_verify = "+919873629664"

# Initiate the verification process
verification_sid = initiate_verification(account_sid, auth_token, service_sid, phone_number_to_verify)

if verification_sid:
    # Simulate entering the OTP (replace with the actual OTP received)
    entered_otp = input("Enter the OTP: ")

    # Verify the OTP
    verify_otp(account_sid, auth_token, service_sid, verification_sid, entered_otp)
