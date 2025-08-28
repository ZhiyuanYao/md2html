# My Awesome Document

This is a demonstration of converting Markdown to a beautiful HTML file.

## Table of Contents
[TOC]

## Features
- Custom styling via CSS
- Syntax highlighting for code
- Table support

### Python Example
Here is a Python code block that will be highlighted.

```python
# this is to test section heading in copy block not counted as real one
import sys

def greet(name):
    """A simple greeting function."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    person = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(person))
```

### List Example

1. First list item
    - First nested list item
        - Second nested list item

2. First list item
    - First nested list item
        - Second nested list item

## Problem 1

**Topic**: Multicritical points (123)

**Thumbnail**: For a system described by two coupled scalar order parameters at a stable tetracritical point, calculate the mean-field ratio of the two order parameter magnitudes in the mixed-symmetry phase.

### Problem Statement

A problem with dispaly math 
$$F(\phi_1, \phi_2) = \frac{1}{2} r_1 \phi_1^2 + \frac{1}{2} r_2 \phi_2^2 + \frac{1}{4} g_1 \phi_1^4 + \frac{1}{4} g_2 \phi_2^4 + \frac{1}{2} g_{12} \phi_1^2 \phi_2^2$$

And inline math $r_1 = r_2 = 0$.

### Solution

The free energy is:
$$F(\phi_1, \phi_2) = \frac{1}{2} r_1 \phi_1^2 + \frac{1}{2} r_2 \phi_2^2 + \frac{1}{4} g_1 \phi_1^4 + \frac{1}{4} g_2 \phi_2^4 + \frac{1}{2} g_{12} \phi_1^2 \phi_2^2$$

Dislay math again:
$$ \frac{|\phi_1|}{|\phi_2|} = \sqrt{\frac{\phi_1^2}{\phi_2^2}} = \sqrt{\frac{g_2 - g_{12}}{g_1 - g_{12}}} $$

This is the final expression for the ratio of the order parameter magnitudes.

### Answer

$$ \boxed{\sqrt{\frac{g_2 - g_{12}}{g_1 - g_{12}}}} $$

---

## Problem 2
### Problem Statement
This is to test table detection (preceding text mingled with table) 

| A | B |
|---|---|
| C | D |


**Standard Model (SM) Sector:**
| Particle | Representation | $g$ | $B$ | $L$ | $Y$ |
|:---|:---|:---:|:---:|:---:|:---:|
| Left-handed quarks | $({\bf 3}, {\bf 2})_{1/6}$ | 6 | 1/3 | 0 | 1/6 |
| Right-handed up-quark | $({\bf 3}, {\bf 1})_{2/3}$| 3 | 1/3 | 0 | 2/3 |
| Right-handed down-quark | $({\bf 3}, {\bf 1})_{-1/3}$ | 3 | 1/3 | 0 | -1/3 |
| Left-handed leptons | $({\bf 1}, {\bf 2})_{-1/2}$| 2 | 0 | 1 | -1/2 |
| Right-handed electron | $({\bf 1}, {\bf 1})_{-1}$ | 1 | 0 | 1 | -1 |
| Higgs boson, $H$ | $({\bf 1}, {\bf 2})_{1/2}$ | 2 | 0 | 0 | 1/2 |

Standalone table should always work.

| Particle | Representation | $g$ | $D$ | $L_D$ | $Y_D$ |
|:---|:---|:---:|:---:|:---:|:---:|
| Left-handed dark quarks, $\Psi_D$| $({\bf 2}, {\bf 2})_{1/2}$ | 4 | 1/2 | 0 | 1/2 |
| Right-handed dark quarks, $\Psi_{D,R}$ | $({\bf 2}, {\bf 1})_{1/2}$ | 2 | 1/2 | 0 | 1/2 |
| Left-handed dark leptons, $\chi_D$ | $({\bf 1}, {\bf 2})_{-1/2}$ | 2 | 0 | 1 | -1/2|
| Dark Higgs boson, $\Phi_D$ | $({\bf 1}, {\bf 2})_{0}$ | 2 | 0 | 0 | 0 |

