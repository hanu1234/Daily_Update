"""
Popen -->This method allows the execution of a program in child process.
      -->this is executed by the operating system as a separate process, so it is platform independent

Popen.poll()         ---> Checks if the child process has terminated.
Popen.wait()         ---> Wait for the child process to terminate.
Popen.communicate()  ---> Allows to interact with the process.
Popen.send_signal()  ---> Sends a signal to the child process.
Popen.terminate()	 ---> Stops the child process.
Popen.kill()	     ---> Kills a child process.

Stdout, also known as standard output, is the default file descriptor where a process can write output.

"""
import subprocess


def send_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()                       # wait until process terminate
    out, err = p.communicate()     # read the output from std out
    encoding = 'utf-8'
    output = str(out, encoding)
    for line in output.split('\n'):
        print(line)


send_command('sudo ifconfig wlan0 down')
send_command('sudo ifconfig wlan0 up')
send_command('sudo iwconfig wlan0 mode monitor')
send_command('sudo iwconfig wlan0 channel 48')
send_command('sudo iwconfig')