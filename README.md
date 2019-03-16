# Flask backend API

## Installation

### Virtualenv

Use the following commands to install and use `virtualenv` with the boilerplate (it is assumed that you already have python and pip installed on your system)

We use virtualenv so that we don't polute our system's python installation.

```
# Install virtualenv
pip install virtualenv (you might need sudo for this one)
cd <your_service_directory>
# Create the virtual environment
virtualenv ./venv
# Activate the virtual environment
source ./venv/bin/activate
```

Once you activate the virtualenv you use the `python` and `pip` from within the environment and not your system's binaries.

You can always deactivate the virtual environment using the following command
```
deactivate
```

### Install dependencies

Install the pip dependencies
```
cd <your_service_directory>
# Activate the virtual environment
source ./venv/bin/activate
pip --no-cache-dir install -r ./requirements.txt --upgrade
```
