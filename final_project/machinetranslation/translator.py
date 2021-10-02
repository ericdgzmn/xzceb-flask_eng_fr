"""
Doc string for module
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

#Prepare the Authenticator
authenticator = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

#Function to translate En-Fr
def english_to_french(english_text):
    """function docstring"""
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
        
    french_text = translation['translations'][0]['translation']
    return french_text

#Function to translate Fr-En
def french_to_english(french_text):
    """function docstring"""
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
        
    english_text = translation['translations'][0]['translation']
    return english_text
