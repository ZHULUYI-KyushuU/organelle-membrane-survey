---
title: "D02 结构计算与AlphaFold时代"
chapter_id: D02
part: D
n_papers: 93
tags: [细胞器膜, 酵母, 文献调研, part-D]
created: 2026-10-13
---

# D02 结构计算与AlphaFold时代

**核心判断：AlphaFold 让“这个蛋白大致长什么样”不再稀缺，细胞器膜研究真正稀缺的是膜环境、构象状态和原位组装；预测擅长提出假说（桥式脂质转运蛋白即是一例），检验与定量仍要靠冷冻电镜/断层成像、整合建模和物理模拟。**

本章要讲清楚什么：膜蛋白结构计算的工具链（共进化与深度学习预测、跨膜拓扑与膜内取向、冷冻电镜/断层成像重构、整合建模、从头设计与脂质位点预测）背后的数学假设，它们为酵母细胞器膜研究做了什么，以及预测“看起来对”与“物理上对”之间的差距。

## 预测方法与酵母蛋白质组的结构化

结构预测起于一个统计物理问题：同源序列的多序列比对（multiple sequence alignment, MSA）里，空间接触的残基会协同突变。Hopf et al., 2012 用最大熵的 Potts 模型提取残基对耦合，并据此从头折叠出多个跨膜蛋白。AlphaFold2 把这条思路换成端到端学习：Evoformer 交换 MSA 与残基对信息，等变结构模块输出坐标，并给出逐残基 pLDDT 与成对 PAE（Jumper et al., 2021）；RoseTTAFold 以三轨网络达到相近精度（Baek et al., 2021），ColabFold 用 MMseqs2 替代耗时的比对检索（Mirdita et al., 2022）。复合物预测靠配对 MSA 与界面评分 ipTM（Evans et al., 2021）；AlphaFold 3 改用 Pairformer 加扩散生成，可联合预测蛋白、核酸与配体（Abramson et al., 2024）。蛋白语言模型绕开比对：掩码训练的表示自发编码接触信息（Rives et al., 2021），ESMFold 据此直接折叠，速度比 AF2 快约一个数量级（Lin et al., 2023）；ProtTrans 的嵌入可直接用于定位与膜结合预测（Elnaggar et al., 2022），ESM3 则把序列、结构与功能放进同一个生成模型（Hayes et al., 2025）。

酵母的蛋白质组已被系统“结构化”：AFDB 收录包括酿酒酵母（*Saccharomyces cerevisiae*）在内的模式生物模型（Varadi et al., 2022），Foldseek 可在海量模型中检索结构相似者（van et al., 2024）。Humphreys et al., 2021 对约 830 万对酵母蛋白做共进化加深度学习的两级筛查，给出 1500 余个可能复合物，并为其中 106 个此前未知的组装给出结构模型；Michaelis et al., 2023 先用亲和纯化-质谱建立互作组，再以 AlphaFold-Multimer 为互作对建模。人类蛋白质组中约 58% 的残基获得可信预测，低 pLDDT 区与内在无序区高度重合（Tunyasuvunakool et al., 2021）。细胞器膜蛋白里也有这类区域，例如 Atg9 的无序 N 端，它靠保守的短序列与 Atg23 结合（Bekkhozhin et al., 2026）；对这类区域，预测不能当作结构来读。

## 膜蛋白的特殊难题：拓扑、取向与预测盲区

跨膜螺旋预测有三代方法。第一代是物理直觉：Kyte-Doolittle 疏水性标度配约 19 残基的滑动窗口（Kyte et al., 1982），再加“正电荷在内”规则，成为 TOPPRED（von et al., 1992）。其物理依据由 Hessa et al., 2005 量化：用系统设计的测试片段测得 Sec61 通道插入的表观自由能，得到随位置变化的生物学疏水性标度。第二代是概率语法：TMHMM 把螺旋、环与帽区写成隐马尔可夫模型（HMM），对跨膜螺旋的预测正确率为 97–98%，并估计 20–30% 的基因编码膜蛋白（Krogh et al., 2001）；Phobius 联合建模信号肽（Käll et al., 2004），TOPCONS 做多预测器共识（Tsirigos et al., 2015）。第三代是语言模型嵌入加条件随机场解码，DeepTMHMM 同时覆盖 α 螺旋与 β 桶（Hallgren et al., 2022）。酵母还有实验标尺：617 个膜蛋白的 C 端报告蛋白融合给出了全局拓扑图（Kim et al., 2006）。

取向问题交给膜嵌入工具：OPM/PPM 在各向异性溶剂模型中最小化转移自由能，给出疏水厚度、倾角与插入深度（Lomize et al., 2012）；MemProtMD 让蛋白在粗粒化模拟中自组装进显式脂双层（Stansfeld et al., 2015；Newport et al., 2019）。AF2 本身不含膜：跨膜区整体可信，但螺旋位置、寡聚态与构象可能出错（Hegedűs et al., 2022），TmAlphaFold 因此为 AFDB 模型计算膜位置并分级（Dobson et al., 2023）。构象单一是另一个盲区：降低 MSA 深度可让 AF2 对转运蛋白与受体采样多种状态，部分与实验构象一致（del et al., 2022）。

## 桥式脂质转运蛋白：预测先行

脂质转运蛋白的经典形象是“穿梭者”：包住一两个脂质分子，在两膜之间往返。桥式蛋白改写了这幅图景。Osawa et al., 2019 解析酵母 Atg2 的 N 端结构，发现疏水凹槽，并在体外证明其可在膜间转运磷脂；Li et al., 2020 对嗜热真菌（*Chaetomium thermophilum*）Vps13 的 N 端片段做冷冻电镜，看到约 160 Å 长、内衬疏水残基的通道，并提出全长蛋白是连接两膜的约 20 nm 桥。两个独立体系里的长疏水槽先后到位，把它们连成一个家族的是预测：Neuman et al., 2022（综述）依据 AlphaFold 预测指出 VPS13、ATG2、SHIP164、Hob/Fmp27、Csf1/Tweek 具有相同的重复 β 槽（repeating beta groove, RBG），构成一个超家族；Levine et al., 2022 用远缘同源检索加预测比较各成员的结构域组成，提示沿桥体分布的保守残基可能是未知伴侣的结合位点；Hanna et al., 2023 综述了其结构、适配蛋白、与翻转酶的偶联及疾病关联。

酵母中的功能验证接踵而来：Csf1 为内质网中 GPI 锚合成提供磷脂酰乙醇胺（Toulmay et al., 2022）；Hob 蛋白（酵母 Fmp27 与 Ypr117w 的同源物）定位于 ER–质膜接触位点，其 C 端可结合质膜磷脂酰肌醇（Neuman et al., 2022，Hob 蛋白）；Hoi1 把 BLTP2（Fmp27）靶向到接触位点，结构预测显示它与中央通道两侧的 α 螺旋突起相互作用，破坏该作用会改变甾醇稳态（Dziurdzik et al., 2026）。线虫（*Caenorhabditis elegans*）BLTP1 同源物 LPD-3 的天然复合物结构中，伴随蛋白 Spigot 结合于脂质入口端，通道内可见脂质密度（Kang et al., 2025）。

