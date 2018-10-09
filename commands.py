
import subprocess
#import os
class CommandDriver():
    def swarm(host, users_to_spawn, hatch_rate, csv_file, timeout):
        host = host.replace("<", "").replace(">", "")
        print(csv_file)
        command = "locust -f locustfile.py --no-web -c {} -r {} --host={} --csv={} --run-time {}m".format(users_to_spawn, hatch_rate, host, csv_file, timeout)
        print(command)
        subprocess.call(command,shell=True)
