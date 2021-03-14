import pandas as pd
import numpy as np
from pyserini.search import SimpleSearcher
import pickle
from sklearn import preprocessing

run_file_path = "run.file.txt" #path of your run file
file_to_read = open("documents_bias.pkl", "rb")
documents_tf_bias = pickle.load(file_to_read)

result = []
with open(run_file_path) as fr:
    for i, line in enumerate(fr):
        vals = line.strip().split(' ')
        biases = documents_tf_bias[vals[2]]
        result.append([int(vals[0]), vals[2], float(vals[4]),np.abs(biases[0]),np.abs(biases[1])])

min_max_scaler = preprocessing.MinMaxScaler()
df = pd.DataFrame(result, columns = ["qid","docid","score","tc","tf"])
groups = df.groupby('qid')
normalized_list = []
for name, gp in groups:
    print(name)
    gp[['score']] = min_max_scaler.fit_transform(gp[['score']])
    gp[['tf']] = min_max_scaler.fit_transform(gp[['tf']])
    for index, row in gp.iterrows():
        normalized_list.append([name, row['docid'], row['score'],row['tc'], row['tf']])
        
normalized_df = pd.DataFrame(normalized_list, columns = ["qid","docid","score","tc","tf"])
normalized_df.head()

def interpolate(landa, retrieval_score, bias_score):
    score = float((1 - landa)*retrieval_score) - (landa * bias_score)
    return score

landa = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

for l in landa:
    tmp = []
    for row in normalized_list:
        tmp.append([row[0], row[1], row[2], row[4], interpolate(l, row[2], row[4])])
    df = pd.DataFrame(tmp, columns = ["qid","docid","retrieval _score","tf","score"])
    df.sort_values(by = ["qid", "score"], ascending = [True, False], inplace = True)
    df.to_csv("run_file_lambda_"+str(l)+".csv", header = None, index = False)
