
from slack import WebClient  # 3rd party "slackclient"
from slack.errors import SlackApiError


def send_slack_message(slack_token, channel_name, message):
    client = WebClient(token=slack_token)
    message = message
    try:
        response = client.chat_postMessage(
            channel=f'#{channel_name}',
            text=message)
        assert response["message"]["text"] == message
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        # str like 'invalid_auth', 'channel_not_found'
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")
