---
title: "A07 内吞内体与ESCRT"
chapter_id: A07
part: A
n_papers: 154
tags: [细胞器膜, 酵母, 文献调研, part-A]
created: 2026-10-13
---

# A07 内吞内体与ESCRT

**酿酒酵母（*Saccharomyces cerevisiae*）的内吞—内体系统把膜上的三类问题拆成了可分别测量、分别建模的对象：质膜内陷是对抗膨压的力学问题，ESCRT-III 切断朝内的膜颈是弹性与几何问题，内体成熟是 Rab 与磷酸肌醇共同定义身份的开关问题；三者都有扎实的酵母数据，但各自“最后一步”的机制仍有互不相容的模型并存。**

**本章要讲清楚什么**：按“形成—分选—回收”梳理酵母内吞与内体：网格蛋白介导内吞的时序与力学，ESCRT/MVB 与 ESCRT-III 的分裂机制，Rab 与磷酸肌醇编码的内体身份，泛素—Rsp5/ART 的货物选择，以及 retromer、AP-3 的回收分选；数学物理表述集中在“定量与物理视角”。

## 1. 内吞的时序模块与纳米架构

酵母的网格蛋白介导内吞（clathrin-mediated endocytosis, CME）是被研究得最细的单个膜事件。最早的遗传证据是 *act1* 与 *sac6*（fimbrin）突变体中 α 因子受体的内化受阻，说明肌动蛋白骨架是内化步骤所需（Kübler et al., 1993）。Kaksonen 等用双色活细胞成像加颗粒追踪发现，皮层接头蛋白与肌动蛋白斑块按固定顺序出现：包被蛋白先在质膜上相对静止地累积，随后肌动蛋白短暂爆发，伴随内陷与小泡内移（Kaksonen et al., 2003）。对约 15 种蛋白及其缺失株的分析又把机器划成早期包被、晚期包被、WASP/Myo、肌动蛋白与两亲蛋白（amphiphysin，即 Rvs 蛋白）等模块，各有自己的招募时间窗（Kaksonen et al., 2005）。综述见 Kaksonen et al., 2018；Goode et al., 2015；Weinberg et al., 2012；肌动蛋白的角色另见 Kaksonen et al., 2006；Engqvist-Goldstein et al., 2003。

起始阶段的机制较晚才有答案：早期蛋白 Ede1 通过多价相互作用在质膜上形成液态凝聚体，破坏凝聚能力会降低内吞起始频率（Kozak et al., 2022）。空间架构方面，Picco 等用质心追踪与时序对齐测出 20 余种蛋白相对内陷顶端的纳米级位置：包被蛋白随顶端内移，肌动蛋白在基部成核而网络向内生长（Picco et al., 2015）；单分子定位的平均成像进一步发现 Las17（酵母 WASP）等成核因子在内陷基部排成环，这种图案化成核与高效成泡相关（Mund et al., 2018）。分子数方面，裂殖酵母（*Schizosaccharomyces pombe*）单个斑块中肌动蛋白峰值约 7000 个分子（Sirotkin et al., 2010）；单分子追踪显示肌动蛋白亚基在位点上停留极短、持续交换，包被蛋白则较稳定（Lacy et al., 2019）。两种酵母并排比较，核心时序与对肌动蛋白的依赖高度保守，早期蛋白驻留时间和位点密度则可以演化（Sun et al., 2019）。

形态学证据来自相关光电显微（correlative light and electron microscopy, CLEM）：在树脂切片中保留荧光并用荧光珠配准（Kukulski et al., 2011），把单个事件的荧光状态与电子断层形貌逐一对应，得到平膜→浅坑→管状内陷→分裂的序列；肌动蛋白在膜尚平坦时已开始聚合，内陷长度随肌动蛋白量增加（Kukulski et al., 2012）。

## 2. 力与形状：肌动蛋白、膨压与分裂

酵母内吞离不开肌动蛋白，一个关键物理变量是膨压（turgor）。降低膨压（渗透支持或细胞壁缺陷）后，酵母内吞对肌动蛋白的绝对需求被解除，而哺乳动物细胞提高膜张力后反而变得依赖肌动蛋白（Aghamohammadzadeh et al., 2009）。裂殖酵母中降低膨压则只是部分绕过肌动蛋白需求并加快内吞（Basu et al., 2014）。“解除”与“部分绕过”是两个物种、两种操作下的不同结果，教科书应并列呈现。

力必须耦联到膜上才有用。Sla2 的 ANTH 域与 Ent1 的 ENTH 域在 PI(4,5)P2 存在下共同组装，把膜与肌动蛋白网络连起来；破坏耦联后肌动蛋白仍聚合，膜却不内陷（Skruzny et al., 2012）。在 Sla2 中插入 FRET 张力传感器，首次在活酵母里测到经 Sla2 传递的肌动蛋白力，且力随内陷进程变化（Abella et al., 2021）。逐个削弱肌动蛋白调控因子，可区分出负责弯曲起始、延伸与分裂的不同功能（Picco et al., 2018）；体外重构的肌动蛋白斑块，其刚度与对应突变株的内吞效率高度相关，提示决定成败的是网络的力学性质而不只是聚合量（Planade et al., 2019）。人（*Homo sapiens*）细胞的 cryo-ET 显示内吞位点肌动蛋白丝主要垂直或倾斜指向膜（Serwas et al., 2022），这是力产生几何的直接结构证据，但来自无细胞壁的哺乳动物细胞，不能直接外推到酵母。

分裂的证据更分散。网格蛋白缺失株与野生型的内陷形状相同，但分裂位置和小泡大小改变（Kukulski et al., 2016）。Rvs161/Rvs167 异二聚体的 BAR 域在内陷管颈部组装并促进分裂（Youn et al., 2010）；发动蛋白样 Vps1 定位于内吞位点，*vps1*Δ 使内陷延长、分裂缺陷（de Rooij et al., 2010）。分裂究竟主要靠 BAR 支架、Vps1 的机械作用，还是脂质相界线张力（理论见下文），现有数据没有裁决。

## 3. ESCRT 的发现与 MVB 分选

遗传学起点是液泡蛋白分选筛选：以 CPY 分泌或 CPY–转化酶融合蛋白为报告，得到首批 *vps/vpt* 突变体（Bankaitis et al., 1986; Rothman et al., 1986）。41 个互补群按液泡形态分为 A–F 六类，class E 突变体积累扩大的前液泡区室（Raymond et al., 1992）；温敏 *vps27* 突变体表明内吞货物与生物合成货物共同经过该区室（Piper et al., 1995）。后来证明 class E 基因就是 ESCRT（endosomal sorting complex required for transport）的组分。

复合体按“信号—招募”逻辑被依次鉴定。Ste2 受体尾部的泛素化是其内吞信号（Hicke et al., 1996）；ESCRT-I（Vps23/Vps28/Vps37）识别泛素化货物并将其分选进 MVB 腔内小泡，泛素由此成为 MVB 分选信号（Katzmann et al., 2001）。ESCRT-II（Vps22/Vps25/Vps36）随后鉴定，并提出 I→II→III 的顺序招募（Babst et al., 2002）；ESCRT-III（Vps20/Snf7/Vps24/Vps2）在膜上组装为大寡聚体，需 Vps4 解聚（Babst et al., 2002，同年另一篇）。Vps4 的 ATP 酶活性控制 class E Vps 蛋白从内体膜解离（Babst et al., 1998）。上游一环是 ESCRT-0 的 Vps27：其 FYVE 域结合 PI3P，并经 PSDP 基序直接招募 ESCRT-I（Katzmann et al., 2003）；ESCRT-I 本身是约 18 nm 的长杆状异源四聚体（Kostelansky et al., 2007）。

体外重构给出分工图景：酵母 ESCRT-III 核心亚基在巨型单层囊泡上即可使膜向内出芽、产生腔内小泡（Wollert et al., 2009）；完整 ESCRT-0/I/II/III 系统中，ESCRT-0 聚集货物，ESCRT-I/II 使膜出芽并把货物限制在芽内，ESCRT-III 在颈部切割（Wollert et al., 2010）。几何上，ESCRT-0/I/II 在外圈浓缩货物、ESCRT-III 在内圈成环的同心圆模型对应了这一分工（Nickerson et al., 2007）；ESCRT-0 与多泛素化货物还能通过多价作用凝聚，相分离被认为促进货物聚集（Banjade et al., 2022）。对 class E 区室的解释也在修正：它不只是 MVB 停滞，而是 ESCRT 缺陷使 Vps21 持续活化、内体过度融合所致（Russell et al., 2012）。综述见 Henne et al., 2011；Hurley et al., 2006；Vietri et al., 2020。

## 4. ESCRT-III 与 Vps4：切断朝内的膜颈

ESCRT-III 作用的膜颈内部与胞质相通，切割必须从颈的胞质侧完成，这是“反向拓扑”分裂（Schöneberg et al., 2017）。体外重构出完整循环：Vps20 成核、Snf7 聚合、Vps24/Vps2 封端、Vps4 依赖解聚，Snf7 聚合受自抑制控制（Saksena et al., 2009）；体内顺序为 Vps20→Snf7→Vps24→Vps2，Snf7 是主要聚合单元，每个复合体约数十拷贝（Teis et al., 2008）。Snf7 核心域晶体结构显示从闭合自抑制到开放活化的转变及丝内界面（Tang et al., 2015），核心域开放后经侧向界面聚合、螺旋曲率随圈数变化的建模见 Shen et al., 2014，侧向静电作用决定异聚体的形成与功能（Banjade et al., 2019）。ESCRT-II 与 Vps20 的结合使 Snf7 成核为两条并行丝（Henne et al., 2012）。哺乳动物证据补充了丝的形态：过表达 CHMP4 在质膜下形成环状丝阵列并使膜外凸（Hanson et al., 2008），IST1–CHMP1B 共聚管的 cryo-EM 结构显示开放构象与正曲率膜结合（McCullough et al., 2015）。

能量从哪里来，目前有两类模型。**弹簧弛豫模型**：高速 AFM 显示 Snf7 在支撑双层上形成螺旋，螺旋被压缩偏离优选曲率而储存弹性能，弛豫时使膜变形（Chiaruttini et al., 2015）；Snf7 螺旋能感知并改变膜曲率（Jukic et al., 2022）。**顺序聚合—亚基交换模型**：酵母 ESCRT-III 按 Snf7→Vps24/Vps2→Did2→Ist1 顺序聚合，每一步改变丝的几何（平螺旋→锥形→管状），Vps4 驱动的亚基替换使膜逐步缩窄并分裂（Pfitzner et al., 2020）；光镊与膜纳米管重构直接测得 Vps4 水解 ATP 产生的力，且亚基周转驱动缩颈与分裂（Schöneberg et al., 2018）。活酵母中，Vps4 经 MIT 域协同结合多个 ESCRT-III 亚基，在小泡形成过程中就已被招募并驱动缩颈（Adell et al., 2014）；Snf7 与 Vps4 同时快速周转，每个 MVB 小泡伴随数轮组装/解聚（Adell et al., 2017）。人源体系的结果相似：亚基在 Vps4 作用下持续交换（Mierzwa et al., 2017），Vps4 先使 CHMP2A/CHMP3 管缩窄再切断（Maity et al., 2019）。

