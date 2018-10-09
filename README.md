# ChatOps-Locust
Directions for use:
download locustio using 'pip install locustio' if you don't already have it.

1) Navigate to the locusttarget directory, run 'npm install', then run 'node app' to start the server.
2) Get a slack bot token and add it to the __main__.py file where indicated. Add your bot to a channel in slack.
3) Navigate to the chatops directory. Run 'python __main__.py' and then talk to the bot in slack to run the test that you want.
4) The resulting csv files will be saved in the project's root directory

To-do:    
[ ] load test results files upload functionality    
[ ] functionality for distributed testing via SSH commands    
[ ] functionality for customizing locust tests using slack chat    
[ ] --help functionality so users can get help from the slack bot    
