import requests
import time

def send_message(conversation_id, message):
    #  API access token
    access_token = "..." #Note: placeholder here in github

    # API endpoint for sending a message
    url = f"https://api.instagram.com/v1/direct_v2/threads/{conversation_id}/items/"

    # Request payload
    payload = {"recipient_user_ids": [conversation_id], "text": message}

    # HTTP headers
    headers = {
        "User-Agent": "Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334)",
        "Accept-Language": "en-US;q=1, pt-BR;q=0.9",
        "X-IG-Capabilities": "3ToAAA==",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    # Send the request
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Error sending message: {response.text}")

if __name__ == "__main__":
    # Cpmversation and message to be sent.
    conversation_id = "Tânia de neve e o 1 anão"
    message = "---------| Perdi o jogo |------------"

    while True:
        send_message(conversation_id, message)
        time.sleep(1800) # Wait 30min before sending the next message
