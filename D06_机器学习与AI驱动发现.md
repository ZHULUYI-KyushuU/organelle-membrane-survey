---
title: "D06 机器学习与AI驱动发现"
chapter_id: D06
part: D
n_papers: 90
tags: [细胞器膜, 酵母, 文献调研, part-D]
created: 2026-10-13
---

# D06 机器学习与AI驱动发现

**机器学习在细胞器膜研究里已经站稳的角色，是把读图、搜结构、排候选这类高通量判断变便宜，并给出遗传学和生化能检验的假设；它还没有被证明能独立给出脂质转运的速率、方向或膜内的物理量。**

**本章要讲清楚什么**：哪些“AI 发现”真正落到了酵母与膜上（桥状脂质转运蛋白、酵母蛋白定位的深度学习分类、冷冻电子断层中的膜与大分子识别）；这些成功各自依赖什么数据与假设；机器学习力场、生成式设计、机器人科学家与大语言模型智能体离膜生物学的真问题还有多远；数据泄漏与基线比较如何避免被漂亮的指标误导。

## 语言模型与结构预测：从预测到假设

AlphaFold2 以 Evoformer 与结构模块端到端预测蛋白结构，在 CASP14 达到近实验精度（Jumper et al., 2021；架构见 [[D02_结构计算与AlphaFold时代]]）。本章只追问预测被拿去发现了什么，路线有三条。其一是序列语言模型：Rives et al. (2021) 在 2.5 亿条序列上做掩码语言建模（masked language modeling），表征自发编码理化性质、同源与结构信息，并可迁移到突变效应与接触预测；Lin et al. (2023) 的 ESM-2 仅凭单条序列预测原子级结构，ESMFold 免去多序列比对因而快得多，并据此预测了数亿条宏基因组蛋白。其二是复合物预测：RoseTTAFold 以序列、距离、坐标三轨联合推理（Baek et al., 2021），AlphaFold 3 用扩散模块把对象扩到核酸、小分子与离子（Abramson et al., 2024）。其三是把结构当文本检索：Foldseek 将三维结构编码为结构字母表再做序列式搜索，比传统结构比对快数个数量级（van Kempen et al., 2024），使对预测结构库做远缘同源搜索成为可能。

酵母上最直接的产出是复合物。Humphreys et al. (2021) 结合蛋白质组范围的共进化分析与深度学习建模，在酿酒酵母 *Saccharomyces cerevisiae* 的蛋白质组中系统识别并建模核心真核复合物；Michaelis et al. (2023) 用 4159 次 pull-down 得到含 3927 个蛋白、31004 个互作的网络，为这类预测提供实验对照。Terwilliger et al. (2024) 把预测与实验电子密度比较，结论是预测为有价值的假设，局部细节与构象状态仍可能不符。膜蛋白的脂质结合态是否同样如此，本章核验的文献中无人系统评估。

## 桥状脂质转运蛋白：AF2 时代最干净的发现案例

Neuman et al. (2022) 结合 AF2 预测与序列分析，提出 Vps13、Atg2、SHIP164、Tweek 等含重复 β-groove 的蛋白构成“桥状”脂质转运蛋白新超家族；Levine et al. (2022) 用序列分析与结构预测系统比较重复 β 槽（repeating beta groove，RBG）超家族，指出 Vps13、Atg2、SHIP164、Hob、Tweek 在形态、功能与互作上各不相同。这两篇都是综述，只负责定位，证据在别处。Kumar et al. (2018) 证明哺乳动物 VPS13A 与 VPS13C 在体外能在膜间转运多种磷脂，并分别驻留于 ER–线粒体/脂滴与 ER–溶酶体接触位点，生化事实早于结构上的统一。Wong et al. (2019) 的综述把脂质转运按机制分为穿梭、桥与管，Reinisch et al. (2021) 综述了含 Vps13、Atg2 在内的非囊泡转运机制。

酵母给出了“预测—遗传学”的闭环。Toulmay et al. (2022) 发现高效的 GPI 锚合成依赖 Csf1，*CSF1* 缺失株积累缺少磷酸乙醇胺（PE）的 GPI 前体；结构预测提示 Csf1 与 Vps13 同属管状脂质转运蛋白，向内质网供应 PE。这里预测提供的是假说，遗传表型与之相容，但转运的方向与速率并未因此得到。Castro et al. (2022) 是不依赖预测的系统筛选：六种接触位点分裂荧光报告子，对 1165 个酵母菌株做共定位成像，发现 100 多个潜在的接触位点驻留蛋白或效应因子，并鉴定出 Vps13 与 Atg2 的三个同源物驻留于多个接触位点；Valm et al. (2017) 的多光谱成像流程则示范了如何在活细胞内定量细胞器的数量、位置与动态接触。Ghanbarpour et al. (2021) 的模型把这些拼起来：桥状蛋白把脂质输入受体膜的一侧，翻转酶（scramblase）使两叶平衡，从而支撑膜扩张与细胞器生成。这个命题可直接写成方程（见下文），机制细节见 [[A14_膜接触位点与脂质转运蛋白]]。

## 酵母图像：从人工目视到自监督表征

Huh et al. (2003) 的 GFP 融合库给出约四千个蛋白的定位图谱，类别靠人工目视判定。Chong et al. (2015) 把自动化遗传学、高通量显微与计算特征分析结合，在蛋白质组尺度测量丰度与定位，并用二元分类器集成生成定位注释。深度学习随后直接读原始像素：Kraus et al. (2017) 的 DeepLoc 优于“手工特征加分类器”，Pärnamaa et al. (2017) 的 11 层网络单细胞准确率达 91%。同名的序列预测器 DeepLoc 是另一回事（Almagro et al., 2017）。Lu et al. (2018, eLife) 整合多个扰动下的定位筛选，区分针对特定扰动的响应与更普遍的响应程序。

