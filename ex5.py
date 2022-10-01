import platform
import subprocess


res = ''

if platform.system().lower() == "windows":
    flag = "-n"
else:
    flag = "-c"

args = ['ping', flag, '5', 'yandex.ru']
subproc = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc.stdout:
    res += line.decode('cp866')

print(res.encode('utf-8').decode('utf-8'))
