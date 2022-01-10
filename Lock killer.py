from subprocess import Popen, PIPE
from time import sleep, strftime, gmtime

def process_check(processname, delay=2):
    try: _processname = bytes(processname, "utf-8")
    except: _processname = b'' + processname
    print("\nverifications locked on program '" + processname + "'.")

    while True:
        sleep(delay)
        print("[{}] check if grogram '{}' is started ...".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), processname))
        
        founds = Popen(
            ("TASKLIST", "/FI", "imagename eq %s" % processname), shell=True, stdout=PIPE
        ).communicate()[0].strip().lower().splitlines()

        if (len(founds) > 1 and _processname in founds[-1]):
            Popen(("TASKKILL", "/F", "/IM", processname), shell=True, stdout=PIPE)
            print("[{}] '{}' try to restart. Program killed!".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), processname))

if __name__ == "__main__":
    try: input = raw_input
    except NameError: pass
    print("""--------------------
Welcome to killer lock program!

Keep the window open for the program to run.
And if you want to stop the program, close the window or type CTRL+C.

Program path: '{}'
Default lock: 'veyon-worker.exe'
Default delay: 2 s
--------------------\n""".format(__file__))

    delay = 2
    custom = input("Do you want to lock another program ? (leet empty if no)\n>>> ").strip()
    
    process_check("veyon-worker.exe" if custom == '' or custom == ".exe"
        else custom if custom.endswith(".exe") else custom+".exe", delay)
