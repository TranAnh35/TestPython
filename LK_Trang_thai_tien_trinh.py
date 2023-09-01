import psutil

def check_status():
    for proc in psutil.process_iter():
        try:
            name = proc.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        else:
            print(name)

check_status()