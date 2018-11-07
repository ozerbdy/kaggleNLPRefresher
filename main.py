import pandas as pd
from bs4 import BeautifulSoup


# Read labeled training data
train = pd.read_csv("all/labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

# Initialize the BeautifulSoup object on a single movie review
example1 = BeautifulSoup(train["review"][0], features="html.parser")

# Print the raw review and then the output of get_text(), for
# comparison
print(train["review"][0])
print(example1.get_text())
