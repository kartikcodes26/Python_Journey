# =========================
# PIP CHEAT SHEET
# =========================

# Check pip
pip --version
pip --help

# Install
pip install numpy
pip install numpy pandas matplotlib

# Specific version
pip install numpy==2.0.0

# Minimum version
pip install "numpy>=2.0"

# Upgrade
pip install --upgrade numpy

# Uninstall
pip uninstall numpy

# List installed packages
pip list

# Show package information
pip show numpy

# Show outdated packages
pip list --outdated

# Check dependencies
pip check

# Freeze installed packages
pip freeze

# Save dependencies
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt


# =========================
# VIRTUAL ENVIRONMENT
# =========================

# Create
python3 -m venv .venv

# Fish
source .venv/bin/activate.fish

# Bash / Zsh
source .venv/bin/activate

# Install inside venv
pip install numpy pandas

# Exit venv
deactivate