## 接触位点与自噬膜扩张：预测如何被检验

Atg2 的桥要持续供脂，需要翻转酶把脂质从胞质叶搬到内叶。酵母 Atg9 是同源三聚体，含垂直与水平通道并有翻转活性（Matoba et al., 2020），人 ATG9A 的结构与模拟给出一致结论（Maeda et al., 2020）。两者的耦合先由预测提出、再被结构确认：van et al., 2022 结合 AlphaFold-Multimer、交联质谱与突变，确定 ATG2A C 端与 ATG9A 的界面，提出两条通道对齐；Wang et al., 2025 的冷冻电镜结构显示二者通道在空间上相连。体内另有并行通路：Vps13 与 Atg2 同在扩张中的吞噬泡边缘转运磷脂，共同决定自噬体膜的扩张速率（Dabrowski et al., 2023）。预测也并非总对：Atg23 与 Atg9 的实验结构和预测在整体构架上存在差异（Bekkhozhin et al., 2026）。

ERMES 提供了从晶体到原位的完整链条：Mmm1–Mdm12 的 SMP 结构域形成连续疏水通道，体外可转运磷脂（Kawano et al., 2018）；原位冷冻断层成像加子断层平均显示 ERMES 是连接 ER 与线粒体外膜的桥状组装，AlphaFold 模型被拟合进密度（Wozny et al., 2023）。系链并不都是桥：Ist2 的 ER 跨膜区与 TMEM16 家族同源、有组成性翻转活性，且 Osh6 穿梭时仍与 Ist2 结合（Arndt et al., 2025）；核-液泡连接处的 Nvj3–Mdm1 形成 α 螺旋装配的容脂通道，不同于 β 槽桥（Aboumourad et al., 2026）。翻转也不限于专职酶：多种蛋白插入酶同样具有磷脂翻转活性（Li et al., 2024）。

## 冷冻电镜与断层成像的计算

“分辨率革命”使难结晶的膜蛋白也能单颗粒成像（Kühlbrandt et al., 2014），其先声是细菌视紫红质二维晶体的电子冷冻显微术（Henderson et al., 1990）。计算上，RELION 把重构写成经验贝叶斯下的最大后验问题，用期望最大化（EM）自动确定正则化参数（Scheres et al., 2012）；cryoSPARC 用随机梯度下降生成初始模型，用分支定界搜索取向（Punjani et al., 2017）；Warp 在采集时实时完成运动校正与颗粒挑选（Tegunov et al., 2019）。断层成像侧，IMOD 负责对齐、重建与膜轮廓建模（Kremer et al., 1996；Mastronarde et al., 2017），AreTomo 实现无基准点对齐（Zheng et al., 2022），RELION-4 把子断层平均写成对二维倾转图像的贝叶斯精修（Zivanov et al., 2022），IsoNet 用自监督网络补偿缺失楔（Liu et al., 2022），MemBrain 先分割膜再定位膜蛋白（Lamm et al., 2022）；全流程见 Young et al., 2023 的综述。

这些工具产出了酵母细胞器膜的原位定量数据：自噬体形成各阶段的膜曲率、膜间距与接触（Bieber et al., 2022）；ER–质膜接触处依赖 tricalbin 的高曲率 ER（Collado et al., 2019）和连接两膜的杆状密度（Hoffmann et al., 2019）；表面形态测量流程把断层分割变成网格上的膜间距、曲率与取向指标（Barad et al., 2023）。酵母 seipin 的跨膜区形成柔性笼（Arlt et al., 2022），果蝇 seipin 的管腔域是十一聚体环（Sui et al., 2018），Ldb16 另含三酰甘油结合位点（Klug et al., 2021）。结构也在改写功能图景：Tim17 形成侧向开放的通道，Mgr2 封闭其侧口（Sim et al., 2023）；Pex13 的 YG 结构域在过氧化物酶体膜上形成类似核孔 FG 重复的相（Gao et al., 2022）。

## 整合建模与酵母核孔

单一方法拿不到完整结构时，用整合结构建模：把多源数据转译为空间约束，经采样与评分得到模型集合（Russel et al., 2012）；其原则——数据、表示、评分、采样、验证与不确定性估计——由 Rout et al., 2019 总结。酿酒酵母核孔复合物（NPC）是标志性案例：Alber et al., 2007 以亲和纯化、沉降、免疫电镜等约束定位约 456 个核孔蛋白；Kim et al., 2018 综合交联质谱、冷冻电镜密度与 SAXS 等，用 IMP 构建 552 个蛋白的整个 NPC，揭示柔性连接与膜环的组织；Upla et al., 2017 以负染电镜加建模表明 16 个 Pom152 拷贝足以组成管腔侧的膜环。Akey et al., 2022 在亚纳米分辨率解析分离酵母 NPC 的内环，并提出管腔 Pom152 环限制孔扩张。原位侧，Allegretti et al., 2020 在裂殖酵母（*Schizosaccharomyces pombe*）细胞内用子断层平均获得 NPC 结构，并捕捉到 NPC 被双层膜结构包裹的降解中间态；Mosalaganti et al., 2022 把 AlphaFold 对核孔蛋白的预测与原位密度结合，建立约 90% 人类 NPC 支架的模型，预测结构由此成为整合建模的“零件库”。需要注意，IMP 输出的是满足约束的模型集合而非单一结构，精度由集合内的涨落估计，这与单颗粒重构用 FSC 衡量分辨率是两种不同的不确定性。

## 从头设计与脂质结合位点预测

膜蛋白设计从物理走向学习。Lu et al., 2018 用 Rosetta 设计出从单体到四聚体、每个亚基含二至四个跨膜区的螺旋束蛋白，晶体结构与模型高度一致，并可在大肠杆菌（*Escherichia coli*）与哺乳动物细胞膜中正确插入；Xu et al., 2020 设计了带水通道的跨膜孔，冷冻电镜结构与设计一致；Vorobieva et al., 2021 归纳出甘氨酸凸起、β 转角等 β 桶设计规则，得到可折叠插入脂膜的跨膜 β 桶，NMR 与晶体结构验证了设计。深度学习管线是 RFdiffusion 生成骨架（Watson et al., 2023）加 ProteinMPNN 设计序列（Dauparas et al., 2022），Kortemme et al., 2024 有综述；Goverde et al., 2024 反向操作，把跨膜折叠（GPCR、claudin）重设计成可溶类似物。本调研的卡片中，尚无在酵母细胞器膜内验证设计蛋白的例子。

