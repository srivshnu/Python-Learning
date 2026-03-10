# =============================================================
# 1) WHY USE A VIRTUAL ENVIRONMENT?
# =============================================================
# A virtual environment helps create an isolated or separate environment 
# for a Python project. This prevents conflicts in dependencies across 
# different projects (e.g., Project A needs Flask 1.1, but Project B 
# needs Flask 2.0).


# =============================================================
# 2) INSTALLING VIRTUALENV (If needed)
# =============================================================
# First, ensure you have the 'virtualenv' tool installed globally.
# Run this in your terminal/command prompt:

# $ pip install virtualenv

# =============================================================
# 3) CREATING A VIRTUAL ENVIRONMENT
# =============================================================
# Navigate to your project folder in the terminal.
# Example: cd Desktop/30DaysOfPython/flask_project

# Command to create a virtual environment named 'venv'
# 
# For Mac/Linux:
# $ virtualenv venv
# 
# For Windows:
# $ python -m venv venv


# =============================================================
# 4) ACTIVATING THE VIRTUAL ENVIRONMENT
# =============================================================
# You must activate the environment before installing packages into it.

# For Mac/Linux:
# $ source venv/bin/activate

# For Windows (Command Prompt / PowerShell):
# $ venv\Scripts\activate

# For Windows (Git Bash):
# $ source venv/Scripts/activate

# Once activated, your terminal prompt will usually show the environment name:
# (venv) user@computer:~/project_folder$


# =============================================================
# 5) MANAGING PACKAGES INSIDE THE VENV
# =============================================================
# After activation, you can check installed packages. It should be mostly empty.
# $ pip freeze

# Install a package specific to this project (e.g., Flask)
# $ pip install Flask

# Check packages again; you will see Flask and its dependencies:
# $ pip freeze
# Output might look like:
# click==8.1.3
# Flask==2.2.2
# itsdangerous==2.1.2
# Jinja2==3.1.2
# MarkupSafe==2.1.1
# Werkzeug==2.2.2

# BEST PRACTICE: Save your project dependencies to a file.
# $ pip freeze > requirements.txt


# =============================================================
# 6) DEACTIVATING THE VIRTUAL ENVIRONMENT
# =============================================================
# When you are done working on the project, deactivate the environment 
# to return to your global Python environment.
# 
# $ deactivate


# =============================================================
# 7) IMPORTANT NOTE FOR VERSION CONTROL (Git)
# =============================================================
# You should NEVER commit the virtual environment folder (e.g., 'venv/') 
# to GitHub. 
# 
# Add the following line to your .gitignore file:
# venv/
