# Bias Aware RM3
## Charts

The impact of our proposed approach on utility (map)
and bias (ARaB) metrics at cutoff 10:

![](charts/map%4010-lambda.png)
![](charts/bias_decrement%4010.png)

The impact of our proposed approach on utility (map)
and bias (ARaB) metrics at cutoff 20:
![](charts/map%4020-lambda.png)
![](charts/bias_decrement%4020.png)

#### Table2 the Bias measurements using ARaB and LIWC-based metrics, for all lambdas in [0,1]

<table class="tg">
<thead>
  <tr>
    <th class="tg-sg5v" rowspan="5"></th>
    <th class="tg-sg5v" rowspan="3">Method</th>
    <th class="tg-sg5v" colspan="3">Robust04</th>
    <th class="tg-sg5v" colspan="3">Gov2</th>
    <th class="tg-sg5v" colspan="3">CW09</th>
    <th class="tg-sg5v" colspan="3">CW12</th>
  </tr>
  <tr>
    <td class="tg-sg5v" colspan="2">ARaB</td>
    <td class="tg-sg5v" rowspan="2">LIWC</td>
    <td class="tg-sg5v" colspan="2">ARaB</td>
    <td class="tg-sg5v" rowspan="2">LIWC</td>
    <td class="tg-sg5v" colspan="2">ARaB</td>
    <td class="tg-sg5v" rowspan="2">LIWC</td>
    <td class="tg-sg5v" colspan="2">ARaB</td>
    <td class="tg-sg5v" rowspan="2">LIWC</td>
  </tr>
  <tr>
    <td class="tg-sg5v">TF</td>
    <td class="tg-sg5v">Boolean</td>
    <td class="tg-sg5v">TF</td>
    <td class="tg-sg5v">Boolean</td>
    <td class="tg-sg5v">TF</td>
    <td class="tg-sg5v">Boolean</td>
    <td class="tg-sg5v">TF</td>
    <td class="tg-sg5v">Boolean</td>
  </tr>
  <tr>
    <td class="tg-sg5v">BM25</td>
    <td class="tg-sg5v">0.61</td>
    <td class="tg-sg5v">0.35</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.48</span></td>
    <td class="tg-sg5v">0.33</td>
    <td class="tg-sg5v">0.14</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.23</td>
    <td class="tg-sg5v">0.08</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.40</td>
    <td class="tg-sg5v">0.14</td>
    <td class="tg-sg5v">0.19</td>
  </tr>
  <tr>
    <td class="tg-sg5v">PRF</td>
    <td class="tg-sg5v">0.60</td>
    <td class="tg-sg5v">0.34</td>
    <td class="tg-sg5v">0.45</td>
    <td class="tg-sg5v">0.39</td>
    <td class="tg-sg5v">0.11</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.21</td>
    <td class="tg-sg5v">0.08</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.42</td>
    <td class="tg-sg5v">0.10</td>
    <td class="tg-sg5v">0.20</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">λ = 0</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.60</td>
    <td class="tg-sg5v">0.34</td>
    <td class="tg-sg5v">0.45</td>
    <td class="tg-sg5v">0.39</td>
    <td class="tg-sg5v">0.11</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.21</td>
    <td class="tg-sg5v">0.08</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.42</td>
    <td class="tg-sg5v">0.10</td>
    <td class="tg-sg5v">0.20</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2"><span style="font-weight:400;font-style:normal">λ = 0.1</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.56</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.33</span></td>
    <td class="tg-sg5v">0.43</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.30</span></td>
    <td class="tg-sg5v">0.09</td>
    <td class="tg-sg5v">0.04</td>
    <td class="tg-sg5v">0.20</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.08</td>
    <td class="tg-sg5v">0.35</td>
    <td class="tg-sg5v">0.09</td>
    <td class="tg-sg5v">0.17</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">7.14</td>
    <td class="tg-sg5v">3.03</td>
    <td class="tg-sg5v">4.65</td>
    <td class="tg-sg5v">30</td>
    <td class="tg-sg5v">22.22</td>
    <td class="tg-sg5v">50</td>
    <td class="tg-sg5v">5</td>
    <td class="tg-sg5v">33.33</td>
    <td class="tg-sg5v"><span style="color:#FE0000">-12.5</span></td>
    <td class="tg-sg5v">20</td>
    <td class="tg-sg5v">11.11</td>
    <td class="tg-sg5v">17.65</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2"><span style="font-weight:400;font-style:normal">λ = 0.2</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.51</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.31</span></td>
    <td class="tg-sg5v">0.41</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.24</span></td>
    <td class="tg-sg5v">0.09</td>
    <td class="tg-sg5v">0.03</td>
    <td class="tg-sg5v">0.19</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.04</td>
    <td class="tg-sg5v">0.31</td>
    <td class="tg-sg5v">0.09</td>
    <td class="tg-sg5v">0.14</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">17.65</td>
    <td class="tg-sg5v">9.68</td>
    <td class="tg-sg5v">9.76</td>
    <td class="tg-sg5v">62.5</td>
    <td class="tg-sg5v">22.22</td>
    <td class="tg-sg5v">100</td>
    <td class="tg-sg5v">10.53</td>
    <td class="tg-sg5v">33.33</td>
    <td class="tg-sg5v">75</td>
    <td class="tg-sg5v">35.48</td>
    <td class="tg-sg5v">11.11</td>
    <td class="tg-sg5v">42.86</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2"><span style="font-weight:400;font-style:normal">λ = 0.3</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.49</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.30</span></td>
    <td class="tg-sg5v">0.39</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.23</span></td>
    <td class="tg-sg5v">0.09</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.18</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.27</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.14</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">22.45</td>
    <td class="tg-sg5v">13.33</td>
    <td class="tg-sg5v"><span style="color:#000">15.38</span></td>
    <td class="tg-sg5v">69.57</td>
    <td class="tg-sg5v">22.22</td>
    <td class="tg-sg5v">20</td>
    <td class="tg-sg5v">16.67</td>
    <td class="tg-sg5v">33.33</td>
    <td class="tg-sg5v"><span style="color:#FE0000">0</span></td>
    <td class="tg-sg5v">55.56</td>
    <td class="tg-sg5v">42.86</td>
    <td class="tg-sg5v">42.86</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2"><span style="font-weight:400;font-style:normal">λ = 0.4</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.45</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.27</span></td>
    <td class="tg-sg5v">0.38</td>
    <td class="tg-sg5v">0.21</td>
    <td class="tg-sg5v">0.08</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.16</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.23</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.13</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">33.33</td>
    <td class="tg-sg5v">25.93</td>
    <td class="tg-sg5v">18.42</td>
    <td class="tg-sg5v">85.71</td>
    <td class="tg-sg5v">37.5</td>
    <td class="tg-sg5v"><span style="color:#000">0</span></td>
    <td class="tg-sg5v">31.25</td>
    <td class="tg-sg5v">60</td>
    <td class="tg-sg5v">40</td>
    <td class="tg-sg5v">82.61</td>
    <td class="tg-sg5v">100</td>
    <td class="tg-sg5v">53.85</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2">λ = 0.5</td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.43</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.25</span></td>
    <td class="tg-sg5v">0.34</td>
    <td class="tg-sg5v">0.18</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.14</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.04</td>
    <td class="tg-sg5v">0.23</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.13</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">39.53</td>
    <td class="tg-sg5v">36</td>
    <td class="tg-sg5v">32.35</td>
    <td class="tg-sg5v">116.67</td>
    <td class="tg-sg5v">57.14</td>
    <td class="tg-sg5v">20</td>
    <td class="tg-sg5v">50</td>
    <td class="tg-sg5v">33.33</td>
    <td class="tg-sg5v">75</td>
    <td class="tg-sg5v">82.61</td>
    <td class="tg-sg5v">100</td>
    <td class="tg-sg5v">53.85</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2"><span style="font-weight:400;font-style:normal">λ = 0.6</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.41</td>
    <td class="tg-sg5v">0.25</td>
    <td class="tg-sg5v">0.33</td>
    <td class="tg-sg5v">0.19</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.04</td>
    <td class="tg-sg5v">0.13</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.23</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.14</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">46.34</td>
    <td class="tg-sg5v">36</td>
    <td class="tg-sg5v">36.36</td>
    <td class="tg-sg5v">105.26</td>
    <td class="tg-sg5v">57.14</td>
    <td class="tg-sg5v">50</td>
    <td class="tg-sg5v">61.54</td>
    <td class="tg-sg5v">60</td>
    <td class="tg-sg5v">0</td>
    <td class="tg-sg5v">82.61</td>
    <td class="tg-sg5v">66.67</td>
    <td class="tg-sg5v">42.86</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2">λ = 0.7</td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.42</td>
    <td class="tg-sg5v">0.24</td>
    <td class="tg-sg5v">0.35</td>
    <td class="tg-sg5v">0.20</td>
    <td class="tg-sg5v">0.07</td>
    <td class="tg-sg5v">0.04</td>
    <td class="tg-sg5v">0.12</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.04</td>
    <td class="tg-sg5v">0.27</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.14</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">42.86</td>
    <td class="tg-sg5v">41.67</td>
    <td class="tg-sg5v">28.57</td>
    <td class="tg-sg5v">95</td>
    <td class="tg-sg5v">57.14</td>
    <td class="tg-sg5v">50</td>
    <td class="tg-sg5v">75</td>
    <td class="tg-sg5v">60</td>
    <td class="tg-sg5v">75</td>
    <td class="tg-sg5v">55.56</td>
    <td class="tg-sg5v">66.67</td>
    <td class="tg-sg5v">42.86</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2">λ = 0.8</td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.42</td>
    <td class="tg-sg5v">0.24</td>
    <td class="tg-sg5v">0.36</td>
    <td class="tg-sg5v">0.22</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.13</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.27</span></td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.13</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">42.86</span></td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">41.67</span></td>
    <td class="tg-sg5v">25</td>
    <td class="tg-sg5v">77.27</td>
    <td class="tg-sg5v">83.33</td>
    <td class="tg-sg5v">20</td>
    <td class="tg-sg5v">61.54</td>
    <td class="tg-sg5v">60</td>
    <td class="tg-sg5v">40</td>
    <td class="tg-sg5v">55.56</td>
    <td class="tg-sg5v">66.67</td>
    <td class="tg-sg5v">53.85</td>
  </tr>
  <tr>
    <td class="tg-sg5v" rowspan="2"><span style="font-weight:400;font-style:normal">λ = 0.9</span></td>
    <td class="tg-sg5v">Our Approach</td>
    <td class="tg-sg5v">0.43</td>
    <td class="tg-sg5v">0.24</td>
    <td class="tg-sg5v">0.36</td>
    <td class="tg-sg5v">0.21</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.13</td>
    <td class="tg-sg5v">0.05</td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">0.21</span></td>
    <td class="tg-sg5v">0.06</td>
    <td class="tg-sg5v">0.10</td>
  </tr>
  <tr>
    <td class="tg-sg5v">Decrease in Bias (%)</td>
    <td class="tg-sg5v">39.53</td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">41.67</span></td>
    <td class="tg-sg5v"><span style="font-weight:400;font-style:normal">25</span></td>
    <td class="tg-sg5v">85.71</td>
    <td class="tg-sg5v">83.33</td>
    <td class="tg-sg5v">20</td>
    <td class="tg-sg5v">61.54</td>
    <td class="tg-sg5v">60</td>
    <td class="tg-sg5v">16.67</td>
    <td class="tg-sg5v">100</td>
    <td class="tg-sg5v">66.67</td>
    <td class="tg-sg5v">100</td>
  </tr>
</tbody>
</table>
