import subprocess

class GetCleaningFunctions:
    def __init__(self):
        pass
    def sanitize_text(self, text):
        match = True
        if match:
            return text
        else:
            return text
    
    # Bare bones TBC

    def check_sudo_command(command):
        try:
            # Prepend 'sudo' to the original command
            sudo_command = ['sudo'] + command.split()
            
            # Execute the command with sudo
            result = subprocess.run(sudo_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # If the command was successful, print the output
            print(f"Command output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            # If an error occurs, print the error
            print(f"Error executing command: {e.stderr}")
        except Exception as e:
            # Handle other possible exceptions
            print(f"An error occurred: {e}")

    # Not yet implemented.
    
