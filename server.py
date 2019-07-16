from score import scorechat_bot

score = scorechat_bot("config.cfg")

def make_reply(msg):
    if msg is not None:
        reply = "Welcome"
    return reply

update_id = None

while True:
    updates = score.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            score.send_message(reply, from_)
