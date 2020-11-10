from pyfcm import FCMNotification

fcm_token = "FIREBASE-TOKEN"
api_key = "SERVER-API-KEY"

push_service = FCMNotification(api_key=api_key)

registration_id = fcm_token

message_title = "Company name"
message_body = "Message body"

result = push_service.notify_single_device(
    registration_id=registration_id,
    message_title=message_title,
    message_body=message_body,
    color="#00FF00",
    extra_notification_kwargs={
        "image": "https://dummyimage.com/600x400/0084ff/fff&text=Demo",
    },
    data_message={
        "mt": "message-type",
    },
)

print(result)
