import os
import subprocess
import pymsgbox
import sys
import shutil
import filecmp

save_dir = os.getenv('LOCALAPPDATA') + "\HoloCure"

if not os.path.isfile("game_path.txt"):
    while True:
        game_path = pymsgbox.prompt(
            text = "Enter your HoloCure.exe path below.\n\nFor example: 'C:\Program Files (x86)\Steam\steamapps\common\HoloCure\HoloCure.exe' without quotation marks.",
            title = "HoloCure AutoBackup Setup"
        )

        if game_path == None: sys.exit()
        if game_path != "":
            if os.path.isfile(game_path) and "HoloCure.exe" in game_path: break
            else: pymsgbox.alert("Game not found. Please try again.", "Error")

    with open("game_path.txt", "w") as f: f.write(game_path)

    pymsgbox.alert(
        text = "File 'game_path.txt' containing 'HoloCure.exe' path created in root directory. You may edit it if you have moved 'HoloCure.exe' somewhere else.",
        title = "HoloCure AutoBackup Setup"
    )

    os.makedirs("holocure_backup")

    for file in os.listdir(save_dir):
        source = f"{save_dir}\{file}"
        target = "holocure_backup" 
        shutil.copy(source, target)

    pymsgbox.alert(
        text = "Folder 'holocure_backup' containing your HoloCure save data created in root directory. Please do not touch it unless necessary.",
        title = "HoloCure AutoBackup Setup"
    )

else:
    with open("game_path.txt", "r") as f: game_path = f.read()

discrepancy_prompt = None

if not filecmp.cmp("holocure_backup\save_n.dat", f"{save_dir}\save_n.dat", False):
    discrepancy_prompt = pymsgbox.confirm(
        text = "Your backup save data does not match your main save data. This may be caused by one of the following reasons:\n\n1. Your main save is corrupted;\n2. Your backup save is corrupted; or\n3. Your most recent save was not backed up by the script.\n\nIt is advised to launch HoloCure without loading the backup to see what happened to your main save. After closing the game, you will be able to choose whether to overwrite your backup with your main save data or not.\n\nYou may also load the backup to see what happened to it instead. Doing this will cause the script to create a copy of your main save before loading the backup. After closing the game, you will be able to choose whether to use your backup as your main save from now on or to revert to the copy of your main save.\n\nWhat will you do?",
        title = "WARNING! - HoloCure AutoBackup",
        buttons = ["Don't load backup", "Load backup", "Exit"]
    )

if discrepancy_prompt == "Exit": sys.exit()
if discrepancy_prompt == "Load backup":
    os.makedirs("main_save_copy")

    for file in os.listdir(save_dir):
        source = f"{save_dir}\{file}"
        target = "main_save_copy" 
        shutil.copy(source, target)

    pymsgbox.alert(
        text = "Folder 'main_save_copy' containing a copy of your main save created in root directory.",
        title = "HoloCure AutoBackup"
    )

    for file in os.listdir("holocure_backup"):
        source = f"holocure_backup\{file}"
        target = f"{save_dir}\{file}"
        if os.path.isfile(source) and os.path.isfile(target): shutil.copy(source, target)
        elif os.path.isfile(source) and not os.path.isfile(target): shutil.copy(source, save_dir)

    pymsgbox.alert(
        text = "Backup loaded.",
        title = "HoloCure AutoBackup"
    )

subprocess.run(game_path)

running = False

while True:
    processes = os.popen('wmic process get description').read()         
    if "HoloCure.exe" in processes and not running: running = True      
    elif "HoloCure.exe" not in processes and running: break             

if discrepancy_prompt == "Don't load backup":
    overwrite_prompt = pymsgbox.confirm(
        text = "Would you like to overwrite your backup with your main save data?",
        title = "HoloCure AutoBackup",
        buttons = ["Yes", "No"]
    )

    if overwrite_prompt == "Yes":
        overwrite_prompt = pymsgbox.confirm(
        text = "The script will overwrite your backup with your main save data.\n\nContinue?",
        title = "HoloCure AutoBackup",
        buttons = ["Yes", "No"]
    )

if discrepancy_prompt == "Load backup":
    overwrite_prompt = pymsgbox.confirm(
        text = "Would you like to use your backup as your main save from now on? If not, the script will revert the changes by transferring the copy of your main save to HoloCure's save directory.",
        title = "HoloCure AutoBackup",
        buttons = ["Yes", "No"]
    )

    if overwrite_prompt == "Yes":
        overwrite_prompt = pymsgbox.confirm(
        text = "The script will overwrite your main save with your backup save data and delete the copy of your main save.\n\nContinue?",
        title = "HoloCure AutoBackup",
        buttons = ["Yes", "No"]
    )

if not discrepancy_prompt or overwrite_prompt == "Yes":
    for file in os.listdir(save_dir):
        source = f"{save_dir}\{file}"
        target = f"holocure_backup\{file}"
        if os.path.isfile(source) and os.path.isfile(target): shutil.copy(source, target)
        if os.path.isfile(source) and not os.path.isfile(target): shutil.copy(source, "holocure_backup")

if discrepancy_prompt == "Load backup":
    if overwrite_prompt == "No":
        for file in os.listdir("main_save_copy"):
            source = f"main_save_copy\{file}"
            target = f"{save_dir}\{file}"
            if os.path.isfile(source) and os.path.isfile(target): shutil.copy(source, target)
            if os.path.isfile(source) and not os.path.isfile(target): shutil.copy(source, save_dir)

    shutil.rmtree("main_save_copy")

sys.exit()