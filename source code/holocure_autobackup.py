import ctypes
import os
import shutil
import subprocess
import sys

# if file 'game_path.txt' does not exist in root, then create file 'game_path.txt' in root containing default steam release HoloCure.exe path
if not os.path.isfile("game_path.txt"):
    with open("game_path.txt", "w") as f: f.write("C:\Program Files (x86)\Steam\steamapps\common\HoloCure\HoloCure.exe")

# get HoloCure.exe path from file 'game_path.txt' and assign it to variable 'game_path'
with open("game_path.txt", "r") as f: game_path = f.read()

# if path 'game_path' is incorrect ("incorrect" meaning 'game_path' is neither a file nor HoloCure.exe itself), then throw an error window and terminate script
if not os.path.isfile(game_path) or "HoloCure.exe" not in game_path:
    ctypes.windll.user32.MessageBoxW(0, "Game not found. Please check 'game_path.txt'.", "Error", 16) # throw error window
    sys.exit() # terminate script

# get holocure data directory and assign it to variable 'save_dir' (basically "%localappdata%\HoloCure" in the windows file explorer)
save_dir = os.getenv('LOCALAPPDATA') + "\HoloCure"

# if directory 'holocure_backup' exists in root and is not empty, then overwrite files in directory 'save_dir' with files in 'holocure_backup'; or else, create directory 'holocure_backup' in root and copy files from 'save_dir' into 'holocure_backup'
if os.path.isdir("holocure_backup") and len(os.listdir("holocure_backup")) > 0:
    for file in os.listdir("holocure_backup"): # iterate through files in provided directory, in this case: 'holocure_backup'
        source = f"holocure_backup\{file}" # parse source file path and assign to variable 'source'
        target = f"{save_dir}\{file}" # parse target file path and assign to variable 'target'
        if os.path.isfile(source) and os.path.isfile(target): shutil.copy(source, target) # if both path 'source' and path 'target' are files, then overwrite file 'target' with file 'source'
        elif os.path.isfile(source) and not os.path.isfile(target): shutil.copy(source, save_dir) # otherwise, if only path 'source' is a file and path 'target' does not exist as a file, then copy file 'source' into directory 'save_dir' instead
else:
    if not os.path.isdir("holocure_backup"): os.makedirs("holocure_backup") # if directory 'holocure_backup' does not exist in root, then create directory 'holocure_backup' in root
    for file in os.listdir(save_dir):
        source = f"{save_dir}\{file}"
        target = f"holocure_backup" # assign directory 'holocure_backup' to variable 'target'
        shutil.copy(source, target) # copy file 'source' into directory 'target'

# run game
subprocess.run(game_path)

# boolean 'running' ensures that script does not terminate early while waiting for HoloCure.exe to run (thus ensuring that script will not corrupt the files in directories 'save_dir' and 'holocure_backup' due to early termination)
running = False

# repeatedly check if HoloCure.exe is running or not; if not, then break loop and proceed to next block of code
while True:
    processes = os.popen('wmic process get description').read()         # get string containing a list of currently running processes in the pc and assign it to variable 'processes' (thus, 'processes' basically acts as the list of currently running processes in the pc)
    if "HoloCure.exe" in processes and not running: running = True      # if string "HoloCure.exe" is found in string 'processes' and boolean 'running' is currently False, then set 'running' to True (if HoloCure.exe is in the list of currently running processes, then it means that HoloCure.exe is running)
    elif "HoloCure.exe" not in processes and running: break             # if "HoloCure.exe" is not found in 'processes' and 'running' is currently True, then end the while loop (if HoloCure.exe is not in the list of currently running processes, then it means that HoloCure.exe has been closed)

# overwrite files in directory 'holocure_backup' with files in directory 'save_dir' and terminate script
for file in os.listdir(save_dir):
    source = f"{save_dir}\{file}"
    target = f"holocure_backup\{file}"
    if os.path.isfile(source) and os.path.isfile(target): shutil.copy(source, target)
    if os.path.isfile(source) and not os.path.isfile(target): shutil.copy(source, "holocure_backup") # if only path 'source' is a file and path 'target' does not exist as a file, then copy file 'source' into directory 'holocure_backup'
sys.exit()