标签昂贵时，自监督表征登场。配对细胞补绘（paired cell inpainting）从酵母单细胞图像无监督学习特征，在定位分类与聚类上优于传统特征（Lu et al., 2019）；PIFiA 对酵母 ORF-GFP 库生成蛋白特征谱，能聚出功能层级、区分多定位蛋白并识别功能模块（Razdaibiedina et al., 2024）；cytoself 无需标签即可区分细胞器及更精细的定位差异（Kobayashi et al., 2022），但据原文它使用的是人类细胞系的内源标记图像库，向酵母迁移尚待检验。分割工具是前置条件：Cellpose 预测梯度流场做实例分割（Stringer et al., 2021），2.0 支持少量标注的人在回路微调（Pachitariu et al., 2022），Cellpose3 加入去噪与上采样（Stringer et al., 2025），µSAM 覆盖光镜与电镜（Archit et al., 2025），YeaZ 专攻酵母明场图像（Dietler et al., 2020）；综述见 Moen et al. (2019)。表型端，Ohya et al. (2005) 用高维形态参数刻画大量缺失株，Mattiazzi et al. (2020) 以神经网络做单细胞分析，显示内吞通路区室的形态多效性与细胞间变异普遍存在，提示“每个基因一个表型向量”是对分布的粗暴压缩。方法细节见 [[D03_显微图像分析与深度学习]]。

## 冷冻电子断层与体积电镜里的机器阅读

Heinrich et al. (2021) 在多种细胞类型的 FIB-SEM 体积中标注多达 35 类细胞器并训练网络，建立了全细胞细胞器分割资源。冷冻电子断层（cryo-ET）信噪比更低，工具更专门：DeePiCt 用 20 个裂殖酵母 *Schizosaccharomyces pombe* 断层图训练并基准测试，监督分割核糖体、脂肪酸合酶、膜、核孔复合体与细胞器（de Teresa-Trueba et al., 2023）；DeepFinder 用三维卷积网络定位并分类多类大分子，比模板匹配快（Moebel et al., 2021）；TomoTwin 用度量学习在嵌入空间定位，无需针对每种蛋白重新训练（Rice et al., 2023）；MemBrain v2 提供膜分割、膜蛋白定位与方向分析的端到端流程（Lamm et al., 2026）。Wozny et al. (2023) 在酵母细胞内解析 ERMES 的分子组织，为内质网–线粒体接触位点的脂质转移提供原位结构依据；这正是上述工具的用武之地，但其流程是否依赖这些网络，本章文献未说明。

局限同样清楚。训练集小（DeePiCt 仅 20 张断层图），标注出自人手，网络学到的是标注者划的边界；对新菌株、新冰厚度、新细胞器的泛化，本章文献中缺少独立检验。

## 膜蛋白与脂质：序列预测、模拟与力场

序列侧，语言模型已进入常规流程：SignalP 6.0 预测五类信号肽（Teufel et al., 2022），DeepLoc 预测定位类别与膜结合状态（Almagro et al., 2017），DeepLoc 2.0 改用语言模型做多标签预测（Thumuluri et al., 2022），DeepTMHMM 预测 α 螺旋与 β 桶跨膜蛋白的拓扑（Hallgren et al., 2022，预印本）。脂质结合位点的专用预测则很薄，本章只有针对无序脂质结合残基的 DisoLipPred（Katuwawala et al., 2021）。

模拟侧，Corradi et al. (2018) 对 10 种膜蛋白在模型质膜中做分子动力学，发现每种蛋白周围有独特的脂质环境“指纹”；Ingólfsson et al. (2022) 用机器学习桥接尺度，研究 RAS 在异质脂质质膜上的脂质依赖动力学；Levental et al. (2023) 综述了脂质纳米环境对膜蛋白的调控。力场方面，Noé et al. (2020) 与 Unke et al. (2021) 综述了学习力场、粗粒化与增强采样；CGnets 用神经网络学习粗粒化力场并再现全原子自由能面（Wang et al., 2019）；Boltzmann 生成器用可逆网络直接采样平衡态（Noé et al., 2019）；Distributional Graphormer 以扩散模型预测平衡分布（Zheng et al., 2024）；Majewski et al. (2023) 的粗粒化势可跨序列迁移并再现折叠热力学。这些工作的对象是蛋白或小分子，本章核验的文献中没有在多组分脂质膜（相分离、曲率）上验证过的机器学习粗粒化势。分子动力学本身见 [[D01_分子动力学模拟]]。

## 生成式设计、闭环实验与智能体

设计方面，RFdiffusion 把 RoseTTAFold 微调成去噪扩散模型，从头生成骨架（Watson et al., 2023），ProteinMPNN 为给定骨架设计序列，序列恢复率高于 Rosetta（Dauparas et al., 2022）。膜蛋白一侧，Xu et al. (2020) 设计跨膜孔，Lu et al. (2018, Science) 设计多次跨膜蛋白并得到与设计一致的晶体结构，Vorobieva et al. (2021) 设计可在脂质环境中折叠的跨膜 β 桶。Goverde et al. (2024) 走了一条有趣的绕路：设计整合膜蛋白（含 GPCR 拓扑）的**可溶性类似物**，热稳定性高并经实验验证，这回避而非解决了脂质环境中的折叠与插入。本章核验的设计工作均不针对酵母细胞器膜的特定蛋白。

闭环方面，King et al. (2004) 描述了物理实现的机器人系统，能提出假设、设计并执行检验实验，用于酵母功能基因组学；Adam 自主提出关于酵母孤儿酶基因的假设，并经独立实验证实（King et al., 2009）；Eve 把定量构效关系的学习与筛选循环自动化，用于重定位抗被忽视热带病的药物（Williams et al., 2015）。Naik et al. (2016) 用主动学习迭代选择实验，不做全排列就学出化合物对多种蛋白亚细胞分布图案的影响。综述见 Wang et al. (2023)。

智能体方面，Coscientist 以 GPT-4 结合文档检索、代码执行与自动化平台完成化学合成任务（Boiko et al., 2023），ChemCrow 为大语言模型接入化学工具（Bran et al., 2024），Virtual Lab 让多个智能体与人类协作设计纳米抗体并经实验验证（Swanson et al., 2025）。三者都不在膜生物学内；酵母遗传加成像的湿实验闭环与膜生物学的 LLM 基准，本章核验的文献里都找不到。

## 表型、脂质组与知识层：数据驱动预测的证据