脂质结合位点预测更难。粗粒化模拟显示每种膜蛋白周围有独特的脂质“指纹”（Corradi et al., 2018），PyLipID 用双截断距离识别结合事件、计算停留时间并以图论聚类找位点（Song et al., 2022）。AlphaFill 从同源实验结构把配体“移植”到 AF 模型（Hekkelman et al., 2023）；RoseTTAFold All-Atom 把蛋白与非蛋白原子统一表示，可预测含小分子的复合物并设计结合小分子的蛋白（Krishna et al., 2024）。但共折叠模型学到的是物理还是训练集，仍有疑问：对结合位点做对抗性突变后，AF3 与 RoseTTAFold All-Atom 仍倾向放置配体（Masters et al., 2025）；LiPP 基准则专门比较共折叠与对接对脂质的预测（Yang et al., 2026）。

## 定量与物理视角

本章每个方法都有可写出的数学骨架，酵母提供的是参数与基准：

- **共进化**：Potts 模型 $P(\sigma)=Z^{-1}\exp[\sum_i h_i(\sigma_i)+\sum_{i<j}J_{ij}(\sigma_i,\sigma_j)]$，耦合 $J_{ij}$ 由平均场或伪似然估计，用以区分直接接触与传递相关（Hopf et al., 2012）。比对的有效序列数 $N_{eff}$ 决定估计质量，酵母蛋白家族的 $N_{eff}$ 是可直接统计的量。
- **插入自由能**：$\Delta G_{app}=-RT\ln K_{app}$，310 K 时 $RT\approx0.62$ kcal/mol（Hessa et al., 2005）；$\Delta G_{app}=-2$ kcal/mol 对应 $K_{app}\approx26$、约 96% 的片段插入。PPM 最小化的转移自由能是其连续介质版本（Lomize et al., 2012）。
- **拓扑 HMM**：用 Viterbi 或前向-后向算法求状态路径后验（Krogh et al., 2001）；“正电荷在内”可被吸收为胞质侧与非胞质侧环区发射概率的差异。20 个残基的 α 螺旋（每残基上升 1.5 Å）约 30 Å，与疏水核心厚度同量级。
- **冷冻电镜**：傅里叶空间模型 $X_i=\mathrm{CTF}_i\,P_{\phi_i}V+N_i$，RELION 对未知取向 $\phi_i$ 边缘化并以 EM 迭代求 MAP（Scheres et al., 2012）；粒子数 $N$ 与分辨率 $d$ 近似 $1/d^2=(2/B)\ln N+c$（Rosenthal–Henderson）。倾转 ±60° 时缺失楔占角度范围的 1/3，IsoNet 即补偿它（Liu et al., 2022）。
- **整合建模**：$p(M|D)\propto p(D|M)\,p(M)$，评分 $S=-\ln p$，用蒙特卡洛/复制交换采样，模型集合的精度本身就是结论（Russel et al., 2012）。
- **扩散**：AF3 与 RFdiffusion 都学习去噪；RFdiffusion 对骨架平移加高斯噪声、取向在 SO(3) 上加噪（Watson et al., 2023）。
- **筛查统计**：Humphreys et al., 2021 的 830 万对中，即使假阳性率仅 $10^{-4}$（假设值）也有约 830 个假阳性，与最终 1500 余个预测同量级（示意计算，并非该文报告的假阳性率），可见多重检验控制不可省。
- **桥的输运估算**：一维扩散的渡越时间 $\tau\approx L^2/2D$；取 $L=20$ nm、$D=1\ \mu m^2/s$（假设为膜内侧向扩散量级），$\tau\approx0.2$ ms。若实测速率远低于此，限速步骤在脂质抽提与装载，而不在沟内扩散。
- **曲率**：Barad et al., 2023 的网格曲率可代入 Helfrich 能 $E=\int[\tfrac{\kappa}{2}(2H-C_0)^2+\kappa_G K]\,dA$，酵母断层给出 $H$ 与膜间距分布。

## 争议与开放问题

**膜环境**：Hegedűs et al., 2022 强调 AF2 不显式考虑膜、可能出错；Akdel et al., 2022 的社区评估逐项给出可用范围；del et al., 2022 的降 MSA 深度只证明部分采样构象与实验一致，并未解决“哪个构象在哪种脂质中占优”。**共折叠是物理还是记忆**：Abramson et al., 2024 报告蛋白-配体精度超过传统对接；Masters et al., 2025 发现位点被破坏后配体仍被放回原处，Yang et al., 2026 的 LiPP 基准则指出共折叠与对接在脂质-蛋白相互作用上都有内在不足。两种说法可以同时成立：基准上平均精度高，不等于对未见位点遵守物理。**桥与穿梭的边界**：RBG 超家族（Neuman et al., 2022；Levine et al., 2022）与 α 螺旋通道（Aboumourad et al., 2026）、始终系链的穿梭蛋白（Arndt et al., 2025）之间，存在连续的中间形态。**预测与实验**：Terwilliger et al., 2024 提醒高置信预测也只是假说，Bekkhozhin et al., 2026 就是一个构架出入的实例。

开放问题：（1）桥式蛋白的脂质流量、方向与驱动力，通道在体内是否被脂质占满；（2）Atg9–Atg2 在酵母体内的化学计量与排布；（3）断层中无标记、低丰度膜蛋白的识别能否由 AF 模板匹配可靠完成；（4）从头设计的膜蛋白能否在酵母细胞器膜内正确插入；（5）分离酿酒酵母 NPC（Akey et al., 2022）与裂殖酵母原位 NPC（Allegretti et al., 2020）的孔径是否一致，需要同条件对照。

## 教科书写作建议

- **配图**：（1）三联图——同一酵母膜蛋白的 AF 模型（按 pLDDT 着色）、TmAlphaFold/PPM 膜平面、冷冻电镜密度，标出膜外环与无序尾；（2）RBG 成员的长度与结构域组成对比，标注适配蛋白与所在接触位点；（3）冷冻断层成像流程图——倾转序列、对齐、重建、膜分割、子断层平均、AF 模型拟合——每一步标出信息损失（缺失楔、CTF、剂量）。
- **专栏**：（1）“pLDDT 不是对错的保证”，用 Terwilliger 与 Hegedűs 的证据讲预测即假说；（2）“从 Atg2 凹槽到 RBG 超家族”，一个预测—验证的案例；（3）“552 个蛋白如何拼成核孔”，讲清约束、评分、采样与模型精度；（4）“co-folding 学到了物理吗”，并列 Abramson 与 Masters 的论据。
- **公式框**：（1）Potts 模型由最大熵约束一、二阶统计量推出；（2）RELION 边缘化似然与 EM 更新；（3）$\tau=L^2/2D$ 及其全部假设。
- **习题**：（1）用 Kyte-Doolittle 标度对一段序列算 19 残基窗口均值并判断跨膜片段；（2）已知 $\Delta G_{app}$，求 $K_{app}$ 与插入比例；（3）$D$ 取膜内值的 1/100，桥的 $\tau$ 变为多少，对实验检验意味着什么；（4）设 8.3×10^6 对筛查、假阳性率分别为 $10^{-3}$、$10^{-5}$，估计假阳性数并讨论如何用共进化预过滤降低它。

