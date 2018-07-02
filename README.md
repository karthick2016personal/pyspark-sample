# PySpark-Boilerplate
A boilerplate for writing PySpark Jobs

For details see accompanyiong blog post at https://developerzen.com/best-practices-writing-production-grade-pyspark-jobs-cb688ac4d20f#.wg3iv4kie
python3.6 -m pip install -r requirements.txt -t ./src/libs/ 
make build
cd dist
spark-submit --py-files jobs.zip,libs.zip main.py --job email --files etl_config.json
python -m unittest /Users/sowmiya/localgit/pyspark-example-project-new/tests/jobs/email/test_email.py