Vps4–Vta1 六聚体与 ESCRT-III 肽段的 cryo-EM 结构显示孔环逐个抓住底物、手递手穿孔易位（Monroe et al., 2017）；MIT 域与 Vps2 的 MIM 基序决定对亚基的选择性识别（Obita et al., 2007）。古菌硫化叶菌属（*Sulfolobus*）中复合 ESCRT-III 聚合体的图案化组装与 Vps4 逐步拆解驱动细胞分裂，提示“顺序聚合—拆解”相当古老（Hurtig et al., 2023）。综述见 McCullough et al., 2018；Pfitzner et al., 2021；Hill et al., 2012。

## 5. 内体身份：Rab 转换与磷酸肌醇

哺乳动物细胞中，单个内体上的 Rab5 被 Rab7 快速替换，称为 Rab 转换（Rink et al., 2005）；秀丽隐杆线虫（*Caenorhabditis elegans*）中，SAND-1/Mon1 置换 Rab5 的 GEF Rabex-5 并招募 Rab7，构成开关（Poteryaev et al., 2010）。酵母对应物是 Rab5 样 Vps21（Horazdovsky et al., 1994）与 Rab7 样 Ypt7。Mon1–Ccz1 是 Ypt7 的 GEF，并结合 Vps21-GTP（Nordmann et al., 2010）；它经 longin 折叠界面激活 Ypt7，且需 PI3P 阳性膜才高效工作（Cabrera et al., 2014）；晶体结构显示三个 longin 域构成催化核心（Kiontke et al., 2017）。体外重构实现了 Vps21-GTP 招募 Mon1–Ccz1 并激活 Ypt7 的级联，Mon1–Ccz1 受磷酸化调控（Langemeyer et al., 2020），其调控位点控制 Rab5→Rab7 转换的时序（Borchers et al., 2023）。终止端由 GAP 承担：Msb3/Gyp3 作用于 Vps21，也影响 Ypt7（Lachmann et al., 2012）。拴系复合体随 Rab 互换：CORVET 对应 Vps21，HOPS 对应 Ypt7，二者共享核心亚基（Balderhaar et al., 2013）；CORVET 特异亚基 Vps8 是 Vps21 的效应器，过表达时与 Vps21-GTP 共同诱导内体聚集（Markgraf et al., 2009）。

磷酸肌醇构成第二层编码。Vps34 是 PI 3-激酶，其活性为液泡蛋白分选所必需（Schu et al., 1993；Herman et al., 1990）；FYVE 域特异结合 PI3P（Burd et al., 1998），PI3P 富集于早期内体与 MVB 腔内小泡膜（Gillooly et al., 2000）；内体 Vps34 复合体 II 呈 V 形，靠多个膜结合位点工作（Rostislavleva et al., 2015）。PI3P 经 Fab1 磷酸化为 PI(3,5)P2：该脂质最早在酵母中被发现，高渗应激使其急剧升高（Dove et al., 1997）；Fab1 是 PI3P 5-激酶，缺失导致巨大液泡与膜稳态缺陷（Gary et al., 1998；Cooke et al., 1998）；*fab1* 突变体中货物滞留在液泡界膜，说明它为 MVB 腔内小泡形成所需（Odorizzi et al., 1998）。Vac14 作为支架把 Fab1 激酶与 Fig4 磷酸酶装配成复合体，使 PI3P 与 PI(3,5)P2 可快速互变（Jin et al., 2008；Rudge et al., 2004）；Svp1/Atg18 是 PI(3,5)P2 效应蛋白（Dove et al., 2004）；哺乳动物 PIKfyve–Vac14–Fig4 的 cryo-EM 结构显示 Vac14 五聚体支架（Lees et al., 2020）。综述见 Huotari et al., 2011；Dove et al., 2009。

## 6. 货物选择：泛素、Rsp5 与 ART

泛素作为内吞信号的第一个证据是 Ste2 尾部泛素化（Hicke et al., 1996）；*NPI1* 就是 *RSP5*，一种 HECT 型泛素连接酶，是 Gap1、Fur4 等转运蛋白诱导降解所必需（Hein et al., 1995）。但质膜蛋白种类繁多，单靠一个 Rsp5 做不到按货物区分的调控，需要接头。Lin 等发现 ART（arrestin-related trafficking adaptor）家族：Art1 介导 Can1 的营养诱导泛素化与内吞，由此提出 ART–Rsp5 网络（Lin et al., 2008）。系统分析 9 个 arrestin 样蛋白对多种转运蛋白的内吞，显示特异性与冗余并存（Nikko et al., 2009）。

接头本身受营养信号调控，且开关各不相同：TORC1–Npr1 激酶磷酸化抑制 Art1，把营养信号与转运蛋白内吞直接连接（MacGurn et al., 2011）；葡萄糖信号下 Rod1/Art4 经去磷酸化与泛素化被激活，介导 Jen1 内吞（Becuwe et al., 2012）；Art2 是维生素 B1 转运蛋白底物诱导内吞的关键调控者（Savocco et al., 2019）。

泛素链的类型在后一步起筛选作用：Rsp5 加上的单泛素足以内吞，但进入 MVB 需要 K63 连接的泛素链（Lauwers et al., 2009）。同一个修饰在内吞和 ESCRT 分选两处携带不同信息，于是调控分成三层：营养信号经激酶/磷酸酶改变 ART 的状态，ART 把 Rsp5 带到特定转运蛋白，泛素链类型再决定货物止于内吞还是进入 MVB。多泛素化货物与 ESCRT-0 能形成凝聚体（Banjade et al., 2022），该凝聚是否区分链型，本章文献未涉及。综述见 Lauwers et al., 2010；Piper et al., 2014；MacGurn et al., 2012。

## 7. 回收与分选路线：retromer、SNX、CPY/AP-3 与自噬交叉

**逆向回收。** Vps29/Vps30/Vps35 是液泡分选受体 Vps10 从内体回收到高尔基所必需（Seaman et al., 1997）；Vps35/Vps29/Vps26 与 Vps5/Vps17 组成 retromer，作为内体膜包被介导逆向运输（Seaman et al., 1998）。Vps35 C 端–Vps29 的晶体结构显示 Vps35 是长 α 螺线管（Hierro et al., 2007）；cryo-ET 子断层平均解出膜管上的 retromer–Vps5 包被：Vps26 二聚体贴膜，Vps35 形成拱形二聚体把包被撑离膜，可适应多种曲率（Kovtun et al., 2018）；哺乳动物 retromer–SNX3 的拱形排列相似但接触方式不同（Leneva et al., 2021）。分选连接蛋白（sorting nexin, SNX）形成并行途径：Snx4/Snx41/Snx42 构成独立于 retromer 的回收途径（Hettema et al., 2003），各 SNX 的货物谱部分重叠又各有特异性（Bean et al., 2017）。管状载体的分裂有两种说法：Vps1 促进 SNX-BAR 包被管分裂，*vps1*Δ 中载体管状化但不能切断（Chi et al., 2014）；Mvp1/SNX8 与 Vps1 又组成不依赖 retromer 的回收途径（Suzuki et al., 2021）。回收终点的分子机器有 Tlg1/Tlg2 syntaxin（Holthuis et al., 1998）、GARP 拴系复合体（Conibear et al., 2000），Snc1 从早期内体回到高尔基即是经典报告系统（Lewis et al., 2000）。综述见 Burd et al., 2014；Bonifacino et al., 2006；Cullen et al., 2018。

**去液泡的两条路。** Vps10 是 CPY 的分选受体（Marcusson et al., 1994），在晚期高尔基与前液泡区室间循环（Cooper et al., 1996）；AP-3 则介导 ALP 从高尔基直接到液泡、绕过前液泡区室（Cowles et al., 1997），该途径不依赖网格蛋白（Stepp et al., 1997），分选信号是 ALP 胞质尾的二亮氨酸样序列（Vowels et al., 1998）。综述见 Bowers et al., 2005；Bryant et al., 1998。

**内体是什么？** 4D 成像显示酵母 TGN 兼作早期内体，内吞货物直接进入 TGN，前液泡区室是唯一独立的晚期内体（Day et al., 2018）；更高分辨率的结果则在 TGN 内看到一个独立的早期/分选子区室（Toshima et al., 2023）。

**与自噬的交叉。** Atg20 与 Atg24 是结合 PI3P 的 PX 域蛋白，协同定位于 PAS（Nice et al., 2002）；Atg20 的 BAR 域有膜弯曲能力，并与 Snx4 共同促进自噬诱导（Popelka et al., 2017）。ESCRT 则作用于液泡界膜：微自噬依赖 ESCRT 与网格蛋白（Oku et al., 2017），ESCRT 可直接在液泡膜上分选泛素化膜蛋白（Zhu et al., 2017）。

## 定量与物理视角

**内陷的力平衡。** 一段半径 r、长度 L 的圆柱管内陷，每增加单位长度的能量由弯曲、张力与膨压三项构成，对 L 求导得到延伸力（忽略顶端帽）：

$$F \approx \underbrace{\pi r^{2}P}_{\text{膨压}} + \underbrace{\frac{\pi\kappa}{r}}_{\text{弯曲}} + \underbrace{2\pi\sigma r}_{\text{张力}}$$

取 r = 25 nm、弯曲模量 κ ≈ 20 k<sub>B</sub>T、张力 σ ≈ 0.1 mN/m（均为示意值），弯曲项约 10 pN，张力项约 16 pN，而 P = 0.2–1 MPa 时膨压项约 400–2000 pN（便记：1 MPa = 1 pN/nm²）。膨压项高出两个数量级，与降低膨压即可解除肌动蛋白依赖的观察一致（Aghamohammadzadeh et al., 2009），数量级也与数值模型给出的 10³ pN 相符（Carlsson et al., 2014；Dmitrieff et al., 2015）。Dmitrieff 等用 Helfrich 弯曲弹性加膨压的轴对称模型，表明点状拉力就能产生管状内陷；Zhang 等比较不同能量泛函与加载方式，指出模型假设会改变力阈值（Zhang et al., 2015）。Hassinger 等发现高膜张力下包被出芽存在 snap-through 失稳，需额外的力越过势垒（Hassinger et al., 2017）；周边蛋白密度与膜张力共同决定平坦→管状/泡状的形状转变（Shi et al., 2015）。Liu 等的力学化学模型把包被招募、肌动蛋白聚合、膜弯曲与相分离耦合，复现了时序（Liu et al., 2009）。