## 与其他章的连接

- [[A14_膜接触位点与脂质转运蛋白]]、[[A13_自噬体膜]]：桥式蛋白、Atg2–Atg9 的生化与定位证据
- [[A05_核膜]]、[[A12_脂滴]]、[[A10_线粒体内膜与嵴]]、[[A11_过氧化物酶体膜]]：NPC、seipin、TIM23、Pex13 的结构
- [[A16_膜蛋白插入拓扑与质量控制]]：Sec61 插入自由能、插入酶的翻转活性、酵母拓扑图
- [[A18_方法学]]、[[D03_显微图像分析与深度学习]]：断层成像与膜分割
- [[D01_分子动力学模拟]]：MemProtMD、PyLipID
- [[B01_膜弹性曲率与形状能量]]：网格曲率与 Helfrich 能
- [[D06_机器学习与AI驱动发现]]、[[E03_合成生物学与工程]]：语言模型、扩散与膜蛋白设计
- [[D04_组学数据科学]]、[[C04_拓扑图论与网络]]：互作组、全组配对筛查与图聚类

## 本章文献表

共 93 篇，全部经 CrossRef 核验 DOI 与题名；按重要性、年份降序。

| # | 引用 | 类型 | 重要性 | 一句话发现 | DOI |
|---|---|---|---|---|---|
| 1 | Kang et al., 2025, *Nature* | primary | 5 | 解析线虫BLTP1同源物LPD-3天然复合物的冷冻电镜结构，发现伴随蛋白Spigot结合于脂质入口端，并观察到通道中的脂质密度。 | [10.1038/s41586-025-08918-y](https://doi.org/10.1038/s41586-025-08918-y) |
| 2 | Abramson et al., 2024, *Nature* | method | 5 | AlphaFold 3以Pairformer加扩散生成模块取代结构模块，可联合预测蛋白、核酸、小分子配体、离子与修饰残基的复合物结构，蛋白-配体对接精度超过传统对接工具。 | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) |
| 3 | Wozny et al., 2023, *Nature* | primary | 5 | 在酿酒酵母中以关联光镜与冷冻断层成像结合子断层平均得到ERMES原位结构，并以AlphaFold模型拟合，显示ERMES形成连接ER与线粒体外膜的桥状组装。 | [10.1038/s41586-023-06050-3](https://doi.org/10.1038/s41586-023-06050-3) |
| 4 | Hanna et al., 2023, *Annual Review of Cell and Developmental Biology* | review | 5 | 综述RBG桥式脂质转运蛋白的结构（多基于AF2与冷冻电镜）、在接触位点的定位与适配蛋白、与磷脂翻转酶的偶联及疾病关联，并列出未解问题。 | [10.1146/annurev-cellbio-120420-014634](https://doi.org/10.1146/annurev-cellbio-120420-014634) |
| 5 | Watson et al., 2023, *Nature* | method | 5 | 在RoseTTAFold结构预测网络上微调去噪扩散模型，从噪声生成蛋白骨架，可实现无条件生成、对称寡聚体、结合蛋白与基序支撑设计，实验成功率高。 | [10.1038/s41586-023-06415-8](https://doi.org/10.1038/s41586-023-06415-8) |
| 6 | Lin et al., 2023, *Science* | method | 5 | 训练至150亿参数的ESM-2语言模型，并据此构建无需MSA的ESMFold，速度比AF2快约一个数量级，用以预测宏基因组6亿余蛋白结构（ESM Atlas）。 | [10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574) |
| 7 | Varadi et al., 2022, *Nucleic Acids Research* | method | 5 | 介绍AlphaFold DB（AFDB）：公开发布包括酿酒酵母在内多个模式生物蛋白质组及UniProt序列的AF2模型及置信度，提供下载与API。 | [10.1093/nar/gkab1061](https://doi.org/10.1093/nar/gkab1061) |
| 8 | Hegedűs et al., 2022, *Cellular and Molecular Life Sciences* | review | 5 | 系统检视AF2对跨膜蛋白的预测：跨膜区整体可信度高，但AF2不显式考虑膜，可能出现跨膜螺旋位置、寡聚状态与构象的错误，需要结合膜定位工具（如TMDET）评估。 | [10.1007/s00018-021-04112-1](https://doi.org/10.1007/s00018-021-04112-1) |
| 9 | Hallgren et al., 2022, *openRxiv* | preprint | 5 | DeepTMHMM以蛋白语言模型嵌入加深度网络与条件随机场解码，同时预测α螺旋与β桶跨膜蛋白及信号肽，准确度超越TMHMM等传统方法。 | [10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609) |
| 10 | Zivanov et al., 2022, *eLife* | method | 5 | RELION-4.0以“伪子断层”和直接对二维倾转图像的贝叶斯精修实现子断层平均，并对每颗粒运动和CTF进行优化，显著提高原位结构分辨率。 | [10.7554/elife.83724](https://doi.org/10.7554/elife.83724) |
| 11 | Akey et al., 2022, *Cell* | primary | 5 | 以单颗粒冷冻电镜解析分离的酵母NPC内环（亚纳米分辨率），结合原位断层与整合建模给出全面模型，并提出管腔Pom152环限制孔扩张。 | [10.1016/j.cell.2021.12.015](https://doi.org/10.1016/j.cell.2021.12.015) |
| 12 | Mosalaganti et al., 2022, *Science* | primary | 5 | 将AlphaFold对核孔蛋白及亚复合物的预测与原位冷冻断层密度结合，构建约90%人类NPC支架的模型，并结合分子动力学研究其与核膜的相互作用。 | [10.1126/science.abm9506](https://doi.org/10.1126/science.abm9506) |
| 13 | Bieber et al., 2022, *Proceedings of the National Academy of Sciences* | primary | 5 | 在酵母细胞中用关联冷冻光镜与冷冻断层成像捕获自噬体形成各阶段，定量吞噬泡膜曲率、膜间距与和ER、液泡的接触，推断膜来源与驱动闭合的力。 | [10.1073/pnas.2209823119](https://doi.org/10.1073/pnas.2209823119) |
| 14 | Neuman et al., 2022, *Trends in Cell Biology* | review | 5 | 基于AlphaFold预测，指出VPS13、ATG2、SHIP164、Hob/Fmp27、Csf1/Tweek等具有相同的重复β槽（RBG）长杆状结构，构成桥式脂质转运蛋白超家族。 | [10.1016/j.tcb.2022.03.011](https://doi.org/10.1016/j.tcb.2022.03.011) |
| 15 | Levine et al., 2022, *Contact* | computational | 5 | 结合远缘同源检索与AlphaFold预测，系统比较RBG桥蛋白家族各成员的结构域组成、长度变异与保守表面，指出沿桥体分布的保守残基可能是未知伴侣的结合位点。 | [10.1177/25152564221134328](https://doi.org/10.1177/25152564221134328) |
| 16 | van et al., 2022, *Molecular Cell* | primary | 5 | 结合AlphaFold-Multimer预测、交联质谱与突变实验，确定ATG2A C端与ATG9A的结合界面，提出Atg2的脂质通道与Atg9的侧向通道对齐。 | [10.1016/j.molcel.2022.10.017](https://doi.org/10.1016/j.molcel.2022.10.017) |
| 17 | Arlt et al., 2022, *Nature Structural &amp; Molecular Biology* | primary | 5 | 解析酿酒酵母Sei1冷冻电镜结构，结合AF2与分子动力学，发现其跨膜区形成柔性笼状结构，可在ER膜中围出三酰甘油聚集区。 | [10.1038/s41594-021-00718-y](https://doi.org/10.1038/s41594-021-00718-y) |
| 18 | Dauparas et al., 2022, *Science* | method | 5 | ProteinMPNN以消息传递图神经网络根据骨架设计序列，序列恢复率显著高于Rosetta，并能挽救此前失败的设计。 | [10.1126/science.add2187](https://doi.org/10.1126/science.add2187) |
| 19 | Jumper et al., 2021, *Nature* | method | 5 | 提出AlphaFold2：以多序列比对与模板为输入，经Evoformer注意力模块与等变结构模块端到端输出原子坐标，并给出逐残基pLDDT与PAE置信度。 | [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) |
| 20 | Tunyasuvunakool et al., 2021, *Nature* | computational | 5 | 将AF2应用于几乎全部人类蛋白质组，约58%残基获得可信预测，并显示低pLDDT区域与内在无序区高度重合。 | [10.1038/s41586-021-03828-1](https://doi.org/10.1038/s41586-021-03828-1) |
| 21 | Evans et al., 2021, *openRxiv* | preprint | 5 | 在多链复合物数据上重新训练AF2，形成AlphaFold-Multimer，用配对MSA和ipTM评分预测异源与同源多聚体界面，界面精度显著优于在单链AF2中用连接子拼接的做法。 | [10.1101/2021.10.04.463034](https://doi.org/10.1101/2021.10.04.463034) |
| 22 | Humphreys et al., 2021, *Science* | computational | 5 | 结合共进化筛选、RoseTTAFold与AF2，对约830万对酿酒酵母蛋白进行全组配对筛查，预测出1500余个可能的复合物，并为其中106个此前未知的组装给出结构模型。 | [10.1126/science.abm4805](https://doi.org/10.1126/science.abm4805) |
| 23 | Vorobieva et al., 2021, *Science* | primary | 5 | 归纳β桶折叠的设计规则（甘氨酸凸起、β转角等），从头设计出可折叠插入脂膜的跨膜β桶，NMR与晶体结构验证设计。 | [10.1126/science.abc8182](https://doi.org/10.1126/science.abc8182) |
| 24 | Rives et al., 2021, *Proceedings of the National Academy of Sciences* | method | 5 | 在2.5亿条蛋白序列上以掩码语言建模训练Transformer（ESM-1b），其表示中自发编码二级结构、接触图与远缘同源信息。 | [10.1073/pnas.2016239118](https://doi.org/10.1073/pnas.2016239118) |
| 25 | Allegretti et al., 2020, *Nature* | primary | 5 | 在裂殖酵母细胞内用冷冻断层成像与子断层平均获得NPC原位结构，并捕捉到NPC被自噬膜包裹降解的中间态。 | [10.1038/s41586-020-2670-5](https://doi.org/10.1038/s41586-020-2670-5) |
| 26 | Li et al., 2020, *Journal of Cell Biology* | primary | 5 | 解析嗜热真菌Vps13 N端片段的冷冻电镜结构，发现一条贯穿的疏水长槽，并结合预测提出全长Vps13为连接两膜的约20 nm长桥。 | [10.1083/jcb.202001161](https://doi.org/10.1083/jcb.202001161) |
| 27 | Matoba et al., 2020, *Nature Structural &amp; Molecular Biology* | primary | 5 | 冷冻电镜解析酵母Atg9同源三聚体结构，发现垂直与水平的通道，并证明Atg9具有脂质翻转（scramblase）活性。 | [10.1038/s41594-020-00518-w](https://doi.org/10.1038/s41594-020-00518-w) |
| 28 | Xu et al., 2020, *Nature* | primary | 5 | 从头设计具有水通道的跨膜孔蛋白（12或16螺旋），冷冻电镜结构与设计一致，可在膜中形成离子选择性通道。 | [10.1038/s41586-020-2646-5](https://doi.org/10.1038/s41586-020-2646-5) |
| 29 | Osawa et al., 2019, *Nature Structural &amp; Molecular Biology* | primary | 5 | 解析酵母Atg2 N端结构域的晶体结构，发现疏水凹槽，并证明Atg2在体外可在膜间直接转运磷脂，该活性是自噬体形成所必需。 | [10.1038/s41594-019-0203-4](https://doi.org/10.1038/s41594-019-0203-4) |
| 30 | Kim et al., 2018, *Nature* | computational | 5 | 综合交联质谱、冷冻电镜密度、SAXS等数据，用IMP构建酿酒酵母NPC的整合结构，揭示柔性连接与膜环的组织方式。 | [10.1038/nature26003](https://doi.org/10.1038/nature26003) |
| 31 | Lu et al., 2018, *Science* | primary | 5 | 用Rosetta从头设计多次跨膜螺旋束蛋白（含二至四聚体），晶体结构与设计模型高度一致，并可在大肠杆菌与哺乳动物细胞膜中正确插入。 | [10.1126/science.aaq1739](https://doi.org/10.1126/science.aaq1739) |
| 32 | Punjani et al., 2017, *Nature Methods* | method | 5 | 提出随机梯度下降从头生成初始模型与分支定界（branch-and-bound）快速搜索取向的算法，使无监督三维重构在单GPU上数分钟内完成。 | [10.1038/nmeth.4169](https://doi.org/10.1038/nmeth.4169) |
| 33 | Lomize et al., 2012, *Nucleic Acids Research* | method | 5 | OPM数据库收录PDB膜蛋白在脂双层中的空间位置，PPM服务器基于各向异性溶剂模型最小化转移自由能来计算疏水厚度、倾角与插入深度。 | [10.1093/nar/gkr703](https://doi.org/10.1093/nar/gkr703) |
| 34 | Scheres et al., 2012, *Journal of Structural Biology* | method | 5 | 以经验贝叶斯框架实现最大后验（MAP）三维重构与分类，通过期望最大化算法自动确定正则化参数，减少人为调参。 | [10.1016/j.jsb.2012.09.006](https://doi.org/10.1016/j.jsb.2012.09.006) |
| 35 | Russel et al., 2012, *PLoS Biology* | method | 5 | 介绍IMP（Integrative Modeling Platform）：将多源实验数据转译为空间约束，经采样与评分得到大分子组装体结构集合。 | [10.1371/journal.pbio.1001244](https://doi.org/10.1371/journal.pbio.1001244) |
| 36 | Alber et al., 2007, *Nature* | computational | 5 | 以多种实验数据（亲和纯化、沉降、免疫电镜等）为空间约束，通过整合建模确定酿酒酵母核孔复合物约456个核孔蛋白的空间排布。 | [10.1038/nature06405](https://doi.org/10.1038/nature06405) |
| 37 | Kim et al., 2006, *Proceedings of the National Academy of Sciences* | primary | 5 | 以C端融合报告蛋白实验测定数百个酵母膜蛋白的C端朝向，结合预测给出酿酒酵母膜蛋白组的全局拓扑图。 | [10.1073/pnas.0604075103](https://doi.org/10.1073/pnas.0604075103) |
| 38 | Krogh et al., 2001, *Journal of Molecular Biology* | method | 5 | 提出TMHMM：以隐马尔可夫模型描述跨膜螺旋、环区与帽区的语法结构，准确预测跨膜螺旋和拓扑，并估计约20–30%的基因编码膜蛋白。 | [10.1006/jmbi.2000.4315](https://doi.org/10.1006/jmbi.2000.4315) |
| 39 | Kremer et al., 1996, *Journal of Structural Biology* | method | 5 | 介绍IMOD程序包：用于电子断层图像序列的对齐、三维重建、可视化与手动建模（膜轮廓勾画）。 | [10.1006/jsbi.1996.0013](https://doi.org/10.1006/jsbi.1996.0013) |
| 40 | von et al., 1992, *Journal of Molecular Biology* | method | 5 | 将疏水性分析与“正电荷在内”规则结合，形成TOPPRED方法，可较准确地预测跨膜片段及其取向。 | [10.1016/0022-2836(92)90934-c](https://doi.org/10.1016/0022-2836(92)90934-c) |
| 41 | Dziurdzik et al., 2026, *Journal of Cell Biology* | primary | 4 | 在酵母中鉴定Hoi1为BLTP2（Fmp27）的接触位点靶向因子，结构预测显示Hoi1与Fmp27中央疏水通道两侧的α螺旋突起相互作用，破坏此相互作用改变甾醇稳态； | [10.1083/jcb.202502131](https://doi.org/10.1083/jcb.202502131) |
| 42 | Wang et al., 2025, *Nature Structural &amp; Molecular Biology* | primary | 4 | 冷冻电镜解析ATG2A-ATG9A复合物，显示ATG2A的脂质通道与ATG9A翻转酶通道在空间上相连，为脂质转运与跨叶平衡偶联提供结构基础。 | [10.1038/s41594-024-01376-6](https://doi.org/10.1038/s41594-024-01376-6) |
| 43 | Arndt et al., 2025, *Nature Structural &amp; Molecular Biology* | primary | 4 | 结合结构与生化研究酿酒酵母ER-质膜主要系链Ist2及其与PS/PI4P交换蛋白Osh6的相互作用，发现Osh6在脂质穿梭中保持与Ist2结合，并显示Ist2的ER跨膜区与TMEM16家族同源、具有组成性脂质翻转活性。 | [10.1038/s41594-025-01660-z](https://doi.org/10.1038/s41594-025-01660-z) |
| 44 | Masters et al., 2025, *Nature Communications* | computational | 4 | 通过对结合位点的对抗性突变等物理检验，发现AF3、RoseTTAFold All-Atom等共折叠模型在配体位点被破坏后仍倾向放置配体，提示其可能更多依赖记忆而非物理。 | [10.1038/s41467-025-63947-5](https://doi.org/10.1038/s41467-025-63947-5) |
| 45 | Hayes et al., 2025, *Science* | method | 4 | ESM3为序列、结构与功能三模态的生成式语言模型，可按提示生成新蛋白，并设计出与已知荧光蛋白序列差异很大的功能性荧光蛋白。 | [10.1126/science.ads0018](https://doi.org/10.1126/science.ads0018) |
| 46 | Terwilliger et al., 2024, *Nature Methods* | perspective | 4 | 将AF2模型与未参与训练的晶体学电子密度图比较，发现即使高置信预测也常有局部主链与侧链偏差，模型应被视为待检验的假说。 | [10.1038/s41592-023-02087-4](https://doi.org/10.1038/s41592-023-02087-4) |
| 47 | van et al., 2024, *Nature Biotechnology* | method | 4 | Foldseek把三级相互作用编码为3Di结构字母表，使结构比对可像序列搜索一样在数亿AF模型中快速完成，灵敏度接近Dali/TM-align。 | [10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) |
| 48 | Li et al., 2024, *Proceedings of the National Academy of Sciences* | primary | 4 | 结合生化重构与分子动力学模拟，发现在ER及不与囊泡运输相连的细胞器膜中工作的多种蛋白插入酶普遍具有磷脂翻转活性，翻转经由蛋白插入所用的亲水通道发生，并在新生肽链存在时被抑制。 | [10.1073/pnas.2319476121](https://doi.org/10.1073/pnas.2319476121) |
| 49 | Krishna et al., 2024, *Science* | method | 4 | RoseTTAFold All-Atom把蛋白残基与非蛋白原子统一表示，可预测含小分子、金属、共价修饰与核酸的复合物，并结合扩散模型设计结合小分子的蛋白。 | [10.1126/science.adl2528](https://doi.org/10.1126/science.adl2528) |
| 50 | Goverde et al., 2024, *Nature* | primary | 4 | 以AF2结构反向设计与ProteinMPNN为管线，将跨膜蛋白折叠（如GPCR、claudin）重新设计为可溶性类似物并保留部分功能。 | [10.1038/s41586-024-07601-y](https://doi.org/10.1038/s41586-024-07601-y) |
| 51 | Kortemme et al., 2024, *Cell* | review | 4 | 综述从Rosetta物理建模到深度学习（RFdiffusion、ProteinMPNN等）的蛋白质从头设计进展，涵盖结合蛋白、酶、膜蛋白与可编程功能。 | [10.1016/j.cell.2023.12.028](https://doi.org/10.1016/j.cell.2023.12.028) |
| 52 | Michaelis et al., 2023, *Nature* | primary | 4 | 对酿酒酵母内源标签蛋白进行大规模亲和纯化-质谱，构建高质量相互作用组，并用AlphaFold-Multimer为相互作用对建模，为未表征蛋白提出功能角色。 | [10.1038/s41586-023-06739-5](https://doi.org/10.1038/s41586-023-06739-5) |
| 53 | Dobson et al., 2023, *Nucleic Acids Research* | method | 4 | 对AFDB中的α螺旋跨膜蛋白模型计算膜平面位置，并按跨膜区几何与拓扑一致性对模型质量分级，提供可检索数据库。 | [10.1093/nar/gkac928](https://doi.org/10.1093/nar/gkac928) |
| 54 | Young et al., 2023, *Annual Review of Biophysics* | review | 4 | 综述原位冷冻断层成像从样品制备（FIB减薄）、数据采集、子断层平均到与AlphaFold模型整合的全流程及其在细胞生物学中的应用。 | [10.1146/annurev-biophys-111622-091327](https://doi.org/10.1146/annurev-biophys-111622-091327) |
| 55 | Barad et al., 2023, *Journal of Cell Biology* | method | 4 | 建立表面形态测量流程：由断层分割生成三角网格表面，计算膜间距、曲率与取向等指标，用于定量比较细胞器（如线粒体嵴）超微结构。 | [10.1083/jcb.202204093](https://doi.org/10.1083/jcb.202204093) |
| 56 | Dabrowski et al., 2023, *Journal of Cell Biology* | primary | 4 | 在酵母中发现Vps13定位于扩张中的吞噬泡边缘，与Atg2并行转运磷脂，二者共同决定自噬体膜扩张速率。 | [10.1083/jcb.202211039](https://doi.org/10.1083/jcb.202211039) |
| 57 | Sim et al., 2023, *Nature* | primary | 4 | 解析酵母TIM23复合物冷冻电镜结构，发现Tim17形成侧向开放的通道，Mgr2封闭其侧向开口，提出新的蛋白导入与分选模型。 | [10.1038/s41586-023-06239-6](https://doi.org/10.1038/s41586-023-06239-6) |
| 58 | Mirdita et al., 2022, *Nature Methods* | method | 4 | 以MMseqs2快速构建MSA替代耗时的数据库检索，使AF2/AF-Multimer可在Colab或本地GPU上运行，速度提升20–30倍且精度相当。 | [10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) |
| 59 | Akdel et al., 2022, *Nature Structural &amp; Molecular Biology* | review | 4 | 社区协作系统评估AF2模型在突变效应、无序区、口袋、复合物和跨膜区等应用中的表现，给出pLDDT/PAE的使用建议与已知局限。 | [10.1038/s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w) |
| 60 | del et al., 2022, *eLife* | computational | 4 | 通过大幅降低MSA深度，使AF2对转运蛋白和GPCR生成多种构象（内向/外向开放等），部分与实验构象一致。 | [10.7554/elife.75751](https://doi.org/10.7554/elife.75751) |
| 61 | Zheng et al., 2022, *Journal of Structural Biology: X* | method | 4 | AreTomo在GPU上实现无基准点的倾转序列对齐、局部运动校正与重建，可实时跟上数据采集速度。 | [10.1016/j.yjsbx.2022.100068](https://doi.org/10.1016/j.yjsbx.2022.100068) |
| 62 | Liu et al., 2022, *Nature Communications* | method | 4 | IsoNet用自监督深度学习从断层数据自身学习补偿“缺失楔形”造成的各向异性分辨率，并同时去噪，改善膜与细胞器的三维形貌。 | [10.1038/s41467-022-33957-8](https://doi.org/10.1038/s41467-022-33957-8) |
| 63 | Lamm et al., 2022, *Computer Methods and Programs in Biomedicine* | method | 4 | MemBrain先分割膜面，再以卷积网络在膜附近定位膜蛋白颗粒中心，用于后续子断层平均。 | [10.1016/j.cmpb.2022.106990](https://doi.org/10.1016/j.cmpb.2022.106990) |
| 64 | Toulmay et al., 2022, *Journal of Cell Biology* | primary | 4 | 在酵母中发现Vps13样蛋白Csf1为ER内GPI锚合成提供磷脂酰乙醇胺，其线虫与人类同源物缺失同样降低GPI锚定蛋白。 | [10.1083/jcb.202111095](https://doi.org/10.1083/jcb.202111095) |
| 65 | Neuman et al., 2022, *Journal of Cell Science* | primary | 4 | 在酵母与果蝇中发现Hobbit/Hob蛋白（酵母Fmp27、Ypr117w的同源物）定位于ER-质膜接触位点，定位依赖N端ER膜锚与保守C端序列，C端可结合质膜磷脂酰肌醇。 | [10.1242/jcs.259086](https://doi.org/10.1242/jcs.259086) |
| 66 | Gao et al., 2022, *Science* | primary | 4 | 发现过氧化物酶体膜蛋白Pex13的YG结构域在膜上形成类似核孔FG重复的水凝胶相，受体Pex5借助芳香族基序分配进入，从而转运折叠态货物。 | [10.1126/science.adf3971](https://doi.org/10.1126/science.adf3971) |
| 67 | Song et al., 2022, *Journal of Chemical Theory and Computation* | method | 4 | PyLipID从MD轨迹中以双截断距离识别脂质结合事件、计算停留时间并以图论聚类识别结合位点，输出代表性结合构象。 | [10.1021/acs.jctc.1c00708](https://doi.org/10.1021/acs.jctc.1c00708) |
| 68 | Elnaggar et al., 2022, *IEEE Transactions on Pattern Analysis and Machine Intelligence* | method | 4 | 在超大规模序列库上训练多种Transformer蛋白语言模型（ProtBert、ProtT5等），其嵌入可直接用于二级结构、亚细胞定位与膜结合预测。 | [10.1109/tpami.2021.3095381](https://doi.org/10.1109/tpami.2021.3095381) |
| 69 | Baek et al., 2021, *Science* | method | 4 | 提出RoseTTAFold：序列、二维距离图与三维坐标三轨并行的网络，精度接近AF2，并能直接产生蛋白-蛋白复合物模型。 | [10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754) |
| 70 | Klug et al., 2021, *Nature Communications* | primary | 4 | 在酵母中研究Sei1与Ldb16复合物，结合结构预测与突变，发现Ldb16含三酰甘油结合的疏水位点，与Sei1共同促成脂滴成核。 | [10.1038/s41467-021-26162-6](https://doi.org/10.1038/s41467-021-26162-6) |
| 71 | Maeda et al., 2020, *Nature Structural &amp; Molecular Biology* | primary | 4 | 解析人ATG9A冷冻电镜结构，揭示三聚体中的网络状通道，结合分子动力学与体外实验证明其翻转脂质的活性。 | [10.1038/s41594-020-00520-2](https://doi.org/10.1038/s41594-020-00520-2) |
| 72 | Newport et al., 2019, *Nucleic Acids Research* | method | 4 | MemProtMD数据库对数千个PDB膜蛋白结构进行粗粒化自组装模拟，提供膜嵌入模型、局部膜变形与逐残基脂质接触数据。 | [10.1093/nar/gky1047](https://doi.org/10.1093/nar/gky1047) |
| 73 | Tegunov et al., 2019, *Nature Methods* | method | 4 | Warp在数据采集时实时完成运动校正、CTF估计、深度学习颗粒挑选与断层预处理，并引入局部时空运动模型。 | [10.1038/s41592-019-0580-y](https://doi.org/10.1038/s41592-019-0580-y) |
| 74 | Rout et al., 2019, *Cell* | review | 4 | 总结整合结构生物学的原则：数据收集、表示、评分、采样和模型验证与不确定性估计，并以核孔复合物等为例说明。 | [10.1016/j.cell.2019.05.016](https://doi.org/10.1016/j.cell.2019.05.016) |
| 75 | Collado et al., 2019, *Developmental Cell* | primary | 4 | 冷冻断层成像显示酵母tricalbin在ER-质膜接触处形成高曲率ER外周结构，缺失tricalbin则这些弯曲结构消失并影响质膜完整性。 | [10.1016/j.devcel.2019.10.018](https://doi.org/10.1016/j.devcel.2019.10.018) |
| 76 | Hoffmann et al., 2019, *Developmental Cell* | primary | 4 | 原位冷冻断层成像在酵母ER-质膜接触处观察到连接两膜的杆状桥接密度，并提示tricalbin参与脂质流动。 | [10.1016/j.devcel.2019.09.019](https://doi.org/10.1016/j.devcel.2019.09.019) |
| 77 | Sui et al., 2018, *Journal of Cell Biology* | primary | 4 | 解析果蝇seipin冷冻电镜结构，显示其管腔结构域形成十一聚体环，含与膜结合的疏水螺旋，提出其在脂滴形成位点组织中性脂。 | [10.1083/jcb.201809067](https://doi.org/10.1083/jcb.201809067) |
| 78 | Kawano et al., 2018, *Journal of Cell Biology* | primary | 4 | 解析酵母Mmm1-Mdm12复合物晶体结构，显示SMP结构域形成连续疏水通道，并在体外证明其在膜间直接转运磷脂。 | [10.1083/jcb.201704119](https://doi.org/10.1083/jcb.201704119) |
| 79 | Corradi et al., 2018, *ACS Central Science* | computational | 4 | 在模拟真实质膜复杂组成的粗粒化体系中对十种膜蛋白进行模拟，发现每种蛋白周围形成独特的脂质组成“指纹”。 | [10.1021/acscentsci.8b00143](https://doi.org/10.1021/acscentsci.8b00143) |
| 80 | Mastronarde et al., 2017, *Journal of Structural Biology* | method | 4 | 描述IMOD中倾转序列自动对齐（基准点追踪或贴片追踪）与重建的批处理流程，实现大规模断层数据的自动化处理。 | [10.1016/j.jsb.2016.07.011](https://doi.org/10.1016/j.jsb.2016.07.011) |
| 81 | Upla et al., 2017, *Structure* | primary | 4 | 结合负染电镜与整合建模解析酵母Pom152的分子构型，表明16个拷贝足以在核膜管腔一侧组成NPC外围的膜环。 | [10.1016/j.str.2017.01.006](https://doi.org/10.1016/j.str.2017.01.006) |
| 82 | Tsirigos et al., 2015, *Nucleic Acids Research* | method | 4 | TOPCONS整合多种拓扑预测器的输出，用HMM求共识拓扑并同时预测信号肽，适用于蛋白质组规模分析。 | [10.1093/nar/gkv485](https://doi.org/10.1093/nar/gkv485) |
| 83 | Stansfeld et al., 2015, *Structure* | method | 4 | 建立自动化流程：用粗粒化（MARTINI）分子动力学让膜蛋白在显式脂双层中自组装，得到膜位置及脂质相互作用。 | [10.1016/j.str.2015.05.006](https://doi.org/10.1016/j.str.2015.05.006) |
| 84 | Kühlbrandt et al., 2014, *Science* | perspective | 4 | 评述直接电子探测器与新的图像处理算法如何使单颗粒冷冻电镜达到近原子分辨率，尤其适合难结晶的膜蛋白。 | [10.1126/science.1251652](https://doi.org/10.1126/science.1251652) |
| 85 | Hopf et al., 2012, *Cell* | computational | 4 | 利用最大熵（Potts模型）从同源序列中推断进化耦合残基对，再据此从头折叠出多个跨膜蛋白的三维结构，精度足以识别构象与寡聚接触。 | [10.1016/j.cell.2012.04.012](https://doi.org/10.1016/j.cell.2012.04.012) |
| 86 | Hessa et al., 2005, *Nature* | primary | 4 | 通过系统设计的测试片段测量Sec61转运通道将其插入ER膜的表观自由能，得到“生物学疏水性标度”及位置依赖贡献。 | [10.1038/nature03216](https://doi.org/10.1038/nature03216) |
| 87 | Käll et al., 2004, *Journal of Molecular Biology* | method | 4 | Phobius将信号肽与跨膜拓扑放入同一HMM联合建模，显著减少信号肽被误判为跨膜螺旋的错误。 | [10.1016/j.jmb.2004.03.016](https://doi.org/10.1016/j.jmb.2004.03.016) |
| 88 | Henderson et al., 1990, *Journal of Molecular Biology* | primary | 4 | 利用二维晶体的高分辨电子冷冻显微术，首次得到细菌视紫红质含七条跨膜螺旋的原子模型。 | [10.1016/s0022-2836(05)80271-2](https://doi.org/10.1016/s0022-2836(05)80271-2) |
| 89 | Kyte et al., 1982, *Journal of Molecular Biology* | method | 4 | 提出Kyte-Doolittle疏水性标度与滑动窗口疏水性曲线，可识别约19残基的疏水跨膜片段。 | [10.1016/0022-2836(82)90515-0](https://doi.org/10.1016/0022-2836(82)90515-0) |
| 90 | Bekkhozhin et al., 2026, *Journal of Biological Chemistry* | primary | 3 | 以结构预测与生化实验研究酵母Atg23与Atg9的相互作用，发现Atg9无序N端与C端远端的保守序列结合Atg23的疏水空腔，且实验结构与预测在整体构架上存在差异。 | [10.1016/j.jbc.2026.113245](https://doi.org/10.1016/j.jbc.2026.113245) |
| 91 | Aboumourad et al., 2026, *Contact: The Journal of Inter-Organelle Communication* | computational | 3 | 以结构预测与系统发育分析研究酵母核-液泡连接处Mdm1与Nvj3复合物，发现其形成α螺旋组装的、可容纳脂质的通道，不同于经典桥式蛋白的β片层结构。 | [10.1177/25152564261471395](https://doi.org/10.1177/25152564261471395) |
| 92 | Yang et al., 2026, *Journal of Chemical Information and Modeling* | computational | 3 | 构建脂质-蛋白复合物基准集LiPP，比较共折叠模型与对接方法预测脂质结合构象的能力，揭示二者在捕捉脂质-蛋白相互作用特征上的内在不足。 | [10.1021/acs.jcim.6c01457](https://doi.org/10.1021/acs.jcim.6c01457) |
| 93 | Hekkelman et al., 2023, *Nature Methods* | method | 3 | AlphaFill依据序列与结构相似性，从PDB同源实验结构把配体、辅因子“移植”到AlphaFold模型中，生成带配体的模型库。 | [10.1038/s41592-022-01685-y](https://doi.org/10.1038/s41592-022-01685-y) |
