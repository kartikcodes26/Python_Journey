# Create virtual environment
python3 -m venv .venv

# Activate — Fish shell
source .venv/bin/activate.fish

# Activate — Bash / Zsh
source .venv/bin/activate

# Activate — Windows CMD
.venv\Scripts\activate

# Activate — Windows PowerShell
.venv\Scripts\Activate.ps1


# Install packages inside the venv
pip install numpy pandas matplotlib

# Save installed packages
pip freeze > requirements.txt

# Install dependencies
pip install -r requirements.txt

# Check environment
which python
which pip

# Exit virtual environment
deactivate


# ==========================================
#           COMMON PROJECT WORKFLOW
# ==========================================

# 1. Create
python3 -m venv .venv

# 2. Activate
source .venv/bin/activate.fish

# 3. Install
pip install -r requirements.txt

# 4. Work...

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Exit
deactivate
