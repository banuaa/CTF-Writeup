import subprocess
import sys

def run_command(arg_list):
    r = subprocess.run(arg_list, capture_output=True)
    if r.stderr:
        output = r.stderr.decode()
    else:
        output = r.stdout.decode()

    return output


_format = "{{.Config}}"
container = "3e47c0ed74b2||id"
arg_list = ['docker', 'inspect', '--format', _format, container]
print(run_command(arg_list)) 
