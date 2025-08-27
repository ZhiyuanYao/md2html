# Sampled Problems

This file contains 10 randomly sampled problems with verify_status: success.

## 🗺️ Problem Roadmap

- **[Problem 1](#problem-1)**: **Multicritical Points**
  - For a system described by two coupled scalar order parameters at a stable tetracritical point, calculate the mean-field ratio of the two order parameter magnitudes in the mixed-symmetry phase.
- **[Problem 2](#problem-2)**: **Experimental Characterization of Crystal Structure**
  - Given the total structure factor $S(Q)$ for a liquid, write the integral transformation to obtain the pair correlation function $g(r)$.
- **[Problem 3](#problem-3)**: **1 N Expansion**
  - Calculate the one-loop beta function for the gauge coupling in an SU(N) Yang-Mills theory coupled to $N_f$ flavors of massless adjoint Majorana fermions in the 't Hooft limit.
---

## Solutions

```latex
\begin{equation}
    f(a) = \frac{1}{2\pi i} \oint\frac{f(z)}{z-a}dz
\end{equation}
```

## Problem 1

**Topic**: Multicritical points (123)

**Thumbnail**: For a system described by two coupled scalar order parameters at a stable tetracritical point, calculate the mean-field ratio of the two order parameter magnitudes in the mixed-symmetry phase.

### Problem

A physical system near a multicritical point is described by two coupled real scalar order parameters, $\phi_1$ and $\phi_2$. Within the mean-field approximation, the Ginzburg-Landau free energy density, $F$, is given by:
$$F(\phi_1, \phi_2) = \frac{1}{2} r_1 \phi_1^2 + \frac{1}{2} r_2 \phi_2^2 + \frac{1}{4} g_1 \phi_1^4 + \frac{1}{4} g_2 \phi_2^4 + \frac{1}{2} g_{12} \phi_1^2 \phi_2^2$$
The parameters $g_1$ and $g_2$ are positive stabilization constants, and $g_{12}$ is a coupling constant. The coefficients $r_1$ and $r_2$ are control parameters (e.g., functions of temperature and pressure).

The system exhibits a stable tetracritical point at $r_1 = r_2 = 0$. The stability of this point requires the quartic couplings to satisfy $g_1 > 0$, $g_2 > 0$, and the condition $g_1 g_2 > g_{12}^2$.

We are interested in the "mixed-symmetry" phase, where the equilibrium state has non-zero expectation values for both order parameters, $\langle \phi_1 \rangle \neq 0$ and $\langle \phi_2 \rangle \neq 0$. Consider the scenario where the system is tuned into this phase along a specific path in the parameter space defined by $r_1 = r_2 = r$, with $r < 0$. For the mixed-symmetry phase to be the stable ground state along this path, the couplings must also satisfy the condition $g_{12} < \min(g_1, g_2)$.

Assuming all these conditions are met, calculate the ratio of the magnitudes of the order parameters, $\frac{|\langle \phi_1 \rangle|}{|\langle \phi_2 \rangle|}$, in this state. Express your answer in terms of the coupling constants $g_1$, $g_2$, and $g_{12}$.

### Solution

The equilibrium state of the system is found by minimizing the Ginzburg-Landau free energy density $F(\phi_1, \phi_2)$ with respect to the order parameters $\phi_1$ and $\phi_2$. The values of $\phi_1$ and $\phi_2$ at the minimum correspond to their expectation values, $\langle \phi_1 \rangle$ and $\langle \phi_2 \rangle$. For simplicity, we will drop the angle brackets during the calculation.

The free energy is:
$$F(\phi_1, \phi_2) = \frac{1}{2} r_1 \phi_1^2 + \frac{1}{2} r_2 \phi_2^2 + \frac{1}{4} g_1 \phi_1^4 + \frac{1}{4} g_2 \phi_2^4 + \frac{1}{2} g_{12} \phi_1^2 \phi_2^2$$

To find the minima, we set the partial derivatives of $F$ with respect to $\phi_1$ and $\phi_2$ to zero:
$$ \frac{\partial F}{\partial \phi_1} = r_1 \phi_1 + g_1 \phi_1^3 + g_{12} \phi_1 \phi_2^2 = \phi_1 (r_1 + g_1 \phi_1^2 + g_{12} \phi_2^2) = 0 $$
$$ \frac{\partial F}{\partial \phi_2} = r_2 \phi_2 + g_2 \phi_2^3 + g_{12} \phi_2 \phi_1^2 = \phi_2 (r_2 + g_2 \phi_2^2 + g_{12} \phi_1^2) = 0 $$

The problem states that we are in the mixed-symmetry phase, which is defined by $\phi_1 \neq 0$ and $\phi_2 \neq 0$. Therefore, we can divide the first equation by $\phi_1$ and the second by $\phi_2$, leading to a system of two coupled linear equations for $\phi_1^2$ and $\phi_2^2$:
$$ g_1 \phi_1^2 + g_{12} \phi_2^2 = -r_1 $$
$$ g_{12} \phi_1^2 + g_2 \phi_2^2 = -r_2 $$

The problem specifies that the system is prepared in a state where $r_1 = r_2 = r < 0$. Substituting this into the system of equations gives:
$$ g_1 \phi_1^2 + g_{12} \phi_2^2 = -r \quad (1)$$
$$ g_{12} \phi_1^2 + g_2 \phi_2^2 = -r \quad (2)$$

Since the right-hand sides of both equations are equal, we can equate the left-hand sides:
$$ g_1 \phi_1^2 + g_{12} \phi_2^2 = g_{12} \phi_1^2 + g_2 \phi_2^2 $$

Now, we rearrange the terms to group $\phi_1^2$ and $\phi_2^2$:
$$ g_1 \phi_1^2 - g_{12} \phi_1^2 = g_2 \phi_2^2 - g_{12} \phi_2^2 $$
$$ (g_1 - g_{12}) \phi_1^2 = (g_2 - g_{12}) \phi_2^2 $$

We are asked to find the ratio $\frac{|\phi_1|}{|\phi_2|}$. We can first find the ratio of the squares:
$$ \frac{\phi_1^2}{\phi_2^2} = \frac{g_2 - g_{12}}{g_1 - g_{12}} $$

The problem states that the couplings satisfy $g_{12} < \min(g_1, g_2)$. This implies that $g_1 - g_{12} > 0$ and $g_2 - g_{12} > 0$. Therefore, the ratio on the right-hand side is positive, which is consistent with the left-hand side being a ratio of squares.

To find the ratio of the magnitudes, we take the square root of both sides:
$$ \frac{|\phi_1|}{|\phi_2|} = \sqrt{\frac{\phi_1^2}{\phi_2^2}} = \sqrt{\frac{g_2 - g_{12}}{g_1 - g_{12}}} $$

This is the final expression for the ratio of the order parameter magnitudes.

### Answer


$$ \boxed{\sqrt{\frac{g_2 - g_{12}}{g_1 - g_{12}}}} $$


---

## Problem 2

**Topic**: experimental characterization of crystal structure (88)

**Thumbnail**: Given the total structure factor $S(Q)$ for a liquid, write the integral transformation to obtain the pair correlation function $g(r)$.

### Problem

In the statistical physics of liquids, the spatial arrangement of particles is described by the pair correlation function, $g(r)$. This function gives the probability of finding a particle at a distance $r$ from a reference particle, relative to the probability expected for a completely random distribution at the same density. The static structure factor, $S(Q)$, which is directly measurable in scattering experiments (like X-ray or neutron diffraction), is related to the Fourier transform of $g(r)$. For an isotropic system with number density $\rho$, the relationship is given by:
$$
S(Q) = 1 + \frac{4\pi\rho}{Q} \int_0^\infty r [g(r) - 1] \sin(Qr) dr
$$
where $Q$ is the magnitude of the scattering wavevector.

Consider a simple model for a liquid where the interaction between particles is described by a square-well potential. The pair correlation function for this model is given by:
$$
g(r) = \begin{cases}
0 & \text{for } r < \sigma \\
g_0 & \text{for } \sigma \le r < \lambda\sigma \\
1 & \text{for } r \ge \lambda\sigma
\end{cases}
$$
Here, $\sigma$ represents the hard-core diameter of the particles, $\lambda\sigma$ (with $\lambda > 1$) is the range of the attractive part of the potential, and $g_0$ is a constant representing the enhanced probability of finding particles in the potential well.

Your task is to calculate the static structure factor $S(Q)$ for this square-well model. Express your answer as a function of $Q$, $\rho$, $\sigma$, $\lambda$, and $g_0$.

### Solution

The static structure factor $S(Q)$ is related to the pair correlation function $g(r)$ by the formula:
$$
S(Q) = 1 + \frac{4\pi\rho}{Q} \int_0^\infty r [g(r) - 1] \sin(Qr) dr
$$
We are given a piecewise pair correlation function $g(r)$. From this, we can define $g(r) - 1$:
$$
g(r) - 1 = \begin{cases}
-1 & \text{for } r < \sigma \\
g_0 - 1 & \text{for } \sigma \le r < \lambda\sigma \\
0 & \text{for } r \ge \lambda\sigma
\end{cases}
$$
The integral in the expression for $S(Q)$ can be split into the regions where $g(r)-1$ is non-zero:
$$
\int_0^\infty r [g(r) - 1] \sin(Qr) dr = \int_0^\sigma r(-1)\sin(Qr)dr + \int_\sigma^{\lambda\sigma} r(g_0 - 1)\sin(Qr)dr
$$
Let's first find the indefinite integral of $r\sin(Qr)$ using integration by parts, $\int u dv = uv - \int v du$.
Let $u=r$ and $dv = \sin(Qr)dr$. Then $du=dr$ and $v = -\frac{1}{Q}\cos(Qr)$.
$$
\int r\sin(Qr)dr = r\left(-\frac{\cos(Qr)}{Q}\right) - \int \left(-\frac{\cos(Qr)}{Q}\right) dr = -\frac{r\cos(Qr)}{Q} + \frac{1}{Q}\int\cos(Qr)dr
$$
$$
\int r\sin(Qr)dr = -\frac{r\cos(Qr)}{Q} + \frac{\sin(Qr)}{Q^2} = \frac{\sin(Qr) - Qr\cos(Qr)}{Q^2}
$$
Now we can evaluate the two definite integrals.

For the first integral:
$$
\int_0^\sigma -r\sin(Qr)dr = -\left[\frac{\sin(Qr) - Qr\cos(Qr)}{Q^2}\right]_0^\sigma
$$
$$
= -\left( \frac{\sin(Q\sigma) - Q\sigma\cos(Q\sigma)}{Q^2} - \frac{\sin(0) - 0}{Q^2} \right) = -\frac{\sin(Q\sigma) - Q\sigma\cos(Q\sigma)}{Q^2}
$$

For the second integral:
$$
\int_\sigma^{\lambda\sigma} r(g_0-1)\sin(Qr)dr = (g_0-1) \left[\frac{\sin(Qr) - Qr\cos(Qr)}{Q^2}\right]_\sigma^{\lambda\sigma}
$$
$$
= \frac{g_0-1}{Q^2} \left[ (\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)) - (\sin(Q\sigma) - Q\sigma\cos(Q\sigma)) \right]
$$
Now, we sum these two parts:
$$
\int_0^\infty r [g(r) - 1] \sin(Qr) dr = -\frac{\sin(Q\sigma) - Q\sigma\cos(Q\sigma)}{Q^2} + \frac{g_0-1}{Q^2} \left[ (\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)) - (\sin(Q\sigma) - Q\sigma\cos(Q\sigma)) \right]
$$
Let's group terms with $(\sin(Q\sigma) - Q\sigma\cos(Q\sigma))$:
$$
= \frac{1}{Q^2} \left[ (-1 - (g_0-1))(\sin(Q\sigma) - Q\sigma\cos(Q\sigma)) + (g_0-1)(\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)) \right]
$$
$$
= \frac{1}{Q^2} \left[ -g_0(\sin(Q\sigma) - Q\sigma\cos(Q\sigma)) + (g_0-1)(\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)) \right]
$$
Finally, we substitute this back into the expression for $S(Q)$:
$$
S(Q) = 1 + \frac{4\pi\rho}{Q} \left( \frac{1}{Q^2} \left[ -g_0(\sin(Q\sigma) - Q\sigma\cos(Q\sigma)) + (g_0-1)(\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)) \right] \right)
$$
$$
S(Q) = 1 + \frac{4\pi\rho}{Q^3} \left[ -g_0(\sin(Q\sigma) - Q\sigma\cos(Q\sigma)) + (g_0-1)(\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)) \right]
$$
This is the final expression for the static structure factor for the given model.

