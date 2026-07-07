import logging
import shutil
import subprocess
import sys
from pathlib import Path

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

WORKING_DIR = Path(__file__).parent
LOG_FILE = WORKING_DIR / "launcher.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

JUPYTER_COMMAND = [
    sys.executable,
    "-m",
    "jupyter",
    "lab",
]

# -------------------------------------------------------
# Logging Helpers
# -------------------------------------------------------

def log_info(msg):
    print(msg)
    logging.info(msg)


def log_error(msg):
    print(msg)
    logging.error(msg)


# -------------------------------------------------------
# Validation
# -------------------------------------------------------

def validate():

    if shutil.which(sys.executable) is None:
        raise RuntimeError("Python executable not found.")

    try:
        subprocess.run(
            [sys.executable, "-m", "jupyter", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )

    except Exception:
        raise RuntimeError(
            "JupyterLab is not installed.\n"
            "Install with:\n"
            "pip install jupyterlab"
        )


# -------------------------------------------------------
# Launch
# -------------------------------------------------------

def launch():

    creation_flags = (
        subprocess.CREATE_NEW_PROCESS_GROUP
        | subprocess.DETACHED_PROCESS
    )

    subprocess.Popen(
        JUPYTER_COMMAND,
        cwd=WORKING_DIR,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
        close_fds=True,
    )


# -------------------------------------------------------
# Main
# -------------------------------------------------------

def main():

    try:

        log_info("Starting launcher...")

        validate()

        launch()

        log_info("Jupyter Lab launched successfully.")

    except Exception as e:

        log_error(str(e))
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()