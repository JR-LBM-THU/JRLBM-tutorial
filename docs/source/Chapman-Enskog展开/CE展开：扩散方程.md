# CE展开：扩散方程

## LBM求解扩散方程模型介绍

> 演化方程：

```{math}
:label: eq1
f_i(\boldsymbol{x}+\boldsymbol{e}_i\delta _t,t+\delta _t)-f_i(\boldsymbol{x},t)=-\frac{1}{\tau}\left[ f_i(\boldsymbol{x},t)-f_{i}^{\mathrm{eq}}(\boldsymbol{x},t) \right]
```
> 平衡态分布函数：
```{math}
:label: eq2
f_{i}^{\mathrm{eq}}(\boldsymbol{x},t)=w_iT
```

> 宏观量计算：
```{math}
:label: eq3
T=\sum_i{f_i}
```

## CE展开的基本假设
$f_i$可以展开为如下的形式：
```{math}
:label: eq4
f_i=f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{(1)}+\varepsilon ^2f_{i}^{(2)}+\cdots 
```

时间导数可以展开为如下的形式：
```{math}
:label: eq5
\frac{\partial}{\partial t}=\varepsilon \frac{\partial}{\partial t_1}+\varepsilon ^2\frac{\partial}{\partial t_2}+\cdots 
```

空间导数则只有一阶展开：
```{math}
:label: eq6
\nabla =\varepsilon \nabla _1
```

## CE展开
将式{eq}`eq1`左侧进行泰勒展开得到：
```{math}
:label: eq7
\delta _t\boldsymbol{D}_{\boldsymbol{i}}f_i+\frac{\delta _{t}^{2}}{2}\left( \boldsymbol{D}_{\boldsymbol{i}} \right) ^2f_i=-\frac{1}{\tau}\left[ f_i\left( \boldsymbol{x},t \right) -f_{i}^{\mathrm{eq}}\left( \boldsymbol{x},t \right) \right] 
```

其中$\boldsymbol{D}_i=\left( \partial_t+\boldsymbol{e}_i \cdot \nabla \right)$，将式{eq}`eq4`，{eq}`eq5`和{eq}`eq6`代入上式得到：
```{math}
:label: eq8
\left( \varepsilon \partial _{t_1}+\varepsilon ^2\partial _{t_2}+\varepsilon \boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) \left( f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
\\
+\frac{\delta _t}{2}\left( \varepsilon \partial _{t_1}+\varepsilon ^2\partial _{t_2}+\varepsilon \boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) ^2\left( f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
\\
=-\frac{1}{\tau \delta _t}\left( \varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
```

**CE展开中的一个基本准则：对于一个等式，其$\varepsilon$的各阶也要分别相等。举例，对于一个等式：**
```{math}
:label: eq9
A\varepsilon +B\varepsilon ^2=C\varepsilon +D\varepsilon ^2
```

**则其中暗含了：$A=C$，$B=D$。**

基于此准则，我们整理了式{eq}`eq8`中$\varepsilon$的各阶项：

> $\varepsilon^1$
```{math}
:label: eq10
\boldsymbol{D}_{1\boldsymbol{i}}f_{i}^{\mathrm{eq}}=\left( \partial _{t1}+\boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) f_{i}^{\mathrm{eq}}=-\frac{1}{\tau \delta _t}f_{i}^{\left( 1 \right)}
```

> $\varepsilon^2$
```{math}
:label: eq11
\partial _{t2}f_{i}^{\mathrm{eq}}+\boldsymbol{D}_{1\boldsymbol{i}}f_{i}^{\left( 1 \right)}+\frac{\delta _t}{2}\left( \boldsymbol{D}_{1\boldsymbol{i}} \right) ^2f_{i}^{\mathrm{eq}}=-\frac{1}{\tau \delta _t}f_{i}^{\left( 2 \right)}
```

根据式{eq}`eq10`可以将式{eq}`eq11`化简：
```{math}
:label: eq12
\partial _{t_2}f_{i}^{\mathrm{eq}}+\boldsymbol{D}_{1\boldsymbol{i}}\left[ \left( 1-\frac{1}{2\tau} \right) f_{i}^{\left( 1 \right)} \right] =-\frac{1}{\tau \delta _t}f_{i}^{\left( 2 \right)}
```

同时，结合式{eq}`eq3`和{eq}`eq4`，我们使用基本准则，可以得到：
```{math}
:label: eq13
\sum_i{f_{i}^{\left( n \right)}}=0  \forall n\geqslant 1
```

对式{eq}`eq10`求0阶矩得到：
```{math}
:label: eq14
\frac{\partial T}{\partial t_1}=0
```

对式{eq}`eq10`求1阶矩得到：
```{math}
:label: eq15
c_{s}^{2}\nabla _1T=-\frac{1}{\tau \delta _t}\sum_i{\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\left( 1 \right)}}
```

对式{eq}`eq12`求0阶矩得到：
```{math}
:label: eq16
\frac{\partial T}{\partial t_2}+\nabla _1\left[ \left( 1-\frac{1}{2\tau} \right) \sum_i{\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\left( 1 \right)}} \right] =0
```

使用式{eq}`eq15`化简上式得到：
```{math}
:label: eq17
\frac{\partial T}{\partial t_2}=\nabla _1\left[ c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) \nabla _1T \right] 
```

考虑式{eq}`eq14`和式{eq}`eq17`得到：
```{math}
:label: eq18
\varepsilon \frac{\partial T}{\partial t_1}+\varepsilon ^2\frac{\partial T}{\partial t_2}=\varepsilon ^2\left\{ \nabla _1\left[ c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) \nabla _1T \right] \right\} 
```

最终得到宏观方程：
```{math}
:label: eq19
\frac{\partial T}{\partial t}=\nabla \left[ c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) \nabla T \right] 
```

其中，对于D1Q3离散速度：
```{math}
:label: eq20
c_{s}^{2}\delta _t\left( \tau -\frac{1}{2} \right) =\frac{\delta _{x}^{2}}{3\delta _t}\left( \tau -\frac{1}{2} \right) \equiv \alpha 
```