**肌动蛋白网络。** 单丝棘轮的停滞力 $f_s \approx (k_BT/\delta)\ln(k_{on}c/k_{off})$（δ ≈ 2.7 nm，k<sub>B</sub>T/δ ≈ 1.5 pN；此为教学用估算，不出自本章文献）仅为几 pN，所以 10³ pN 量级的力至少需要数百根丝并联。Carlsson 等的连续介质模型分析基部与顶端聚合如何决定力的大小与方向（Carlsson et al., 2014；综述见 Carlsson et al., 2018）；Nickaeen 等的有限元模型表明在实测 Arp2/3 聚合速率下网络力足以对抗膨压（Nickaeen et al., 2019；Nickaeen et al., 2022）；Cytosim 粒子模拟提出 Arp2/3 网络靠力反馈实现载荷自适应（Akamatsu et al., 2020）；基于计数数据的 ODE 模型显示快速拆解需要丝片段的释放（Berro et al., 2010）。分裂方面，Liu 等的相界线张力模型把能量写成 $E_{line}=2\pi r\gamma$，缩颈使之降低（Liu et al., 2006）。

**ESCRT-III 的弹性杆。** 把丝视为弹性杆，能量为 $E=\int\left[\tfrac{B}{2}(c-c_0)^2+\tfrac{C}{2}(\tau-\tau_0)^2\right]ds-wA_{adh}$（c 为曲率、τ 为扭率、w 为粘附能密度），持续长度 $\ell_p=B/k_BT$。Lenz 等给出固有弯曲丝使膜屈曲的长度判据（Lenz et al., 2009）；Fabrikant 等的圆顶模型（Fabrikant et al., 2009）与 Agudo-Canalejo 等的锥形模型比较表明锥形更易克服分裂势垒（Agudo-Canalejo et al., 2018）；粗粒化分子动力学表明丝几何由平螺旋变为锥形/螺旋线就足以成管并分裂（Harker-Kirschneck et al., 2019），分子动力学给出 ESCRT-III 丝的持续长度、弯曲与扭转刚度（Mandal et al., 2020）；弹性形状转变的综述见 Chiaruttini et al., 2017。酵母可提供的参数包括：螺旋几何（Chiaruttini et al., 2015）、Snf7 拷贝数（Teis et al., 2008）、招募与周转动力学（Adell et al., 2017）和 Vps4 产生的力（Schöneberg et al., 2018）。

**Rab 双稳态。** Rab5/Rab7 的自激活加交叉抑制可写成示意性的两变量 ODE（非原文方程）：$\dot a=s_a+\frac{v a^n}{K^n+a^n}\frac{1}{1+(b/K_i)^m}-\delta_a a$，b 同理。Del Conte-Zerial 等证明此类系统可表现为双稳态 toggle 或 cut-out 开关（Del Conte-Zerial et al., 2008）。酵母提供的约束有：Mon1–Ccz1 同时需要 Vps21-GTP 与 PI3P 膜（两个输入的符合检测，Cabrera et al., 2014；Langemeyer et al., 2020）和 GAP（Lachmann et al., 2012），缺的是原位浓度与结合常数。内体网络整体可用随机融合/分裂/成熟过程描述，并从内体大小与货物分布反推速率常数（Foret et al., 2012）。

**图像分析算法。** 多蛋白内吞事件的亚像素质心追踪与时序对齐（Picco et al., 2017），以及在裂殖酵母中把异步事件按连续时间对齐的“时序超分辨重对齐”（Berro et al., 2014），是从定量成像得到次序与参数的基础。

## 争议与开放问题

- **力究竟如何产生。** Carlsson 等估计需约数千 pN，Nickaeen 等认为实测聚合速率已足够，Dmitrieff 等认为点拉力即可，哺乳动物数据强调弹性回复与载荷自适应（Akamatsu et al., 2020）。唯一的活体力读数来自 Sla2 传感器（Abella et al., 2021），尚不足以裁决模型。
- **网格蛋白是否定形。** 内陷形状不依赖网格蛋白（Kukulski et al., 2016），但力学化学模型依赖包被—曲率反馈（Liu et al., 2009）。
- **分裂机制。** BAR（Youn et al., 2010）、Vps1（de Rooij et al., 2010）与线张力（Liu et al., 2006）的相对贡献未定。
- **ESCRT-III 的能量来源。** 弹簧弛豫（Chiaruttini et al., 2015）与顺序聚合—Vps4 主动交换（Pfitzner et al., 2020；Schöneberg et al., 2018）如何在同一个 MVB 颈部统一；主动重塑的部分证据来自人源蛋白与体外体系（Maity et al., 2019）。腔内小泡尺寸（约 25 nm 量级）由丝固有曲率、货物凝聚还是膜张力决定，也未解决。
- **内体是成熟还是区室间运输。** Rab 级联在酵母中已在体外重构（Langemeyer et al., 2020），但 Day 等的极简内膜系统与 Toshima 等的 TGN 子区室、经典前液泡区室之间尚未调和。
- **回收载体如何分裂。** Vps1 对 SNX-BAR 管（Chi et al., 2014）与对 Mvp1 途径（Suzuki et al., 2021）的作用并不等同。
- **ART 的组合逻辑。** 特异与冗余并存（Nikko et al., 2009），翻译后开关各不相同（MacGurn et al., 2011；Becuwe et al., 2012），能否有统一规则未知。
- **PI(3,5)P2 的局部浓度与寿命。** Fig4 是 5-磷酸酶，却与 Fab1 同处一个 Vac14 复合体（Rudge et al., 2004；Jin et al., 2008），它对 PI(3,5)P2 的净效应在动力学上如何成立，缺原位定量。

## 教科书写作建议

**配图**
1. 内吞时空图：横轴为时间，把 Kaksonen 等的模块时序与 Kukulski 等的平膜→浅坑→管状→小泡形态序列对齐，纵轴叠加 Picco 等的各蛋白相对顶端位置。
2. 力平衡对数条形图：弯曲、张力、膨压三项各约 10、16、10³ pN，旁附管状内陷示意图并标出 r 与 P。
3. ESCRT-III 两个模型并排：Chiaruttini 的螺旋弹簧能量图与 Pfitzner 的“平螺旋→锥形→管”序列，标明各自的证据体系（高速 AFM 与体外光镊/活酵母）。

**专栏**
1. 「从 CPY 分泌到 ESCRT」：1986 年的筛选如何经 class E 形态分类变成复合体名录（Bankaitis et al., 1986；Raymond et al., 1992；Katzmann et al., 2001）。
2. 「同一事件，两种酵母」：芽殖与裂殖酵母的内吞比较（Sun et al., 2019），说明哪些数据可跨物种借用（Sirotkin et al., 2010 的分子数、Basu et al., 2014 的膨压实验）。
3. 「Rab 转换的三方证据」：哺乳动物、线虫、酵母各自证明了什么（Rink et al., 2005；Poteryaev et al., 2010；Nordmann et al., 2010）。

**公式框**
1. 内陷力平衡 $F = \pi r^2P+\pi\kappa/r+2\pi\sigma r$ 的推导与量级估算。
2. 弹性杆能量与圆环弯曲能 $\pi B/R$。
3. 两变量 Rab 示意 ODE 的零斜线与鞍结分岔。

**习题**
1. 取 r = 25 nm，P = 0.2、0.5、1 MPa，计算三项力并解释降低膨压后肌动蛋白依赖消失。
2. 单丝停滞力取 3–5 pN，估算产生 10³ pN 需要多少根并联丝，并与单个斑块约 7000 个肌动蛋白分子比较。
3. 设 ℓ<sub>p</sub> = 1 μm，估算半径 25 nm 的 ESCRT-III 完整环的弯曲能（单位 k<sub>B</sub>T），再与球形芽的弯曲能 8πκ（取 κ = 20 k<sub>B</sub>T）比较。

## 与其他章的连接

- [[A03_质膜]]：PI(4,5)P2、膨压与细胞壁，即内吞位点所处的质膜环境。
- [[A06_高尔基体膜]]：TGN 兼作早期内体，GARP 与 Vps10 回收。
- [[A08_液泡膜]]：HOPS/Ypt7、PI(3,5)P2 与液泡大小、微自噬。
- [[A13_自噬体膜]]：Atg20/24 与 ESCRT 对自噬体封闭的贡献。
- [[A15_膜曲率融合分裂的分子机器]]：BAR、Vps1 与 ESCRT-III 的并列比较。
- [[A17_膜生物物理与脂质域_实验侧]]：Ede1 与 ESCRT-0 的凝聚。
- [[A18_方法学]]：CLEM、cryo-ET 与定量成像。
- [[B01_膜弹性曲率与形状能量]]：Helfrich 能量与管状内陷。
- [[B03_膜融合与分裂的物理]]：反向拓扑分裂与线张力。
- [[B05_非平衡与活性膜物理]]：肌动蛋白网络的主动力。
- [[C02_反应扩散与模式形成]]：Rab 域与内体身份。
- [[C05_动力系统与脂稳态建模]]：toggle/cut-out 开关与分岔分析。
- [[D01_分子动力学模拟]]：ESCRT-III 粗粒化模拟。
- [[D03_显微图像分析与深度学习]]：事件追踪与时序对齐。
- [[E01_演化视角]]：古菌 ESCRT-III 与内膜系统起源。

## 本章文献表

共 154 篇，全部经 CrossRef 核验 DOI 与题名；按重要性、年份降序。

