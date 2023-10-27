##############################
# remove old images
##############################

docker rm --force $(docker ps |grep 'l10-transform1')
docker rmi --force $(docker images |grep 'l10-transform1')
docker images -a | grep "l10-transform1" | awk '{print $3}' | xargs docker rmi

docker rm --force $(docker ps |grep 'l10-transform2')
docker rmi --force $(docker images |grep 'l10-transform2')
docker images -a | grep "l10-transform2" | awk '{print $3}' | xargs docker rmi


##############################
# build new pipeline images
##############################

docker build -t darianharrison89/l10-transform1:0.3.4 --build-arg http_proxy=http://web-proxy.corp.hpecorp.net:8080 --build-arg HTTPS_PROXY=http://web-proxy.corp.hpecorp.net:8080 ./transformation_1/
# docker build -t darianharrison89/l10-pipeline:0.3.4 .

docker build -t darianharrison89/l10-transform2:0.3.4 --build-arg http_proxy=http://web-proxy.corp.hpecorp.net:8080 --build-arg HTTPS_PROXY=http://web-proxy.corp.hpecorp.net:8080 ./transformation_2/
# docker build -t darianharrison89/l10-pipeline:0.3.4 .

##############################
# push new pipeline images
##############################

docker push darianharrison89/l10-transform1:0.3.4
docker push darianharrison89/l10-transform2:0.3.4

##############################
# compile and serve pipeline
##############################
dsl-compile --py pipeline.py --output l10-pipeline-0.3.4.tar.gz
cp l10-pipeline-0.3.4.tar.gz /var/www/html/staticfiles

# on ui
# you can just paste http://10.163.169.28/staticfiles/l10-pipelines.tar.gz