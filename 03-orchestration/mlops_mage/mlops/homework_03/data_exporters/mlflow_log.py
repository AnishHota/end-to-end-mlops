import mlflow
import pickle

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("hw3_mage")

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    dv = data[0]
    model = data[1]

    with open('preprocessor.b', 'wb') as f:
        pickle.dump(dv, f)

    with mlflow.start_run():
        mlflow.log_artifact("preprocessor.b",artifact_path="preprocessor")
        mlflow.sklearn.log_model(model, artifact_path="model_sklearn")

