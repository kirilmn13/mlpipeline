import hydra
from omegaconf import DictConfig

@hydra.main(version_base=None, config_path="../../config", config_name="test")
def test_hydra(config: DictConfig):
    assert config.testvar == "testvar"


if __name__ == "__main__":
    test_hydra()
    