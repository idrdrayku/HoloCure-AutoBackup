# HoloCure-AutoBackup
A script that automatically backs up your HoloCure save data. Also loads existing backup data automatically.

# How to use:
1. Download ```holocure_autobackup.7z``` from Releases.
2. Extract the downloaded .7z file.
3. Move the ```holocure_autobackup``` folder to desired location.
4. Edit the ```game_path.txt``` file inside the ```holocure_autobackup``` folder and replace the contents with your ```HoloCure.exe``` path if necessary.
    - To determine your ```HoloCure.exe``` path:
        1. Go to your Steam Library.
        2. Right-click ```HoloCure``` in the list, navigate to ```Manage > Browse local files```, and click it.

           ![2](https://github.com/idrdrayku/HoloCure-AutoBackup/assets/143723408/5ad19b25-bb09-4a97-9c05-7db0944327c9)

        3. Click the file explorer's address bar and it should change into a highlighted text. The highlighted text is the Steam directory of HoloCure, and in this example, it is ```D:\SteamLibrary\steamapps\common\HoloCure```.
           
           ![3](https://github.com/idrdrayku/HoloCure-AutoBackup/assets/143723408/d1eeeb28-c266-4b69-a956-361fd5a93c73)

        4. Add ```\HoloCure.exe``` to the end of your HoloCure directory, and the result will be your ```HoloCure.exe``` path. In this example, ```D:\SteamLibrary\steamapps\common\HoloCure``` becomes ```D:\SteamLibrary\steamapps\common\HoloCure\HoloCure.exe```.
        5. Replace the contents of ```game_path.txt``` with your ```HoloCure.exe``` path and save it.

           ![4](https://github.com/idrdrayku/HoloCure-AutoBackup/assets/143723408/d3e66612-7523-4348-87c5-05d5e73fcc90)

5. Set HoloCure's launch options in Steam with this command: ```"{path to holocure_autobackup.exe}" %command%```. (Note: The quotations marks around the path and ```%command%``` stay.)
    - To determine your ```holocure_autobackup.exe``` path:
        1. Open the ```holocure_autobackup``` folder.
        2. Click the file explorer's address bar and it should change into a highlighted text. The highlighted text is the directory of HoloCure AutoBackup, and in this example, it is ```D:\Program Files\holocure_autobackup```.

           ![5](https://github.com/idrdrayku/HoloCure-AutoBackup/assets/143723408/099b16e0-dcc6-4562-a0eb-e3c0c3e7b5eb)

        3. Add ```\holocure_autobackup.exe``` to the end of your HoloCure AutoBackup directory, and the result will be your ```holocure_autobackup.exe``` path. In this example, ```D:\Program Files\holocure_autobackup``` becomes ```D:\Program Files\holocure_autobackup\holocure_autobackup.exe```.
        4. Insert your ```holocure_autobackup.exe``` path into the ```"{path to holocure_autobackup.exe}" %command%``` command and set it as the launch option for HoloCure. In this example, ```"{path to holocure_autobackup.exe}" %command%``` becomes ```"D:\Program Files\holocure_autobackup\holocure_autobackup.exe" %command%```.

           ![6](https://github.com/idrdrayku/HoloCure-AutoBackup/assets/143723408/d7607939-2474-4289-9c1d-db68c22a8df2)

        5. Close the window.
6. Launch the game through Steam and it should work.
