
## FLOW

 pipeline setup

 ![Alt Text](./docs/pipeline.jpg)


 Another way to visualize the pipeline setup

 ![Alt Text](./docs/kubeflow.png)


## 0. PREREQUISITES

a. Kubernetes cluster
b. Kubeflow installed on Kubernetes Cluster
c. Docker
```bash
docker --version
```
d. Pyhton3 and Python Package Manager (pip3)
```bash
python3 --version
pip3 --version
```
e. SDK
```bash
pip3 install kfp --upgrade
pip3 install requests --upgrade
pip3 install pip install kfp-server-api
```
sources:
```
https://www.kubeflow.org/docs/pipelines/sdk/install-sdk/
https://www.kubeflow.org/docs/pipelines/sdk/sdk-overview/
```

## 1. APPLICATION LOGIC

```bash
cat ./my_pipeline/transformation_1/transform_1.py
cat ./my_pipeline/transformation_2/transform_2.py
```

## 2. BULD AND PUSH TO IMAGE REGISTRY

a. Dockerfile
```bash
cat ./my_pipeline/transformation_1/Dockerfile
cat ./my_pipeline/transformation_2/Dockerfile
```

b. build images
```bash
docker build -t darianharrison89/my-transform1:0.0.0 --build-arg http_proxy=http://web-proxy.corp.hpecorp.net:8080 --build-arg HTTPS_PROXY=http://web-proxy.corp.hpecorp.net:8080 ./transformation_1/
# docker build -t darianharrison89/my-pipeline:0.0.0 .

docker build -t darianharrison89/my-transform2:0.0.0 --build-arg http_proxy=http://web-proxy.corp.hpecorp.net:8080 --build-arg HTTPS_PROXY=http://web-proxy.corp.hpecorp.net:8080 ./transformation_2/
# docker build -t darianharrison89/my-pipeline:0.0.0 .
```

c. push new pipeline images
```bash
docker push darianharrison89/my-transform1:0.0.0
docker push darianharrison89/my-transform2:0.0.0
```

## 3. DEVELOP COMPONENTS.YAML

```bash
cat ./my_pipeline/transformation_1/component.yaml
cat ./my_pipeline/transformation_2/component.yaml
```

## 4. COMPILE THE JOB EXECUTION DAG

## 5. RUN PIPELINE ON UI



## compile and serve pipeline
```
dsl-compile --py pipeline.py --output my-pipeline-0.0.0.tar.gz
cp my-pipeline-0.0.0.tar.gz /var/www/html/staticfiles
```




## a. compile and serve pipeline 

```bash
git clone
git pull
dsl-compile --py pipeline.py --output my-pipeline-0.0.0.tar.gz
# cp my-pipeline-0.0.0.tar.gz /var/www/html/staticfiles (optionally)
```
# on ui
# you can just paste http://10.163.169.28/staticfiles/my-pipelines.tar.gz



# on ui

to execute, simply do 
```
git clone project
cd pipelines
sh recompile-rebuld.sh

then on ui:
create experiment
# you can just paste http://10.163.169.28/staticfiles/my-pipelines.tar.gz
run pipieline
```





<!-- docker rm --force $(docker ps |grep 'my-transform1')
docker rmi --force $(docker images |grep 'my-transform1')
docker images -a | grep "my-transform1" | awk '{print $3}' | xargs docker rmi

docker rm --force $(docker ps |grep 'my-transform2')
docker rmi --force $(docker images |grep 'my-transform2')
docker images -a | grep "my-transform2" | awk '{print $3}' | xargs docker rmi -->



3. 
on ui (get tar.gz file from server):
```
upload from url> http://10.163.168.140/staticfiles/<pipeline-name>.tar.gz
create experiment (name = first-experiment ) > create run > choose experiment (first-experiment) > start
```

on k8s master you can verify
```
k get all -n anonymous
```


* 1) **program.py** Write the program that contains your component’s logic. The program must use files and command-line arguments to pass data to and from the component.ent.
```
Write your application code, program.py. For example, write code to transform data or train a model.
```
* 2) **build-image.sh** Containerize the program.
```
Create a Docker container image that packages your program (program.py) and upload the container image to a registry.
```
* 3) **component.yaml** Write a component specification in YAML format that describes the component for the Kubeflow Pipelines system.
```
Write a pipeline function using the Kubeflow Pipelines DSL to define the pipeline and include all the pipeline components.
```
* 4) Use the Kubeflow Pipelines SDK to load your component, use it in a pipeline and run that pipeline.
a) **pipelines.py** 
```
Write a component function using the Kubeflow Pipelines DSL to define your pipeline’s interactions with the component’s Docker container.
```
b) **pipelines.tar.gz** Compile the pipeline to generate a compressed YAML definition of the pipeline. 
```
dsl-compile --py [path/to/python/pipelines.py] --output pipelines.tar.gz
```
* 5) **run-pipelines.py** Test, Use the Kubeflow Pipelines SDK to run the pipeline:
```
client-pipeline.py
```

* **steps to build share your pipeline** 

* create python script with invocation arguments
* test script and arguments
* conteinerize the program
* create component.yaml
* compile the code
* push to shared directory