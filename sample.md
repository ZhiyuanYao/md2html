# Sample Document for MD2HTML Testing

This document demonstrates the conversion of Markdown to HTML with comprehensive testing of all supported features.

## Table of Contents
[TOC]

## Unicode Character Tests

This section tests the rendering of various Unicode characters and symbols.

### Mathematical Symbols
- Superscripts: x², x³, x⁴, x⁵, x⁶, x⁷, x⁸, x⁹, x¹⁰
- Subscripts: H₂O, CO₂, CH₄, N₂O, SO₄²⁻, Ca²⁺
- Greek letters: α, β, γ, δ, ε, ζ, η, θ, λ, μ, π, ρ, σ, τ, φ, χ, ψ, ω
- Greek capitals: Α, Β, Γ, Δ, Ε, Θ, Λ, Π, Σ, Φ, Ψ, Ω
- Math operators: ±, ×, ÷, ≠, ≤, ≥, ≈, ∞, ∑, ∏, ∫, ∂, ∇, √, ∆

### Physical Units  
- Speed: m/s², km/h, rad/s²
- Energy: J/kg·K, W/m²·K, kWh
- Temperature: °C, °F, K
- Angles: 45°, 90°, 180°, 2π radians
- Electricity: μA, mV, kΩ, MΩ

---

## LaTeX Math Delimiter Tests

This section demonstrates all supported LaTeX math delimiter types and features.

### Display Math Delimiters

#### 1. Double Dollar Signs 
Test `$$...$$` math
$$F(x) = \int_{-\infty}^{\infty} f(t) e^{-2\pi ixt} dt$$

#### 2. Square Brackets Display Math
Test `\[...\]` math
\[
E = mc^2 + \frac{1}{2}mv^2
\]

#### 3. Standalone Boxed Expressions (Auto Display Math)
Test standalone `\boxed{...}` 
\boxed{\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}

### Inline Math Delimiters

#### 4. Single Dollar Signs 
Test `$...$` math 
The quadratic formula is $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ for solving $ax^2 + bx + c = 0$.

#### 5. Parentheses Inline Math 
Test `\(...\)` math. Einstein's mass-energy equivalence is \(E = mc^2\) where \(c\) is the speed of light.

### Complex Nested Examples

#### Mixed Delimiters in Same Paragraph
Consider the equation $f(x) = x^2 + 1$ and the integral \(\int_0^1 f(x)dx\). The solution is:
$$\int_0^1 (x^2 + 1)dx = \left[\frac{x^3}{3} + x\right]_0^1 = \frac{4}{3}$$

#### Nested Braces in Boxed Expressions
\boxed{\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}}

\boxed{\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e}

#### Complex Display Math with Multiple Lines
\[
\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{align}
\]

### Boxed Math Inside Other Delimiters

#### Boxed Inside Display Math
$$\boxed{H = -\sum_i p_i \log p_i}$$

#### Multiple Boxed Expressions
The final answers are:
$$\boxed{x_1 = \frac{-b + \sqrt{\Delta}}{2a}} \quad \text{and} \quad \boxed{x_2 = \frac{-b - \sqrt{\Delta}}{2a}}$$

### Edge Cases and Special Characters

#### Greek Letters and Special Symbols
$$\alpha + \beta = \gamma \quad \Rightarrow \quad \sum_{i=1}^n \alpha_i = \prod_{j=1}^m \beta_j$$

#### Fractions within Fractions
\boxed{\frac{\frac{a}{b} + \frac{c}{d}}{\frac{e}{f} - \frac{g}{h}}}

#### Matrix Notation
\[
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
\]

---

## List Formatting Tests

This section tests various list types and nesting patterns.

### Normal List With Preceding Text 

**Final Answer Format Instructions:**  
- Your answer must be a single analytic expression.  
- Use the symbol $\pi$ for pi.  
- Use standard mathematical notation: multiplication must be denoted explicitly (e.g., $a \cdot b$ or $ab$), and fractions must be written using `\frac{}{}`.  
- The expression must be boxed using `$\boxed{}$`.


### Mixed Indentation Lists
1. First main item
    - Nested bullet point (4-space indent)
        - Deeply nested item (8-space indent)
    - Another nested item
2. Second main item
    - Different indentation (2-space indent)
    - Sub-item with 4-space indent