### Answer


$$ \boxed{S(Q) = 1 + \frac{4\pi\rho}{Q^3} \left[ (g_0-1)\left(\sin(Q\lambda\sigma) - Q\lambda\sigma\cos(Q\lambda\sigma)\right) - g_0\left(\sin(Q\sigma) - Q\sigma\cos(Q\sigma)\right) \right]} $$


---

## Problem 3

**Topic**: 1 N expansion (60)

**Thumbnail**: Calculate the one-loop beta function for the gauge coupling in an SU(N) Yang-Mills theory coupled to $N_f$ flavors of massless adjoint Majorana fermions in the 't Hooft limit.

### Problem

Consider an SU(N) Yang-Mills theory in four spacetime dimensions, coupled to $N_f$ flavors of massless Majorana fermions, with each flavor transforming in the adjoint representation of the gauge group. The Lagrangian for this theory is given by:
$$ \mathcal{L} = -\frac{1}{4} F_{\mu\nu}^a F^{a\mu\nu} + i \sum_{i=1}^{N_f} \bar{\psi}_i^a \gamma^\mu (D_\mu \psi_i)^a $$
where $a = 1, \dots, N^2-1$ is the gauge group index, $i = 1, \dots, N_f$ is the flavor index, and $\psi_i^a$ are the Majorana fermion fields. The field strength tensor is $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c$, and the covariant derivative acting on an adjoint field is $(D_\mu \psi)^a = \partial_\mu \psi^a + g f^{abc} A_\mu^b \psi^c$. Here, $g$ is the gauge coupling constant and $f^{abc}$ are the structure constants of the SU(N) Lie algebra.

