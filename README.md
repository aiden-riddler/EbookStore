# GitHub Upload Guide

1. **Create a GitHub Repository**
   - Go to [https://github.com](https://github.com) and log in.
   - Click on the "New" button to create a new repository.
   - Name your repository, add an optional description, and set the visibility (public or private).
   - Click "Create repository".

2. **Initialize Git in Your Project Folder**
   - Open a terminal and navigate to the root folder of your Python project.
   - Run the following commands:
     ```bash
     git init
     ```

3. **Add and Commit Your Project Files**
   - Add all your project files to Git with:
     ```bash
     git add .
     ```
   - Commit the changes with a message:
     ```bash
     git commit -m "Initial commit"
     ```

4. **Link Your Project to the GitHub Repository**
   - Copy the repository URL from GitHub (something like `https://github.com/username/repository.git`).
   - In your terminal, add the remote repository:
     ```bash
     git remote add origin https://github.com/username/repository.git
     ```

5. **Push Your Project to GitHub**
   - Upload your files by running:
     ```bash
     git push -u origin master
     ```

6. **Verify on GitHub**
   - Go back to your repository page on GitHub, and you should see all your files uploaded.
