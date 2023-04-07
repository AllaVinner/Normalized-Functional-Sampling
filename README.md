# Normalized-Functional-Sampling

## Abstract 
I often find myself in a position where I want to sample points from some exotic distribution. Most recently when I 
wanted to play around with the spiral dataset. However, an issue I have encountered is that there is an obvious way 
of generating points for said dataset, but this naive approach creates a none-uniform density. A simple example is 
to sample points in a disk by uniformly sampling the radius and the angle. The generated shape might be correct, but 
it will have more points in the center, a quality not always desirable. To address this issue, I propose an equation 
that yields a function which maps the naive input space onto itself with a tilted density so as to generate a uniform 
distribution in the final generated dataset.

I.e. given a naive generator function 

$$
f: T /rightarrow X
$$

, find ${z: T /rightarrow T}$, such that $/frac{1}{2}$ 




$x + y$







