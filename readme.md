to execute, simply do 
```
git clone project
cd pipelines
sh recompile-rebuld.sh

then on ui:
create experiment
copy url
run pipieline
```


minio:
you may expose minio and view the items
user: minio
pass: minio123

helper sources:
```
https://www.kubeflow.org/docs/pipelines/sdk/component-development/    
https://github.com/kubeflow/pipelines/tree/master/samples/contrib/versioned-pipeline-ci-samples/helloworld-ci-sample
https://github.com/kubeflow/pipelines/blob/master/sdk/python/kfp/dsl/types.py
```