3. Third main item with multiple paragraphs This paragraph is part of item 3.
    - Nested list after paragraph
    - Another nested item

### Complex Nested Structure
1. **Project Setup**
    This is the main project setup phase.
    1. Create virtual environment:
       ```bash
       python -m venv venv
       source venv/bin/activate  # Linux/Mac
       venv\Scripts\activate     # Windows
       ```
    2. Install dependencies:
      - Core packages: `pip install markdown`
      - Optional packages: `pip install beautifulsoup4`

2. **Configuration**
    - Edit configuration file
    - Set up templates  
    - Configure themes
   
3. **Testing**
    Run tests to verify setup.
    - Unit tests: `pytest tests/`
    - Integration tests: `pytest integration/`

### GitHub-Style Task Lists

**Project Development Checklist:**
- [x] Set up project structure
- [x] Implement basic markdown conversion
- [x] Add syntax highlighting with Prism.js
- [x] Create responsive table system
- [x] Migrate from Python markdown to Mistune
- [ ] Add table of contents generation
- [ ] Implement advanced math rendering
- [ ] Create mobile-responsive design
- [ ] Add print stylesheet optimization

**Feature Implementation Status:**
- [x] **Core Features**
  - [x] Markdown to HTML conversion
  - [x] Code syntax highlighting
  - [x] Math equation rendering
- [x] **Advanced Tables**
  - [x] Responsive padding adjustment
  - [x] Hover effects and modern styling
  - [x] Natural width sizing
- [ ] **Enhanced Features**
  - [x] Section collapsing functionality
  - [ ] Advanced TOC with anchor links
  - [ ] Custom theme system
  - [ ] Plugin architecture

---

## Table Formatting Tests

This section tests various table layouts and formatting options.

### Basic Table
| Column A | Column B | Column C |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Item X   | Item Y   | Item Z   |

### Scientific Data Table
| Particle | Representation | $g$ | $B$ | $L$ | $Y$ |
|:---------|:---------------|:---:|:---:|:---:|:---:|
| Left-handed quarks | $({\bf 3}, {\bf 2})_{1/6}$ | 6 | 1/3 | 0 | 1/6 |
| Right-handed up-quark | $({\bf 3}, {\bf 1})_{2/3}$| 3 | 1/3 | 0 | 2/3 |
| Right-handed down-quark | $({\bf 3}, {\bf 1})_{-1/3}$ | 3 | 1/3 | 0 | -1/3 |
| Left-handed leptons | $({\bf 1}, {\bf 2})_{-1/2}$| 2 | 0 | 1 | -1/2 |
| Right-handed electron | $({\bf 1}, {\bf 1})_{-1}$ | 1 | 0 | 1 | -1 |
| Higgs boson, $H$ | $({\bf 1}, {\bf 2})_{1/2}$ | 2 | 0 | 0 | 1/2 |

### Performance Statistics Table
| Subject | Total Files | ✓ Success | ✗ Failure | Success Rate | ? Missing |
|---------|-------------|-----------|-----------|--------------|-----------|
| Electromagnetism | 24,782 | 12,379 | 12,352 | 50.0% | 51 |
| Linear Algebra | 62,265 | 47,324 | 14,506 | 76.0% | 435 |
| Many Body Physics | 42,146 | 19,577 | 22,407 | 46.5% | 162 |
| Mathematical Analysis | 76,771 | 50,986 | 25,407 | 66.4% | 378 |
| Mechanics | 21,965 | 12,129 | 9,768 | 55.2% | 68 |
| **TOTAL** | **379,752** | **142,395** | **84,440** | **37.5%** | **1,094** |

---


## Code Syntax Highlighting Tests

This section demonstrates syntax highlighting for various programming languages.

### JSON Configuration
```json
{
    "name": "md2html-converter",
    "version": "1.0.0",
    "dependencies": {
        "markdown": "^3.4.0"
    },
    "settings": {
        "theme": "elegant",
        "math_support": true,
        "code_highlighting": true
    }
}
```

### JavaScript Example
```javascript
class MathUtils {
    static factorial(n) {
        if (n === 0 || n === 1) return 1;
        return n * this.factorial(n - 1);
    }
    
    static isPrime(num) {
        if (num < 2) return false;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    }
}
```


