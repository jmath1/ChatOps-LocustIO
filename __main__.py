

import os
import time
import re
from slackclient import SlackClient
from load_test_conversation import LoadTestingChat

# instantiate Slack client
userOAuthAccessToken = "YOUR TOKEN HERE"
slack_client = SlackClient(userOAuthAccessToken)
# chatopsbot's user ID in Slack: value is assigned after the bot starts up
chatops_bot_id = None

# constants
EXAMPLE_COMMAND = "run"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
class ChatOpsBot():


    def parse_direct_mention(message_text):
        """
            Finds a direct mention (a mention that is at the beginning) in message text
            and returns the user ID which was mentioned. If there is no direct mention, returns None
        """
        matches = re.search(MENTION_REGEX, message_text)
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

    def parse_bot_commands(slack_events):
        """
            Parses a list of events coming from the Slack RTM API to find bot commands.
            If a bot command is found, this function returns a tuple of command and channel.
            If its not found, then this function returns None, None.
        """
        for event in slack_events:
            if event["type"] == "message" and not "subtype" in event:
                user_id, message = ChatOpsBot.parse_direct_mention(event["text"])
                if user_id == chatops_bot_id:
                    return message, event["channel"]
        return None, None

    def handle_command(command, channel):
        """
            Executes bot command if the command contains the
            words "run" or "test"
        """

        # Finds and executes the given command or giving a response
        response = "I don't know that command. Consult my documentation."

        if "run" or "test" in command:
            LoadTestingChat(channel, slack_client)
        else:
            response = default_response
            slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=response
            )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Chatops Bot connected and running!")
        # get bot's user ID by calling Web API method `auth.test`
        chatops_bot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = ChatOpsBot.parse_bot_commands(slack_client.rtm_read())
            if command:
                ChatOpsBot.handle_command(command, channel)
            time.sleep(1)
    else:
        print("Connection failed. Exception traceback printed above.")
