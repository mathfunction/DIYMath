#  威力彩 - 頭獎期望值小研究 !!

$$
\begin{array}{ll}
0.& \color{red}{生成函數複習: 多項式連乘 P(x) = P_1(x)P_2(x)，加法代表"互斥或"，乘法代表"獨立事件"，P(1) \ 代表組合數} \\ 
1.& 假設不同的彩卷集:  \{x_1,x_2,....x_m\} , \text{其中 } m = C^{38}_{6}C^{8}_{1} = 22085448 ,並假設 \ x_1 \ 為頭獎的那張，獎金 J 元 \\
2.&  1 張彩卷組合表示: \  (x_1+x_2＋...+x_m) \\ 
3.&  1 張沒中頭獎彩卷組合表示 : (x_2+...+x_m) \  所以機率為 \frac{m-1}{m} = 1-\frac{1}{m} ＝ 1-p  \\
4.& K 個人購買 n_k 張彩卷的組合(\color{red}{不論別人個人間是否有重複彩卷})，可寫成   P_{total}(x) = (x_1+x_2+...+x_m)^{n} , 其中 \  n = \sum_{k=1}^{K}n_k \\
5-1.& 至少有1張中獎組合表示: P_{x_1\geq 1}(x) = (x_1+x_2+...+x_m)^{n} - (x_2+...+x_m)^{n} \ 所以機率為 \frac{P_{total}(1)-P_{x_1\geq 1}(1)}{P_{total}(1)} = 1-(1-p)^{n} \\
5-2.& = \underbrace{C^{n}_{n} x_1^n}_{所有張中頭獎} + C^{n}_{n-1} x_1^{n-1}y + ... + \underbrace{C^{n}_{2} x_1^{2}y^{n-2}}_{恰有兩張中} + \underbrace{C^{n}_{1}x_{1}y^{n-1}}_{一張獨得} , 其中 \ y = (x_2+x_3+...+x_m)\\
6.&  恰有 \ i \ 張中頭獎機率 = \frac{C^{n}_{i}(m-1)^{n-i}}{m^{i}} = C^{n}_{i}p^{i}(1-p)^{i} \\
7.&  買 \color{red}{相異} n_k 張中頭獎機率 = \frac{C^{m-1}_{n_k-1}}{C^{m}_{n_k}} = \frac{n_k}{m} =: p_{k}   \\
\end{array}
$$


$$






$$

$$



$$
