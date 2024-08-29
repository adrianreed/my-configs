import os
import subprocess
import shutil
import pwd

def switch_to_bash():
    current_shell = os.getenv("SHELL")
    bash_path = "/bin/bash"
    
    if current_shell != bash_path:
        print(f"Current shell is {current_shell}. Changing to {bash_path}.")
        user_name = pwd.getpwuid(os.getuid()).pw_name
        try:
            subprocess.run(['chsh', '-s', bash_path, user_name], check=True)
            print(f"Default shell changed to {bash_path}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to change shell: {e}")
    else:
        print(f"Current shell is already {bash_path}.")

def configure_bash():
    files_to_copy = [".bash_aliases", ".bash_profile", ".bash_prompt", ".bashrc"]
    home_directory = os.path.expanduser("~")
    
    for file_name in files_to_copy:
        src_path = os.path.join(os.getcwd(), file_name)
        dest_path = os.path.join(home_directory, file_name)
        
        if os.path.exists(src_path):
            try:
                shutil.copy(src_path, dest_path)
                print(f"Copied {file_name} to {dest_path}.")
            except shutil.Error as e:
                print(f"Error copying {file_name}: {e}")
        else:
            print(f"Source file {src_path} does not exist. Skipping.")

if __name__ == "__main__":
    switch_to_bash()
    configure_bash()