In the 't Hooft limit, we take $N \to \infty$ and $g \to 0$ such that the 't Hooft coupling $\lambda = g^2 N$ is held fixed. The running of this coupling is described by its beta function, $\beta_\lambda(\lambda) = \mu \frac{d\lambda}{d\mu}$, where $\mu$ is the renormalization scale.

Calculate the one-loop beta function $\beta_\lambda(\lambda)$ for the 't Hooft coupling in this theory. You may use the following standard results for the SU(N) group theory factors in the adjoint representation: the quadratic Casimir is $C_2(\text{adj}) = N$, and the index is $T(\text{adj}) = N$.

### Solution

The first step is to compute the one-loop beta function for the gauge coupling $g$, which is given by the general formula:
$$ \beta(g) = \mu \frac{dg}{d\mu} = -b_0 \frac{g^3}{16\pi^2} + \mathcal{O}(g^5) $$
The coefficient $b_0$ depends on the particle content of the theory. For a generic gauge theory, it is given by:
$$ b_0 = \frac{11}{3} C_2(G) - \frac{2}{3} \sum_{\text{fermions}} N_f T(R_f) - \frac{1}{6} \sum_{\text{scalars}} N_s T(R_s) $$
where the sum is over all fermion and real scalar representations. The fermion term's coefficient is $\frac{2}{3}$ for Majorana or Weyl fermions and $\frac{4}{3}$ for Dirac fermions. Our theory contains only gauge bosons and $N_f$ flavors of Majorana fermions.