基因到表型这一端，酵母数据最丰富。Costanzo et al. (2016) 构建了覆盖酵母绝大多数基因的遗传相互作用网络（超过 2300 万双突变体，约 55 万条负相互作用、约 35 万条正相互作用）；DCell 把 2526 个细胞子系统的层级嵌入可见神经网络，在数百万基因型上模拟酵母生长，并给出各子系统贡献（Ma et al., 2018）。但 Ahlmann-Eltze et al. (2025) 发现多个深度学习与基础模型的基因扰动预测并未优于简单线性基线，scGPT 这类预训练生成式模型（Cui et al., 2024）在扰动预测上的优势因此仍待检验。工程端，Zhang et al. (2020) 把基因组规模代谢模型与机器学习结合以优化色氨酸代谢；Baker et al. (2025) 用机器学习流程筛选需过表达的因子，使过氧化物酶体功能容量比野生型提高 137%，多酶途径区室化使香叶醇产量提高 80%，见 [[A11_过氧化物酶体膜]]。

脂质组方面，Ejsing et al. (2009) 给出酵母脂质组的定量基准，Klose et al. (2012) 显示它随生长条件与温度大幅变化，MS-DIAL 4 整合 MS/MS 谱库、碰撞截面与保留时间自动注释大量脂质亚类（Tsugawa et al., 2020）。机器学习做生物标志的范例却在人：Poss et al. (2020) 分析血清脂质组，发现鞘脂是独立于胆固醇的冠心病风险标志。酵母细胞器水平的“脂质组—表型”建模，本章文献里是空白。

知识层上，STRING 整合实验、共表达与文本挖掘证据（Szklarczyk et al., 2023），BioBERT 提升生物医学文本挖掘（Lee et al., 2020），Hetionet 用异质知识网络预测药物重定位（Himmelstein et al., 2017），词嵌入甚至能预测尚未报道的功能材料（Tshitoyan et al., 2019）。酵母的权威注释来自 SGD（Wong et al., 2023），而定位或功能预测器又以这些注释为标签：注释出自文献，文献偏向研究得多的蛋白，循环由此形成（这是本章的推论，不是上述论文的结论）。因果与解释方面，Kemmeren et al. (2014) 对约四分之一酵母基因的缺失株做全基因组表达谱，Meinshausen et al. (2016) 用酵母基因扰动数据检验基于不变性的因果预测，TreeExplainer 给出树模型的精确 SHAP 值（Lundberg et al., 2020）。

## 定量与物理视角

**掩码语言模型与 Potts 模型。** 训练目标为 $\mathcal L=-\mathbb E\sum_{i\in M}\log p_\theta(x_i\mid x_{\setminus M})$。若蛋白家族服从 Potts 模型 $P(x)\propto\exp[\sum_i h_i(x_i)+\sum_{i<j}J_{ij}(x_i,x_j)]$（直接耦合分析 DCA 的基础），则 $p(x_i\mid x_{\setminus i})\propto\exp[h_i(x_i)+\sum_j J_{ij}(x_i,x_j)]$ 恰是一层 softmax；Transformer 可视为把成对耦合推广为依赖整条序列的高阶函数。这是概念性对应，不是所引论文的结论。酵母可提供的参数：Michaelis et al. (2023) 的互作真值集，用来标定复合物预测置信度的阈值。

**力匹配与 Boltzmann 生成器。** 粗粒化映射 $\xi=\Xi(r)$ 下，力匹配最小化 $\mathbb E\|\Xi F(r)+\nabla_\xi U_\theta(\xi)\|^2$；函数类足够大时极小点的梯度对应平均力势 $-k_BT\ln p(\xi)$，函数类受限时热力学一致性不被保证。Boltzmann 生成器依赖变量替换 $p_X(x)=p_Z(F_{xz}(x))\,|\det J_{xz}|$，使似然可计算。酵母提供的输入：Ejsing et al. (2009) 与 Klose et al. (2012) 的脂质摩尔分数 $x_i$ 及其随温度的变化，可作为多组分膜模拟的组成参数。

**扩散与逆折叠。** 前向加噪 $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\,\epsilon$，训练 $\mathbb E\|\epsilon_\theta(x_t,t)-\epsilon\|^2$ 等价于去噪得分匹配；RFdiffusion 把它用于由刚体框架（SE(3)）表示的骨架，ProteinMPNN 则在给定骨架上自回归地采样序列。

**主动学习。** 选择 $e^*=\arg\max_e I(\theta;y_e\mid D)$；高斯过程下 $I=\tfrac12\ln(1+\sigma_f^2(e)/\sigma_n^2)$。噪声 $\sigma_n^2$ 在酵母里可由单细胞间变异估计（Mattiazzi et al., 2020），重复板数据则可标定批次效应。

**因果与归因。** 缺失株是对节点的硬干预 $\mathrm{do}(X_k=0)$。不变因果预测（ICP）接受那些使残差分布在各干预环境下不变的预测因子集合，取其交集；Shapley 值 $\phi_i=\sum_{S\subseteq N\setminus\{i\}}\frac{|S|!(|N|-|S|-1)!}{|N|!}[v(S\cup\{i\})-v(S)]$ 来自合作博弈，是关联意义上的归因，不等于因果效应。

**桥状蛋白加翻转酶的玩具模型。** 设两叶脂质数之差 $\Delta=N_c-N_l$，桥提供净通量 $J$，翻转酶以速率 $k_s$ 平衡：$\dot\Delta=J-k_s\Delta$，稳态 $\Delta^*=J/k_s$，面积差弹性能 $\propto(\Delta-\Delta_0)^2$（见 [[B01_膜弹性曲率与形状能量]]）。$J$ 与 $k_s$ 的实测值，本章文献中没有。

## 争议与开放问题

并列的证据与分歧：

- **基础模型与线性基线。** Cui et al. (2024) 展示预训练生成式模型可微调用于扰动预测，Ahlmann-Eltze et al. (2025) 却显示多种方法不优于线性基线；两者任务设置不同，对膜相关表型谁更准，无人检验。
- **预测是证据还是假设。** Neuman et al. (2022) 以预测统一超家族，Terwilliger et al. (2024) 强调预测不能替代实验。Toulmay et al. (2022) 示范的是预测在先、遗传学在后的次序。
- **泄漏与可重复性。** Kapoor et al. (2023)、Walsh et al. (2021) 的 DOME 建议、Laine et al. (2021) 与 Greener et al. (2022) 反复强调划分与报告。酵母同一菌株的细胞共享遗传背景、培养板与批次，若按细胞随机划分训练集与测试集，泛化会被高估；这是对上述论述的应用性推论，不是它们对酵母数据的实测。
- **自监督与监督。** Lu et al. (2019) 与 Razdaibiedina et al. (2024) 各自报告优于既有方法，但本章文献中没有统一基准把它们放在同一把尺子上。

