# RandomGUI

RandomGUI is a tool designed to automatically generate multiple random numbers or random combinations. It comes equipped with a historical query function, allowing users to track and review past random selections. Additionally, it provides the flexibility to choose whether the generated random numbers can be repeated.

## Requirements

Ensure the following dependencies are installed:

```bash
1. Python 3.11
2. PyQt5
3. PyCharm
4. Qt Designer
5. PyUIC5
6. Pyrcc5
```

# How to Build?
Follow these steps to build RandomGUI using PyInstaller:

Open the command prompt (cmd.exe).

Navigate to the project directory.

Execute the following command:

```bash
pyinstaller -F -w -i icon.ico RandomGUI.py GUI.py GUI2.py GUI3.py GUI4.py qtimage_rc.py
```
This command will package RandomGUI and its dependencies into a standalone executable. The -F flag creates a single executable file, while the -w flag runs the program without a console window. The -i flag allows you to specify an icon for the executable.

Feel free to customize the build process according to your preferences and project requirements.
