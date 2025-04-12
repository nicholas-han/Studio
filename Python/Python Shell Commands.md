# Python Shell Commands
## Open Python in Shell
```bash
winpty python # activate a Python environment
>>> quit() # quit the current Python environment
export PYTHONPATH=/c/dir1/subdir3/subsubdir2 # "import" Python files in a folder

bash -c "python code.py > out.txt" # use this when stdout is not working
```

## Create a Virtual Environment
```bash
python -m virtualenv <env_name>
virtualenv <env_name> # create a virtual environment under the current folder
source <env_name>/Scripts/activate # enter a virtual environment
```