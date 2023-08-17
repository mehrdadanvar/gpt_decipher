import os
import jwt
import time
from dotenv import load_dotenv
secret_key = os.getenv("JWT_SECRET")
secret_algorithem = os.getenv("JWT_ALGORITHM")




def generate_token(user):
    iat = time.time()
    expires = iat + 86400
    encododed_token = jwt.encode({"email":user.email,"iat":iat,"expires":expires},key=secret_key,algorithm=secret_algorithem)
    print(encododed_token)
    return encododed_token
    
    return {"access_token":encododed_token}



def decode_token(token):
    decoded_token = jwt.decode(token, key = secret_key, algorithms=secret_algorithem)


