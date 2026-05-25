# Automated File Organizer

A lightweight Python script that automatically categorizes and sorts files from your `Downloads` folder into organized directories on your `Desktop`.

> [!WARNING]
> **CRITICAL WARNING:** Running this script physically moves your files. Once the process completes, **you cannot automatically undo this action or return the files to their original directories.** Make sure you review the file rules before executing.

## Requirements
* **Python**: Version 3.6 or higher.
* **Operating System**: Windows, macOS, or Linux.
* **Standard Libraries**: No external libraries are needed. The script uses built-in modules (`pathlib`, `shutil`).

---

## 1. How to Install Python

### Windows
1. Download the installer from the official [Python Website](https://python.org).
2. Run the `.exe` installer.
3. **Important**: Check the box that says **"Add python.exe to PATH"** before clicking **Install Now**.
4. Open Command Prompt and verify:
   ```cmd
   python --version
   ```

### macOS
1. Open Terminal.
2. Install Python using Homebrew (recommended):
   ```bash
   brew install python
   ```
3. Alternatively, download the installer from the official website and run the package.
4. Verify the installation:
   ```bash
   python3 --version
   ```

### Linux
1. Open your terminal.
2. Run the update and installation command for your distribution:
   * **Ubuntu/Debian**: 
     ```bash
     sudo apt update && sudo apt install python3 python3-pip
     ```
   * **Fedora**: 
     ```bash
     sudo dnf install python3
     ```
3. Verify the installation:
   ```bash
   python3 --version
   ```

---

## 2. Setup & Execution (By OS)

First, save the script file as `organizer.py` inside a folder on your computer.

### Windows Setup
1. Open **Command Prompt** or **PowerShell**.
2. Navigate to the folder where you saved the script:
   ```cmd
   cd C:\Users\YOUR_USERNAME\Path\To\Script
   ```
3. Run the script manually:
   ```cmd
   python organizer.py
   ```

### macOS Setup
1. Open **Terminal**.
2. Navigate to the folder where you saved the script:
   ```bash
   cd /Users/YOUR_USERNAME/Path/To/Script
   ```
3. Run the script manually:
   ```bash
   python3 organizer.py
   ```

### Linux Setup
1. Open your terminal.
2. Navigate to the folder where you saved the script:
   ```bash
   cd /home/YOUR_USERNAME/Path/To/Script
   ```
3. Run the script manually:
   ```bash
   python3 organizer.py
   ```

---

## 3. How to Schedule (By OS)

### Windows Automation (Task Scheduler)
1. Open the start menu, search for **Task Scheduler**, and open it.
2. Click **Create Basic Task...** in the right-hand panel.
3. Set the name to `File Organizer` and choose **Daily**.
4. Set the action to **Start a program**.
5. Configure the settings:
   * **Program/script**: Type `pythonw` (runs the script silently without a black command window).
   * **Add arguments**: Type `organizer.py`.
   * **Start in**: Paste the full path to the folder where you saved your script.
6. Click **Finish**.

### macOS Automation (Automator Folder Actions)
1. Open **Automator** from your Applications folder and select **New Document**.
2. Choose **Folder Action**.
3. At the top of the window, change "Choose folder" to your **Downloads** folder.
4. Drag the **Run Shell Script** action from the left library pane into the right workflow panel.
5. Set the **Shell** dropdown menu to `/bin/bash`.
6. Paste the following line (replace with your actual python3 path and script location):
   ```bash
   /usr/local/bin/python3 /Users/YOUR_USERNAME/path/to/organizer.py
   ```
7. Save the workflow (`Cmd + S`) and name it `Auto Organizer`. It triggers instantly when files land in Downloads.

### Linux Automation (Cron)
1. Open your terminal.
2. Open your system's crontab configuration file:
   ```bash
   crontab -e
   ```
3. Add this line at the very bottom of the file to run the script every day at midnight (replace with your actual system paths):
   ```text
   0 0 * * * /usr/bin/python3 /home/YOUR_USERNAME/path/to/organizer.py
   ```
4. Save and exit the text editor. The task is scheduled immediately.
