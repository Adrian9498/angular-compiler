# Angular compiler 💻

Have you ever had to do the dist, copy, paste method to bring your angular updates to the **development branch**? 🙄

This script help you with that task, with just running this python script within some arguments your changes will be compiled and delivered to your favorite dist branch.

## How to use? 🙌

It's pretty simple, you'll need 4 arguments:

- Path to the angular project
- Path where the copy of dist folder will be created 
- Angular project name
- Target Folder after branch switch

Example right here:
``

    python .\angular-compiler.py C:\Users\User\Desktop\Angular_Folder C:\Users\User\Desktop angular-app angular-dev
    
    
``

I hope it helps! feel free to make it better!