#create hypothesis test to prove ai assisted tools better than human using aivshuman.csv file
import pandas as pd
from scipy import stats
from distapp.configurations.config import Config
def hypothesis_test():
    config = Config()
    df = pd.read_csv(config.hypothesis_path)
    ai_assisted = df[df['developer_type'] == 'AI Assisted']['logic_score']
    human = df[df['developer_type'] == 'Human Only']['logic_score']
    return ai_assisted.to_list(), human.to_list()

if __name__ == "__main__":
    ai_assisted, human = hypothesis_test()
    print("AI Assisted Logic Scores:", ai_assisted)
    print("Human Logic Scores:", human)