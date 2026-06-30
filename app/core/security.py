
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from config import settings
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_schema=HTTPBearer()


firebase_creds=credentials.Certificate({
    "type":"service_account",
    "project_id": settings.GOOGLE_PROJECT_ID,
    "private_key": settings.GOOGLE_PRIVATE_KEY.replace("\\n", "\n"),
    "client_email": settings.GOOGLE_CLIENT_EMAIL,
    "token_uri": settings.TOKEN_URL,
})

default_app = firebase_admin.initialize_app(firebase_creds)


def verify_firebase_token(token: str):

    decoded_token = auth.verify_id_token(token)
    return decoded_token

def get_current_firebase_user(creds:HTTPAuthorizationCredentials= Depends(bearer_schema)):

    token=creds.credentials
    try:
        decoded_token = verify_firebase_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired Token"
        ) 


