# CE展开：对流扩散方程
文档视频讲解：
> [LBM求解对流扩散方程的Chapman-Enskog展开(CE展开)](https://www.bilibili.com/video/BV1dR9tY7EBu/?share_source=copy_web&vd_source=6cb794fb9d90103946fb79ba5f60451f)

**<font color='red'>红色为相对于扩散方程增加的内容</font>**

**<font color='blue'>蓝色为误差项</font>**

## LBM求解对流扩散方程模型介绍
> 演化方程：

```{math}
:label: CE-conv-diff-eq1
f_i(\boldsymbol{x}+\boldsymbol{e}_i\delta _t,t+\delta _t)-f_i(\boldsymbol{x},t)=-\frac{1}{\tau}\left[ f_i(\boldsymbol{x},t)-f_{i}^{\mathrm{eq}}(\boldsymbol{x},t) \right]
```

> 平衡态分布函数：

```{math}
:label: CE-conv-diff-eq2
f_{i}^{\mathrm{eq}}(\boldsymbol{x},t)=w_iT\left( 1+\frac{\boldsymbol{e}_{\boldsymbol{i}}\cdot \boldsymbol{u}}{c_{s}^{2}} \right) 
```

> 宏观量计算：

```{math}
:label: CE-conv-diff-eq3
T=\sum_i{f_i}
```

**注：由平衡态分布函数可以得到**

```{math}
:label: CE-conv-diff-eq0
{\color[RGB]{240, 0, 0} \sum_i{f_{i}^{\mathrm{eq}}}=T, \sum_i{\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\mathrm{eq}}}=\boldsymbol{u}T, \sum_i{\boldsymbol{e}_{\boldsymbol{i}}\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\mathrm{eq}}}=Tc_{s}^{2}\mathbf{I}}
```

## CE展开的基本假设
$f_i$可以展开为如下的形式：
```{math}
:label: CE-conv-diff-eq4
f_i=f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{(1)}+\varepsilon ^2f_{i}^{(2)}+\cdots 
```

时间导数可以展开为如下的形式：
```{math}
:label: CE-conv-diff-eq5
\frac{\partial}{\partial t}=\varepsilon \frac{\partial}{\partial t_1}+\varepsilon ^2\frac{\partial}{\partial t_2}+\cdots 
```

空间导数则只有一阶展开：
```{math}
:label: CE-conv-diff-eq6
\nabla =\varepsilon \nabla _1
```

## CE展开
将式{eq}`CE-conv-diff-eq1`左侧进行泰勒展开得到：
```{math}
:label: CE-conv-diff-eq7
\delta _t\boldsymbol{D}_{\boldsymbol{i}}f_i+\frac{\delta _{t}^{2}}{2}\left( \boldsymbol{D}_{\boldsymbol{i}} \right) ^2f_i=-\frac{1}{\tau}\left[ f_i\left( \boldsymbol{x},t \right) -f_{i}^{\mathrm{eq}}\left( \boldsymbol{x},t \right) \right] 
```

其中$\boldsymbol{D}_i=\left( \partial_t+\boldsymbol{e}_i \cdot \nabla \right)$，将式{eq}`CE-conv-diff-eq4`，{eq}`CE-conv-diff-eq5`和{eq}`CE-conv-diff-eq6`代入上式得到：
```{math}
:label: CE-conv-diff-eq8
\left( \varepsilon \partial _{t_1}+\varepsilon ^2\partial _{t_2}+\varepsilon \boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) \left( f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
\\
+\frac{\delta _t}{2}\left( \varepsilon \partial _{t_1}+\varepsilon ^2\partial _{t_2}+\varepsilon \boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) ^2\left( f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
\\
=-\frac{1}{\tau \delta _t}\left( \varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
```

CE展开中的一个基本准则：对于一个等式，其$\varepsilon$的各阶也要分别相等。举例，对于一个等式：
```{math}
:label: CE-conv-diff-eq9
A\varepsilon +B\varepsilon ^2=C\varepsilon +D\varepsilon ^2
```

则其中暗含了：$A=C$，$B=D$。

基于此准则，我们整理了式{eq}`CE-conv-diff-eq8`中$\varepsilon$的各阶项：

> $\varepsilon^1$
```{math}
:label: CE-conv-diff-eq10
\boldsymbol{D}_{1\boldsymbol{i}}f_{i}^{\mathrm{eq}}=\left( \partial _{t1}+\boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) f_{i}^{\mathrm{eq}}=-\frac{1}{\tau \delta _t}f_{i}^{\left( 1 \right)}
```

> $\varepsilon^2$
```{math}
:label: CE-conv-diff-eq11
\partial _{t2}f_{i}^{\mathrm{eq}}+\boldsymbol{D}_{1\boldsymbol{i}}f_{i}^{\left( 1 \right)}+\frac{\delta _t}{2}\left( \boldsymbol{D}_{1\boldsymbol{i}} \right) ^2f_{i}^{\mathrm{eq}}=-\frac{1}{\tau \delta _t}f_{i}^{\left( 2 \right)}
```

根据式{eq}`CE-conv-diff-eq10`可以将式{eq}`CE-conv-diff-eq11`化简：
```{math}
:label: CE-conv-diff-eq12
\partial _{t_2}f_{i}^{\mathrm{eq}}+\boldsymbol{D}_{1\boldsymbol{i}}\left[ \left( 1-\frac{1}{2\tau} \right) f_{i}^{\left( 1 \right)} \right] =-\frac{1}{\tau \delta _t}f_{i}^{\left( 2 \right)}
```

同时，结合式{eq}`CE-conv-diff-eq3`和{eq}`CE-conv-diff-eq4`，我们使用基本准则，可以得到：
```{math}
:label: CE-conv-diff-eq13
\sum_i{f_{i}^{\left( n \right)}}=0 \quad \forall n\geqslant 1
```

对式{eq}`CE-conv-diff-eq10`求0阶矩得到：
```{math}
:label: CE-conv-diff-eq14
\frac{\partial T}{\partial t_1}{\color[RGB]{240, 0, 0} +\nabla _1\left( \boldsymbol{u}T \right) }=0
```

对式{eq}`CE-conv-diff-eq10`求1阶矩得到：
```{math}
:label: CE-conv-diff-eq15
{\color[RGB]{240, 0, 0} \frac{\partial \left( \boldsymbol{u}T \right)}{\partial t_1}+}c_{s}^{2}\nabla _1T=-\frac{1}{\tau \delta _t}\sum_i{\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\left( 1 \right)}}
```

对式{eq}`CE-conv-diff-eq12`求0阶矩得到：
```{math}
:label: CE-conv-diff-eq16
\frac{\partial T}{\partial t_2}+\nabla _1\left[ \left( 1-\frac{1}{2\tau} \right) \sum_i{\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\left( 1 \right)}} \right] =0
```

使用式{eq}`CE-conv-diff-eq15`化简上式得到：
```{math}
:label: CE-conv-diff-eq17
\frac{\partial T}{\partial t_2}=\nabla _1\left[ c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) \nabla _1T \right] {\color[RGB]{240, 0, 0} +\nabla _1\left[ \delta _t\left( \tau -\frac{1}{2} \right) \frac{\partial \left( \boldsymbol{u}T \right)}{\partial t_1} \right] }
```

考虑式{eq}`CE-conv-diff-eq14`和式{eq}`CE-conv-diff-eq17`得到：
```{math}
:label: CE-conv-diff-eq18
\varepsilon \frac{\partial T}{\partial t_1}+\varepsilon ^2\frac{\partial T}{\partial t_2}{\color[RGB]{240, 0, 0} +\varepsilon \nabla _1\left( \boldsymbol{u}T \right) }=
\\
\varepsilon ^2\left\{ \nabla _1\left[ c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) \nabla _1T \right] {\color[RGB]{240, 0, 0} +\nabla _1\left[ \delta _t\left( \tau -\frac{1}{2} \right) \frac{\partial \left( \boldsymbol{u}T \right)}{\partial t_1} \right] } \right\}
```

最终得到宏观方程：
```{math}
:label: CE-conv-diff-eq19
\frac{\partial T}{\partial t}{\color[RGB]{240, 0, 0} +\nabla \left( \boldsymbol{u}T \right) }=\nabla \left[ c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) \nabla T \right] {\color[RGB]{0, 0, 240} +\varepsilon \nabla \left[ \delta _t\left( \tau -\frac{1}{2} \right) \frac{\partial \left( \boldsymbol{u}T \right)}{\partial t_1} \right] }
```

其中，对于D1Q3离散速度：
```{math}
:label: CE-conv-diff-eq20
c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) =\frac{\delta _{x}^{2}}{3\delta _t}\left( \tau -\frac{1}{2} \right) \equiv \alpha 
```

**忽略误差项后可得：**
```{math}
:label: CE-conv-diff-eq21
{\color[RGB]{240, 0, 0} \frac{\partial T}{\partial t}+\nabla \left( \boldsymbol{u}T \right) =\nabla \left( \alpha \nabla T \right) }
```

---

**如果您觉得这个项目对您有帮助，可以考虑用以下方式支持我：**

- ☕ 请我喝杯咖啡
> 如果条件允许，[欢迎捐赠支持](../支持与捐赠/支持与捐赠.md)！  
> 每一分都是对我莫大的鼓励，让我能投入更多时间维护和更新。

- 📄 引用我的文章
> 如果暂时不便捐赠，[适当引用我的文章](../我的文章/我的文章.md)也是极好的支持！  
> 您的引用能帮助这个工作获得更多关注，同样让我感到无比欣慰。

无论哪种方式，都是对我的巨大支持！🙏感谢您让开源世界更美好！✨