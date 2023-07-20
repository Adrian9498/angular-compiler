
import os
import sys
import subprocess

def main():
    #Flag to determine if directory exists
    exists = False
    
    #Getting path from arguments
    arguments = sys.argv
    
    #If find arguments
    if len(arguments) > 1:
        #path to the angular project
        path = arguments[1]
        #path to create the copy of dist folder
        copy_path = arguments[2]
        #Angular project name
        angular_name = arguments[3]
        #Target folder
        target_folder = arguments[4]

    #we are loking for the 'angular.json' file
    target = "\\angular.json"
    
    #Searching if path is an angular project
    if os.path.exists(path) and os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            if root != path:
                dirs.clear()
            for filename in files:
                file_path = os.path.join(root, filename)
                if file_path == (path+target):
                    exists = True
                    break
            if(exists):
                break
    else:
        print("The specified directory does not exist.")
    
    # If the path is actually an angular project, then we proceed to execute the commands
    if (not exists):
        return

    #Copy commands
    command_copy = f"xcopy {path}\\dist  {copy_path} /E /I /H /Y"
    command_copy_fn = f"xcopy {copy_path}\\{angular_name} {path}\\{target_folder} /E /I /H /Y"
    
    # List of commands to execute, add git add . , git commit -m "Message" , git push if needed
    commands = ["ng build",command_copy,"git checkout test",command_copy_fn]  
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True,cwd=path)
        print("Output:", result.stdout)
        print("Error:", result.stderr)
        print("Return Code:", result.returncode)
        print("--------------------------------")

if __name__ == '__main__':
    main()