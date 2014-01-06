# datahubup(load)

This small script will take an API Key (for datahub.io) and a filename (for a local file) and upload it to datahub.io and then printing out the URL of the uploaded file.


## Installation

The quickest way to install is:

```
git clone https://github.com/rossjones/datahubup.git
cd datahubup
virtualenv .
. bin/activate
python setup.py develop
```

This will then (inside the virtualenv) create a script called datahubup which can be run on the command line (as described below).  If you do this without the virtualenv you may need appropriate use of sudo.

## Usage

You should run the command with an API Key and a filename:

```
datahubup MY_API_KEY sample.csv
```

If the location of datahubup is not in your system path you will need to provide the full path to the script.