### Solution 

Placeholder for solution paragraph 1. 

Placeholder for solution paragraph 2. 

### Answer
$$\boxed{-\frac{42}{13}}$$

---

## Problem 3
### Parameter Sets
You are provided with three sets of parameters in JSON format. Your code should be able to run on any of these sets.

**Set 1:**
```json
{
    "duration": 10,
    "fs": 1000,
    "baseline_coeffs": [1.0e-9, 0.5e-9],
    "noise_std": 2.0e-10,
    "event_count": 15,
    "peak_loc_range": [1.0, 9.0],
    "peak_amp_range": [1.0e-9, 5.0e-9],
    "peak_width_range": [0.01, 0.05],
    "seed": 42
}
```

**Set 2:**
```json
{
    "duration": 20,
    "fs": 2000,
    "baseline_coeffs": [5.0e-9, -0.2e-9],
    "noise_std": 1.0e-9,
    "event_count": 30,
    "peak_loc_range": [1.0, 19.0],
    "peak_amp_range": [3.0e-9, 10.0e-9],
    "peak_width_range": [0.02, 0.08],
    "seed": 123
}
```

**Set 3:**
```json
{
    "duration": 5,
    "fs": 5000,
    "baseline_coeffs": [2.0e-9, 0.0],
    "noise_std": 0.5e-9,
    "event_count": 10,
    "peak_loc_range": [0.5, 4.5],
    "peak_amp_range": [8.0e-9, 15.0e-9],
    "peak_width_range": [0.005, 0.015],
    "seed": 2024
}
```

### Output
The function should return a single numeric value: the mean moles of electrons per event ($\bar{n}_e$), rounded to an appropriate number of significant figures, but for the purpose of this problem, round to 6 decimal places (relative to the base unit, not femto/pico etc). For example, `1.234567e-18`. If no events are detected, the function should return `0.0`.

## Solution(Gemini-2.5-pro)
### Solution Plan

The problem requires a multi-step signal processing and analysis pipeline. The plan is to first generate the specified current-time data, then process it to isolate and integrate the event spikes, and finally compute the average moles of electrons per event.

#### Constants and Setup
-   The Faraday constant, $F$, is a key physical constant. We will use the value from `scipy.constants.Faraday`.

#### 1. Signal Generation
-   **Time Array**: A time vector `t` will be created using `numpy.linspace` or `numpy.arange` from `0` to `duration` with a total of `duration * fs` points.
-   **Randomness**: To ensure reproducibility, the random number generator will be seeded using `numpy.random.seed(seed)`.
-   **Baseline**: The linear baseline current $I_{\text{base}} = a + bt$ will be calculated vectorized over the time array `t`.
-   **Events**: A loop running `event_count` times will generate the peaks. In each iteration:
    -   Peak parameters (location $\mu_i$, amplitude $A_i$, width $\sigma_i$) are drawn from their respective uniform distributions using `numpy.random.uniform()`.
    -   A Gaussian function $A_i \exp(-\frac{(t - \mu_i)^2}{2\sigma_i^2})$ is computed and added to an initially zero `I_events` array.
-   **Noise**: Gaussian noise will be generated using `numpy.random.normal(0, noise_std, size=len(t))`.
-   **Total Signal**: The final signal is the sum of the components: $I_{\text{total}} = I_{\text{base}} + I_{\text{events}} + I_{\text{noise}}$.

#### 2. Baseline Correction
-   Since the peaks are relatively sparse, a linear regression on the total signal can provide a good estimate of the baseline parameters.
-   We will use `scipy.stats.linregress(x=t, y=I_total)` to obtain the estimated slope and intercept of the baseline.
-   The estimated baseline is then subtracted from the total signal to obtain a baseline-corrected signal: $I_{\text{corrected}} = I_{\text{total}} - (slope \cdot t + intercept)$.

