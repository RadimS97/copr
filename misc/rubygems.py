import os
import time
from subprocess import PIPE, Popen, call


SLEEP = 4
CONFIG = os.path.join(os.path.expanduser("~"), ".config/copr-dev")
USER = "frostyx"
COPR = "RubyGems"


def all_gems():
    # Require `rubygems` package
    cmd = ["gem", "search"]
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, error = proc.communicate()
    return [x.split()[0] for x in output.split("\n")[:-1]]


def submit_build(copr, gem):
    command = ["/usr/bin/copr-cli", "--config", CONFIG,
               "buildgem", copr, "--gem", gem, "--nowait"]
    call(command)


def main():
    for gem in all_gems():
        print("Submitting gem {0}".format(gem))
        submit_build("{}/{}".format(USER, COPR), gem)
        print("")
        time.sleep(SLEEP)

if __name__ == "__main__":
    main()
