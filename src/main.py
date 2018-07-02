#!/usr/bin/python
import argparse
import importlib
import time
import os
import sys

if os.path.exists('libs.zip'):
    sys.path.insert(0, 'libs.zip')
else:
    sys.path.insert(0, './libs')

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')

# # pylint:disable=E0401
# try:
#     import pyspark
# except:
#     import findspark
#     findspark.init()
#     import pyspark


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a PySpark job')
    parser.add_argument('--job', type=str, required=True, dest='job_name', help="The name of the job module you want to run. (ex: poc will run job on jobs.poc package)")
    parser.add_argument('--files', type=str, required=True, dest='file_name',
                        help="The name of the config file for the module you want to run. (ex: poc will run job on jobs.poc package)")

    args = parser.parse_args()
    print ("Called with arguments: %s" % args)

    job_module = importlib.import_module('jobs.%s' % args.job_name)

    start = time.time()
    job_module.analyze(files=[args.file_name])
    end = time.time()

    print ("\nExecution of job %s took %s seconds" % (args.job_name, end-start))
