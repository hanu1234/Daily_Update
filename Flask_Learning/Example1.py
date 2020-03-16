from flask import Flask
import subprocess
import re
import time

app = Flask(__name__)


def execute_commands(cmd, search_string):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = None
    for line in process.stdout:
        if re.search(search_string, line.decode()):
            out = line
            break
    print(out)
    return out


@app.route('/windows/starthub', methods=['GET'])
def start_hub():
    # start the selenium hub
    cmd = 'netstat -ano'
    output = execute_commands(cmd, ":4444")
    if output:
        print("Hub is running on port:{}".format(output))
    else:
        pr = subprocess.Popen("C:\\selenium_grid\\starthub.bat", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        time.sleep(10)

    status = execute_commands(cmd, ":4444")
    return output


@app.route('/windows/startnode', methods=['GET'])
def start_node():
    # check the node status
    cmd = 'netstat -ano'
    output = execute_commands(cmd, ":5556")
    if output:
        print("Node is running on port:{}".format(output))
    else:
        pr = subprocess.Popen("C:\\selenium_grid\\startnode.bat", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        time.sleep(10)
    status = execute_commands(cmd, ":5556")
    return status


@app.route('/')
def messgae():
    return "Happy_serfing"


if __name__ == '__main__':
    app.run(host='10.234.106.226', debug=True)