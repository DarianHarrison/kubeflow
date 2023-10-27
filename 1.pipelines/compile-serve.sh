git pull

##############################
# compile and serve pipeline
##############################
dsl-compile --py pipeline.py --output my-pipeline-0.0.0.tar.gz
cp my-pipeline-0.0.0.tar.gz /var/www/html/staticfiles

# on ui
# you can just paste http://10.163.169.28/staticfiles/my-pipelines.tar.gz