The gauge bosons (gluons) are in the adjoint representation of SU(N). Their contribution to $b_0$ is the first term, where $C_2(G)$ is the quadratic Casimir of the adjoint representation. We are given $C_2(\text{adj}) = N$.
So, the gauge boson contribution is:
$$ b_{0, \text{gauge}} = \frac{11}{3} N $$
The fermions are also in the adjoint representation. We have $N_f$ flavors of massless Majorana fermions. For each flavor, the representation is $R_f = \text{adj}$, and we are given that the index for this representation is $T(\text{adj}) = N$. The contribution from $N_f$ flavors of Majorana fermions is:
$$ b_{0, \text{fermion}} = - \frac{2}{3} N_f T(\text{adj}) = - \frac{2}{3} N_f N $$
The total one-loop coefficient $b_0$ is the sum of these contributions:
$$ b_0 = b_{0, \text{gauge}} + b_{0, \text{fermion}} = \frac{11}{3} N - \frac{2N_f}{3} N = \frac{N}{3} (11 - 2N_f) $$
Substituting this into the expression for $\beta(g)$, we get:
$$ \beta(g) = - \frac{N(11 - 2N_f)}{3} \frac{g^3}{16\pi^2} $$
This expression is valid for any $N$. Now, we want to find the beta function for the 't Hooft coupling, $\lambda = g^2 N$. We use the definition $\beta_\lambda(\lambda) = \mu \frac{d\lambda}{d\mu}$ and the chain rule. Since $N$ is a fixed parameter (even in the limit $N\to\infty$), it does not depend on the renormalization scale $\mu$.
$$ \beta_\lambda(\lambda) = \mu \frac{d(g^2 N)}{d\mu} = N \mu \frac{d(g^2)}{d\mu} $$
Using the chain rule for the derivative of $g^2$:
$$ \mu \frac{d(g^2)}{d\mu} = 2g \left( \mu \frac{dg}{d\mu} \right) = 2g \beta(g) $$
So, we can express $\beta_\lambda$ in terms of $\beta(g)$:
$$ \beta_\lambda(\lambda) = 2gN \beta(g) $$
Now, we substitute our result for $\beta(g)$:
$$ \beta_\lambda(\lambda) = 2gN \left( - \frac{N(11 - 2N_f)}{3} \frac{g^3}{16\pi^2} \right) $$
Let's simplify this expression:
$$ \beta_\lambda(\lambda) = - \frac{2N^2 (11 - 2N_f)}{48\pi^2} g^4 = - \frac{N^2 (11 - 2N_f)}{24\pi^2} g^4 $$
Finally, we express the result in terms of the 't Hooft coupling $\lambda = g^2 N$. We can write $g^4 N^2 = (g^2 N)^2 = \lambda^2$.
Substituting this into our expression for $\beta_\lambda(\lambda)$:
$$ \beta_\lambda(\lambda) = - \frac{(11 - 2N_f)}{24\pi^2} \lambda^2 $$
This is the one-loop beta function for the 't Hooft coupling $\lambda$. It is finite in the 't Hooft limit, as expected.

### Answer


$$ \boxed{-\frac{(11 - 2N_f)\lambda^2}{24\pi^2}} $$


---
