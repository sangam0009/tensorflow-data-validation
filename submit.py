import kfp.components as comp
from kfp.v2 import compiler, dsl

tfdv_stats = comp.load_component_from_file("tfdv_config.yaml")


@dsl.pipeline(name="taxi-pred-pipeline-score", description="chicago taxi predition")
def pipelineTask():
    """Calling components"""
    data_prep_pipe = tfdv_stats()


# def compile_pipeline_json():
#     """Compile and save the json .
#     Parameters
#     ----------
#     context_obj : dict
#         Context dictionary from relevant config file
#     model_type : str
#         choices:{'model_top_15', 'model_below_15'}
#         pipeline artifact for required model type.
#     Returns
#     -------
#     Success/Failure message
#     """

compiler.Compiler().compile(
    pipeline_func=pipelineTask, package_path="tfdv.json"
)

