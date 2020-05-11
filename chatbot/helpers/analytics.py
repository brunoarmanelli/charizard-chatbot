from __app__.chatbot.base import *

api_key = config.chatbase_key
platform = config.chatbase_platform
version = config.chatbase_version

def handled_intent(user_id, intent, message):
    time_stamp = datetime.timestamp(datetime.now())
    message_set = MessageSet(api_key=api_key, platform=platform, version=version)

    msg = Message(api_key=api_key, platform=platform, message=message,
            intent=intent, version=version, user_id=user_id,
            type=MessageTypes.USER, not_handled=False,
            time_stamp=time_stamp)

    message_set.append_message(msg)
    response = message_set.send()

def handled(user_id, message):
    time_stamp = datetime.timestamp(datetime.now())
    message_set = MessageSet(api_key=api_key, platform=platform, version=version)

    msg = Message(api_key=api_key, platform=platform, message=message,
            version=version, user_id=user_id,
            type=MessageTypes.USER, not_handled=False,
            time_stamp=time_stamp)

    message_set.append_message(msg)
    response = message_set.send()

def not_handled(user_id, message):
    time_stamp = datetime.timestamp(datetime.now())
    message_set = MessageSet(api_key=api_key, platform=platform, version=version)

    msg = Message(api_key=api_key, platform=platform, message=message,
            version=version, user_id=user_id,
            type=MessageTypes.USER, not_handled=True,
            time_stamp=time_stamp)

    message_set.append_message(msg)
    response = message_set.send()