| # | 引用 | 类型 | 重要性 | 一句话发现 | DOI |
|---|---|---|---|---|---|
| 1 | Pfitzner et al., 2020, *Cell* | primary | 5 | 在体外发现酵母 ESCRT-III 亚基按 Snf7→Vps24/Vps2→Did2→Ist1 顺序聚合，每一步改变丝的几何（平螺旋→锥形→管状），由 Vps4 驱动的亚基替换使膜逐步缩窄并分裂。 | [10.1016/j.cell.2020.07.021](https://doi.org/10.1016/j.cell.2020.07.021) |
| 2 | Kaksonen et al., 2018, *Nature Reviews Molecular Cell Biology* | review | 5 | 综述网格蛋白介导内吞从起始、包被组装、膜弯曲、分裂到脱包被的分子机制，并行比较酵母与哺乳动物系统，强调物理因素（膜张力、膨压）对机制差异的决定作用。 | [10.1038/nrm.2017.132](https://doi.org/10.1038/nrm.2017.132) |
| 3 | Schöneberg et al., 2018, *Science* | primary | 5 | 用光镊与膜纳米管重构酵母 ESCRT-III/Vps4，直接测得 Vps4 水解 ATP 时产生的力，并证明 ATP 依赖的亚基周转驱动膜管缩窄与分裂。 | [10.1126/science.aat1839](https://doi.org/10.1126/science.aat1839) |
| 4 | Kovtun et al., 2018, *Nature* | primary | 5 | 用 cryo-ET 子断层平均解出酵母 retromer 与 Vps5 在膜管上的组装结构：Vps26 二聚体贴膜、Vps35 形成拱形二聚体把包被撑离膜，揭示可适应多种曲率的包被几何。 | [10.1038/s41586-018-0526-z](https://doi.org/10.1038/s41586-018-0526-z) |
| 5 | Schöneberg et al., 2017, *Nature Reviews Molecular Cell Biology* | review | 5 | 系统比较 ESCRT-III 膜分裂的各种物理模型（锥形螺旋、弹簧弛豫、Vps4 驱动亚基交换），并总结结构与体外证据。 | [10.1038/nrm.2016.121](https://doi.org/10.1038/nrm.2016.121) |
| 6 | Picco et al., 2015, *eLife* | primary | 5 | 开发高精度质心追踪与时序对齐方法，测得 20 余种内吞蛋白相对于膜内陷顶端的纳米级位置与运动轨迹，绘出内吞机器随时间变化的空间架构图：包被蛋白随内陷顶端内移，肌动蛋白成核在基部而网络整体向内生长。 | [10.7554/elife.04535](https://doi.org/10.7554/elife.04535) |
| 7 | Goode et al., 2015, *Genetics* | review | 5 | YeastBook 综述，系统梳理酵母内吞的 60 余种蛋白、遗传学工具、时序模块及肌动蛋白调控网络。 | [10.1534/genetics.112.145540](https://doi.org/10.1534/genetics.112.145540) |
| 8 | Tang et al., 2015, *eLife* | primary | 5 | 解出 Snf7 核心域的晶体结构，揭示从闭合自抑制到开放活化构象的转变及丝内亚基界面，并鉴定膜结合的疏水/碱性表面。 | [10.7554/elife.12548](https://doi.org/10.7554/elife.12548) |
| 9 | Chiaruttini et al., 2015, *Cell* | primary | 5 | 用高速 AFM 观察 Snf7 在支撑双层上形成螺旋，证明螺旋被压缩偏离其优选曲率而储存弹性能，弛豫时可使膜变形，提出'螺旋弹簧'模型。 | [10.1016/j.cell.2015.10.017](https://doi.org/10.1016/j.cell.2015.10.017) |
| 10 | Kukulski et al., 2012, *Cell* | primary | 5 | 用相关光电显微（CLEM）把荧光时序与电子断层三维形貌对应，重建酵母内吞膜从平坦→浅坑→管状内陷→分裂的完整形态序列，并定量各阶段膜面积与曲率。 | [10.1016/j.cell.2012.05.046](https://doi.org/10.1016/j.cell.2012.05.046) |
| 11 | Henne et al., 2012, *Cell* | primary | 5 | 用电镜观察到 Snf7 在膜上形成螺旋/环状丝，发现 ESCRT-II 与 Vps20 的结合使 Snf7 成核为两条并行丝并决定螺旋结构，提出 ESCRT-II/III 协同决定膜颈几何。 | [10.1016/j.cell.2012.08.039](https://doi.org/10.1016/j.cell.2012.08.039) |
| 12 | MacGurn et al., 2012, *Annual Review of Biochemistry* | review | 5 | 综述泛素在膜蛋白质量控制、内吞、MVB 分选与降解全过程中的作用，重点讨论 Rsp5–ART 系统。 | [10.1146/annurev-biochem-060210-093619](https://doi.org/10.1146/annurev-biochem-060210-093619) |
| 13 | Henne et al., 2011, *Developmental Cell* | review | 5 | 综述 ESCRT 在 MVB、胞质分裂、病毒出芽中的共性机制，强调 ESCRT-III 聚合与 Vps4 在反向拓扑分裂中的核心地位。 | [10.1016/j.devcel.2011.05.015](https://doi.org/10.1016/j.devcel.2011.05.015) |
| 14 | Wollert et al., 2010, *Nature* | primary | 5 | 重构完整的 ESCRT-0/I/II/III 系统，显示 ESCRT-0 聚集泛素化货物，ESCRT-I/II 使膜出芽并把货物限制在芽内，ESCRT-III 在颈部切割，提出 MVB 形成的分工模型。 | [10.1038/nature08849](https://doi.org/10.1038/nature08849) |
| 15 | Nordmann et al., 2010, *Current Biology* | primary | 5 | 证明 Mon1-Ccz1 是 Ypt7 的鸟苷酸交换因子，并与 Vps21-GTP 结合，提示 Rab5→Rab7 级联在酵母中成立。 | [10.1016/j.cub.2010.08.002](https://doi.org/10.1016/j.cub.2010.08.002) |
| 16 | Wollert et al., 2009, *Nature* | primary | 5 | 在巨型单层囊泡上重构酵母 ESCRT-III 四个核心亚基，首次证明 ESCRT-III 足以把膜向囊泡内出芽并切割，Vps4 使之循环。 | [10.1038/nature07836](https://doi.org/10.1038/nature07836) |
| 17 | Lin et al., 2008, *Cell* | primary | 5 | 鉴定 ART 家族（α-arrestin）作为 Rsp5 接头，发现 Art1 介导 Can1 的营养诱导泛素化与内吞，提出 ART-Rsp5 网络模型。 | [10.1016/j.cell.2008.09.025](https://doi.org/10.1016/j.cell.2008.09.025) |
| 18 | Kaksonen et al., 2005, *Cell* | primary | 5 | 系统分析约 15 个内吞蛋白在 GFP 标记下的动态并结合缺失突变，把内吞机器划分为早期包被、晚期包被、WASP/Myo、肌动蛋白与两性蛋白四个功能模块，每个模块有独立的招募时序与功能。 | [10.1016/j.cell.2005.09.024](https://doi.org/10.1016/j.cell.2005.09.024) |
| 19 | Rink et al., 2005, *Cell* | primary | 5 | 在哺乳动物细胞中活体观察到单个内体上 Rab5 被 Rab7 快速替换，提出'Rab 转换'作为内体成熟的机制。 | [10.1016/j.cell.2005.06.043](https://doi.org/10.1016/j.cell.2005.06.043) |
| 20 | Kaksonen et al., 2003, *Cell* | primary | 5 | 用双色活细胞成像追踪 Ste2 受体、Sla1/Pan1 等接头与 Abp1 标记的肌动蛋白，首次建立酵母内吞事件的严格时序：包被蛋白先在质膜上静止累积，随后肌动蛋白短暂爆发驱动内陷与小泡内移。 | [10.1016/s0092-8674(03)00883-3](https://doi.org/10.1016/s0092-8674(03)00883-3) |
| 21 | Babst et al., 2002, *Developmental Cell* | primary | 5 | 鉴定 Vps22/Vps25/Vps36 组成的 ESCRT-II，并提出 ESCRT-I→II→III 顺序招募的级联模型。 | [10.1016/s1534-5807(02)00219-8](https://doi.org/10.1016/s1534-5807(02)00219-8) |
| 22 | Babst et al., 2002, *Developmental Cell* | primary | 5 | 鉴定 Vps20/Snf7/Vps24/Vps2 组成的 ESCRT-III，发现其在膜上组装为大寡聚体、受 Vps4 解聚，并证明其为 MVB 分选所需。 | [10.1016/s1534-5807(02)00220-4](https://doi.org/10.1016/s1534-5807(02)00220-4) |
| 23 | Katzmann et al., 2001, *Cell* | primary | 5 | 鉴定 Vps23/Vps28/Vps37 组成的 ESCRT-I 复合体，证明其识别泛素化货物并将其分选入 MVB 腔内小泡，确立泛素是 MVB 分选信号。 | [10.1016/s0092-8674(01)00434-2](https://doi.org/10.1016/s0092-8674(01)00434-2) |
| 24 | Odorizzi et al., 1998, *Cell* | primary | 5 | 发现 Fab1 产生的 PI(3,5)P2 为 MVB 腔内小泡形成与膜蛋白分选所必需，fab1 突变体中货物滞留在液泡界膜，首次把该脂质与 MVB 途径联系起来。 | [10.1016/s0092-8674(00)81707-9](https://doi.org/10.1016/s0092-8674(00)81707-9) |
| 25 | Seaman et al., 1998, *The Journal of Cell Biology* | primary | 5 | 生化鉴定 Vps35/Vps29/Vps26 与 Vps5/Vps17 组成的 retromer 复合体，并证明其作为内体膜包被介导逆向运输。 | [10.1083/jcb.142.3.665](https://doi.org/10.1083/jcb.142.3.665) |
| 26 | Gary et al., 1998, *The Journal of Cell Biology* | primary | 5 | 证明 Fab1 是 PI3P 5-激酶，fab1 突变体 PI(3,5)P2 缺失并出现巨大液泡与膜稳态缺陷。 | [10.1083/jcb.143.1.65](https://doi.org/10.1083/jcb.143.1.65) |
| 27 | Dove et al., 1997, *Nature* | primary | 5 | 首次在酵母中发现 PI(3,5)P2，并证明高渗应激使其水平急剧升高。 | [10.1038/36613](https://doi.org/10.1038/36613) |
| 28 | Cowles et al., 1997, *Cell* | primary | 5 | 发现 AP-3 复合体介导碱性磷酸酶 ALP 从高尔基直接到液泡、绕过前液泡区室的途径。 | [10.1016/s0092-8674(01)80013-1](https://doi.org/10.1016/s0092-8674(01)80013-1) |
| 29 | Hicke et al., 1996, *Cell* | primary | 5 | 证明 α 因子受体 Ste2 的配体诱导内吞需要其胞质尾部被泛素化，首次确立泛素作为内吞信号。 | [10.1016/s0092-8674(00)80982-4](https://doi.org/10.1016/s0092-8674(00)80982-4) |
| 30 | Marcusson et al., 1994, *Cell* | primary | 5 | 鉴定 Vps10 为 CPY 的跨膜分选受体，在高尔基结合 CPY 前肽并把它运往前液泡区室。 | [10.1016/0092-8674(94)90219-4](https://doi.org/10.1016/0092-8674(94)90219-4) |
| 31 | Schu et al., 1993, *Science* | primary | 5 | 证明 Vps34 是 PI 3-激酶，其激酶活性为液泡蛋白分选所必需，首次把 PI3P 与膜运输联系起来。 | [10.1126/science.8385367](https://doi.org/10.1126/science.8385367) |
| 32 | Raymond et al., 1992, *Molecular Biology of the Cell* | primary | 5 | 把 41 个 vps 互补群按液泡形态分为 A–F 六类，并发现 class E 突变体积累扩大的前液泡区室，后来证明 class E 基因就是 ESCRT 组分。 | [10.1091/mbc.3.12.1389](https://doi.org/10.1091/mbc.3.12.1389) |
| 33 | Kozak et al., 2022, *eLife* | primary | 4 | 发现早期包被蛋白 Ede1 通过多价相互作用在质膜上形成液态凝聚体，凝聚体的形成促进内吞位点起始； | [10.7554/elife.72865](https://doi.org/10.7554/elife.72865) |
| 34 | Serwas et al., 2022, *Developmental Cell* | primary | 4 | 用 cryo-ET 原位解析哺乳动物内吞位点肌动蛋白丝的取向、长度与分支角度，发现丝主要垂直或倾斜指向膜，为力产生几何提供直接结构证据。 | [10.1016/j.devcel.2022.04.012](https://doi.org/10.1016/j.devcel.2022.04.012) |
| 35 | Abella et al., 2021, *Developmental Cell* | primary | 4 | 在 Sla2 中插入 FRET 张力传感器，首次在活酵母中测得肌动蛋白经 Sla2 传递到膜的力，并显示力在内陷过程中随时间变化。 | [10.1016/j.devcel.2021.08.007](https://doi.org/10.1016/j.devcel.2021.08.007) |
| 36 | Pfitzner et al., 2021, *Trends in Cell Biology* | review | 4 | 总结 ESCRT-III 顺序聚合、亚基交换与几何变化驱动膜变形的新模型，统一体外与体内观察。 | [10.1016/j.tcb.2021.04.005](https://doi.org/10.1016/j.tcb.2021.04.005) |
| 37 | Akamatsu et al., 2020, *eLife* | primary | 4 | 结合哺乳动物细胞中肌动蛋白分子计数与 Cytosim 粒子模拟，提出 Arp2/3 网络通过力反馈实现载荷自适应，网络内部的弹性回复提供内陷力。 | [10.7554/elife.49840](https://doi.org/10.7554/elife.49840) |
| 38 | Vietri et al., 2020, *Nature Reviews Molecular Cell Biology* | review | 4 | 综述 ESCRT 在 MVB、膜修复、核膜封闭、自噬体封口、微自噬等广泛功能，强调共同的膜颈切割原理。 | [10.1038/s41580-019-0177-4](https://doi.org/10.1038/s41580-019-0177-4) |
| 39 | Langemeyer et al., 2020, *eLife* | primary | 4 | 在体外重构 Vps21-GTP 招募 Mon1-Ccz1 并激活 Ypt7 的级联，发现 Mon1-Ccz1 需先被磷酸化调控并与膜上 Rab5 结合，确立保守的 Rab 转换机制。 | [10.7554/elife.56090](https://doi.org/10.7554/elife.56090) |
| 40 | Sun et al., 2019, *eLife* | primary | 4 | 在同一成像条件下并列比较芽殖酵母与裂殖酵母的内吞蛋白时序与数量，发现核心时序与肌动蛋白依赖高度保守，但早期蛋白驻留时间、内吞位点密度等在两物种间可演化。 | [10.7554/elife.50749](https://doi.org/10.7554/elife.50749) |
| 41 | Nickaeen et al., 2019, *Molecular Biology of the Cell* | computational | 4 | 构建肌动蛋白聚合、交联与膜力学耦合的有限元计算模型，显示在实验测得的 Arp2/3 聚合速率下肌动蛋白网络能产生足以对抗膨压的力，并给出网络应力分布。 | [10.1091/mbc.e19-01-0059](https://doi.org/10.1091/mbc.e19-01-0059) |
| 42 | Harker-Kirschneck et al., 2019, *BMC Biology* | computational | 4 | 用粗粒化分子动力学模拟证明 ESCRT-III 丝从平螺旋变为锥形/螺旋线的几何变化足以驱动膜管形成与分裂，无需额外马达。 | [10.1186/s12915-019-0700-2](https://doi.org/10.1186/s12915-019-0700-2) |
| 43 | Mund et al., 2018, *Cell* | primary | 4 | 用超分辨单分子定位显微对 23 个内吞蛋白做系统的纳米尺度平均成像，发现肌动蛋白成核因子 Las17 等呈环状分布于内陷基部，Arp2/3 网络由此以几何图案组织，使力产生更高效。 | [10.1016/j.cell.2018.06.032](https://doi.org/10.1016/j.cell.2018.06.032) |
| 44 | Picco et al., 2018, *Molecular Biology of the Cell* | primary | 4 | 系统敲除或削弱各肌动蛋白调控因子后定量内陷动力学，区分出负责启动弯曲、延伸和分裂的不同肌动蛋白功能，并估算各步骤所需的网络性质。 | [10.1091/mbc.e17-11-0688](https://doi.org/10.1091/mbc.e17-11-0688) |
| 45 | Carlsson et al., 2018, *Current Opinion in Cell Biology* | review | 4 | 综述肌动蛋白聚合如何产生弯曲膜的力，比较推、拉、弹性回复等机制并总结各模型的力预测与实验验证现状。 | [10.1016/j.ceb.2017.11.007](https://doi.org/10.1016/j.ceb.2017.11.007) |
| 46 | McCullough et al., 2018, *Annual Review of Cell and Developmental Biology* | review | 4 | 综述 ESCRT-III 开放/闭合构象切换、丝状聚合体结构、Vps4 六聚体穿孔易位机制与膜重塑的动力学。 | [10.1146/annurev-cellbio-100616-060600](https://doi.org/10.1146/annurev-cellbio-100616-060600) |
| 47 | Day et al., 2018, *Developmental Cell* | primary | 4 | 用 4D 成像证明酵母 TGN 兼作早期内体，内吞货物直接进入 TGN； | [10.1016/j.devcel.2017.12.014](https://doi.org/10.1016/j.devcel.2017.12.014) |
| 48 | Cullen et al., 2018, *Nature Reviews Molecular Cell Biology* | review | 4 | 综述内体上'降解 vs 回收'的分子决策：retromer、retriever、SNX、ESCRT 的相互作用及其疾病意义。 | [10.1038/s41580-018-0053-7](https://doi.org/10.1038/s41580-018-0053-7) |
| 49 | Mierzwa et al., 2017, *Nature Cell Biology* | primary | 4 | 在人细胞中用定量成像发现 ESCRT-III 聚合体不是静态结构，其亚基在 Vps4 作用下持续交换，交换是膜重塑所必需。 | [10.1038/ncb3559](https://doi.org/10.1038/ncb3559) |
| 50 | Adell et al., 2017, *eLife* | primary | 4 | 用活酵母定量成像测得 ESCRT-III 与 Vps4 在内体上的招募动力学：Snf7 与 Vps4 同时且快速周转，每次 MVB 小泡形成伴随数轮组装/解聚循环。 | [10.7554/elife.31652](https://doi.org/10.7554/elife.31652) |
| 51 | Monroe et al., 2017, *eLife* | primary | 4 | 解出酵母 Vps4–Vta1 六聚体结合 ESCRT-III 肽段的 cryo-EM 结构，揭示螺旋排列的孔环逐个抓住底物并以手递手方式穿孔易位。 | [10.7554/elife.24487](https://doi.org/10.7554/elife.24487) |
| 52 | Chiaruttini et al., 2017, *Current Opinion in Cell Biology* | review | 4 | 从弹性杆理论角度综述 ESCRT-III 丝的曲率、扭转与聚合动力学如何共同决定膜变形模式。 | [10.1016/j.ceb.2017.07.002](https://doi.org/10.1016/j.ceb.2017.07.002) |
| 53 | Kiontke et al., 2017, *Nature Communications* | primary | 4 | 解出 Mon1-Ccz1 核心与 Ypt7 复合物的晶体结构，揭示三个 longin 域构成的催化核心及其打开 Rab 核苷酸口袋的机制。 | [10.1038/ncomms14034](https://doi.org/10.1038/ncomms14034) |
| 54 | Dmitrieff et al., 2015, *PLOS Computational Biology* | theory | 4 | 用 Helfrich 弹性膜加膨压的轴对称模型计算在膨压下形成内陷所需的力与能量，证明点状拉力即可产生酵母观察到的管状内陷形态，并预测力随内陷长度变化。 | [10.1371/journal.pcbi.1004538](https://doi.org/10.1371/journal.pcbi.1004538) |
| 55 | McCullough et al., 2015, *Science* | primary | 4 | 用 cryo-EM 解出人 IST1–CHMP1B 共聚管的近原子结构，揭示 ESCRT-III 开放构象与正曲率膜结合，提出 ESCRT-III 也可执行正常拓扑分裂。 | [10.1126/science.aad8305](https://doi.org/10.1126/science.aad8305) |
| 56 | Rostislavleva et al., 2015, *Science* | primary | 4 | 解出酵母 Vps34 复合体 II（Vps34/Vps15/Vps30/Vps38）的晶体结构，呈 V 形并通过多个膜结合位点在内体膜上工作。 | [10.1126/science.aac7365](https://doi.org/10.1126/science.aac7365) |
| 57 | Carlsson et al., 2014, *Biophysical Journal* | theory | 4 | 用肌动蛋白网络的连续介质模型估算酵母内吞斑块所能产生的力，分析聚合位置（基部 vs 顶端）与网络弹性如何决定力的大小与方向，得出内陷需约数千 pN。 | [10.1016/j.bpj.2014.02.035](https://doi.org/10.1016/j.bpj.2014.02.035) |
| 58 | Shen et al., 2014, *Journal of Cell Biology* | primary | 4 | 结合电镜与建模解析 Snf7 螺旋丝的亚基排列，发现核心域构象开放后通过侧向界面聚合，并提出螺旋曲率随圈数变化的力学模型。 | [10.1083/jcb.201403108](https://doi.org/10.1083/jcb.201403108) |
| 59 | Adell et al., 2014, *Journal of Cell Biology* | primary | 4 | 在酵母中证明 Vps4 通过 MIT 域与多个 ESCRT-III 亚基协同结合，在小泡形成过程中已被招募并驱动颈部缩窄，而非仅在分裂后拆解。 | [10.1083/jcb.201310114](https://doi.org/10.1083/jcb.201310114) |
| 60 | Cabrera et al., 2014, *Journal of Cell Science* | primary | 4 | 确定 Mon1-Ccz1 通过 longin 折叠界面激活 Ypt7，并需结合 PI3P 膜才能高效工作，把 Rab 转换与内体脂质偶联。 | [10.1242/jcs.140921](https://doi.org/10.1242/jcs.140921) |
| 61 | Burd et al., 2014, *Cold Spring Harbor Perspectives in Biology* | review | 4 | 综述 retromer 的组成、结构、与 SNX-BAR/Snx3 的组合及其在酵母和哺乳动物中的货物回收功能。 | [10.1101/cshperspect.a016774](https://doi.org/10.1101/cshperspect.a016774) |
| 62 | Piper et al., 2014, *Cold Spring Harbor Perspectives in Biology* | review | 4 | 综述泛素结合域、E3/DUB 在内吞与 ESCRT 分选中的作用，比较酵母与哺乳动物系统。 | [10.1101/cshperspect.a016808](https://doi.org/10.1101/cshperspect.a016808) |
| 63 | Basu et al., 2014, *Molecular Biology of the Cell* | primary | 4 | 在裂殖酵母中用渗透压调控膨压，发现降低膨压可部分绕过肌动蛋白需求并加快内吞，结合模型估算膨压对内陷的阻力。 | [10.1091/mbc.e13-10-0618](https://doi.org/10.1091/mbc.e13-10-0618) |
| 64 | Balderhaar et al., 2013, *Journal of Cell Science* | review | 4 | 综述共享核心亚基的 CORVET（Rab5/Vps21 效应）与 HOPS（Rab7/Ypt7 效应）复合体如何分别介导内体与液泡融合，提出两者随 Rab 转换互换的模型。 | [10.1242/jcs.107805](https://doi.org/10.1242/jcs.107805) |
| 65 | Skruzny et al., 2012, *Proceedings of the National Academy of Sciences* | primary | 4 | 证明 Sla2 的 ANTH 域与 Ent1 的 ENTH 域在 PI(4,5)P2 存在下共同组装，把膜与肌动蛋白网络物理耦联； | [10.1073/pnas.1207011109](https://doi.org/10.1073/pnas.1207011109) |
| 66 | Kukulski et al., 2011, *Journal of Cell Biology* | method | 4 | 建立在树脂切片中保留荧光并用荧光珠做基准进行纳米精度配准的 CLEM 方法，使单个内吞事件的荧光状态可与电子断层形态逐一对应。 | [10.1083/jcb.201009037](https://doi.org/10.1083/jcb.201009037) |
| 67 | Huotari et al., 2011, *The EMBO Journal* | review | 4 | 综述内体成熟的全过程：Rab 转换、PI3P→PI(3,5)P2、酸化、腔内小泡形成与运动，整合为统一框架。 | [10.1038/emboj.2011.286](https://doi.org/10.1038/emboj.2011.286) |
| 68 | MacGurn et al., 2011, *Cell* | primary | 4 | 发现 TORC1–Npr1 激酶通过磷酸化抑制 Art1，把营养信号与转运蛋白内吞直接联系。 | [10.1016/j.cell.2011.09.054](https://doi.org/10.1016/j.cell.2011.09.054) |
| 69 | Sirotkin et al., 2010, *Molecular Biology of the Cell* | primary | 4 | 用定量荧光显微计数裂殖酵母单个内吞斑块中 16 种蛋白的分子数随时间变化（肌动蛋白峰值约 7000 分子），建立内吞机器的化学计量时间表。 | [10.1091/mbc.e10-02-0157](https://doi.org/10.1091/mbc.e10-02-0157) |
| 70 | Poteryaev et al., 2010, *Cell* | primary | 4 | 在线虫中发现 SAND-1/Mon1 通过置换 Rab5 GEF Rabex-5 并招募 Rab7 实现 Rab 转换开关。 | [10.1016/j.cell.2010.03.011](https://doi.org/10.1016/j.cell.2010.03.011) |
| 71 | Lauwers et al., 2010, *Trends in Cell Biology* | review | 4 | 综述单泛素、K63 链等不同泛素修饰在酵母转运蛋白内吞、回收与 MVB 分选中的差异化作用。 | [10.1016/j.tcb.2010.01.004](https://doi.org/10.1016/j.tcb.2010.01.004) |
| 72 | Aghamohammadzadeh et al., 2009, *Nature Cell Biology* | primary | 4 | 通过降低酵母膨压（渗透支持或细胞壁缺陷）发现肌动蛋白对内吞的绝对需求被解除，而哺乳动物细胞提高膜张力后反而变得依赖肌动蛋白。 | [10.1038/ncb1918](https://doi.org/10.1038/ncb1918) |
| 73 | Liu et al., 2009, *PLoS Biology* | theory | 4 | 建立把包被蛋白招募、肌动蛋白聚合、膜弯曲与脂质相分离耦合的力学-化学模型，复现酵母内吞蛋白时序与内陷形态，提出曲率依赖的反馈是时序自组织的来源。 | [10.1371/journal.pbio.1000204](https://doi.org/10.1371/journal.pbio.1000204) |
| 74 | Saksena et al., 2009, *Cell* | primary | 4 | 用纯化酵母蛋白在脂质体上重构 ESCRT-III 的 Vps20 成核、Snf7 聚合、Vps24/Vps2 封端以及 Vps4 依赖的解聚循环，提出 Snf7 聚合受自抑制控制。 | [10.1016/j.cell.2008.11.013](https://doi.org/10.1016/j.cell.2008.11.013) |
| 75 | Lenz et al., 2009, *Physical Review Letters* | theory | 4 | 用弹性理论证明吸附在膜上的固有弯曲丝（如 ESCRT-III）当长度超过阈值时会使膜屈曲形成管状/出芽结构，给出屈曲判据。 | [10.1103/physrevlett.103.038101](https://doi.org/10.1103/physrevlett.103.038101) |
| 76 | Fabrikant et al., 2009, *PLoS Computational Biology* | theory | 4 | 建立 ESCRT-III 圆顶（dome）模型：丝聚合为倒锥形圆顶，膜与圆顶的粘附能驱使颈部缩窄至半融合从而分裂，并计算所需能量。 | [10.1371/journal.pcbi.1000575](https://doi.org/10.1371/journal.pcbi.1000575) |
| 77 | Nikko et al., 2009, *Traffic* | primary | 4 | 系统分析 9 个 arrestin 样蛋白对多种转运蛋白的内吞作用，显示特异性与冗余并存。 | [10.1111/j.1600-0854.2009.00990.x](https://doi.org/10.1111/j.1600-0854.2009.00990.x) |
| 78 | Dove et al., 2009, *Biochemical Journal* | review | 4 | 综述 PI(3,5)P2 的合成、效应器与在内体-溶酶体功能中的作用。 | [10.1042/bj20081950](https://doi.org/10.1042/bj20081950) |
| 79 | Teis et al., 2008, *Developmental Cell* | primary | 4 | 证明 ESCRT-III 亚基按 Vps20→Snf7→Vps24→Vps2 顺序组装，Snf7 为主要聚合单元（每个复合体约数十拷贝），聚合体形成是货物隔离所必需。 | [10.1016/j.devcel.2008.08.013](https://doi.org/10.1016/j.devcel.2008.08.013) |
| 80 | Hanson et al., 2008, *The Journal of Cell Biology* | primary | 4 | 过表达人 CHMP4 时在质膜下观察到环状/螺旋丝阵列，并能使质膜向外突起，首次在细胞内看到 ESCRT-III 丝状聚合体及其膜变形能力。 | [10.1083/jcb.200707031](https://doi.org/10.1083/jcb.200707031) |
| 81 | Del et al., 2008, *Molecular Systems Biology* | theory | 4 | 建立 Rab5/Rab7 正反馈与交叉抑制的 ODE 模型，证明系统可表现为双稳态 toggle 或 cut-out 开关，解释内体身份的突变式转换。 | [10.1038/msb.2008.45](https://doi.org/10.1038/msb.2008.45) |
| 82 | Hierro et al., 2007, *Nature* | primary | 4 | 解出 Vps35 C 端–Vps29 复合物晶体结构，揭示 Vps35 为长 α 螺线管、Vps29 结合其一端，提出货物识别亚复合体的架构。 | [10.1038/nature06216](https://doi.org/10.1038/nature06216) |
| 83 | Kaksonen et al., 2006, *Nature Reviews Molecular Cell Biology* | review | 4 | 综述肌动蛋白在内吞各步骤的作用，提出肌动蛋白网络以'推拉'方式提供内陷力的模型，并比较酵母与哺乳动物。 | [10.1038/nrm1940](https://doi.org/10.1038/nrm1940) |
| 84 | Liu et al., 2006, *Proceedings of the National Academy of Sciences* | theory | 4 | 提出脂质相界面线张力驱动内吞小泡分裂的理论模型：BAR 蛋白与脂质酶在管颈部造成相分离，相界面的线张力足以在无发动蛋白时完成缩颈分裂。 | [10.1073/pnas.0601045103](https://doi.org/10.1073/pnas.0601045103) |
| 85 | Hurley et al., 2006, *Annual Review of Biophysics and Biomolecular Structure* | review | 4 | 系统整理 ESCRT-0/I/II/III 与 Vps4 的早期晶体结构与相互作用网络，提出泛素-脂质-蛋白协同识别的结构框架。 | [10.1146/annurev.biophys.35.040405.102126](https://doi.org/10.1146/annurev.biophys.35.040405.102126) |
| 86 | Bowers et al., 2005, *Biochimica et Biophysica Acta (BBA) - Molecular Cell Research* | review | 4 | 综述 CPY 途径、AP-3 途径与 MVB 途径的分子机制及 vps 基因功能分类。 | [10.1016/j.bbamcr.2005.04.004](https://doi.org/10.1016/j.bbamcr.2005.04.004) |
| 87 | Katzmann et al., 2003, *The Journal of Cell Biology* | primary | 4 | 证明 Vps27（ESCRT-0）通过 FYVE 域结合 PI3P 并通过 PSDP 基序直接招募 ESCRT-I 到内体，把 PI3P、泛素与 ESCRT 级联串联。 | [10.1083/jcb.200302136](https://doi.org/10.1083/jcb.200302136) |
| 88 | Hettema et al., 2003, *The EMBO Journal* | primary | 4 | 发现 Snx4/Snx41/Snx42 构成与 retromer 独立的回收途径，分别从早期内体回收 Snc1 等货物。 | [10.1093/emboj/cdg062](https://doi.org/10.1093/emboj/cdg062) |
| 89 | Nice et al., 2002, *Journal of Biological Chemistry* | primary | 4 | 鉴定 Atg20（Cvt20）与 Atg24（Cvt13）为 PX 域 PI3P 结合蛋白，二者协同定位于 PAS 并为选择性自噬所需。 | [10.1074/jbc.m204736200](https://doi.org/10.1074/jbc.m204736200) |
| 90 | Gillooly et al., 2000, *The EMBO Journal* | primary | 4 | 用 FYVE 探针与免疫电镜定位 PI3P，发现其富集于早期内体与 MVB 腔内小泡膜上。 | [10.1093/emboj/19.17.4577](https://doi.org/10.1093/emboj/19.17.4577) |
| 91 | Babst et al., 1998, *The EMBO Journal* | primary | 4 | 证明 Vps4 的 ATP 酶活性控制 class E Vps 蛋白从内体膜解离，ATP 酶失活突变使复合体滞留在膜上。 | [10.1093/emboj/17.11.2982](https://doi.org/10.1093/emboj/17.11.2982) |
| 92 | Burd et al., 1998, *Molecular Cell* | primary | 4 | 证明 FYVE 域（Vps27、Vac1 等）特异结合 PI3P，建立 PI3P→FYVE 蛋白招募的信号逻辑。 | [10.1016/s1097-2765(00)80125-2](https://doi.org/10.1016/s1097-2765(00)80125-2) |
| 93 | Bryant et al., 1998, *Microbiology and Molecular Biology Reviews* | review | 4 | 系统综述 vps 突变体分类、CPY/ALP/内吞途径与前液泡区室的概念。 | [10.1128/mmbr.62.1.230-247.1998](https://doi.org/10.1128/mmbr.62.1.230-247.1998) |
| 94 | Seaman et al., 1997, *The Journal of Cell Biology* | primary | 4 | 发现 Vps29/Vps30/Vps35 为 Vps10 受体从内体回收到高尔基所需，奠定 retromer 的遗传基础。 | [10.1083/jcb.137.1.79](https://doi.org/10.1083/jcb.137.1.79) |
| 95 | Stepp et al., 1997, *The Journal of Cell Biology* | primary | 4 | 独立证明 AP-3 为 ALP 替代途径所需，并显示该途径不依赖网格蛋白。 | [10.1083/jcb.139.7.1761](https://doi.org/10.1083/jcb.139.7.1761) |
| 96 | Cooper et al., 1996, *The Journal of cell biology* | primary | 4 | 证明 Vps10 在晚期高尔基与前液泡区室间循环，其胞质尾部决定回收。 | [10.1083/jcb.133.3.529](https://doi.org/10.1083/jcb.133.3.529) |
| 97 | Hein et al., 1995, *Molecular Microbiology* | primary | 4 | 发现 NPI1 即 Rsp5 HECT E3，是 Gap1/Fur4 等转运蛋白诱导降解所必需。 | [10.1111/j.1365-2958.1995.mmi_18010077.x](https://doi.org/10.1111/j.1365-2958.1995.mmi_18010077.x) |
| 98 | Horazdovsky et al., 1994, *The EMBO Journal* | primary | 4 | 克隆 VPS21 并证明其编码 Rab5 样 GTP 酶，为 CPY 分选与内体功能所需。 | [10.1002/j.1460-2075.1994.tb06382.x](https://doi.org/10.1002/j.1460-2075.1994.tb06382.x) |
| 99 | Kübler et al., 1993, *The EMBO Journal* | primary | 4 | 利用 act1 与 sac6（fimbrin）突变体证明酵母 α 因子受体的内化步骤需要肌动蛋白细胞骨架，首次把肌动蛋白与内吞直接联系起来。 | [10.1002/j.1460-2075.1993.tb05947.x](https://doi.org/10.1002/j.1460-2075.1993.tb05947.x) |
| 100 | Bankaitis et al., 1986, *Proceedings of the National Academy of Sciences* | primary | 4 | 用 CPY-转化酶融合蛋白分泌筛选获得首批 vpt/vps 突变体。 | [10.1073/pnas.83.23.9075](https://doi.org/10.1073/pnas.83.23.9075) |
| 101 | Rothman et al., 1986, *Cell* | primary | 4 | 分离分泌 CPY 的 vpl/vps 突变体，证明液泡蛋白错分选进入晚期分泌途径。 | [10.1016/0092-8674(86)90819-6](https://doi.org/10.1016/0092-8674(86)90819-6) |
| 102 | Borchers et al., 2023, *Proceedings of the National Academy of Sciences* | primary | 3 | 鉴定 Mon1-Ccz1 上的磷酸化与膜结合调控位点，证明它们控制 Rab5→Rab7 转换时序与内体成熟。 | [10.1073/pnas.2303750120](https://doi.org/10.1073/pnas.2303750120) |
| 103 | Toshima et al., 2023, *eLife* | primary | 3 | 用高分辨成像发现内吞货物先进入 TGN 内一个独立的早期/分选子区室，再分流到 PVE 或回收，部分调和 Day 2018 与经典早期内体观点。 | [10.7554/elife.84850](https://doi.org/10.7554/elife.84850) |
| 104 | Nickaeen et al., 2022, *Molecular Biology of the Cell* | computational | 3 | 扩展肌动蛋白驱动内吞模型，解释芽殖酵母与裂殖酵母内吞斑块运动差异源于网络成核位置与交联差异。 | [10.1091/mbc.e21-07-0362](https://doi.org/10.1091/mbc.e21-07-0362) |
| 105 | Jukic et al., 2022, *Nature Communications* | primary | 3 | 用高速 AFM 与曲率可控的膜发现 Snf7 螺旋优先在特定曲率成核并能主动改变膜曲率，给出曲率感知与生成的定量关系。 | [10.1038/s41467-022-29850-z](https://doi.org/10.1038/s41467-022-29850-z) |
| 106 | Banjade et al., 2022, *Science Advances* | primary | 3 | 发现 ESCRT-0 与多泛素化货物通过多价相互作用形成凝聚体，相分离促进货物在内体上的聚集与分选。 | [10.1126/sciadv.abm5149](https://doi.org/10.1126/sciadv.abm5149) |
| 107 | Leneva et al., 2021, *Science Advances* | primary | 3 | 解出哺乳动物 retromer–SNX3 在膜管上的 cryo-ET 结构，显示与酵母拱形排列相似但接触方式不同，货物与 SNX3 共同决定包被几何。 | [10.1126/sciadv.abf8598](https://doi.org/10.1126/sciadv.abf8598) |
| 108 | Suzuki et al., 2021, *eLife* | primary | 3 | 发现 Mvp1 与 Vps1 组成不依赖 retromer 的内体回收途径，Mvp1 四聚体使膜管状化、Vps1 分裂，回收多种膜蛋白。 | [10.7554/elife.69883](https://doi.org/10.7554/elife.69883) |
| 109 | Mandal et al., 2020, *Biophysical Journal* | computational | 3 | 用分子动力学计算 ESCRT-III 丝的持续长度、弯曲与扭转刚度，并模拟其在膜上的曲率诱导效应。 | [10.1016/j.bpj.2020.01.033](https://doi.org/10.1016/j.bpj.2020.01.033) |
| 110 | Lees et al., 2020, *Molecular Cell* | primary | 3 | 解出 PIKfyve–Vac14–Fig4 复合体的 cryo-EM 结构，揭示 Vac14 五聚体支架与激酶/磷酸酶的排列。 | [10.1016/j.molcel.2020.10.003](https://doi.org/10.1016/j.molcel.2020.10.003) |
| 111 | Lacy et al., 2019, *eLife* | primary | 3 | 用单分子光漂白与追踪测量裂殖酵母内吞位点上肌动蛋白与包被蛋白的周转：肌动蛋白亚基在位点上停留极短且持续交换，而包被蛋白稳定结合。 | [10.7554/elife.52355](https://doi.org/10.7554/elife.52355) |
| 112 | Planade et al., 2019, *PLOS Biology* | primary | 3 | 在体外用酵母提取物重构肌动蛋白斑块并以 AFM 测量其刚度，发现斑块刚度与对应突变株的内吞效率高度相关，提示网络力学性质而非聚合量决定内吞成败。 | [10.1371/journal.pbio.3000500](https://doi.org/10.1371/journal.pbio.3000500) |
| 113 | Banjade et al., 2019, *eLife* | primary | 3 | 用遗传互补与体外聚合实验证明 Snf7 与 Vps24/Vps2 间的侧向静电相互作用决定异聚体形成与膜分裂功能。 | [10.7554/elife.46207](https://doi.org/10.7554/elife.46207) |
| 114 | Maity et al., 2019, *Science Advances* | primary | 3 | 用高速 AFM 实时观察 Vps4 作用于 CHMP2A/CHMP3 螺旋管，发现 Vps4 先使管缩窄再切断，支持 Vps4 主动重塑模型。 | [10.1126/sciadv.aau7198](https://doi.org/10.1126/sciadv.aau7198) |
| 115 | Agudo-Canalejo et al., 2018, *PLOS Computational Biology* | theory | 3 | 用膜弹性理论比较圆顶与锥形 ESCRT 结构通过粘附驱动膜分裂的能量景观，指出锥形结构更有利于克服分裂势垒。 | [10.1371/journal.pcbi.1006422](https://doi.org/10.1371/journal.pcbi.1006422) |
| 116 | Hassinger et al., 2017, *Proceedings of the National Academy of Sciences* | theory | 3 | 用弹性膜模型发现在高膜张力下包被诱导的出芽存在 snap-through 失稳，需要额外的力（如肌动蛋白）跨越能量势垒，解释膜张力决定肌动蛋白需求。 | [10.1073/pnas.1617705114](https://doi.org/10.1073/pnas.1617705114) |
| 117 | Picco et al., 2017, *Methods in Cell Biology* | method | 3 | 详述多蛋白内吞事件的自动检测、质心亚像素追踪、时序对齐与平均轨迹计算的算法流程与软件实现。 | [10.1016/bs.mcb.2016.11.002](https://doi.org/10.1016/bs.mcb.2016.11.002) |
| 118 | Bean et al., 2017, *Traffic* | primary | 3 | 系统分析酵母各 SNX 对货物的选择性，发现 Snx3、Snx4 复合体与 retromer 的货物谱部分重叠又有特异性。 | [10.1111/tra.12459](https://doi.org/10.1111/tra.12459) |
| 119 | Popelka et al., 2017, *Proceedings of the National Academy of Sciences* | primary | 3 | 解出 Atg20 BAR 域结构并证明其膜弯曲能力与 Snx4 共同促进自噬诱导。 | [10.1073/pnas.1708367114](https://doi.org/10.1073/pnas.1708367114) |
| 120 | Zhu et al., 2017, *eLife* | primary | 3 | 证明 ESCRT 可直接在液泡膜上把泛素化液泡膜蛋白分选入腔内，不经过内体 MVB。 | [10.7554/elife.26403](https://doi.org/10.7554/elife.26403) |
| 121 | Oku et al., 2017, *Journal of Cell Biology* | primary | 3 | 发现酵母液泡膜微自噬依赖 ESCRT 与网格蛋白，把 MVB 机制延伸到液泡界膜内陷。 | [10.1083/jcb.201611029](https://doi.org/10.1083/jcb.201611029) |
| 122 | Kukulski et al., 2016, *eLife* | primary | 3 | 用 CLEM 比较野生型与网格蛋白缺失株的内陷形态，发现网格蛋白并不决定内陷形状，而是影响分裂位置与小泡大小。 | [10.7554/elife.16036](https://doi.org/10.7554/elife.16036) |
| 123 | Zhang et al., 2015, *Biophysical Journal* | theory | 3 | 系统比较不同膜能量泛函与力加载方式在膨压下对内陷形态与力阈值的预测，指出模型假设如何改变力的估算。 | [10.1016/j.bpj.2014.11.3481](https://doi.org/10.1016/j.bpj.2014.11.3481) |
| 124 | Berro et al., 2014, *Molecular Biology of the Cell* | method | 3 | 提出'时序超分辨重对齐'算法，把多个异步内吞事件按连续时间对齐以提高时间分辨率，并据此解析斑块各蛋白的到达次序。 | [10.1091/mbc.e13-01-0004](https://doi.org/10.1091/mbc.e13-01-0004) |
| 125 | Chi et al., 2014, *Journal of Cell Biology* | primary | 3 | 证明发动蛋白样 Vps1 定位于 SNX-BAR 包被的内体管并促进其分裂，vps1Δ 中逆向运输载体管状化但不能切割。 | [10.1083/jcb.201309084](https://doi.org/10.1083/jcb.201309084) |
| 126 | Weinberg et al., 2012, *Trends in Cell Biology* | review | 3 | 总结酵母内吞各阶段的分子事件，提出'包被成熟检查点'等概念，并讨论膜脂（PI(4,5)P2）与肌动蛋白的协同。 | [10.1016/j.tcb.2011.09.001](https://doi.org/10.1016/j.tcb.2011.09.001) |
| 127 | Hill et al., 2012, *Biochimica et Biophysica Acta (BBA) - Molecular Cell Research* | review | 3 | 综述 Vps4 的 MIT 域、AAA 环与辅因子 Vta1 的结构及其与 ESCRT-III MIM 基序的识别。 | [10.1016/j.bbamcr.2011.08.017](https://doi.org/10.1016/j.bbamcr.2011.08.017) |
| 128 | Lachmann et al., 2012, *Molecular Biology of the Cell* | primary | 3 | 鉴定 Msb3/Gyp3 为 Vps21 的 GAP，证明 GAP 活性对终止 Rab5 信号与内体成熟的重要性。 | [10.1091/mbc.e11-12-1030](https://doi.org/10.1091/mbc.e11-12-1030) |
| 129 | Russell et al., 2012, *Journal of Cell Science* | primary | 3 | 发现 class E 区室的形成源于 ESCRT 缺陷导致 Vps21 持续活化与内体过度融合，而非单纯 MVB 停滞。 | [10.1242/jcs.111310](https://doi.org/10.1242/jcs.111310) |
| 130 | Foret et al., 2012, *Current Biology* | theory | 3 | 提出用随机融合/分裂/成熟过程描述内体网络，并从定量图像的内体大小与货物分布反推速率常数。 | [10.1016/j.cub.2012.06.021](https://doi.org/10.1016/j.cub.2012.06.021) |
| 131 | Becuwe et al., 2012, *Journal of Cell Biology* | primary | 3 | 发现 Rod1/Art4 在葡萄糖信号下经去磷酸化与泛素化激活，介导 Jen1 内吞，提出 ART 的翻译后修饰开关。 | [10.1083/jcb.201109113](https://doi.org/10.1083/jcb.201109113) |
| 132 | Rooij et al., 2010, *Journal of Cell Science* | primary | 3 | 发现发动蛋白样 Vps1 定位于内吞位点并参与内陷与分裂，vps1Δ 导致内陷延长与分裂缺陷，提示酵母也存在发动蛋白依赖的分裂贡献。 | [10.1242/jcs.070508](https://doi.org/10.1242/jcs.070508) |
| 133 | Berro et al., 2010, *Molecular Biology of the Cell* | theory | 3 | 基于定量计数数据建立裂殖酵母内吞肌动蛋白斑块组装与拆解的 ODE 模型，发现单体解离不足以解释快速拆解，需要丝片段的释放（切断）。 | [10.1091/mbc.e10-06-0494](https://doi.org/10.1091/mbc.e10-06-0494) |
| 134 | Youn et al., 2010, *Molecular Biology of the Cell* | primary | 3 | 通过结构导向突变与活细胞成像解析 Rvs161/Rvs167 异二聚体 BAR 域的膜结合与弯曲功能，证明 BAR 域在内陷管颈部组装并促进分裂。 | [10.1091/mbc.e10-03-0181](https://doi.org/10.1091/mbc.e10-03-0181) |
| 135 | Lauwers et al., 2009, *Journal of Cell Biology* | primary | 3 | 证明 Rsp5 对 Gap1 等转运蛋白加上 K63 连接的泛素链是进入 MVB 的特异信号，单泛素足以内吞但不足以 MVB 分选。 | [10.1083/jcb.200810114](https://doi.org/10.1083/jcb.200810114) |
| 136 | Markgraf et al., 2009, *Molecular Biology of the Cell* | primary | 3 | 证明 CORVET 特异亚基 Vps8 作为 Vps21 效应器，过表达时与 Vps21-GTP 共同诱导内体聚集，支持 CORVET 为 Rab5 依赖的内体拴系复合体。 | [10.1091/mbc.e09-06-0521](https://doi.org/10.1091/mbc.e09-06-0521) |
| 137 | Jin et al., 2008, *The EMBO Journal* | primary | 3 | 证明 Vac14 作为支架把 Fab1 激酶与 Fig4 磷酸酶组装为一个复合体，使 PI3P 与 PI(3,5)P2 可快速互变。 | [10.1038/emboj.2008.248](https://doi.org/10.1038/emboj.2008.248) |
| 138 | Nickerson et al., 2007, *The EMBO Reports* | theory | 3 | 提出 MVB 分选的同心圆模型：ESCRT-0/I/II 在外圈浓缩货物，ESCRT-III 在内圈形成分裂环，几何上解释货物如何被包入小泡。 | [10.1038/sj.embor.7401004](https://doi.org/10.1038/sj.embor.7401004) |
| 139 | Obita et al., 2007, *Nature* | primary | 3 | 解出 Vps4 MIT 域与 ESCRT-III（Vps2）C 端 MIM 基序复合物结构，解释 Vps4 如何选择性识别特定 ESCRT-III 亚基。 | [10.1038/nature06171](https://doi.org/10.1038/nature06171) |
| 140 | Kostelansky et al., 2007, *Cell* | primary | 3 | 解出酵母 ESCRT-I 四聚体（Vps23/Vps28/Vps37/Mvb12）的晶体结构，显示其为约 18 nm 的长杆状分子，两端分别结合泛素/ESCRT-0 与 ESCRT-II。 | [10.1016/j.cell.2007.03.016](https://doi.org/10.1016/j.cell.2007.03.016) |
| 141 | Bonifacino et al., 2006, *Nature Reviews Molecular Cell Biology* | review | 3 | 综述内体到 TGN 逆向运输的包被（retromer、网格蛋白/AP-1）、拴系（GARP）与 SNARE 机制。 | [10.1038/nrm1985](https://doi.org/10.1038/nrm1985) |
| 142 | Dove et al., 2004, *The EMBO Journal* | primary | 3 | 鉴定 Svp1/Atg18 为 PI(3,5)P2 效应蛋白（PROPPIN 家族），介导液泡膜回收。 | [10.1038/sj.emboj.7600203](https://doi.org/10.1038/sj.emboj.7600203) |
| 143 | Rudge et al., 2004, *Molecular Biology of the Cell* | primary | 3 | 鉴定 Fig4 为 PI(3,5)P2 5-磷酸酶并与 Vac14 结合，共同调控液泡大小。 | [10.1091/mbc.e03-05-0297](https://doi.org/10.1091/mbc.e03-05-0297) |
| 144 | Engqvist-Goldstein et al., 2003, *Annual Review of Cell and Developmental Biology* | review | 3 | 早期经典综述，比较酵母与哺乳动物中肌动蛋白对内吞的贡献，并提出肌动蛋白可提供内陷、分裂与小泡运动的力。 | [10.1146/annurev.cellbio.19.111401.093127](https://doi.org/10.1146/annurev.cellbio.19.111401.093127) |
| 145 | Lewis et al., 2000, *Molecular Biology of the Cell* | primary | 3 | 用 GFP-Snc1 建立内吞-回收报告系统，证明 Snc1 从早期内体经 Tlg1/Tlg2 依赖途径回到高尔基再分泌。 | [10.1091/mbc.11.1.23](https://doi.org/10.1091/mbc.11.1.23) |
| 146 | Conibear et al., 2000, *Molecular Biology of the Cell* | primary | 3 | 鉴定 GARP 复合体（Vps52/53/54）为内体到晚期高尔基逆向运输的拴系因子。 | [10.1091/mbc.11.1.305](https://doi.org/10.1091/mbc.11.1.305) |
| 147 | Cooke et al., 1998, *Current Biology* | primary | 3 | 独立证明 Fab1 为应激激活的 PI3P 5-激酶并为液泡功能所需。 | [10.1016/s0960-9822(07)00513-1](https://doi.org/10.1016/s0960-9822(07)00513-1) |
| 148 | Vowels et al., 1998, *The EMBO Journal* | primary | 3 | 鉴定 ALP 胞质尾的二亮氨酸样信号为 AP-3 途径的分选信号。 | [10.1093/emboj/17.9.2482](https://doi.org/10.1093/emboj/17.9.2482) |
| 149 | Holthuis et al., 1998, *The EMBO Journal* | primary | 3 | 鉴定 Tlg1 与 Tlg2 为 TGN/内体 syntaxin，为内吞回收与 TGN 功能所需。 | [10.1093/emboj/17.1.113](https://doi.org/10.1093/emboj/17.1.113) |
| 150 | Piper et al., 1995, *The Journal of cell biology* | primary | 3 | 用温敏 vps27 突变体证明内吞与生物合成货物共同经过前液泡区室（PVC），阻断时在 class E 区室积累。 | [10.1083/jcb.131.3.603](https://doi.org/10.1083/jcb.131.3.603) |
| 151 | Herman et al., 1990, *Molecular and Cellular Biology* | primary | 3 | 克隆并表征 VPS34，证明其为液泡蛋白分选与液泡遗传所需。 | [10.1128/mcb.10.12.6742-6754.1990](https://doi.org/10.1128/mcb.10.12.6742-6754.1990) |
| 152 | Hurtig et al., 2023, *Science Advances* | primary | 2 | 在古菌 Sulfolobus 中观察到复合 ESCRT-III 聚合体的图案化组装与 Vps4 逐步拆解驱动分裂，提示顺序聚合-拆解原理在演化上古老。 | [10.1126/sciadv.ade5224](https://doi.org/10.1126/sciadv.ade5224) |
| 153 | Savocco et al., 2019, *PLOS Biology* | primary | 2 | 发现 Art2 介导维生素 B1 转运蛋白的底物诱导内吞，并解析 Art2 的调控位点。 | [10.1371/journal.pbio.3000512](https://doi.org/10.1371/journal.pbio.3000512) |
| 154 | Shi et al., 2015, *Nature Communications* | theory | 2 | 用理论与实验证明周边蛋白密度与膜张力共同决定膜从平坦到管状/泡状的形态转变，存在由张力控制的分岔。 | [10.1038/ncomms6974](https://doi.org/10.1038/ncomms6974) |
