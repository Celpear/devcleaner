import os
import shutil
import sys
import logging
import colorlog
import subprocess

# Set up logging with color output
def setup_logging():
    logger = logging.getLogger('clear_script')
    handler = logging.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s: %(message)s',
        datefmt=None,
        log_colors={
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

# Function to delete node_modules folder
def delete_node_modules(directory, logger):
    for root, dirs, files in os.walk(directory, topdown=False):
        if 'node_modules' in dirs:
            node_modules_path = os.path.join(root, 'node_modules')
            try:
                shutil.rmtree(node_modules_path)  # delete node_modules folder
                logger.info(f'Successfully deleted: {node_modules_path}')
            except Exception as e:
                logger.error(f"Failed to delete {node_modules_path}: {e}")

# Function to delete build folders
def delete_build_folders(directory, logger):
    for root, dirs, files in os.walk(directory, topdown=False):
        if '.next' in dirs:
            next_path = os.path.join(root, '.next')
            try:
                shutil.rmtree(next_path)  # delete .next folder
                logger.info(f'Successfully deleted: {next_path}')
            except Exception as e:
                logger.error(f"Failed to delete {next_path}: {e}")

        if 'build' in dirs:
            build_path = os.path.join(root, 'build')
            try:
                shutil.rmtree(build_path)  # delete build folder
                logger.info(f'Successfully deleted: {build_path}')
            except Exception as e:
                logger.error(f"Failed to delete {build_path}: {e}")

        # Android Studio build folder
        if 'app/build' in dirs:
            android_build_path = os.path.join(root, 'app', 'build')
            try:
                shutil.rmtree(android_build_path)  # delete Android Studio build folder
                logger.info(f'Successfully deleted: {android_build_path}')
            except Exception as e:
                logger.error(f"Failed to delete {android_build_path}: {e}")

        # Xcode build folder
        if 'build' in dirs and 'DerivedData' not in root:
            xcode_build_path = os.path.join(root, 'build')
            try:
                shutil.rmtree(xcode_build_path)  # delete Xcode build folder
                logger.info(f'Successfully deleted: {xcode_build_path}')
            except Exception as e:
                logger.error(f"Failed to delete {xcode_build_path}: {e}")

# Function to delete Poetry virtualenv cache
def delete_poetry_cache(logger):
    user_home = os.environ.get('HOME')  # Get the home directory of the current user
    if user_home:
        poetry_cache_dir = os.path.join(user_home, 'Library', 'Caches', 'pypoetry', 'virtualenvs')
        if os.path.exists(poetry_cache_dir):
            try:
                shutil.rmtree(poetry_cache_dir)
                logger.info(f'Successfully deleted: {poetry_cache_dir}')
            except Exception as e:
                logger.error(f"Failed to delete {poetry_cache_dir}: {e}")
        else:
            logger.info(f'The Poetry cache directory does not exist: {poetry_cache_dir}')
    else:
        logger.error("Home directory not found. Cannot delete Poetry cache.")

# Function to run pip cache purge
def pip_cache_purge(logger):
    try:
        subprocess.run(["pip", "cache", "purge"], check=True)  # Execute pip cache purge
        logger.info('Successfully purged pip cache')
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to purge pip cache: {e}")

# Function to display help message
def show_help():
    help_message = """
Usage: python3 devcleaner.py <directory_path> [--clear-cache]

Options:
  <directory_path>   The directory path where the cleanup will be performed.
  --clear-cache      If specified, clears the caches for Poetry and Pip.

Description:
  This script deletes the following:
    - node_modules folders
    - build folders (.next, build, app/build, etc.)
    - Poetry virtualenv cache
    - Pip cache (when --clear-cache flag is provided)

Example:
  python3 devcleaner.py /path/to/directory --clear-cache
  python3 devcleaner.py /path/to/directory
"""
    print(help_message)

# Main execution
if len(sys.argv) < 2:
    show_help()
    sys.exit(1)

# Check if --help flag is passed
if '--help' in sys.argv:
    show_help()
    sys.exit(0)

# Check if --clear-cache flag is passed
clear_cache = '--clear-cache' in sys.argv
target_dir = sys.argv[1]  # The directory path argument

if os.path.exists(target_dir):
    logger = setup_logging()
    delete_node_modules(target_dir, logger)
    delete_build_folders(target_dir, logger)
    
    if clear_cache:
        delete_poetry_cache(logger)  # Clear Poetry cache
        pip_cache_purge(logger)  # Clear Pip cache
    
    logger.info('Cleanup process completed.')
else:
    print(f"The specified directory '{target_dir}' does not exist.")
