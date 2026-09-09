conda create -n NAME python=VERSION
conda activate NAME
conda deactivate
conda install PACKAGE
conda list
conda env list
conda env remove -n NAME
conda env export > environment.yml

Remember:

Conda environment  → isolated Python + packages
activate.d         → run setup when environment activates
deactivate.d       → cleanup when environment deactivates
environment.yml    → recipe for recreating the environment
.gitignore         → don't commit the actual .conda environment
