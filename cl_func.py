from google.cloud import translate_v2 as translate
import base64
import functions_framework

# Initialize the Google Cloud Translation client
translate_client = translate.Client()

@functions_framework.cloud_event
def translate_german_to_english(cloud_event):
    """Triggered from a message on a Cloud Pub/Sub topic."""
    # Decode the Pub/Sub message
    pubsub_message = cloud_event.data["message"]["data"]
    message = base64.b64decode(pubsub_message).decode("utf-8")

    print(f"Received German text: {message}")

    # Translate from German to English
    result = translate_client.translate(message, source_language='de', target_language='en')
    translated_text = result['translatedText']

    print(f"Translated to English: {translated_text}")
