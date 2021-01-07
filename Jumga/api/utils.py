import os, hashlib, warnings, requests, json
import base64
from Crypto.Cipher import DES3
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / 'Jumga/.env'
load_dotenv(env_path, verbose=True)

SECRET_KEY = os.getenv("RAVE_SECRET_KEY")
ENCRYPTION_KEY = os.getenv("RAVE_ENCRYPTION_KEY")

class Rave():    

    def __init__(self, secret_key: str, encryption_key: str) -> None: 
        self.secret_key = secret_key
        self.encryption_key = encryption_key
        self.headers = headers = {
            'content-type': 'application/json',
            "Authorization": self.secret_key
        }

    def encryptData(self, data: str) -> str:
        """
        This is the encryption function that encrypts your payload by passing the text and your encryption Key.
        """
        blockSize = 8
        padDiff = blockSize - (len(data) % blockSize)
        cipher = DES3.new(self.encryption_key, DES3.MODE_ECB)
        data = "{}{}".format(data, "".join(chr(padDiff) * padDiff))
        # cipher.encrypt - the C function that powers this doesn't accept plain string, rather it accepts byte strings, hence the need for the conversion below
        test = data.encode('utf-8')
        encrypted = base64.b64encode(cipher.encrypt(test)).decode("utf-8")
        return encrypted


    def charge_card(self, payload: dict) -> dict:

        # encrypt the hashed secret key and payment parameters with the encrypt function
        encrypt_3DES_key = self.encryptData(json.dumps(payload))

        # payment payload
        body = {
            "client": encrypt_3DES_key,
        }

        # card charge endpoint
        endpoint = "https://api.flutterwave.com/v3/charges?type=card"

        # set the content type to application/json

        response = requests.post(endpoint, headers=self.headers, data=json.dumps(body))
        return response.json()

    def validate_charge(self, flw_ref: str, otp: str, tx_type="card") -> dict:
        body = {
            "otp": otp,
            "flw_ref": flw_ref,
            "type": tx_type
        }

        endpoint = "https://api.flutterwave.com/v3/validate-charge"

        response = requests.post(endpoint, headers=self.headers, data=json.dumps(body))
        return response.json()


    def verify_transaction(self, id: str) -> dict:
        endpoint = f"https://api.flutterwave.com/v3/transactions/{id}/verify"

        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    
    def get_all_banks(self, country: str) -> dict:
        endpoint = f"https://api.flutterwave.com/v3/banks/{country}"

        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def charge_bank_ng(self, payload: dict) -> dict:
        endpoint = "https://api.flutterwave.com/v3/charges?type=debit_ng_account"

        response = requests.post(endpoint, headers=self.headers, data=json.dumps(payload))
        return response.json()


# payload = {
#    "tx_ref":"MC-1585230ew9v5050e9",
#    "amount":"100",
#    "account_bank":"044",
#    "account_number":"0690000031",
#    "currency":"NGN",
#    "email":"user@flw.com",
#    "phone_number":"0902620185",
#    "fullname":"Yemi Desola"
# }

# rave = Rave(SECRET_KEY, ENCRYPTION_KEY)
# bank_charge = rave.charge_bank_ng(payload)
# print(bank_charge, "\n\n\n")

# valid = rave.validate_charge(bank_charge["data"]["flw_ref"], "12345", "account")
# print(valid)