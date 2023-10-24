import hydra
from evaluate_model import evaluate
from process import process_data
from train_model import train
import os

@hydra.main(version_base=None, config_path="../../config", config_name="main")
def main(config):
    process_data(config)
    train(config)
    evaluate(config)


if __name__ == "__main__":
    os.environ["MLFLOW_TRACKING_USERNAME"] = "kirilmn13"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = "e90bb58aed2b444b24a588dc01e9240810700ac2"
    main()