#### 3. Peak Detection
-   The core of the event identification will be `scipy.signal.find_peaks`. This function efficiently finds local maxima in a 1D array.
-   To distinguish genuine peaks from noise, a `height` threshold is necessary. A robust choice is a multiple of the known noise standard deviation, e.g., `height = 5 * noise_std`.
-   To avoid detecting multiple maxima on a single noisy peak, a `distance` parameter will be set. This specifies the minimum horizontal distance in samples between peaks. A sensible value is `distance = min_width * fs`, where `min_width` is the lower bound of `peak_width_range`.

#### 4. Peak Integration (Charge Calculation)
-   For each peak found, we need to determine its boundaries for integration. The `scipy.signal.peak_widths` function is ideal for this.
-   We will call `scipy.signal.peak_widths(I_corrected, peaks, rel_height=0.5)`, where `peaks` is the array of peak indices from `find_peaks`. `rel_height=0.5` measures the full width at half maximum (FWHM), which is a standard and robust choice.
-   This function returns several properties, including `left_ips` and `right_ips`, which are the interpolated start and end points of each peak at the specified relative height.
-   These floating-point indices will be converted to integer indices for slicing: `start_idx = np.floor(left_ips).astype(int)` and `end_idx = np.ceil(right_ips).astype(int)`.
-   A loop will iterate through each detected peak:
    -   Slice the `I_corrected` and `t` arrays using the `start_idx` and `end_idx`.
    -   Calculate the charge $Q_i$ for the peak by numerical integration using `scipy.integrate.trapz(y=current_slice, x=time_slice)`. The trapezoidal rule is simple and sufficient for this dense data.
    -   The calculated charges for all peaks are stored in a list.

#### 5. Final Calculation
-   If the list of detected peaks is empty (i.e., no peaks were found above the threshold), the function will return `0.0`.
-   Otherwise, the list of charges ($Q_i$) is converted to a NumPy array.
-   Each charge is converted to moles of electrons using the formula $n_{e,i} = Q_i / F$.
-   The mean of the resulting array of moles is computed using `numpy.mean()`.
-   This final value is returned as the result. A single numeric value. The complexity of this entire pipeline is dominated by the signal generation and processing steps, which are linear in the number of samples, approximately $O(\text{duration} \times \text{fs})$.

