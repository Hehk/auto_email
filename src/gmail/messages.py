import re
import base64


def get_message_data(service, message_id):
    message = get_message(service, message_id)
    previous_messages = get_previous_messages(service, message)

    return {
        "message": parse_message(message),
        "previous_messages": map(parse_message, previous_messages),
    }


def get_message(service, message_id):
    return service.users().messages().get(userId="me", id=message_id).execute()


def get_previous_messages(service, message):
    thread = (
        service.users().threads().get(userId="me", id=message.get("threadId")).execute()
    )
    message_id = message.get("id")

    messages = thread.get("messages")
    previous_messages = []
    for message in messages:
        if message_id != message.get("id"):
            previous_messages.append(message)
        else:
            break

    return previous_messages


def parse_message(message):
    parts = message.get("payload").get("parts")
    part = None
    for p in parts:
        if p.get("mimeType") == "text/plain":
            part = p
            break

    content = None
    if part:
        data = part.get("body").get("data")
        encoded = bytes(str(data), encoding="utf-8")
        content = base64.urlsafe_b64decode(encoded).decode("utf-8")

    lines = content.split("\n")
    message = []
    for line in lines:
        result = re.search(r"^On.*<.*>,? wrote:", line)
        if result:
            break
        else:
            message.append(line)

    message = "\n".join(message)
    return message
