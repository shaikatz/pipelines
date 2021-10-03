kfp_endpoint = 'https://71700505d90fcf58-dot-us-central1.pipelines.googleusercontent.com/'

import kfp
from kfp import components

download_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/240543e483076ae718f82c6f280441daa2f041fd/components/web/Download/component.yaml')
run_notebook_op = components.load_component_from_url('https://raw.githubusercontent.com/shaikatz/pipelines/master/components/contrib/notebooks/Run_notebook_using_papermill/component.yaml')

def notebook_pipeline(start_date_epoch, end_date_epoch):
    notebook = download_op('https://raw.githubusercontent.com/kubeflow/pipelines/93fc34474bf989998cf19445149aca2847eee763/components/notebooks/samples/test_notebook.ipynb').output    
    
    run_notebook_op(
        notebook=notebook,
        parameters={'start_date_epoch': start_date_epoch, 'end_date_epoch': end_date_epoch},
        input_data="Optional. Pass output of any component here. Can be a directory.",
        packages_to_install=["matplotlib"],
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline_func=notebook_pipeline, package_path='pipeline.yaml')
    # pipelin_run = kfp.Client(host=kfp_endpoint).create_run_from_pipeline_func(notebook_pipeline, arguments={})