开放问题：

1. AF2/AF3 对膜蛋白与脂质结合态的可靠度如何评估？
2. 桥状蛋白的货物选择性、方向与速率，能否由结构预测加模拟定量推断？
3. 酵母定位分类器如何跨菌株、跨应激、跨成像平台泛化？
4. 自监督表征能否分辨同一细胞器内的膜域与接触位点亚群？
5. 机器学习粗粒化势能否在多组分脂质膜上保持热力学一致并可迁移？
6. 设计的膜蛋白在真实脂质组成的膜中如何验证插入与功能？
7. LLM 智能体在酵母湿实验闭环中的错误传播如何度量？

## 教科书写作建议

**配图**
1. 并排展示 Vps13、Atg2、Csf1 等 RBG 成员的预测骨架，沿沟槽着色疏水性并叠加 pLDDT，标出可信与不可信的区段。
2. 训练/测试划分示意：按细胞随机划分与按菌株、板划分两种方案，标出同一菌株细胞跨集合的泄漏路径（示意图，不冒充实测数据）。
3. 力匹配三联图：全原子轨迹、粗粒化映射、学得的自由能面。

**专栏**
1. “Adam 与 Eve”：机器人科学家做了什么、没做什么（King et al., 2009；Williams et al., 2015）。
2. “同名不同物”：图像的 DeepLoc 与序列的 DeepLoc。
3. “为什么能设计膜蛋白的可溶性类似物”（Goverde et al., 2024）。

**公式框**
1. 掩码语言模型与 Potts 条件分布。
2. 力匹配与平均力势。
3. Shapley 值与高斯过程下的信息增益。

**习题**
1. 推导 Potts 模型的条件分布是 softmax，并比较其参数个数与一个小型 Transformer。
2. 求解 $\dot\Delta=J-k_s\Delta$，讨论 $k_s\ll J/N$ 时膜会如何响应。
3. 给定一套酵母单细胞图像数据，列出三种泄漏路径并设计检测方法。

## 与其他章的连接

- [[D02_结构计算与AlphaFold时代]]：AF2/AF3 的架构与置信度，本章只取发现案例。
- [[D03_显微图像分析与深度学习]]：分割与自监督表征的方法细节。
- [[D01_分子动力学模拟]]：力匹配与粗粒化的物理基础。
- [[D04_组学数据科学]]、[[D05_整细胞建模与空间模拟]]：遗传相互作用网络、DCell 与整细胞模型的对照。
- [[A14_膜接触位点与脂质转运蛋白]]、[[A13_自噬体膜]]：RBG 超家族、Atg2 与桥状转运。
- [[A11_过氧化物酶体膜]]、[[E03_合成生物学与工程]]：机器学习增强的过氧化物酶体区室化。
- [[A18_方法学]]：高内涵筛选与冷冻电子断层的实验侧。
- [[B01_膜弹性曲率与形状能量]]、[[C06_信息优化与设计原理]]：面积差弹性与信息增益。
- [[E04_科学史与哲学视角]]：机器人科学家与“自动化科学”的哲学争论。

## 本章文献表

共 90 篇，全部经 CrossRef 核验 DOI 与题名；按重要性、年份降序。