### Python Code Block
```python
# Test of Python syntax highlighting
import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

if __name__ == "__main__":
    numbers = fibonacci(10)
    print(f"First 10 Fibonacci numbers: {numbers}")
```


---

## Problem Examples

This section contains sample problems demonstrating real-world usage scenarios.

## Problem 1: Physics - Multicritical Points

**Topic**: Multicritical points (Advanced Statistical Mechanics)

**Thumbnail**: For a system described by two coupled scalar order parameters at a stable tetracritical point, calculate the mean-field ratio of the two order parameter magnitudes in the mixed-symmetry phase.

### Problem Statement

Consider a system with free energy functional:
$$F(\phi_1, \phi_2) = \frac{1}{2} r_1 \phi_1^2 + \frac{1}{2} r_2 \phi_2^2 + \frac{1}{4} g_1 \phi_1^4 + \frac{1}{4} g_2 \phi_2^4 + \frac{1}{2} g_{12} \phi_1^2 \phi_2^2$$

At the tetracritical point, both order parameters can be non-zero. Find the ratio of the order parameter magnitudes when $r_1 = r_2 = 0$.

### Solution

The equilibrium conditions are:
$$\frac{\partial F}{\partial \phi_1} = r_1 \phi_1 + g_1 \phi_1^3 + g_{12} \phi_1 \phi_2^2 = 0$$
$$\frac{\partial F}{\partial \phi_2} = r_2 \phi_2 + g_2 \phi_2^3 + g_{12} \phi_1^2 \phi_2 = 0$$

Setting $r_1 = r_2 = 0$ and assuming non-trivial solutions:
$$g_1 \phi_1^2 + g_{12} \phi_2^2 = 0 \quad \Rightarrow \quad \phi_1^2 = -\frac{g_{12}}{g_1} \phi_2^2$$
$$g_2 \phi_2^2 + g_{12} \phi_1^2 = 0 \quad \Rightarrow \quad \phi_2^2 = -\frac{g_{12}}{g_2} \phi_1^2$$

Substituting the second into the first:
$$\phi_1^2 = -\frac{g_{12}}{g_1} \left(-\frac{g_{12}}{g_2} \phi_1^2\right) = \frac{g_{12}^2}{g_1 g_2} \phi_1^2$$

For non-trivial solutions: $\frac{g_{12}^2}{g_1 g_2} = 1$, thus $g_{12}^2 = g_1 g_2$.

The ratio of magnitudes is:
$$\frac{|\phi_1|}{|\phi_2|} = \sqrt{\frac{g_2 - g_{12}}{g_1 - g_{12}}}$$

### Answer
$$\boxed{\sqrt{\frac{g_2 - g_{12}}{g_1 - g_{12}}}}$$

---

## Problem 2: Mathematics - Advanced Calculus

**Topic**: Multivariable optimization with constraints

**Thumbnail**: Find the extrema of $f(x,y) = x^2 + y^2 - xy$ subject to the constraint $x + y = 1$.

### Problem Statement

Using Lagrange multipliers, find the critical points of:
$$f(x,y) = x^2 + y^2 - xy$$
subject to the constraint:
$$g(x,y) = x + y - 1 = 0$$

### Solution

Set up the Lagrangian:
$$\mathcal{L}(x,y,\lambda) = x^2 + y^2 - xy - \lambda(x + y - 1)$$

Taking partial derivatives:
$$\frac{\partial \mathcal{L}}{\partial x} = 2x - y - \lambda = 0$$
$$\frac{\partial \mathcal{L}}{\partial y} = 2y - x - \lambda = 0$$
$$\frac{\partial \mathcal{L}}{\partial \lambda} = -(x + y - 1) = 0$$

From the first two equations: $2x - y = 2y - x$, which gives $3x = 3y$, so $x = y$.

Using the constraint $x + y = 1$ with $x = y$:
$$2x = 1 \quad \Rightarrow \quad x = y = \frac{1}{2}$$

The critical point is $\left(\frac{1}{2}, \frac{1}{2}\right)$ with function value:
$$f\left(\frac{1}{2}, \frac{1}{2}\right) = \frac{1}{4} + \frac{1}{4} - \frac{1}{4} = \frac{1}{4}$$

### Answer
\boxed{\text{Minimum at } \left(\frac{1}{2}, \frac{1}{2}\right) \text{ with value } \frac{1}{4}}

---
