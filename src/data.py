from src.gmail.messages import get_message_data, get_sends
from src.gmail.service import get_service


def get_training_data(email):
    service = get_service(email)
    sends = get_sends(service, top=10)
    send_data = []
    for send in sends:
        send_data.append(get_message_data(service, send.get("id")))
    return send_data
