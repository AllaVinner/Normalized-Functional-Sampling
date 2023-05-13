# Normalized-Functional-Sampling

## Abstract 
When sampling points from a multidimensional distribution, it is often the case that one wants the points to be uniformly sampled from the multidimisional geometry body given. Howerver, the kanonical way of sampling from the body is usually not uniform. For example, sampling points from a disk can be done by drawing two points from a uniform distribution where the first points represent the radius of the the point, and the seconde the angle. The strategy ensures that all the drawn points are drawn from the disk, however, the sampling desnity will be greater in the center of the disk then in the outer parts.

**Proposed Strategy** 
$$
\begin{align*}
    \text{Given a function } & f: x \mapsto y \\
    \text{find } & g: \xi \mapsto x \\
    \text{where } & D_g=I_g=D_f\\
    \text{such that } & g(D)=D \\
    \text{and } & J_{f}(x)J_{g}(\xi)|D|=|I|\\
    \text{where functional } & J_{f}(x) := \sqrt{\bigg |\det \bigg ( \frac{\partial f}{\partial x}^T \frac{\partial f}{\partial x} \bigg ) \bigg|}  \\
\end{align*}
$$
Here, $D$ and $I$ are refering to the domain and image of the functions respectivly, and typically $D \sub \mathbb{R}^m$ and $I \sub \mathbb{R}^n$. 
There is no unique solution as the equation only restricts the $g$ in one dimension. Hence, some assumptions or decisions will need to be made about the function $g$ to be able to solve the equation (see the example section).

The equation can be split up into two constraits. The first is a global one which simply restricts the function not to move points out of the domain: $g(D)=D$. The second one is a local restriction which states that the density change introduced by $f$ must be compensated for by $g$ at every point, so that the the combined density change equals the ratio between the domain and image volumes. 


## Problem Formulation
Let $g$ be a naive generating function from $T \sub R^m$ to $X\sub R^n$. For our generating function to behave nicely, we would like it to fullfill:

$$
   \frac{ \int_{X'} d|x|^m}{\int_{X} d|x|^m}  = \frac{ \int_{T'} d|t| }{\int_{T} d|t|}  
$$

The $d|t|$ syntax, refferce to the measure unit in $T$, for a normal euclidean space this is simply $\Pi dt_i$. In a similar way $d|x|^m$ refferce to the $m$-dimensional measure in $X$. For example, if $m=2$, and $n=3$, $d|x|^m$ is the area unit in 3-dimensional space. $T'$ is an arbitrary subset of $T$, and $X'=g(T')$.
The equation then expresses that for an arbitrary subset $T'$ of the domain, $T'$ takes up the same amount of the 'space' as a ratio of the whole set in the domain and in the image. 

## Example Problem
A typical example of this issue arise if we want to sample uniformly from a disk. A straight forward way of sample the points is to uniformly sample a radius $r \in [0, R]$, and an angle $\alpha \in [0, 2\pi]$. Doing so generates points in the desired disk, but with a non-uniform density. Image XXX a shows an example of 1000 generated points using this strategy, whereas the b shows the desired density distribution. To reffer back to the problem formulation, $g: [0, R] \times [0, 2\pi] \rightarrow \mathbb{R}^2$, with $T= [0, R] \times [0, 2\pi] \in \mathbb{R}^2$. And more precisly:
$$
g(r,\alpha) = 
\begin{pmatrix}
    r \cos(\alpha) \\
    r \sin(\alpha)
\end{pmatrix}
$$

Putting the data into problem formulation equation and we get:
$$
\begin{align}
    \int_{X'}d|x|^m &= \int_{T'} \bigg |\frac{\partial g}{\partial t} \bigg | d|t|   =  \int_{T'}  drd\alpha \\
    \int_{X} d|x|^m &= \pi R^2 \\
    \int_{T'} d|t| &= \int_{T'} r drd\alpha \\  
    \int_{T} d|t| &= 2\pi R \\
    \Rightarrow \\
    0 &= \int_{T'} r - \frac{R}{2} drd\alpha \quad \text{Not solvable!}

\end{align}
$$

## Solution Derivation
Lets do the same process as in the example process, but with out assuming anything about the jacobian.

$$
\begin{align}
    
 0 &= \int_{T'} \bigg | \frac{\partial g}{\partial t} \bigg | - \frac{|X|}{|T|} d|t|, \quad \forall T' \sub T \Rightarrow \\
 0 &= \bigg | \frac{\partial g}{\partial t} \bigg | - \frac{|X|}{|T|}
\end{align}
$$



