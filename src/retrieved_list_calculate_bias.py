import collections
import numpy as np
import pickle

experiments = ['RM3_biased_0.0',
               'RM3_unbiased_0.1',
               'RM3_unbiased_0.2',
               'RM3_unbiased_0.3',
               'RM3_unbiased_0.4',
               'RM3_unbiased_0.5',
               'RM3_unbiased_0.6',
               'RM3_unbiased_0.7',
               'RM3_unbiased_0.8',
               'RM3_unbiased_0.9'
               ]


metrics = ['RaB', 'ARaB'] 
methods = ['tf', 'bool']

main_path = "/data/"

qry_bias_paths = {}
for metric in metrics:
    qry_bias_paths[metric] = {}
    for exp_name in experiments:
        qry_bias_paths[metric][exp_name] = {}
        for _method in methods:
            qry_bias_paths[metric][exp_name][_method] = main_path + '%s_run_bias_%s_%s.pkl' % (exp_name, _method, metric)
        

at_ranklist = [5, 10, 20, 30, 50, 100]
at_ranklist = [10]
qry_bias_perqry = {}

for metric in metrics:
    qry_bias_perqry[metric] = {}
    for exp_name in experiments:
        qry_bias_perqry[metric][exp_name] = {}
        for _method in methods:
            _path = qry_bias_paths[metric][exp_name][_method]
            print (_path)
            with open(_path, 'rb') as fr:
                qry_bias_perqry[metric][exp_name][_method] = pickle.load(fr)
                
query_ids = [i for i in range(701,850)] # defining the range of the query ids

eval_results_bias = {}
eval_results_feml = {}
eval_results_male = {}

for metric in metrics:
    eval_results_bias[metric] = {}
    eval_results_feml[metric] = {}
    eval_results_male[metric] = {}
    for exp_name in experiments:
        eval_results_bias[metric][exp_name] = {}
        eval_results_feml[metric][exp_name] = {}
        eval_results_male[metric][exp_name] = {}
        for _method in methods:
            eval_results_bias[metric][exp_name][_method] = {}
            eval_results_feml[metric][exp_name][_method] = {}
            eval_results_male[metric][exp_name][_method] = {}
            for at_rank in at_ranklist:
                _bias_list = []
                _feml_list = []
                _male_list = []

                for qryid in query_ids:
                    _bias_list.append(qry_bias_perqry[metric][exp_name][_method][at_rank][qryid][0])
                    _feml_list.append(qry_bias_perqry[metric][exp_name][_method][at_rank][qryid][1])
                    _male_list.append(qry_bias_perqry[metric][exp_name][_method][at_rank][qryid][2])
                    
                eval_results_bias[metric][exp_name][_method][at_rank] = np.mean([(_male_x-_feml_x) for _male_x, _feml_x in zip(_male_list, _feml_list)])
                eval_results_feml[metric][exp_name][_method][at_rank] = np.mean(_feml_list)
                eval_results_male[metric][exp_name][_method][at_rank] = np.mean(_male_list)
                
                             
for metric in metrics:
    print (metric)
    for at_rank in at_ranklist:
        for _method in methods:
            tmp.append(metric)
            tmp.append(at_rank)
            tmp.append(_method)
            for exp_name in experiments:
                print ("%25s\t%2d %5s\t%f\t%f\t%f" % (exp_name, at_rank, _method, eval_results_bias[metric][exp_name][_method][at_rank], eval_results_feml[metric][exp_name][_method][at_rank], eval_results_male[metric][exp_name][_method][at_rank]))
            print ()
        print ("==========")           
                