## Python code
```python
import numpy as np
import scipy.stats
import scipy.signal
import scipy.integrate
import scipy.constants

def solve_electron_moles(params: dict) -> float:
    """
    Analyzes a simulated electro-collision signal to find the mean moles of 
    electrons transferred per event.

    The process involves:
    1. Generating a signal with baseline, Gaussian peaks, and noise.
    2. Estimating and removing the linear baseline.
    3. Detecting peaks (events) in the corrected signal.
    4. Integrating each peak's current to find the charge.
    5. Converting charges to moles of electrons and finding the average.

    Args:
        params (dict): A dictionary of parameters for signal generation.

    Returns:
        float: The average moles of electrons per detected event.
    """
    # Unpack parameters from the dictionary
    duration = params['duration']
    fs = params['fs']
    a, b = params['baseline_coeffs']
    noise_std = params['noise_std']
    event_count = params['event_count']
    peak_loc_range = params['peak_loc_range']
    peak_amp_range = params['peak_amp_range']
    peak_width_range = params['peak_width_range']
    seed = params['seed']
    
    # Use the Faraday constant from SciPy
    F = scipy.constants.Faraday

    # 1. Signal Generation
    np.random.seed(seed)
    num_points = int(duration * fs)
    t = np.linspace(0, duration, num_points)

    # Baseline and a container for event signals
    I_base = a + b * t
    I_events = np.zeros_like(t)

    # Generate Gaussian peaks for each event
    for _ in range(event_count):
        mu = np.random.uniform(*peak_loc_range)
        A = np.random.uniform(*peak_amp_range)
        sigma = np.random.uniform(*peak_width_range)
        I_events += A * np.exp(-((t - mu)**2) / (2 * sigma**2))

    # Generate noise
    I_noise = np.random.normal(0, noise_std, num_points)

    # Combine components into the total signal
    I_total = I_base + I_events + I_noise

    # 2. Baseline Correction
    # Estimate baseline from the total signal using linear regression
    slope, intercept, _, _, _ = scipy.stats.linregress(t, I_total)
    I_baseline_est = slope * t + intercept
    I_corrected = I_total - I_baseline_est

    # 3. Peak Detection
    # Set detection threshold and minimum peak distance
    height_threshold = 5 * noise_std
    min_peak_dist_s = peak_width_range[0]
    min_peak_dist_samples = int(min_peak_dist_s * fs)
    
    # Find peaks in the corrected signal
    peaks, _ = scipy.signal.find_peaks(
        I_corrected, height=height_threshold, distance=min_peak_dist_samples
    )

    if len(peaks) == 0:
        return 0.0

    # 4. Determine Integration Boundaries
    # Use peak_widths to find start and end of each peak for integration
    widths_info = scipy.signal.peak_widths(I_corrected, peaks, rel_height=0.5)
    left_ips = widths_info[2]
    right_ips = widths_info[3]

    start_indices = np.floor(left_ips).astype(int)
    end_indices = np.ceil(right_ips).astype(int)
    
    # Clip indices to ensure they are within the array bounds
    start_indices = np.maximum(0, start_indices)
    end_indices = np.minimum(num_points - 1, end_indices)

    # 5. Integrate Peaks to Find Charge
    charges = []
    for i in range(len(peaks)):
        start_idx, end_idx = start_indices[i], end_indices[i]
        
        # Ensure there are at least two points for integration
        if end_idx > start_idx:
            time_slice = t[start_idx : end_idx + 1]
            current_slice = I_corrected[start_idx : end_idx + 1]
            # Integrate using the trapezoidal rule to get charge in Coulombs
            charge = scipy.integrate.trapz(current_slice, time_slice)
            if charge > 0: # Only consider positive charges (physical phenomenon)
                charges.append(charge)

    if not charges:
        return 0.0
        
    # 6. Calculate Mean Moles of Electrons
    moles_per_event = np.array(charges) / F
    mean_moles = np.mean(moles_per_event)

    return mean_moles

def main():
    """
    Defines parameter sets and runs the solver for each, returning the results.
    """
    param_sets = [
        {
            "duration": 10, "fs": 1000, "baseline_coeffs": [1.0e-9, 0.5e-9], 
            "noise_std": 2.0e-10, "event_count": 15, "peak_loc_range": [1.0, 9.0], 
            "peak_amp_range": [1.0e-9, 5.0e-9], "peak_width_range": [0.01, 0.05], "seed": 42
        },
        {
            "duration": 20, "fs": 2000, "baseline_coeffs": [5.0e-9, -0.2e-9], 
            "noise_std": 1.0e-9, "event_count": 30, "peak_loc_range": [1.0, 19.0], 
            "peak_amp_range": [3.0e-9, 10.0e-9], "peak_width_range": [0.02, 0.08], "seed": 123
        },
        {
            "duration": 5, "fs": 5000, "baseline_coeffs": [2.0e-9, 0.0], 
            "noise_std": 0.5e-9, "event_count": 10, "peak_loc_range": [0.5, 4.5], 
            "peak_amp_range": [8.0e-9, 15.0e-9], "peak_width_range": [0.005, 0.015], "seed": 2024
        }
    ]

    results = []
    for params in param_sets:
        result = solve_electron_moles(params)
        # Round final result to specified precision
        results.append(round(result, 6 + 18)) # 1e-18 precision, round at 24th decimal place.

    return results

if __name__ == '__main__':
    # Execute the main function and print the results for verification.
    results = main()
    # Let's format the output to be readable in scientific notation
    formatted_results = [f"{res:.6e}" for res in results]
    print(formatted_results)

```

------

