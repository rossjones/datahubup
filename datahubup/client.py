import os
import sys

import ckanclient

def usage(msg=None):
    if msg:
        print msg
    print """
This command requires two arguments, the API key at datahub.io, and the local
name of the file to upload.

    datahubup XXXX-XXXX-XXXX-XXXX localfile.txt
    """

def main():
    try:
        _, apikey, filename = sys.argv
    except Exception, e:
        usage()
        sys.exit(1)

    if not os.path.exists(filename):
        usage("Could not find file: %s" % filename)
        sys.exit(1)

    try:
        client = ckanclient.CkanClient(base_location='http://datahub.io/api',
            api_key=apikey)
        result = client.upload_file(filename)
        print result[0]
    except Exception, exc:
        usage("Failed to upload file: %s" % exc)
        sys.exit(1)


