
### Create conda environment
```conda create --name env_name python=3.7```
### Activate conda environment
```conda activate env_name```
### Deactivate conda environment
```conda deactivate```
### List all conda environments
```conda env list``` or ```conda info --envs```
### Remove conda environment
```conda env remove --name env_name```
### Install package in conda environment
```conda install -n env_name package_name``` or
```conda install package_name``` (if environment is activated)
### List all packages in conda environment
```conda list -n env_name``` or ```conda list``` (if environment is activated)
### Remove package from conda environment
```conda remove -n env_name package_name``` or ```conda remove package_name``` (if environment is activated)
### Export conda environment
```conda env export --name env_name > environment.yml```
### Create conda environment from environment.yml
```conda env create --name myenv --file environment.yml``` or
```conda env create -f environment.yml```
### Update conda environment from environment.yml
```conda env update --name myenv --file environment.yml --prune```
### Remove conda environment from environment.yml
```conda env remove -n env_name``` or ```conda env remove -f environment.yml```
### Create conda environment from requirements.txt
```conda create --name env_name --file requirements.txt```
### Update conda environment from requirements.txt
```conda install --name env_name --file requirements.txt```
### Remove conda environment from requirements.txt
```conda env remove --name env_name``` or ```conda remove --file requirements.txt```
### Create requirements.txt from conda environment
```conda list -n env_name --export > requirements.txt```
### Create conda environment from pip requirements.txt
```conda create --name env_name --file requirements.txt --channel conda-forge```
### Update conda environment from pip requirements.txt
```conda install --name env_name --file requirements.txt --channel conda-forge```
### Remove conda environment from pip requirements.txt
```conda env remove --name env_name``` or ```conda remove --file requirements.txt```
### Create pip requirements.txt from conda environment
```conda list -n env_name --export > requirements.txt``` or ```conda list --export > requirements.txt``` (if environment is activated)
