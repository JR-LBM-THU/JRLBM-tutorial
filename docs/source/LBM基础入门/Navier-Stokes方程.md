# Navier-Stokes方程
文档视频讲解：

> [LBM求解Couette(库埃特)流动：Zou-He与非平衡外推边界条件](https://www.bilibili.com/video/BV1PkcueFE2z/?share_source=copy_web&vd_source=6cb794fb9d90103946fb79ba5f60451f)

> [LBM求解泊肃叶(Poiseuille)流动](https://www.bilibili.com/video/BV1enNoeWEMg/?share_source=copy_web&vd_source=6cb794fb9d90103946fb79ba5f60451f)

这节我们介绍一下**NS方程**的格子玻尔兹曼方法实现。

## 什么是Navier-Stokes方程?
Navier-Stokes方程是描述流体运动的基本方程，它是由Navier和Stokes两位科学家在19世纪提出的,形式如下:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \boldsymbol{u}) = 0
$$

$$
\frac{\partial (\rho \boldsymbol{u})}{\partial t} + \nabla \cdot (\rho \boldsymbol{u} \boldsymbol{u}) = -\nabla p + \nabla \cdot \left[\mu (\nabla \boldsymbol{u} + \nabla \boldsymbol{u}^T) + \lambda \left(\nabla \cdot \boldsymbol{u} \right)\mathbf{I}\right] + \boldsymbol{F}
$$

其中$\rho$是密度，$\boldsymbol{u}$是速度，$p$是压力，$\mu$是动力粘度，$\lambda$是第二粘度系数，$\boldsymbol{F}$是外力。

对于不可压缩流体，密度$\rho$为常数，那么NS方程可以简化为：

$$
\nabla \cdot \boldsymbol{u} = 0
$$

$$
\frac{\partial \boldsymbol{u}}{\partial t} + \boldsymbol{u} \cdot \nabla \boldsymbol{u} = -\frac{1}{\rho} \nabla p + \nu \nabla^2 \boldsymbol{u} + \boldsymbol{F}
$$

## NS方程的D2Q9模型
NS方程的求解一般采用D2Q9模型，其与扩散方程、对流扩散方程的区别仅在于速度的计算和平衡态分布函数为：

$$
f_i^\mathrm{eq}(\rho,\boldsymbol{u}) = w_i \rho\left[1 + \frac{\boldsymbol{e_i\cdot u}}{c^2_s}+\frac{(\boldsymbol{e_i\cdot u})^2}{2c^4_s} - \frac{\boldsymbol{u}^2}{2c^2_s}\right]
$$

$$
\rho\boldsymbol{u} = \sum_i f_i \boldsymbol{e_i}
$$

> 九个离散速度

$$
e_i = \left\{
\begin{aligned}
&0, \quad i=0 \\
&c\left[\cos \frac{\pi (i-1)}{2}, \sin \frac{\pi (i-1)}{2}\right], \quad i=1,2,3,4 \\
&\sqrt{2}c\left( \cos \left[ (2i -1)\frac{\pi}{4} \right] ,\sin \left[ (2i -1)\frac{\pi}{4} \right] \right), \quad i=5,6,7,8
\end{aligned}
\right.
$$

> 对应的权重

$$
w_0 = 4/9, \quad w_{1-4} = 1/9, \quad w_{5-8} = 1/36
$$

> 演化方程

$$
f_i(\boldsymbol{x}+\boldsymbol{e}_i \delta_t,t+\delta_t)=f_i(\boldsymbol{x},t)-\frac{1}{\tau}[f_i(\boldsymbol{x},t)-f_i^{\mathrm{eq}}(\boldsymbol{x},t)]
$$

也可以写成如下的形式：

$$
f_i(\boldsymbol{x}+\boldsymbol{e}_i \delta_t,t+\delta_t)=(1-\omega) f_i(\boldsymbol{x},t)+\omega f_i^{\mathrm{eq}}(\boldsymbol{x},t)
$$

其中$\omega = 1/\tau$。
> 宏观量

$$
\rho= \sum_i f_i, \quad p=\rho c^2_s
$$

> 运动粘度

$$
\nu = \frac{\delta _x^2}{3\delta_t}\left(\tau - \frac{1}{2}\right)
$$

## 应用：库埃特流动
### 解析解
库埃特流动是一种经典的流体力学问题，是一种瞬态流动，流体在两个平行板之间流动，上板以速度$U$向右移动，下板静止，流体在两板之间流动，从静止时刻开始，流体的速度分布随时间的演化为：

$$
u_x(y,t) = U\frac{y}{H}-\frac{2U}{\pi}\sum_{n=1}^{\infty}\frac{1}{n}\exp\left({-n^2\pi^2\frac{\nu t}{H^2}}\right)\sin \left[n\pi\left(1-\frac{y}{H}\right)\right]
$$

其中$H$是两板之间的距离，$\nu$是运动粘度。
### 非平衡态外推格式
该格式的基本假设为，壁面处的非平衡态部分和临近格子的非平衡态部分是一致的，即：

$$
f_\mathrm{near} - f^\mathrm{eq}_\mathrm{near}  = f_\mathrm{wall} - f^\mathrm{eq}_\mathrm{wall}
$$

其中，near表示临界格子，wall表示壁面格子。则：

$$
f_\mathrm{wall} = f^\mathrm{eq}_\mathrm{wall} + f_\mathrm{near} - f^\mathrm{eq}_\mathrm{near}
$$

### Zou-He边界条件
以上边界为例，$\rho,f_4,f_7,f_8$4个参数未知，但我们只有如下三个方程：

$$
\rho = \sum_i f_i
$$

$$
\rho u_x/c = \sum_i f_i e_{ix}/c=f_1+ f_5 + f_8 - f_3 - f_6 - f_7
$$

$$
\rho u_y/c = \sum_i f_i e_{iy}/c = f_2 + f_5 + f_6 - f_4 - f_7 - f_8
$$

因此，Zou-He提出如下的假设，在边界处：

$$
f_4 =f_2
$$

也就是说$f_4$按照全反弹的方式计算，则三个方程，三个未知数就可以解出:

$$
f_7 = f_5 - \frac{\rho(u_x+u_y)}{2c} + \frac{f_1 - f_3}{2}
$$

$$
f_8 = f_6 + \frac{\rho(u_x-u_y)}{2c} - \frac{f_1 - f_3}{2}
$$

$$
\rho = \frac{1}{1+u_y/c}\left[f_0 + f_1 + f_3 + 2(f_2 + f_5 + f_6)\right]
$$
### 数值模拟结果
下图是库埃特流动的数值模拟结果，其中$\nu=0.1$，$H=50$，$U=0.1$，$L=4$。选择不同的边界条件和时间、空间步长进行计算。
```{figure} fig/fig4/ZouHe-dx=1-dt=1.png
:width: 50%
:alt: logo
:align: center
Zou-He边界条件，$\delta_x = 1$，$\delta_t = 1$
```
<!-- <img src="./couette/ZouHe-dx=1-dt=1.png" alt="Image description" width="500"/> -->

```{figure} fig/fig4/ZouHe-dx=2-dt=2.png
:width: 50%
:alt: logo
:align: center
Zou-He边界条件，$\delta_x = 2$，$\delta_t = 2$
```
<!-- <img src="./couette/ZouHe-dx=2-dt=2.png" alt="Image description" width="500"/> -->

```{figure} fig/fig4/noequ-dx=1-dt=1.png
:width: 50%
:alt: logo
:align: center
非平衡态外推格式，$\delta_x = 1$，$\delta_t = 1$
```
<!-- <img src="./couette/noequ-dx=1-dt=1.png" alt="Image description" width="500"/> -->

```{figure} fig/fig4/noequ-dx=2-dt=2.png
:width: 50%
:alt: logo
:align: center
非平衡态外推格式，$\delta_x = 2$，$\delta_t = 2$
```
<!-- <img src="./couette/noequ-dx=2-dt=2.png" alt="Image description" width="500"/> -->

可以看到，两种边界条件都与计算结果很好的吻合，而且可以任意的调节时间、空间步长，而不影响计算结果。

## 应用：泊肃叶流动
### 解析解
泊肃叶流动是一种经典的流体力学问题，是一种稳态流动，流体在两个平行板之间由压力驱动。进出口压差为$\Delta P$，两板之间的距离为$H$，流到长度为$L$，则此时流体的速度分布为：

$$
u_y(x) = \frac{\Delta P}{2\mu L}x(H-x)
$$

其中$\mu$是动力粘度，$x$是流体的位置，范围为$[0,H]$。
### 数值模拟结果
下图是泊肃叶流动的数值模拟结果，其中$\nu=0.1$，$H=20$，$L=50$，$\Delta P = 0.001$。选择不同的时间、空间步长进行计算。进出口压力使用**非平衡态外推格式**，两侧壁面使用**全反弹边界条件**。使用最大速度与解析解的相对误差作为评价标准：

$$
\epsilon = \frac{\max |u_y - u_y^\mathrm{analytic}|}{\max |u_y^\mathrm{analytic}|}
$$
```{figure} fig/fig4/dx=0.5-dt=0.25.png
:width: 50%
:alt: logo
:align: center
当$\delta_x = 0.5$，$\delta_t = 0.25$时，$\epsilon=7.2e-04$
```
<!-- <img src="./Poiseuille/dx=0.5-dt=0.25.png" alt="Image description" width="500"/> -->

```{figure} fig/fig4/dx=1-dt=1.png
:width: 50%
:alt: logo
:align: center
当$\delta_x = 1$，$\delta_t = 1$时，$\epsilon=0.0028$
```
<!-- <img src="./Poiseuille/dx=1-dt=1.png" alt="Image description" width="500"/> -->

```{figure} fig/fig4/dx=2-dt=4.png
:width: 50%
:alt: logo
:align: center
当$\delta_x = 2$，$\delta_t = 4$时，$\epsilon=0.0111$
```
<!-- <img src="./Poiseuille/dx=2-dt=4.png" alt="Image description" width="500"/> -->

```{figure} fig/fig4/log-log.png
:width: 50%
:alt: logo
:align: center
绘制$\delta_x$与$\epsilon$的关系
```
<!-- <img src="./Poiseuille/log-log.png" alt="Image description" width="500"/> -->

可以看到，LBM具有二阶精度。