from src.utils import *

def main(a,b):
	sum = add(a,b)
	print(sum)

if __name__=="__main__":
	main(12,13)

from configs.config import DATA_PATH, LEARNING_RATE

print("Loading data from:", DATA_PATH)
print("Training with learning rate:", LEARNING_RATE)
