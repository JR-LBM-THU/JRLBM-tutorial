# CE展开：Navier-Stokes方程

文档B站视频讲解：
> [LBM求解Navier-Stokes方程的Chapman-Enskog展开(CE展开)](https://www.bilibili.com/video/BV1EuibBiEYv/)

**<font color="red">红色为相对于对流扩散方程增加的部分关键内容</font>**

## LBM求解Navier-Stokes方程模型介绍
> 演化方程：

```{math}
:label: CE-ns-eq1
f_i(\boldsymbol{x}+\boldsymbol{e}_i\delta _t,t+\delta _t)-f_i(\boldsymbol{x},t)=-\frac{1}{\tau}\left[ f_i(\boldsymbol{x},t)-f_{i}^{\mathrm{eq}}(\boldsymbol{x},t) \right]
```

> 平衡态分布函数：

```{math}
:label: CE-ns-eq2
f_{i}^{\mathrm{eq}}(\boldsymbol{x},t)=w_i \rho \left[ 1+\frac{\boldsymbol{e}_{\boldsymbol{i}}\cdot \boldsymbol{u}}{c_{s}^{2}} +\frac{\left( \boldsymbol{e}_{\boldsymbol{i}}\cdot \boldsymbol{u} \right) ^2}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot \boldsymbol{u}}{2c_{s}^{2}} \right]
```

> 宏观量计算：

```{math}
:label: CE-ns-eq3
\rho=\sum_i{f_i}, \quad \rho \boldsymbol{u}=\sum_i{\boldsymbol{e}_i f_i}
```

**注：由平衡态分布函数可以得到**

```{math}
:label: CE-ns-eq0
\sum_i{f_{i}^{\mathrm{eq}}}=\rho, \quad \sum_i{\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\mathrm{eq}}}=\rho \boldsymbol{u}, \quad \sum_i{\boldsymbol{e}_{\boldsymbol{i}}\boldsymbol{e}_{\boldsymbol{i}}f_{i}^{\mathrm{eq}}}=\Pi^{(0)}= \rho c_{s}^{2}\mathbf{I}+\rho \boldsymbol{u}\boldsymbol{u}
```
其中 $\mathbf{I}$ 为单位张量，记$p=\rho c_s^2$，最后会看到$p$即为流体的静压力。

## CE展开的基本假设
$f_i$可以展开为如下的形式：
```{math}
:label: CE-ns-eq4
f_i=f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{(1)}+\varepsilon ^2f_{i}^{(2)}+\cdots 
```

时间导数可以展开为如下的形式：
```{math}
:label: CE-ns-eq5
\frac{\partial}{\partial t}=\varepsilon \frac{\partial}{\partial t_1}+\varepsilon ^2\frac{\partial}{\partial t_2}+\cdots 
```

空间导数则只有一阶展开：
```{math}
:label: CE-ns-eq6
\nabla =\varepsilon \nabla _1
```

## CE展开
将式{eq}`CE-ns-eq1`左侧进行泰勒展开得到：
```{math}
:label: CE-ns-eq7
\delta _t\boldsymbol{D}_{\boldsymbol{i}}f_i+\frac{\delta _{t}^{2}}{2}\left( \boldsymbol{D}_{\boldsymbol{i}} \right) ^2f_i=-\frac{1}{\tau}\left[ f_i\left( \boldsymbol{x},t \right) -f_{i}^{\mathrm{eq}}\left( \boldsymbol{x},t \right) \right] 
```

其中$\boldsymbol{D}_i=\left( \partial_t+\boldsymbol{e}_i \cdot \nabla \right)$，将式{eq}`CE-ns-eq4`，{eq}`CE-ns-eq5`和{eq}`CE-ns-eq6`代入上式得到：
```{math}
:label: CE-ns-eq8
\left( \varepsilon \partial _{t_1}+\varepsilon ^2\partial _{t_2}+\varepsilon \boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) \left( f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
\\
+\frac{\delta _t}{2}\left( \varepsilon \partial _{t_1}+\varepsilon ^2\partial _{t_2}+\varepsilon \boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) ^2\left( f_{i}^{\mathrm{eq}}+\varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
\\
=-\frac{1}{\tau \delta _t}\left( \varepsilon f_{i}^{\left( 1 \right)}+\varepsilon ^2f_{i}^{\left( 2 \right)} \right) 
```

CE展开中的一个基本准则：对于一个等式，其$\varepsilon$的各阶也要分别相等。举例，对于一个等式：
```{math}
:label: CE-ns-eq9
A\varepsilon +B\varepsilon ^2=C\varepsilon +D\varepsilon ^2
```

则其中暗含了：$A=C$，$B=D$。

基于此准则，我们整理了式{eq}`CE-ns-eq8`中$\varepsilon$的各阶项：

> $\varepsilon^1$
```{math}
:label: CE-ns-eq10
\boldsymbol{D}_{1\boldsymbol{i}}f_{i}^{\mathrm{eq}}=\left( \partial _{t1}+\boldsymbol{e}_{\boldsymbol{i}}\cdot \nabla _1 \right) f_{i}^{\mathrm{eq}}=-\frac{1}{\tau \delta _t}f_{i}^{\left( 1 \right)}
```

> $\varepsilon^2$
```{math}
:label: CE-ns-eq11
\partial _{t2}f_{i}^{\mathrm{eq}}+\boldsymbol{D}_{1\boldsymbol{i}}f_{i}^{\left( 1 \right)}+\frac{\delta _t}{2}\left( \boldsymbol{D}_{1\boldsymbol{i}} \right) ^2f_{i}^{\mathrm{eq}}=-\frac{1}{\tau \delta _t}f_{i}^{\left( 2 \right)}
```

根据式{eq}`CE-ns-eq10`可以将式{eq}`CE-ns-eq11`化简：
```{math}
:label: CE-ns-eq12
\partial _{t_2}f_{i}^{\mathrm{eq}}+\boldsymbol{D}_{1\boldsymbol{i}}\left[ \left( 1-\frac{1}{2\tau} \right) f_{i}^{\left( 1 \right)} \right] =-\frac{1}{\tau \delta _t}f_{i}^{\left( 2 \right)}
```

同时，结合式{eq}`CE-ns-eq3`和{eq}`CE-ns-eq4`，我们使用基本准则，可以得到**可解性条件**：
```{math}
:label: CE-ns-eq13
\sum_i{f_{i}^{\left( n \right)}}=0, \quad {\color[RGB]{240, 0, 0} \sum_i{\boldsymbol{e}_i f_{i}^{\left( n \right)}}=0} \quad \forall n\geqslant 1
```

对式{eq}`CE-ns-eq10`求0阶矩得到：
```{math}
:label: CE-ns-eq14
\frac{\partial \rho}{\partial t_1} +\nabla _1 \cdot \left( \rho \boldsymbol{u} \right) =0
```

对式{eq}`CE-ns-eq10`求1阶矩得到：
```{math}
:label: CE-ns-eq15
{\color[RGB]{240, 0, 0} \frac{\partial \left( \rho \boldsymbol{u} \right)}{\partial t_1} +\nabla _1 \cdot \Pi^{(0)} = 0}
```
即 Euler 方程。

对式{eq}`CE-ns-eq12`求0阶矩得到：
```{math}
:label: CE-ns-eq16
\frac{\partial \rho}{\partial t_2} = 0
```
(注：此处利用了可解性条件 $\sum f_i^{(1)}=0$ 和 $\sum f_i^{(2)}=0$)

对式{eq}`CE-ns-eq12`求1阶矩得到：
```{math}
:label: CE-ns-eq17
{\color[RGB]{240, 0, 0} \frac{\partial (\rho \boldsymbol{u})}{\partial t_2} + \nabla_1 \cdot \left[ \left( 1 - \frac{1}{2\tau} \right) \sum_i \boldsymbol{e}_i \boldsymbol{e}_i f_i^{(1)} \right] = 0}
```

为了计算 $\Pi^{(1)} = \sum \boldsymbol{e}_i \boldsymbol{e}_i f_i^{(1)}$，利用式{eq}`CE-ns-eq10`（为了推导方便，这部分切换为索引标识法）：
```{math}
:label: CE-ns-eq18
\Pi^{(1)}_{ij} = \sum_i e_{i,i} e_{i,j} f_i^{(1)} = -\tau \delta_t \sum_i e_{i,i} e_{i,j} \left( \frac{\partial}{\partial t_1}+\boldsymbol{e}_{i}\cdot \nabla _1 \right)f_i ^{\mathrm{eq}}
```
展开上式：
```{math}
:label: CE-ns-eq18-1
\Pi^{(1)}_{ij} = -\tau \delta_t \left[ \frac{\partial}{\partial t_1} \left( \sum_i e_{i,i} e_{i,j} f_i^{\mathrm{eq}} \right) + \frac{\partial}{\partial x_{1,k}} \left( \sum_i e_{i,i} e_{i,j} e_{i,k} f_i^{\mathrm{eq}} \right) \right]
```
其中二阶矩 $\sum_i e_{i,i} e_{i,j} f_i^{\mathrm{eq}} = \Pi^{(0)}_{ij} = \rho u_i u_j + p \delta_{ij}$。
三阶矩 $\Lambda^{(0)}_{ijk} = \sum_i e_{i,i} e_{i,j} e_{i,k} f_i^{\mathrm{eq}}$。

---

**$\Pi^{(1)}_{ij}$的详细推导如下：（很复杂，可跳过）**

1. **分析第二项（空间导数项）**
   对于标准的 D2Q9 或 D3Q19 模型，利用平衡态分布函数的性质，三阶矩为：
   ```{math}
   :label: CE-ns-eq18-2
   \Lambda^{(0)}_{ijk} = \rho c_s^2 \left( u_i \delta_{jk} + u_j \delta_{ik} + u_k \delta_{ij} \right)
   ```
   对其求导：
   ```{math}
   :label: CE-ns-eq18-3
   \begin{aligned}
   \frac{\partial}{\partial x_{1,k}} \Lambda^{(0)}_{ijk} &= \frac{\partial}{\partial x_{1,k}} \left[ \rho c_s^2 \left( u_i \delta_{jk} + u_j \delta_{ik} + u_k \delta_{ij} \right) \right] \\
   &= \frac{\partial (\rho c_s^2 u_i)}{\partial x_{1,j}} + \frac{\partial (\rho c_s^2 u_j)}{\partial x_{1,i}} + \frac{\partial (\rho c_s^2 u_k)}{\partial x_{1,k}} \delta_{ij} \\
   &= c_s^2 \left( \rho \frac{\partial u_i}{\partial x_{1,j}} + u_i \frac{\partial \rho}{\partial x_{1,j}} \right) + c_s^2 \left( \rho \frac{\partial u_j}{\partial x_{1,i}} + u_j \frac{\partial \rho}{\partial x_{1,i}} \right) \\
   &+ c_s^2 \delta_{ij} \frac{\partial (\rho u_k)}{\partial x_{1,k}}
   \end{aligned}
   ```

2. **分析第一项（时间导数项）**
   ```{math}
   :label: CE-ns-eq18-4
   \frac{\partial}{\partial t_1} \Pi^{(0)}_{ij} = \frac{\partial}{\partial t_1} (\rho u_i u_j + p \delta_{ij}) = \frac{\partial (\rho u_i u_j)}{\partial t_1} + c_s^2 \delta_{ij} \frac{\partial \rho}{\partial t_1}
   ```
   利用 $\varepsilon^1$ 阶的连续性方程（式{eq}`CE-ns-eq14`）：$\frac{\partial \rho}{\partial t_1} = -\frac{\partial (\rho u_k)}{\partial x_{1,k}}$，代入 $p$ 的导数项：
   ```{math}
   :label: CE-ns-eq18-5
   c_s^2 \delta_{ij} \frac{\partial \rho}{\partial t_1} = -c_s^2 \delta_{ij} \frac{\partial (\rho u_k)}{\partial x_{1,k}}
   ```
   对于 $\rho u_i u_j$ 的导数项，展开为：
   ```{math}
   :label: CE-ns-eq18-6
   \frac{\partial (\rho u_i u_j)}{\partial t_1} = u_j \frac{\partial (\rho u_i)}{\partial t_1} + u_i \frac{\partial (\rho u_j)}{\partial t_1} - u_i u_j \frac{\partial \rho}{\partial t_1}
   ```
   利用 $\varepsilon^1$ 阶的动量方程（式{eq}`CE-ns-eq15`）：$\frac{\partial (\rho u_i)}{\partial t_1} = -\frac{\partial (\rho u_i u_k + p \delta_{ik})}{\partial x_{1,k}}$，代入上式：
   ```{math}
   :label: CE-ns-eq18-7
   \begin{aligned}
   &\frac{\partial (\rho u_i u_j)}{\partial t_1} \\
   &= u_j \left[ -\frac{\partial (\rho u_i u_k)}{\partial x_{1,k}} - \frac{\partial p}{\partial x_{1,i}} \right] + u_i \left[ -\frac{\partial (\rho u_j u_k)}{\partial x_{1,k}} - \frac{\partial p}{\partial x_{1,j}} \right] + u_i u_j \frac{\partial (\rho u_k)}{\partial x_{1,k}} \\
   &= -u_j \frac{\partial (\rho u_i u_k)}{\partial x_{1,k}} - c_s^2 u_j \frac{\partial \rho}{\partial x_{1,i}} - u_i \frac{\partial (\rho u_j u_k)}{\partial x_{1,k}} - c_s^2 u_i \frac{\partial \rho}{\partial x_{1,j}} + u_i u_j \frac{\partial (\rho u_k)}{\partial x_{1,k}}
   \end{aligned}
   ```
   进一步化简上式中的对流项导数：
   ```{math}
   :label: CE-ns-eq18-8
   \begin{aligned}
   & -u_j \frac{\partial (\rho u_i u_k)}{\partial x_{1,k}} - u_i \frac{\partial (\rho u_j u_k)}{\partial x_{1,k}} + u_i u_j \frac{\partial (\rho u_k)}{\partial x_{1,k}} \\
   &= -u_j \left( \rho u_k \frac{\partial u_i}{\partial x_{1,k}} + u_i \frac{\partial (\rho u_k)}{\partial x_{1,k}} \right) - u_i \left( \rho u_k \frac{\partial u_j}{\partial x_{1,k}} + u_j \frac{\partial (\rho u_k)}{\partial x_{1,k}} \right) \\
   & + u_i u_j \frac{\partial (\rho u_k)}{\partial x_{1,k}} \\
   &= -\rho u_j u_k \frac{\partial u_i}{\partial x_{1,k}} - \rho u_i u_k \frac{\partial u_j}{\partial x_{1,k}} - u_i u_j \frac{\partial (\rho u_k)}{\partial x_{1,k}} \\
   &= -\frac{\partial (\rho u_i u_j u_k)}{\partial x_{1,k}}
   \end{aligned}
   ```
   所以：
   ```{math}
   :label: CE-ns-eq18-9
   \frac{\partial (\rho u_i u_j)}{\partial t_1} = -c_s^2 u_j \frac{\partial \rho}{\partial x_{1,i}} - c_s^2 u_i \frac{\partial \rho}{\partial x_{1,j}} - \frac{\partial (\rho u_i u_j u_k)}{\partial x_{1,k}}
   ```

3. **合并各项**
   将式{eq}`CE-ns-eq18-3`、式{eq}`CE-ns-eq18-5`和式{eq}`CE-ns-eq18-9`代入式{eq}`CE-ns-eq18-1`：
   ```{math}
   :label: CE-ns-eq18-10
   \begin{aligned}
   & \Pi^{(1)}_{ij} \\
   &= -\tau \delta_t \left[ \left( -c_s^2 u_j \frac{\partial \rho}{\partial x_{1,i}} - c_s^2 u_i \frac{\partial \rho}{\partial x_{1,j}} - \frac{\partial (\rho u_i u_j u_k)}{\partial x_{1,k}} - c_s^2 \delta_{ij} \frac{\partial (\rho u_k)}{\partial x_{1,k}} \right) \right. \\
   &\quad \left. + \left( \rho c_s^2 \frac{\partial u_i}{\partial x_{1,j}} + c_s^2 u_i \frac{\partial \rho}{\partial x_{1,j}} + \rho c_s^2 \frac{\partial u_j}{\partial x_{1,i}} + c_s^2 u_j \frac{\partial \rho}{\partial x_{1,i}} + c_s^2 \delta_{ij} \frac{\partial (\rho u_k)}{\partial x_{1,k}} \right) \right]
   \end{aligned}
   ```
   可以看到，包含 $\frac{\partial \rho}{\partial x}$ 的项和包含 $\delta_{ij}$ 的项都相互抵消了：
   ```{math}
   :label: CE-ns-eq18-11
   \Pi^{(1)}_{ij} = -\tau \delta_t \left[ \rho c_s^2 \left( \frac{\partial u_i}{\partial x_{1,j}} + \frac{\partial u_j}{\partial x_{1,i}} \right) - \frac{\partial (\rho u_i u_j u_k)}{\partial x_{1,k}} \right]
   ```
   其中 $\frac{\partial (\rho u_i u_j u_k)}{\partial x_{1,k}}$ 是 $O(u^3)$ 的误差项，通常忽略不计。
---
最终得到非平衡态应力张量：
```{math}
:label: CE-ns-eq19
\Pi^{(1)}_{ij} \approx -\tau \delta_t \rho c_s^2 \left( \frac{\partial u_i}{\partial x_{1,j}} + \frac{\partial u_j}{\partial x_{1,i}} \right)
```
即：
```{math}
\Pi^{(1)} \approx -\tau \delta_t \rho c_s^2 (\nabla_1 \boldsymbol{u} + (\nabla_1 \boldsymbol{u})^T)
```

同时考虑式{eq}`CE-ns-eq0`、{eq}`CE-ns-eq14`、{eq}`CE-ns-eq15`、{eq}`CE-ns-eq16`、{eq}`CE-ns-eq17`及{eq}`CE-ns-eq19`得到：
```{math}
:label: CE-ns-eq20
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \boldsymbol{u}) = 0
```
```{math}
:label: CE-ns-eq21
{\color[RGB]{240, 0, 0} \frac{\partial (\rho \boldsymbol{u})}{\partial t} + \nabla \cdot (\rho \boldsymbol{u} \boldsymbol{u}) = -\nabla p + \nabla \cdot \left[ \rho \nu (\nabla \boldsymbol{u} + (\nabla \boldsymbol{u})^T) \right]}
```
其中$p=\rho c_s^2$，粘度由下式给出：
```{math}
:label: CE-ns-eq22
{\color[RGB]{240, 0, 0}\nu = c_s^2 \left( \tau - \frac{1}{2} \right) \delta_t}
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
