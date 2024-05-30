from pathlib import Path

root = Path(__file__).parent.parent  # top-level directory
DATA_PATH = Path('/home/hudson/Desktop/Unicamp/datasets/') #root / "data/"  # datasets and pretrained weights
TRAINING_PATH = root / "outputs/training/"  # training checkpoints
EVAL_PATH = root / "outputs/results/"  # eivaluation results
