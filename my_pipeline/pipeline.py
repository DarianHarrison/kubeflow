	# https://www.kubeflow.org/docs/pipelines/sdk/sdk-overview/ # for all "kfp" packages list 
import kfp.dsl as dsl
import kfp.components as components

@dsl.pipeline(name='my-pipeline-0.0.0', description='Chained pipelines')

def generic_pipeline(transform_1_input1: str, param_1: int):

  # simple_op = components.load_component_from_url('http://10.163.168.140/staticfiles/transformation_1/component.yaml') # if we decide to serve this file from online source
  transform_1 = components.load_component_from_file('./transformation_1/component.yaml')
  transform_1_step = transform_1(transform_1_input1=transform_1_input1, param_1=param_1) # pass in param

  # simple_op = components.load_component_from_url('http://10.163.168.140/transformation_2/component.yaml') # if we decide to serve this file from online source
  transform_2 = components.load_component_from_file('./transformation_2/component.yaml')
  transform_2_step = transform_2(transform_2_input1= '%s' % transform_1_step.outputs['transform_1_output1']) # pass in param

if __name__ == '__main__':
  import kfp.compiler as compiler
  compiler.Compiler().compile(generic_pipeline, __file__ + '.yaml')