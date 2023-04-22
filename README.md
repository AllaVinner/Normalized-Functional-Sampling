# Normalized-Functional-Sampling

## Abstract 
I often find myself in a position where I want to sample points from some exotic distribution. Most recently when I 
wanted to play around with the spiral dataset. However, an issue I have encountered is that there is an obvious way 
of generating points for said dataset, but this naive approach creates a none-uniform density. A simple example is 
to sample points in a disk by uniformly sampling the radius and the angle. The generated shape might be correct, but 
it will have more points in the center, a quality not always desirable. To address this issue, I propose an equation 
that yields a function which maps the naive input space onto itself with a tilted density so as to generate a uniform 
distribution in the final generated dataset.

I.e. given a naive generator function $f: T \rightarrow X$, find an injective mapping $z: T \rightarrow T$ that satisfy $|\frac{\partial f}{\partial z}||\frac{\partial z}{\partial t}|= \frac{|X|}{|T|}$. 


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



