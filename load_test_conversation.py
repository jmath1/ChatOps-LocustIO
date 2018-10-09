import time
from commands import CommandDriver
class LoadTestingChat():
    """
    This is a proof of concept. I expect inputs to be correct as
    this development focuses on the functionality of the chatbot,
    not correcting the user
    """

    slackclient = None
    channel = None

    #so I don't have to repeat the talking functionality
    def talk(self,text):
        self.slack_client.api_call(
            "chat.postMessage",
            channel=self.channel,
            text=text
        )

    def get_input(self):
        #going through the testing process unless 'exit' is typed
        while True:
            for event in self.slack_client.rtm_read():
                if event["type"] == "message" and not "subtype" in event:
                    if event["text"] == "exit":
                        return "exit"
                    else:
                        return event["text"]

            time.sleep(1)

    def ask_question(self):
        """ ask the questions. If "exit" is an answer,
        it will be returned and handled in the init method"""

        self.talk("What is the name of the website that we are testing?")
        website = self.get_input()
        if website == "exit":
            return "exit"
        self.talk("What is the number of users we will spawn?")
        users_to_spawn = self.get_input()
        if website == "exit":
            return "exit"
        self.talk("What is the hatch rate?")
        hatch_rate = self.get_input()
        if hatch_rate == "exit":
            return "exit"
        self.talk("What is the name of the csv file to save to?")
        csv_file = self.get_input()
        if csv_file == "exit":
            return "exit"
        self.talk("What is the length (in minutes) of your test?")
        timeout = self.get_input()
        if timeout == "exit":
            return "exit"

        self.talk("Just confirming... you want me to load test {} with {} users at {} users per second for {} minutes? (Y/N)".format(website, users_to_spawn, hatch_rate, timeout))
        final_decision = self.get_input()
        if final_decision.lower() == "yes" or "y":
            return website, users_to_spawn, hatch_rate, csv_file, timeout
        else:
            website, users_to_spawn, hatch_rate, csv_file, timeout = self.ask_question()
            return website, users_to_spawn, hatch_rate, csv_file, timeout

    def uploadFile(file, channel):
        my_file = {
          'file' : (file, open("{}".format('.csv'), 'rb'), 'csv')
        }

        payload={
          "filename":file,
          "token":token,
          "channels":[channel],
        }

        r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
    def __init__(self, channel, slack_client):
        self.channel = channel
        self.slack_client = slack_client
        slack_events = self.slack_client.rtm_read()
        website, users_to_spawn, hatch_rate, csv_file, timeout = self.ask_question()
        self.talk("Hold on for {} minutes... running locust tests...".format(timeout))
        results_generator = CommandDriver.swarm(website, users_to_spawn, hatch_rate, csv_file, timeout)
        self.talk("Your file has been saved")
        #uploadFile("{}_distribution.csv".format(csv_file), token)
        #uploadFile("{}_requests.csv".format(csv_file), token)

        """
        #continuously generate locust output until the user types a command with "stop"
        while True:
            for event in slack_events:
                if event["type"] == "message" and not "subtype" in event:
                    if "stop" in event["text"]:
                        break
                else:
                    for path in results_generator:
                        talk(path)
        """
