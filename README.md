# Clear Script

This script is designed to help clean up various common build and cache directories in a project, such as `node_modules`, `build` folders, and caches for Poetry and Pip. It's intended for macOS and should be used with caution.

## ⚠️🚨 IMPORTANT NOTES 🚨⚠️

- **🚨 USE AT YOUR OWN RISK:** The script will delete files and directories on your computer. It is recommended to review and back up any important data before using the script!
- **🔍 VERIFY BEFORE RUNNING:** The script can potentially remove important data. Be sure to double-check your setup before running the script.



## Features

- Deletes `node_modules` directories in the specified project.
- Removes build directories like `.next`, `build`, and Android/iOS build folders.
- Clears Poetry's virtual environment cache.
- Purges Pip's cache (optional with the `--clear-cache` flag).

## Usage

Once the dependencies are installed, you can run the script as follows:

1. To run the script and clean up a project directory:
```bash
   pip install -r requirements.txt && python3 devcleaner.py <directory_path>
```
   Replace `<directory_path>` with the path of the project or Git Folder you want to clean.

2. If you also want to clear both Poetry and Pip caches, use the `--clear-cache` flag:
```bash
   pip install -r requirements.txt && python3 devcleaner.py <directory_path> --clear-cache
```
   This will delete both the Poetry virtualenvs cache and purge Pip's cache.

3. For help or more options, you can use the `-h` or `--help` flag:
```bash
   pip install -r requirements.txt && python3 devcleaner.py --help
```
   This will show the help message and explain the script's usage in more detail.

