# On the Orthogonality of Bias and Utility in Ad hoc Retrieval
This repository contains the code and resources for our bias-aware query expansion method, which diminishes the existing gender biases among retrived set of documents. The main focus of this approach in on controlling the bias in psuedo relevance feedback. Our work has shown that it is possible to effectively revise a user query that would lead to a less biased ranked list of documents. Based on our experiments, we find that a less biased revised query can maintain utility and at the same time reduce bias. We believe that this work lays the foundation for considering fairness and utility as two cooperating measures as opposed to being viewed as competing aspects.

In order to revise the initial query in a way that utility is maintained while significantly reducing bias, we re-rank the retrieved list of documents by BM25 using the interpolation formula:


<p style="text-align: center;"> Rel<sub>debiased</sub>(d) = (1-&lambda;) Rel(d) -  &lambda; Bias(d) </p> 


We evaluate our approach by measuring the geneder bias in the retrieved lists of queries for our bias-aware expansion method against simple BM25 and RM3 expansion methods.  Associated run files for each of the methods can be found in [results/runs](https://github.com/biasawareprf/bias-aware-PRF/tree/main/results/runs) directory.The run files for our bias-aware expansion method are available for different values of lambda that determines the level of being sensitive towards biasedness of documents. In addition, the original queries and bias-aware expanded queries for Robust04, GOV2, CW09, CW12 are available in the [results/queries](https://github.com/biasawareprf/bias-aware-PRF/tree/main/results/queries) directory.

We selected the interpolation coefficient (\lambda) from \[0, 1\] with 0.1 incerement. In order to explore whether bias has actually been reduced systematically in the retrieved list of documents, we measure the degree of bias using two diffirent appraoches including ARaB methods and LIWC Toolkit. Our results for &lambda; = 0.5 are provided in table 1. The complete set of results for all &lambda; values are available in Table2 in [results](https://github.com/biasawareprf/bias-aware-PRF/tree/main/results) directory. The results show that regardless of the metric used to measure the bias of the retrieved ranked list of documents, bias is decreased significantly on all the three bias metrics. The percentage of decrease in bias is consistent across all metrics and always statistically significant.

#### Table 1: Bias measurements using ARaB and LIWC-based metrics.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="3">Method</th>
    <th class="tg-fymr" colspan="3"><b>Robust04</th>
    <th class="tg-fymr" colspan="3"><b>GOV2</th>
    <th class="tg-fymr" colspan="3"><b>CW9</th>
    <th class="tg-fymr" colspan="3"><b>CW12</th>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="2">ARaB</td>
    <td class="tg-0pky" rowspan="2">LIWC</td>
    <td class="tg-0pky" colspan="2">ARaB</td>
    <td class="tg-0pky" rowspan="2">LIWC</td>
    <td class="tg-0pky" colspan="2">ARaB</td>
    <td class="tg-0pky" rowspan="2">LIWC</td>
    <td class="tg-0pky" colspan="2">ARaB</td>
    <td class="tg-0pky" rowspan="2">LIWC</td>
  </tr>
  <tr>
    <td class="tg-0pky">TF</td>
    <td class="tg-0pky">Boolean</td>
    <td class="tg-0pky">TF</td>
    <td class="tg-0pky">Boolean</td>
    <td class="tg-0pky">TF</td>
    <td class="tg-0pky">Boolean</td>
    <td class="tg-0pky">TF</td>
    <td class="tg-0pky">Boolean</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7btt"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent"><b>BM25 <a href="https://github.com/biasawareprf/bias-aware-PRF/tree/main/results/runs/BM25" target="_top"> (Run) </a></span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.61</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.35</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.48</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.33</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.14</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.07</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.23</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.08</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.05</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.40</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.14</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.19</span></td>
  </tr>
  <tr>
    <td class="tg-7btt"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent"><b>PRF <a href="https://github.com/biasawareprf/bias-aware-PRF/tree/main/results/runs/PRF" target="_top"> (Run) </a></span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.61</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.34</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.45</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.39</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.11</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.07</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.22</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.07</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.07</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.42</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.10</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.2</span></td>
  </tr>
  <tr>
    <td class="tg-7btt"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent"><b>Our Approach <a href="https://github.com/biasawareprf/bias-aware-PRF/tree/main/results/runs/Bias-aware%20PRF" target="_top"> (Run) </a></span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.43</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.27</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.34</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.18</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.07</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.05</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.14</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.06</span></td>
    <td class="tg-8r26"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.04</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.23</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.05</span></td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.13</span></td>
  </tr>
  <tr>
    <td class="tg-7btt"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent"><b>Decrease in Bias (%) </span></td>
    <td class="tg-pllx"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">29.5</span></td>
    <td class="tg-pllx"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">20.6</span></td>
    <td class="tg-pllx"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">24.4</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">53.8</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">36.4</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">28.6</span></td>
    <td class="tg-pllx"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">36.4</span></td>
    <td class="tg-pllx"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">14.3</span></td>
    <td class="tg-pllx"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">42.9</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">45.2</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">50.0</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">35.0</span></td>
  </tr>
</tbody>
</table>




## Usage

##### In order to achieve a less biased reformulated set of queries, given the initial queries and corresponding relevant documents, one should replicate the following steps:

1. use `documents_calculate_bias.py` script to calculate the bias level of the documents of the given collection.

2. Use `interpolation.py` script to interpolate the retrieval score (given by BM25) with the bias score of each document to re-rank the documents. (In our experiments, we have selected lambda in range of [0,1] with 0.1 increment.)

3. Use [anserini](https://github.com/castorini/anserini) toolkit to perform pseudo relevance feedback and expand the queries based on the top 10 documents of each query. In order to have a less biased expansion, we added a function called customised_RM3 in the SimpleSearcher class of anserini to expand each query based on the given initial query and the re-ranked list of documents that are less biased in comparison with the original run. The changes are made in the SimpleSearcher and RM3ReRanker classes of anserini that is forked into [this repository](https://github.com/biasawareprf/anserini). Finally, the searcher returns a list of retrieved documents based on the expanded queries which can be found [here](https://github.com/biasawareprf/bias-aware-PRF/tree/main/results/runs/Bias-aware%20PRF).

##### In order to evaluate the bias-aware expanded queries and calculate the level of gender biases inside the retirieved documents of each run file:

1. You can use the following command inside the anserini directory to evaluate the performance of the bias-aware expanded queries:
```
tools/eval/trec_eval.9.0.4/trec_eval -m map -m P.30 results/queries/Original Queries/RB04/RB04_qrels.txt /results/runs/Bias-aware PRF/RB04/retrieved_list_unbiased_lambda_0.5.txt
```
2. You may use `runs_calculate_bias.py` and `retrieved_list_calculate_bias.py` scripts for calculating the TF ARab and TF Boolean metrics introduced in [Do Neural Ranking Models Intensify Gender Bias?](https://github.com/navid-rekabsaz/GenderBias_IR) . In addition, the codes for one other metric namely, LIWC are included inside [src/LIWC](https://github.com/biasawareprf/bias-aware-PRF/tree/main/src/LIWC) directory. The LIWC lexicon is proprietary, so it is not included in this repository. The lexicon data can be purchased from [liwc.net](http://liwc.wpengine.com/).