| # | 引用 | 类型 | 重要性 | 一句话发现 | DOI |
|---|---|---|---|---|---|
| 1 | Abramson et al., 2024, *Nature* | method | 5 | AlphaFold 3 以扩散模块统一预测蛋白、核酸、小分子与离子等复合物结构，对蛋白–配体等相互作用的精度明显超过此前专用方法。 | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) |
| 2 | Goverde et al., 2024, *Nature* | method | 5 | 用稳健的深度学习流程设计复杂折叠及整合膜蛋白（含 GPCR 拓扑）的可溶性类似物，设计具有高热稳定性并经实验验证。 | [10.1038/s41586-024-07601-y](https://doi.org/10.1038/s41586-024-07601-y) |
| 3 | M. et al., 2024, *Nature Machine Intelligence* | method | 5 | ChemCrow 为大语言模型接入多种化学工具，可完成合成规划与分子设计任务。 | [10.1038/s42256-024-00832-8](https://doi.org/10.1038/s42256-024-00832-8) |
| 4 | Lin et al., 2023, *Science* | method | 5 | ESM-2 语言模型仅凭单条序列即可预测原子级结构，ESMFold 速度远快于依赖多序列比对的方法。 | [10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574) |
| 5 | Watson et al., 2023, *Nature* | method | 5 | RFdiffusion 把 RoseTTAFold 微调为去噪扩散模型，可从头生成蛋白骨架，用于单体、结合体、对称组装和功能位点支架设计，并经实验验证。 | [10.1038/s41586-023-06415-8](https://doi.org/10.1038/s41586-023-06415-8) |
| 6 | Wang et al., 2023, *Nature* | review | 5 | 综述 AI 在假设生成、实验设计、数据解析与自动化闭环发现中的角色与挑战。 | [10.1038/s41586-023-06221-2](https://doi.org/10.1038/s41586-023-06221-2) |
| 7 | Boiko et al., 2023, *Nature* | primary | 5 | Coscientist 以 GPT-4 为核心，结合文档检索、代码执行与自动化实验平台，自主规划并完成化学合成任务。 | [10.1038/s41586-023-06792-0](https://doi.org/10.1038/s41586-023-06792-0) |
| 8 | de et al., 2023, *Nature Methods* | method | 5 | 以 20 个裂殖酵母断层图（标注核糖体、脂肪酸合酶、膜、核孔复合体、细胞器等）训练并基准测试 DeePiCt，用于监督分割与大分子定位。 | [10.1038/s41592-022-01746-2](https://doi.org/10.1038/s41592-022-01746-2) |
| 9 | Neuman et al., 2022, *Trends in Cell Biology* | review | 5 | 结合 AF2 结构预测与序列分析，提出 VPS13、ATG2、SHIP164、Tweek 等含重复 β-groove 的蛋白构成“桥状”脂质转运蛋白新超家族。 | [10.1016/j.tcb.2022.03.011](https://doi.org/10.1016/j.tcb.2022.03.011) |
| 10 | Ingólfsson et al., 2022, *Proceedings of the National Academy of Sciences* | computational | 5 | 提出以机器学习桥接尺度的多尺度模拟框架，研究 RAS 在含异质脂质的质膜上的脂质依赖性动力学。 | [10.1073/pnas.2113297119](https://doi.org/10.1073/pnas.2113297119) |
| 11 | Kobayashi et al., 2022, *Nature Methods* | method | 5 | cytoself 以自监督学习仅从蛋白定位图像学习表征，无需标签即可区分细胞器及其更精细的定位差异。 | [10.1038/s41592-022-01541-z](https://doi.org/10.1038/s41592-022-01541-z) |
| 12 | Dauparas et al., 2022, *Science* | method | 5 | ProteinMPNN 基于消息传递神经网络为给定骨架设计序列，序列恢复率高于 Rosetta，并挽救了此前失败的设计。 | [10.1126/science.add2187](https://doi.org/10.1126/science.add2187) |
| 13 | Jumper et al., 2021, *Nature* | method | 5 | AlphaFold2 以 Evoformer 与结构模块端到端预测蛋白三维结构，在 CASP14 中达到接近实验的精度。 | [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) |
| 14 | Rives et al., 2021, *Proceedings of the National Academy of Sciences* | method | 5 | 在 2.5 亿条序列上以掩码语言建模训练的 Transformer，其表征自发编码了氨基酸理化性质、同源关系和结构信息。 | [10.1073/pnas.2016239118](https://doi.org/10.1073/pnas.2016239118) |
| 15 | Humphreys et al., 2021, *Science* | computational | 5 | 结合蛋白质组范围的氨基酸共进化分析与深度学习结构建模（RoseTTAFold 与 AlphaFold），在酵母蛋白质组内系统识别并构建核心真核蛋白复合物的模型。 | [10.1126/science.abm4805](https://doi.org/10.1126/science.abm4805) |
| 16 | Stringer et al., 2021, *Nature Methods* | method | 5 | Cellpose 在多样化细胞图像上训练，通过预测空间梯度流场做实例分割，可跨细胞类型与成像模态使用。 | [10.1038/s41592-020-01018-x](https://doi.org/10.1038/s41592-020-01018-x) |
| 17 | Heinrich et al., 2021, *Nature* | primary | 5 | 在多种细胞类型的 FIB-SEM 体积中标注多达 35 类细胞器，并训练深度网络自动分割，建立全细胞细胞器分割资源。 | [10.1038/s41586-021-03977-3](https://doi.org/10.1038/s41586-021-03977-3) |
| 18 | Noé et al., 2020, *Annual Review of Physical Chemistry* | review | 5 | 综述机器学习在分子模拟中的应用，包括学习力场、粗粒化、增强采样与动力学模型。 | [10.1146/annurev-physchem-042018-052331](https://doi.org/10.1146/annurev-physchem-042018-052331) |
| 19 | Lu et al., 2019, *PLOS Computational Biology* | method | 5 | 提出“配对细胞补绘”自监督任务，从酵母单细胞图像无监督学习特征，其表征在定位分类与聚类上优于传统特征。 | [10.1371/journal.pcbi.1007348](https://doi.org/10.1371/journal.pcbi.1007348) |
| 20 | Wang et al., 2019, *ACS Central Science* | method | 5 | 提出用神经网络学习粗粒化力场（CGnets），使粗粒化模型能再现全原子自由能面。 | [10.1021/acscentsci.8b00913](https://doi.org/10.1021/acscentsci.8b00913) |
| 21 | Kraus et al., 2017, *Molecular Systems Biology* | method | 5 | 用深度卷积神经网络（DeepLoc）直接从原始图像对酵母蛋白亚细胞定位分类，优于传统特征加分类器方法。 | [10.15252/msb.20177551](https://doi.org/10.15252/msb.20177551) |
| 22 | Costanzo et al., 2016, *Science* | primary | 5 | 构建覆盖酵母绝大多数基因的全局遗传相互作用网络，揭示由功能模块构成的层级结构。 | [10.1126/science.aaf1420](https://doi.org/10.1126/science.aaf1420) |
| 23 | Naik et al., 2016, *eLife* | method | 5 | 用主动机器学习迭代选择少量实验，在不做完全部实验的情况下学习化合物对多种蛋白亚细胞分布图案的影响。 | [10.7554/elife.10047](https://doi.org/10.7554/elife.10047) |
| 24 | Chong et al., 2015, *Cell* | primary | 5 | 将自动化遗传学、高通量显微与计算特征分析结合，在蛋白质组尺度测量酵母 GFP 融合蛋白的丰度与定位，并用二元分类器集成从单细胞数据生成定位注释。 | [10.1016/j.cell.2015.04.051](https://doi.org/10.1016/j.cell.2015.04.051) |
| 25 | Williams et al., 2015, *Journal of The Royal Society Interface* | primary | 5 | 机器人科学家 Eve 通过定量构效关系学习与测试的循环整合并自动化文库筛选，并以计量经济学分析表明 AI 选药优于常规筛选； | [10.1098/rsif.2014.1289](https://doi.org/10.1098/rsif.2014.1289) |
| 26 | Kemmeren et al., 2014, *Cell* | primary | 5 | 对约四分之一酵母基因（重点为推定调控因子）的缺失株做全基因组表达谱，扰动特征反映复合物与通路架构，并揭示大量基因特异性抑制子。 | [10.1016/j.cell.2014.02.054](https://doi.org/10.1016/j.cell.2014.02.054) |
| 27 | King et al., 2009, *Science* | primary | 5 | 机器人科学家 Adam 自主提出并实验检验关于酵母孤儿酶编码基因的假设，其结论经独立实验证实。 | [10.1126/science.1165620](https://doi.org/10.1126/science.1165620) |
| 28 | King et al., 2004, *Nature* | primary | 5 | 描述一个物理实现的机器人系统：能自动提出解释观测的假设、设计并执行检验实验，用于酵母功能基因组学研究。 | [10.1038/nature02236](https://doi.org/10.1038/nature02236) |
| 29 | Huh et al., 2003, *Nature* | primary | 5 | 对出芽酵母大部分蛋白的 GFP 融合库做荧光显微定位，给出约四千个蛋白的亚细胞定位图谱。 | [10.1038/nature02026](https://doi.org/10.1038/nature02026) |
| 30 | Lamm et al., 2026, *Nature Methods* | method | 4 | MemBrain v2 提供冷冻电子断层图中膜的分割、膜蛋白定位与方向分析的端到端流程。 | [10.1038/s41592-026-03178-8](https://doi.org/10.1038/s41592-026-03178-8) |
| 31 | Baker et al., 2025, *Nature Chemical Biology* | primary | 4 | 通过机器学习流程筛选需过表达的因子，使酵母过氧化物酶体功能容量比野生型提高 137%，多酶途径区室化使香叶醇产量提高 80%（最高 9.5 g/L）。 | [10.1038/s41589-024-01759-2](https://doi.org/10.1038/s41589-024-01759-2) |
| 32 | Swanson et al., 2025, *Nature* | primary | 4 | 由多个 LLM 智能体组成的“虚拟实验室”与人类研究者协作设计纳米抗体并经实验验证。 | [10.1038/s41586-025-09442-9](https://doi.org/10.1038/s41586-025-09442-9) |
| 33 | Ahlmann-Eltze et al., 2025, *Nature Methods* | primary | 4 | 多个深度学习与基础模型的基因扰动效应预测方法并未优于简单线性基线。 | [10.1038/s41592-025-02772-6](https://doi.org/10.1038/s41592-025-02772-6) |
| 34 | Stringer et al., 2025, *Nature Methods* | method | 4 | Cellpose3 集成去噪、去模糊与上采样的图像恢复，改善噪声或低分辨率图像中的分割。 | [10.1038/s41592-025-02595-5](https://doi.org/10.1038/s41592-025-02595-5) |
| 35 | Archit et al., 2025, *Nature Methods* | method | 4 | µSAM 在大规模显微数据上微调 Segment Anything，提供光镜与电镜的通用分割与跟踪工具。 | [10.1038/s41592-024-02580-4](https://doi.org/10.1038/s41592-024-02580-4) |
| 36 | van et al., 2024, *Nature Biotechnology* | method | 4 | Foldseek 把三维结构编码为结构字母表后做序列式搜索，速度比传统结构比对快数个数量级且保持较高灵敏度。 | [10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) |
| 37 | Terwilliger et al., 2024, *Nature Methods* | perspective | 4 | 将 AF2 预测与实验电子密度图对比，指出预测可作为有价值的假设，但局部细节与构象状态仍可能与实验不符。 | [10.1038/s41592-023-02087-4](https://doi.org/10.1038/s41592-023-02087-4) |
| 38 | Razdaibiedina et al., 2024, *Molecular Systems Biology* | method | 4 | 对酵母 ORF-GFP 库成像，用自监督方法从单细胞图像生成蛋白特征谱，在分子表征学习上优于已有方法，并可聚类出功能层级、区分多定位蛋白、识别功能模块。 | [10.1038/s44320-024-00029-6](https://doi.org/10.1038/s44320-024-00029-6) |
| 39 | Zheng et al., 2024, *Nature Machine Intelligence* | method | 4 | Distributional Graphormer 用扩散模型直接预测分子体系的平衡分布，可生成蛋白多构象。 | [10.1038/s42256-024-00837-3](https://doi.org/10.1038/s42256-024-00837-3) |
| 40 | Cui et al., 2024, *Nature Methods* | method | 4 | scGPT 是在大规模单细胞数据上预训练的生成式 Transformer，可微调用于细胞类型注释与扰动预测等任务。 | [10.1038/s41592-024-02201-0](https://doi.org/10.1038/s41592-024-02201-0) |
| 41 | Michaelis et al., 2023, *Nature* | primary | 4 | 用高灵敏度高通量亲和富集质谱对 GFP 标记的酵母文库做 4159 次 pull-down，得到含 3927 个蛋白、31004 个互作的网络，使蛋白数翻倍、可靠互作增至约三倍。 | [10.1038/s41586-023-06739-5](https://doi.org/10.1038/s41586-023-06739-5) |
| 42 | Levental et al., 2023, *Nature Reviews Molecular Cell Biology* | review | 4 | 综述脂质纳米环境（邻近脂质与整体膜性质）调控膜蛋白结构与功能的机制及证据。 | [10.1038/s41580-022-00524-4](https://doi.org/10.1038/s41580-022-00524-4) |
| 43 | Majewski et al., 2023, *Nature Communications* | method | 4 | 训练出可跨序列迁移的粗粒化蛋白神经网络势，能再现多种蛋白的折叠热力学。 | [10.1038/s41467-023-41343-1](https://doi.org/10.1038/s41467-023-41343-1) |
| 44 | Szklarczyk et al., 2023, *Nucleic Acids Research* | method | 4 | STRING 提供整合实验、共表达与文本挖掘证据的蛋白关联网络，并支持功能富集分析。 | [10.1093/nar/gkac1000](https://doi.org/10.1093/nar/gkac1000) |
| 45 | Wong et al., 2023, *GENETICS* | method | 4 | SGD 是酵母基因组与功能注释的权威数据库，该更新介绍了服务器架构、泛基因组命名与外部资源整合。 | [10.1093/genetics/iyac191](https://doi.org/10.1093/genetics/iyac191) |
| 46 | Rice et al., 2023, *Nature Methods* | method | 4 | TomoTwin 用度量学习在嵌入空间定位断层图中的大分子，无需针对每种蛋白重新训练。 | [10.1038/s41592-023-01878-z](https://doi.org/10.1038/s41592-023-01878-z) |
| 47 | Wozny et al., 2023, *Nature* | primary | 4 | 在酵母细胞内解析 ERMES 的分子组织，为内质网–线粒体接触位点的脂质转移机制提供原位结构依据。 | [10.1038/s41586-023-06050-3](https://doi.org/10.1038/s41586-023-06050-3) |
| 48 | Kapoor et al., 2023, *Patterns* | review | 4 | 系统梳理多个领域基于机器学习的研究中的数据泄漏问题，并提出模型信息表以提高可复现性。 | [10.1016/j.patter.2023.100804](https://doi.org/10.1016/j.patter.2023.100804) |
| 49 | Levine et al., 2022, *Contact* | review | 4 | 用序列分析与结构预测系统比较 RBG 超家族各成员的结构域组成，揭示 VPS13、ATG2、SHIP164、Hob、Tweek 在形态、功能与互作上的差异。 | [10.1177/25152564221134328](https://doi.org/10.1177/25152564221134328) |
| 50 | Toulmay et al., 2022, *Journal of Cell Biology* | primary | 4 | 酵母中高效的 GPI 锚合成依赖 Csf1，缺失者积累缺少磷酸乙醇胺的 GPI 前体； | [10.1083/jcb.202111095](https://doi.org/10.1083/jcb.202111095) |
| 51 | Castro et al., 2022, *eLife* | primary | 4 | 用六种接触位点分裂荧光报告子对 1165 个酵母菌株做共定位成像筛选，发现超过 100 个潜在接触位点驻留蛋白或效应因子，并鉴定出 Vps13 与 Atg2 的三个同源物驻留于多个接触位点。 | [10.7554/elife.74602](https://doi.org/10.7554/elife.74602) |
| 52 | Pachitariu et al., 2022, *Nature Methods* | method | 4 | Cellpose 2.0 支持人在回路微调，让用户用少量标注图像在预训练模型基础上训练自定义模型。 | [10.1038/s41592-022-01663-4](https://doi.org/10.1038/s41592-022-01663-4) |
| 53 | Greener et al., 2022, *Nature Reviews Molecular Cell Biology* | review | 4 | 面向生物学家介绍机器学习方法、评估与常见陷阱。 | [10.1038/s41580-021-00407-0](https://doi.org/10.1038/s41580-021-00407-0) |
| 54 | Thumuluri et al., 2022, *Nucleic Acids Research* | method | 4 | DeepLoc 2.0 基于蛋白语言模型做多标签亚细胞定位预测，并用注意力指示分选信号。 | [10.1093/nar/gkac278](https://doi.org/10.1093/nar/gkac278) |
| 55 | Teufel et al., 2022, *Nature Biotechnology* | method | 4 | SignalP 6.0 用蛋白语言模型预测五类信号肽及切割位点。 | [10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3) |
| 56 | Hallgren et al., 2022, *openRxiv* | preprint | 4 | DeepTMHMM 用蛋白语言模型预测 α 螺旋与 β 桶跨膜蛋白的拓扑和信号肽。 | [10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609) |
| 57 | Baek et al., 2021, *Science* | method | 4 | RoseTTAFold 用序列、距离与三维坐标三轨网络联合推理，精度接近 AlphaFold2，并可直接建模蛋白复合物。 | [10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754) |
| 58 | Reinisch et al., 2021, *Journal of Cell Biology* | review | 4 | 综述非囊泡脂质运输机制，涵盖穿梭型转运蛋白及 VPS13/ATG2 等桥状蛋白如何在接触位点转移脂质。 | [10.1083/jcb.202012058](https://doi.org/10.1083/jcb.202012058) |
| 59 | Ghanbarpour et al., 2021, *Proceedings of the National Academy of Sciences* | theory | 4 | 提出桥状脂质转运蛋白与脂质翻转酶（scramblase）协作的模型：转运蛋白把脂质输入受体膜的一侧，翻转酶使两叶平衡，从而支持膜扩张与细胞器生成。 | [10.1073/pnas.2101562118](https://doi.org/10.1073/pnas.2101562118) |
| 60 | Unke et al., 2021, *Chemical Reviews* | review | 4 | 综述机器学习力场的构建方法、对称性要求与适用边界。 | [10.1021/acs.chemrev.0c01111](https://doi.org/10.1021/acs.chemrev.0c01111) |
| 61 | Vorobieva et al., 2021, *Science* | method | 4 | 设计跨膜 β 桶蛋白，结构与设计一致，并可在脂质环境中折叠。 | [10.1126/science.abc8182](https://doi.org/10.1126/science.abc8182) |
| 62 | Moebel et al., 2021, *Nature Methods* | method | 4 | DeepFinder 用三维卷积神经网络在冷冻电子断层图中定位并分类多类大分子，比模板匹配更快。 | [10.1038/s41592-021-01275-4](https://doi.org/10.1038/s41592-021-01275-4) |
| 63 | Walsh et al., 2021, *Nature Methods* | perspective | 4 | 提出生物学监督式机器学习验证与报告的最低建议，涵盖数据、优化、模型与评估。 | [10.1038/s41592-021-01205-4](https://doi.org/10.1038/s41592-021-01205-4) |
| 64 | Laine et al., 2021, *Nature Methods* | perspective | 4 | 讨论深度学习生物图像分析中可复现性的风险，并给出数据、验证与报告方面的指引。 | [10.1038/s41592-021-01284-3](https://doi.org/10.1038/s41592-021-01284-3) |
| 65 | Tsugawa et al., 2020, *Nature Biotechnology* | method | 4 | MS-DIAL 4 整合 MS/MS 谱库、碰撞截面与保留时间，建立脂质组图谱，实现对大量脂质亚类的自动注释。 | [10.1038/s41587-020-0531-2](https://doi.org/10.1038/s41587-020-0531-2) |
| 66 | Mattiazzi et al., 2020, *Molecular Systems Biology* | primary | 4 | 结合自动化酵母遗传学、高内涵筛选与基于神经网络的单细胞图像分析，以内吞通路四个亚细胞区室的形态为模型，评估细胞间表型变异。 | [10.15252/msb.20199243](https://doi.org/10.15252/msb.20199243) |
| 67 | Xu et al., 2020, *Nature* | method | 4 | 从头设计跨膜孔蛋白，并用电生理与结构实验验证其孔道特性。 | [10.1038/s41586-020-2646-5](https://doi.org/10.1038/s41586-020-2646-5) |
| 68 | Zhang et al., 2020, *Nature Communications* | primary | 4 | 把基因组规模代谢模型与机器学习结合，预测并优化酵母色氨酸代谢工程菌株。 | [10.1038/s41467-020-17910-1](https://doi.org/10.1038/s41467-020-17910-1) |
| 69 | Lee et al., 2020, *Bioinformatics* | method | 4 | 在 PubMed 摘要与 PMC 全文上继续预训练的 BERT，使生物医学命名实体识别、关系抽取与问答任务显著优于通用 BERT。 | [10.1093/bioinformatics/btz682](https://doi.org/10.1093/bioinformatics/btz682) |
| 70 | Lundberg et al., 2020, *Nature Machine Intelligence* | method | 4 | TreeExplainer 为树模型提供精确的 SHAP 值计算，支持局部与全局解释及交互效应分析。 | [10.1038/s42256-019-0138-9](https://doi.org/10.1038/s42256-019-0138-9) |
| 71 | Wong et al., 2019, *Nature Reviews Molecular Cell Biology* | review | 4 | 综述脂质转运蛋白以穿梭、桥与管三种方式在膜间转运脂质的结构与机制。 | [10.1038/s41580-018-0071-5](https://doi.org/10.1038/s41580-018-0071-5) |
| 72 | Noé et al., 2019, *Science* | method | 4 | Boltzmann 生成器用可逆神经网络把简单分布映射到平衡态分布，实现无需长时间模拟的构象采样。 | [10.1126/science.aaw1147](https://doi.org/10.1126/science.aaw1147) |
| 73 | Tshitoyan et al., 2019, *Nature* | primary | 4 | 对材料科学摘要无监督训练词嵌入，其向量编码了隐含知识，并能预测尚未被报道的功能材料。 | [10.1038/s41586-019-1335-8](https://doi.org/10.1038/s41586-019-1335-8) |
| 74 | Moen et al., 2019, *Nature Methods* | review | 4 | 综述深度学习在细胞图像分类、分割与追踪中的应用、数据需求与局限。 | [10.1038/s41592-019-0403-1](https://doi.org/10.1038/s41592-019-0403-1) |
| 75 | Kumar et al., 2018, *Journal of Cell Biology* | primary | 4 | VPS13A 与 VPS13C 在体外能在膜间转运多种磷脂，并分别定位于 ER 与线粒体/脂滴及 ER 与溶酶体等接触位点。 | [10.1083/jcb.201807019](https://doi.org/10.1083/jcb.201807019) |
| 76 | Corradi et al., 2018, *ACS Central Science* | computational | 4 | 对嵌入模型质膜的 10 种膜蛋白做分子动力学模拟，发现每种膜蛋白周围都有独特的脂质环境“指纹”。 | [10.1021/acscentsci.8b00143](https://doi.org/10.1021/acscentsci.8b00143) |
| 77 | Lu et al., 2018, *eLife* | primary | 4 | 提出可扩展方法整合多个扰动下的酵母蛋白定位筛选，区分针对特定扰动的响应与更普遍的响应程序。 | [10.7554/elife.31872](https://doi.org/10.7554/elife.31872) |
| 78 | Ma et al., 2018, *Nature Methods* | method | 4 | 可见神经网络 DCell 嵌入 2526 个细胞子系统的层级结构，在数百万基因型上训练以模拟酵母生长，并可解释各子系统的贡献。 | [10.1038/nmeth.4627](https://doi.org/10.1038/nmeth.4627) |
| 79 | Lu et al., 2018, *Science* | method | 4 | 从头设计多次跨膜蛋白，晶体结构与设计模型高度一致。 | [10.1126/science.aaq1739](https://doi.org/10.1126/science.aaq1739) |
| 80 | Valm et al., 2017, *Nature* | primary | 4 | 用多光谱成像与五步成像信息学流程，在活细胞中同时标记多种细胞器，定量其数量、体积、速度、位置与动态接触，绘制细胞器互作组。 | [10.1038/nature22369](https://doi.org/10.1038/nature22369) |
| 81 | Pärnamaa et al., 2017, *G3 Genes／Genomes／Genetics* | method | 4 | 用 11 层神经网络对酵母 GFP 库图像做亚细胞定位分类，单细胞准确率达 91%。 | [10.1534/g3.116.033654](https://doi.org/10.1534/g3.116.033654) |
| 82 | Himmelstein et al., 2017, *eLife* | method | 4 | 构建整合多个公共资源的异构知识网络 Hetionet，并用其预测药物重定位。 | [10.7554/elife.26726](https://doi.org/10.7554/elife.26726) |
| 83 | Almagro et al., 2017, *Bioinformatics* | method | 4 | DeepLoc 用循环神经网络与注意力机制从序列预测亚细胞定位类别及膜结合状态，无需手工特征。 | [10.1093/bioinformatics/btx431](https://doi.org/10.1093/bioinformatics/btx431) |
| 84 | Meinshausen et al., 2016, *Proceedings of the National Academy of Sciences* | method | 4 | 给出基于不变性原理的因果预测方法（ICP）的软件，并用酵母基因扰动数据检验其可靠性。 | [10.1073/pnas.1510493113](https://doi.org/10.1073/pnas.1510493113) |
| 85 | Klose et al., 2012, *PLoS ONE* | primary | 4 | 量化不同生长条件和温度下的酵母脂质组，显示脂质组有较大可塑性。 | [10.1371/journal.pone.0035063](https://doi.org/10.1371/journal.pone.0035063) |
| 86 | Ejsing et al., 2009, *Proceedings of the National Academy of Sciences* | primary | 4 | 用定量鸟枪法质谱对酵母脂质组做全局定量，给出各类脂质分子种的含量基准。 | [10.1073/pnas.0811700106](https://doi.org/10.1073/pnas.0811700106) |
| 87 | Ohya et al., 2005, *Proceedings of the National Academy of Sciences* | primary | 4 | 用高维形态参数对大量酵母基因缺失突变株做大规模表型分析，建立基因功能与形态的关联。 | [10.1073/pnas.0509436102](https://doi.org/10.1073/pnas.0509436102) |
| 88 | Katuwawala et al., 2021, *Bioinformatics* | method | 3 | 提出基于序列的深度学习预测器 DisoLipPred，用于预测蛋白中无序脂质结合残基。 | [10.1093/bioinformatics/btab640](https://doi.org/10.1093/bioinformatics/btab640) |
| 89 | Poss et al., 2020, *Journal of Clinical Investigation* | primary | 3 | 用机器学习分析血清脂质组，发现鞘脂可作为独立于胆固醇的冠心病风险生物标志物。 | [10.1172/jci131838](https://doi.org/10.1172/jci131838) |
| 90 | Dietler et al., 2020, *Nature Communications* | method | 3 | 卷积神经网络（YeaZ）可在多种成像条件下准确分割酵母明场图像，并配套追踪工具。 | [10.1038/s41467-020-19557-4](https://doi.org/10.1038/s41467-020-19557-4) |
