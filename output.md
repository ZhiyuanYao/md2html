# angular displacement, velocity, and acceleration

## Problem 0
##### Background
In a cutting-edge research facility, engineers are testing a new flywheel energy storage system. The flywheel, which is initially stationary, is accelerated by a magnetic propulsion system that delivers a constant angular acceleration $\alpha$. This system is crucial for renewable energy applications, as it stores excess energy as rotational kinetic energy. To evaluate the system's performance, the engineers need to determine the angular displacement of the flywheel after a time interval $t$.

##### Knowledge Points Tested
- Definition of angular acceleration as the time derivative of angular velocity: $\alpha = \frac{d\omega}{dt}$.
- Definition of angular velocity as the time derivative of angular displacement: $\omega = \frac{d\theta}{dt}$.
- Integration of constant acceleration to derive angular velocity and displacement.
- Application of initial conditions (rest at $t=0$) to solve for constants of integration.

##### Intradisciplinary Connections
This problem connects to rotational kinematics, where constant angular acceleration parallels constant linear acceleration in translational motion. The derived equation $\theta = \frac{1}{2} \alpha t^2$ mirrors the linear displacement formula $s = \frac{1}{2} a t^2$, reinforcing the analogy between linear and rotational dynamics.

##### Interdisciplinary Connections
- **Engineering**: Flywheel energy storage systems are used in electric grids and electric vehicles to stabilize power supply and recover braking energy.
- **Environmental Science**: Efficient energy storage reduces reliance on fossil fuels by enabling better integration of intermittent renewable sources like wind and solar power.

##### Real-World Applications
Flywheel systems are deployed in:
1. **Data Centers**: Provide uninterrupted power during grid failures.
2. **Public Transportation**: Regenerative braking in trains and buses converts kinetic energy into rotational energy for reuse.
3. **Spacecraft**: Stabilize orientation and store energy in satellites.

##### Problem Statement
Starting from the fundamental definitions of angular acceleration and angular velocity, derive the angular displacement $\theta$ of the flywheel after time $t$. The flywheel starts from rest at $t=0$ and experiences a constant angular acceleration $\alpha$. Express your answer analytically in terms of $\alpha$ and $t$. Ensure all steps of the derivation are justified, and state any assumptions made.  
**Note**: Express trigonometric functions in radians (e.g., $\sin(1.2)$), and use $\exp(x)$ for exponential functions. Do not evaluate numerical constants; keep the expression symbolic.

## Solution
**Step 1: Relate angular acceleration to angular velocity**  
Angular acceleration $\alpha$ is defined as the rate of change of angular velocity $\omega$ with respect to time:  
$$\alpha = \frac{d\omega}{dt}.$$  
Since $\alpha$ is constant, integrate both sides with respect to time:  
$$\int d\omega = \int \alpha  dt.$$  
This yields:  
$$\omega = \alpha t + C,$$  
where $C$ is the constant of integration.

**Step 2: Apply initial condition for angular velocity**  
The flywheel starts from rest at $t=0$, so $\omega(0) = 0$. Substituting this initial condition:  
$$0 = \alpha \cdot 0 + C \implies C = 0.$$  
Thus, the angular velocity simplifies to:  
$$\omega = \alpha t.$$

**Step 3: Relate angular velocity to angular displacement**  
Angular velocity $\omega$ is defined as the rate of change of angular displacement $\theta$:  
$$\omega = \frac{d\theta}{dt}.$$  
Substitute $\omega = \alpha t$:  
$$\frac{d\theta}{dt} = \alpha t.$$  
Integrate both sides with respect to time:  
$$\int d\theta = \int \alpha t  dt.$$  
This gives:  
$$\theta = \alpha \cdot \frac{t^2}{2} + D,$$  
where $D$ is another constant of integration.

**Step 4: Apply initial condition for angular displacement**  
At $t=0$, the flywheel is at its initial position, so $\theta(0) = 0$. Substituting:  
$$0 = \alpha \cdot \frac{0^2}{2} + D \implies D = 0.$$  
Thus, the angular displacement is:  
$$\theta = \frac{1}{2} \alpha t^2.$$  

**Assumptions**:  
- The angular acceleration $\alpha$ is constant.  
- No frictional torque or external disturbances affect the motion.  
- The flywheel's moment of inertia remains unchanged during acceleration.

## Answer
$$\boxed{\dfrac{1}{2} \alpha t^{2}}$$

------
## Problem 1
##### Background
Flywheels are heavy rotating disks used to store kinetic energy in mechanical systems. They play critical roles in applications like energy grid stabilization, hybrid vehicle regenerative braking, and industrial machinery inertia control. When a flywheel decelerates due to friction or applied torque, its motion follows the same kinematic principles as linear motion but in rotational form.

##### Knowledge Points Tested
1. Application of rotational kinematics equations for constant angular acceleration.
2. Solving for time using initial angular velocity and angular acceleration.
3. Understanding the physical interpretation of angular deceleration.

##### Intradisciplinary Connections
- Rotational kinematics directly parallels linear kinematics (e.g., $\omega = \omega_0 + \alpha t$ is analogous to $v = u + at$).
- Connects to torque and moment of inertia via $\tau = I\alpha$, though this problem focuses purely on kinematics.

##### Interdisciplinary Connections
- **Mechanical Engineering**: Flywheel energy storage systems require precise deceleration control to manage power output.
- **Physics**: Demonstrates conservation principles—kinetic energy decreases linearly with angular velocity squared ($K = \frac{1}{2}I\omega^2$).

##### Real-World Applications
- **Regenerative Braking**: Electric trains use flywheel deceleration to convert kinetic energy back into electrical energy.
- **Manufacturing**: Flywheels in punch presses must stop within precise time windows to synchronize with production lines.

##### Problem Statement
A titanium alloy flywheel in a satellite stabilization system rotates at an initial angular velocity of $\omega_0$ rad/s. To reconfigure its orientation, engineers apply braking torque that causes a uniform angular deceleration of $\alpha$ rad/s². Derive an expression for the time required for the flywheel to come to a complete stop. Express your answer solely in terms of the given parameters $\omega_0$ and $\alpha$.

## Solution
We start with the rotational kinematics equation for angular velocity under constant angular acceleration:  
$$\omega = \omega_0 + \alpha t,$$  
where $\omega$ is the final angular velocity, $\omega_0$ is the initial angular velocity, $\alpha$ is the angular acceleration, and $t$ is time.  

Since the flywheel decelerates uniformly, $\alpha$ is negative. However, the problem states the deceleration magnitude as $\alpha$, so we use $-\alpha$ in the equation. When the flywheel stops, $\omega = 0$. Substituting these values:  
$$0 = \omega_0 + (-\alpha) t.$$  

Solving for $t$:  
$$0 = \omega_0 - \alpha t,$$  
$$\alpha t = \omega_0,$$  
$$t = \frac{\omega_0}{\alpha}.$$  

This result shows that the stopping time is directly proportional to the initial angular velocity and inversely proportional to the deceleration magnitude. The derivation relies solely on the definition of constant angular acceleration and requires no numerical substitution.

## Answer
$$\boxed{\dfrac{\omega_0}{\alpha}}$$

------
## Problem 2
##### Background
In automotive engineering, the motion of a wheel is a combination of translation and rotation. When a tire rolls without slipping, its center moves linearly while points on its rim follow cycloidal paths. This motion is governed by a fundamental constraint: the arc length unrolled on the road equals the distance traveled by the wheel's center. Anti-lock braking systems (ABS) rely on precise calculations of rotational and linear speeds to prevent skidding, demonstrating the real-world importance of these concepts.

##### Knowledge Points Tested
- Definition of angular velocity and its relationship to linear speed.
- Condition for rolling without slipping.
- Rigid body kinematics and the connection between translational and rotational motion.

##### Intradisciplinary Connections
This problem connects to circular motion kinematics, centripetal acceleration, and torque dynamics. It extends to systems with combined rotation and translation, such as gears and pulleys.

##### Interdisciplinary Connections
- **Mechanical Engineering**: Wheel design in vehicles and robotics.
- **Physics**: Conservation of energy in rotational systems.
- **Applied Mathematics**: Parametric equations describing cycloidal motion.

##### Real-World Applications
- Calculating optimal tire rotation rates for fuel efficiency.
- Designing traction control systems that adjust wheel spin during acceleration.
- Developing precision odometers that convert wheel rotations to distance measurements.

##### Problem Statement
A car travels in a straight line at a constant linear speed $v$. Its tires have radius $r$ and roll without slipping. Derive an expression for the angular velocity $\omega$ of the tires.  
**Express your answer analytically in terms of the given quantities $v$ and $r$.**  
*Follow these formatting rules:*  
- Use standard mathematical notation (e.g., $\frac{a}{b}$ for fractions).  
- Do **not** substitute numerical values for any parameters.  
- Express the final answer as a single simplified expression.

## Solution
The condition for rolling without slipping requires that the linear distance traveled by the wheel's center equals the arc length unrolled by a point on the rim. Consider a time interval $\Delta t$:  
- The linear distance traveled by the center is $\Delta s = v \Delta t$.  
- The corresponding arc length unrolled is $r \Delta \theta$, where $\Delta \theta$ is the angular displacement in radians.  

By the no-slip condition:  

$$
\Delta s = r \Delta \theta
$$
  
Substituting $\Delta s = v \Delta t$:  

$$
v \Delta t = r \Delta \theta
$$
  
Rearranging to isolate the angular displacement:  

$$
\Delta \theta = \frac{v \Delta t}{r}
$$
  
The average angular velocity over $\Delta t$ is $\bar{\omega} = \frac{\Delta \theta}{\Delta t}$. Substituting the expression for $\Delta \theta$:  

$$
\bar{\omega} = \frac{\frac{v \Delta t}{r}}{\Delta t} = \frac{v}{r}
$$
  
As $\Delta t \to 0$, the average angular velocity approaches the instantaneous angular velocity $\omega$:  

$$
\omega = \lim_{\Delta t \to 0} \bar{\omega} = \frac{v}{r}
$$
  
This result is consistent with the definition of rolling without slipping, where the linear speed at the rim (relative to the center) equals $r\omega$, and the bottom point's instantaneous velocity relative to the ground is zero. Thus, the angular velocity is directly proportional to the linear speed and inversely proportional to the radius.

## Answer
\[
\boxed{\dfrac{v}{r}}
\]

------
## Problem 3
##### Background
Centrifuges are essential devices in scientific laboratories and industrial processes, used to separate components of a mixture based on density differences through rapid rotation. The acceleration profile of a centrifuge is critical for efficiency and sample integrity. Consider a centrifuge rotor starting from complete rest and undergoing constant angular acceleration to reach a target operational angular velocity.

##### Knowledge Points Tested
- Kinematic equations for rotational motion under constant angular acceleration  
- Relationship between angular displacement, angular velocity, and angular acceleration  
- Conversion between angular displacement (radians) and number of revolutions  

##### Intradisciplinary Connections
This problem connects to linear kinematics (displacement, velocity, acceleration) and reinforces the analogy between linear and rotational motion. It also extends to moment of inertia and torque in dynamics when analyzing forces during acceleration.

##### Interdisciplinary Connections
Centrifuge operation principles apply to biology (cell separation), chemistry (precipitate isolation), and aerospace engineering (artificial gravity simulation). Mathematical modeling of acceleration profiles is crucial in control systems engineering for precision instrumentation.

##### Real-World Applications
- Medical laboratories: Separating blood components for diagnostics  
- Wastewater treatment: Removing solids from liquids  
- Space research: Simulating high-gravity environments for astronaut training  
- Materials science: Isolating nanoparticles in colloidal suspensions  

##### Problem Statement
A laboratory centrifuge starts from rest and accelerates uniformly with constant angular acceleration. It reaches a final angular velocity of $\omega$ radians per second after $t$ seconds of acceleration. Derive an expression for the total number of revolutions, $N$, completed by the centrifuge rotor during this acceleration phase. Express $N$ exclusively in terms of the given parameters $\omega$ and $t$.  

**Important Instructions for Final Answer Format:**  
- Your answer must be a single analytic expression.  
- Use only the symbols $\omega$ (angular velocity) and $t$ (time).  
- Express fractions using two-field LaTeX notation (e.g., `\frac{a}{b}`).  
- Do **not** include units, numerical constants, or unevaluated expressions.  
- One revolution equals $2\pi$ radians.

## Solution
**Step 1: Identify known quantities**  
- Initial angular velocity, $\omega_0 = 0$ (starts from rest)  
- Final angular velocity, $\omega$  
- Time interval, $t$  
- Constant angular acceleration, $\alpha$ (implicit; will be eliminated)  

**Step 2: Apply rotational kinematics equations**  
The angular displacement $\theta$ under constant acceleration is:  
$$\theta = \omega_0 t + \frac{1}{2} \alpha t^2$$  
Substitute $\omega_0 = 0$:  
$$\theta = \frac{1}{2} \alpha t^2 \quad (1)$$  

The relationship between angular velocity and acceleration is:  
$$\omega = \omega_0 + \alpha t$$  
Substitute $\omega_0 = 0$:  
$$\omega = \alpha t \quad \Rightarrow \quad \alpha = \frac{\omega}{t} \quad (2)$$  

**Step 3: Eliminate $\alpha$ using Equation (2)**  
Substitute $\alpha = \frac{\omega}{t}$ from Equation (2) into Equation (1):  
$$\theta = \frac{1}{2} \left( \frac{\omega}{t} \right) t^2$$  
Simplify:  
$$\theta = \frac{1}{2} \omega t$$  

**Step 4: Convert angular displacement to revolutions**  
Since one revolution equals $2\pi$ radians:  
$$N = \frac{\theta}{2\pi}$$  
Substitute $\theta = \frac{1}{2} \omega t$:  
$$N = \frac{\frac{1}{2} \omega t}{2\pi} = \frac{\omega t}{4\pi}$$  

**Conclusion**  
The total number of revolutions completed during acceleration is $\frac{\omega t}{4\pi}$.

## Answer
$$\boxed{\dfrac{\omega t}{4\pi}}$$

------
## Problem 4
##### Background
Rotational motion is a fundamental concept in physics, describing how objects spin around an axis. Angular quantities like displacement, velocity, and acceleration govern this motion, analogous to their linear counterparts but adapted for circular paths. Real-world systems such as amusement park rides, rotating machinery, and celestial bodies exhibit these principles. This problem explores a merry-go-round undergoing constant angular deceleration—a scenario where friction or braking torque reduces rotational speed uniformly.

##### Knowledge Points Tested
- Kinematic equations for rotational motion with constant angular acceleration  
- Conversion between angular displacement units (revolutions to radians)  
- Algebraic manipulation of rotational parameters ($\theta$, $\omega$, $\alpha$)  
- Interpretation of deceleration in rotational systems  

##### Intradisciplinary Connections
- Relates to linear kinematics ($v^2 = u^2 + 2as$ vs. $\omega_f^2 = \omega_i^2 + 2\alpha\theta$)  
- Extends to torque ($\tau = I\alpha$) and moment of inertia in dynamics  
- Connects to centripetal acceleration in circular motion  

##### Interdisciplinary Connections
- **Engineering:** Calculating braking torque in rotating machinery  
- **Astronomy:** Modeling spin-down of pulsars or planetary rotation  
- **Robotics:** Controlling angular velocity in robotic joints  

##### Real-World Applications
- Designing braking systems for carousels or industrial turntables  
- Analyzing flywheel energy storage deceleration  
- Regulating spin rates in centrifuges or washing machines  

##### Problem Statement  
A merry-go-round decelerates uniformly from an initial angular velocity $\omega_i$ to a final angular velocity $\omega_f$ (both in rad/s) while completing exactly $N$ full revolutions. Derive an expression for its angular acceleration $\alpha$ in terms of $\omega_i$, $\omega_f$, $N$, and fundamental constants. Assume constant angular acceleration.  

**Formatting Instructions:**  
- Express $\alpha$ as a simplified analytic expression using $\omega_i$, $\omega_f$, $N$, and $\pi$.  
- Use radians for all angular measures.  
- Do **not** substitute numerical values.

## Solution
**Step 1: Convert revolutions to radians**  
The merry-go-round completes $N$ revolutions. Since 1 revolution = $2\pi$ radians, the total angular displacement $\theta$ is:  
$$ \theta = 2\pi N \ \text{rad} $$  

**Step 2: Apply rotational kinematics**  
For constant angular acceleration, the relationship between initial angular velocity ($\omega_i$), final angular velocity ($\omega_f$), angular acceleration ($\alpha$), and angular displacement ($\theta$) is:  
$$ \omega_f^2 = \omega_i^2 + 2\alpha\theta $$  
This equation mirrors the linear kinematics formula $v^2 = u^2 + 2as$, adapted for rotational motion.  

**Step 3: Solve for angular acceleration**  
Substitute $\theta = 2\pi N$ into the kinematic equation:  
$$ \omega_f^2 = \omega_i^2 + 2\alpha(2\pi N) $$  
Simplify the expression:  
$$ \omega_f^2 = \omega_i^2 + 4\pi N\alpha $$  
Isolate $\alpha$ by rearranging terms:  
$$ 4\pi N\alpha = \omega_f^2 - \omega_i^2 $$  
$$ \alpha = \frac{\omega_f^2 - \omega_i^2}{4\pi N} $$  

**Step 4: Interpret the sign**  
Since the merry-go-round is decelerating ($\omega_f < \omega_i$), $\omega_f^2 - \omega_i^2 < 0$. Thus, $\alpha$ is negative, consistent with deceleration. The expression inherently captures this directional property.  

**Conclusion**  
The derived expression for angular acceleration is $\alpha = \dfrac{\omega_f^2 - \omega_i^2}{4\pi N}$.

## Answer
$$\boxed{\dfrac{\omega_f^{2} - \omega_i^{2}}{4\pi N}}$$

------
## Problem 5
##### Background
Centripetal acceleration is a crucial concept in circular motion, describing the acceleration directed toward the center of a circular path that keeps an object moving in a circle. This acceleration arises in diverse real-world contexts, such as planetary orbits, centrifuges, and roller coaster design. Understanding how to derive it from fundamental principles reinforces the connection between linear and angular kinematics.

##### Knowledge Points Tested
1. Definition of angular velocity ($\omega$) and its relationship to linear velocity ($v$).
2. Vector differentiation for acceleration in circular motion.
3. Magnitude calculation of acceleration vectors.
4. Centripetal acceleration as a function of angular quantities.

##### Intradisciplinary Connections
- **Kinematics**: Relates angular displacement, velocity, and acceleration.
- **Dynamics**: Connects centripetal acceleration to centripetal force via Newton's second law ($F_c = m a_c$).
- **Coordinate Systems**: Uses parametric equations in polar coordinates.

##### Interdisciplinary Connections
- **Engineering**: Critical for designing rotating machinery (e.g., turbines, wheels) to avoid structural failure.
- **Astrophysics**: Models orbital motion of celestial bodies under gravitational centripetal acceleration.
- **Transportation**: Informs safe speed limits for vehicles on curved roads or racetracks.

##### Real-World Applications
1. **Artificial Gravity in Space Stations**: Rotating habitats generate "gravity" via centripetal acceleration ($a_c = \omega^2 R$), where $R$ is the station radius.
2. **Centrifuges in Laboratories**: Separate substances by density; acceleration magnitude depends on $\omega$ and rotor radius $R$.
3. **AMUSEMENT PARK RIDES**: Loops in roller coasters require precise $a_c$ calculations for rider safety.

##### Problem Statement
Consider a particle moving uniformly in a circle of radius $R$ with constant angular velocity $\omega$. The position vector of the particle at time $t$ is given by:  
$$ \vec{r}(t) = R \cos(\omega t)  \hat{\imath} + R \sin(\omega t)  \hat{\jmath}, $$  
where $\omega$ is in radians per second. Starting from this position vector, derive the magnitude of the centripetal acceleration $a_c$. Express $a_c$ symbolically in terms of $\omega$ and $R$ only.  

**Instructions**:  
1. Compute the velocity vector $\vec{v}(t)$ by differentiating $\vec{r}(t)$ with respect to time.  
2. Compute the acceleration vector $\vec{a}(t)$ by differentiating $\vec{v}(t)$ with respect to time.  
3. Find the magnitude of $\vec{a}(t)$.  
4. Simplify to show $a_c = \omega^2 R$.

## Solution
**Step 1: Velocity vector via differentiation**  
The position vector is:  
$$ \vec{r}(t) = R \cos(\omega t)  \hat{\imath} + R \sin(\omega t)  \hat{\jmath}. $$  
Differentiate $\vec{r}(t)$ with respect to time $t$:  
$$ \vec{v}(t) = \frac{d\vec{r}}{dt} = R \left[ -\omega \sin(\omega t)  \hat{\imath} + \omega \cos(\omega t)  \hat{\jmath} \right] = -R \omega \sin(\omega t)  \hat{\imath} + R \omega \cos(\omega t)  \hat{\jmath}. $$  

**Step 2: Acceleration vector via differentiation**  
Differentiate $\vec{v}(t)$ with respect to time $t$:  
$$ \vec{a}(t) = \frac{d\vec{v}}{dt} = -R \omega \left[ \omega \cos(\omega t)  \hat{\imath} + \omega \sin(\omega t)  \hat{\jmath} \right] = -R \omega^2 \cos(\omega t)  \hat{\imath} - R \omega^2 \sin(\omega t)  \hat{\jmath}. $$  
Factor out $-\omega^2$:  
$$ \vec{a}(t) = -\omega^2 \left[ R \cos(\omega t)  \hat{\imath} + R \sin(\omega t)  \hat{\jmath} \right] = -\omega^2 \vec{r}(t). $$  

**Step 3: Magnitude of acceleration**  
The magnitude of $\vec{a}(t)$ is:  
$$ \left| \vec{a}(t) \right| = \left| -\omega^2 \vec{r}(t) \right| = \omega^2 \left| \vec{r}(t) \right|. $$  
The magnitude of the position vector $\vec{r}(t)$ is the radius $R$:  
$$ \left| \vec{r}(t) \right| = \sqrt{ \left[ R \cos(\omega t) \right]^2 + \left[ R \sin(\omega t) \right]^2 } = \sqrt{ R^2 (\cos^2(\omega t) + \sin^2(\omega t)) } = \sqrt{R^2} = R. $$  
Thus,  
$$ \left| \vec{a}(t) \right| = \omega^2 R. $$  

**Step 4: Final expression**  
The magnitude of the centripetal acceleration is $a_c = \omega^2 R$.

## Answer
$$\boxed{\omega^{2} R}$$

------
# angular frequency and phase relationships

## Problem 0
#### Background
A mass-spring system is a fundamental model in physics that exhibits simple harmonic motion. It consists of a mass attached to a spring, oscillating about an equilibrium position due to Hooke's law restoring force. Such systems appear in engineering (e.g., vehicle suspensions), seismology (earthquake modeling), and molecular physics (vibrational modes). The motion is characterized by amplitude (maximum displacement) and angular frequency, with energy continuously transforming between kinetic and potential forms.

#### Knowledge Points Tested
- Relationship between position, velocity, and acceleration in simple harmonic motion.
- Conservation of mechanical energy in oscillatory systems.
- Expressions for kinetic and potential energy in a mass-spring system.
- Identification of extremal points in periodic motion.

#### Intradisciplinary Connections
This problem connects to wave mechanics (energy-density analogs), damped/driven oscillations (energy dissipation), and Lagrangian mechanics (energy-based formulations).

#### Interdisciplinary Connections
- **Electrical Engineering**: LC circuits exhibit identical energy oscillations between magnetic (kinetic analog) and electric (potential analog) forms.
- **Biology**: Resonant energy transfer in molecular vibrations during photosynthesis.
- **Geophysics**: Energy propagation in seismic waves through elastic media.

#### Real-World Applications
- **Tuned Mass Dampers**: Skyscrapers use oscillating masses to dissipate kinetic energy from earthquakes/wind.
- **Atomic Force Microscopy**: Measures surface interactions via spring-system energy shifts.
- **Biomechanics**: Analysis of tendon elasticity during running.

#### Problem Statement
A mass $m$ attached to a spring oscillates with amplitude $A$ and angular frequency $\omega$. The position $x(t)$ is given by $x(t) = A \cos(\omega t + \phi)$, where $\phi$ is an arbitrary phase constant. Derive an expression for the maximum kinetic energy $K_{\text{max}}$ of the mass during its motion. Express your answer symbolically in terms of $m$, $A$, and $\omega$. Use standard mathematical notation and ensure trigonometric functions are written in unevaluated form (e.g., $\sin(\theta)$). Do **not** substitute numerical values for any constants.

## Solution
The kinetic energy $K$ of the mass is given by:  
$$ K = \frac{1}{2} m v^2 $$  
where $v$ is the velocity. Velocity is the time derivative of position $x(t) = A \cos(\omega t + \phi)$:  
$$ v = \frac{dx}{dt} = -A \omega \sin(\omega t + \phi) $$  
Substitute $v$ into the kinetic energy expression:  
$$ K = \frac{1}{2} m \left[ -A \omega \sin(\omega t + \phi) \right]^2 = \frac{1}{2} m A^2 \omega^2 \sin^2(\omega t + \phi) $$  
Kinetic energy is maximized when $\sin^2(\omega t + \phi)$ is maximized. Since $\sin^2(\theta)$ has a maximum value of 1 for any real $\theta$:  
$$ \max \left[ \sin^2(\omega t + \phi) \right] = 1 $$  
Thus, the maximum kinetic energy is:  
$$ K_{\text{max}} = \frac{1}{2} m A^2 \omega^2 \cdot 1 = \frac{1}{2} m A^2 \omega^2 $$  
This result aligns with energy conservation: At maximum displacement ($x = \pm A$), potential energy is maximized at $\frac{1}{2} k A^2$ (where $k = m \omega^2$ is the spring constant) and kinetic energy is zero. At equilibrium ($x = 0$), all energy is kinetic, giving $K_{\text{max}} = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2$.

## Answer
$$\boxed{\dfrac{1}{2} m A^{2} \omega^{2}}$$

------
## Problem 1
##### Background
A simple pendulum consists of a point mass (called the bob) suspended from a fixed point by a string of length $L$. When displaced by a small angle $\theta$ from its equilibrium position and released, it undergoes simple harmonic motion. The angular frequency $\omega$ characterizes how rapidly the pendulum oscillates and depends on the pendulum's length and the acceleration due to gravity $g$. Pendulums are used in timekeeping devices like grandfather clocks, where their periods must be precisely controlled by adjusting their lengths.

##### Knowledge Points Tested
1. Derivation of the angular frequency for a simple pendulum using Newton's second law and small-angle approximation.
2. Relationship between pendulum length and angular frequency.
3. Calculation of ratios based on physical dependencies.

##### Intradisciplinary Connections
- Connects to harmonic motion in mechanics: The restoring force analysis parallels spring-mass systems, where $\omega = \sqrt{k/m}$.
- Relates to wave physics: Angular frequency links to periodic motion concepts like period $T = 2\pi / \omega$.

##### Interdisciplinary Connections
- **Engineering**: Pendulum length adjustments in seismometers measure ground motion during earthquakes by exploiting frequency relationships.
- **Geophysics**: Variations in $g$ (due to altitude/latitude) affect pendulum frequency, enabling gravimetric surveys.

##### Real-World Applications
- **Horology**: Pendulum clocks regulate time via length-dependent periods; a 1 m pendulum has a ~2 s period for small swings.
- **Structural Engineering**: Pendulum analogs model sway in tall buildings under wind loads, with natural frequencies dictating stability.

##### Problem Statement
Two simple pendulums, Pendulum A (length $L$) and Pendulum B (length $4L$), are released simultaneously from small, identical initial displacements. Both bobs have negligible size and identical mass $m$, and air resistance is ignored. Using Newton's laws and the small-angle approximation:  
1. Derive the angular frequency $\omega_A$ for Pendulum A and $\omega_B$ for Pendulum B.  
2. Find the ratio $\omega_A / \omega_B$.  
Express the ratio as a simplified integer or fraction.

## Solution
**Step 1: Equation of motion for a simple pendulum**  
Consider a pendulum of length $L$ with bob mass $m$. At a displacement angle $\theta$, the tangential component of gravity provides the restoring force:  

$$ F_{\text{tangential}} = -mg \sin\theta $$
  
For small $\theta$ (in radians), $\sin\theta \approx \theta$, so:  

$$ F_{\text{tangential}} \approx -mg\theta $$
  
Applying Newton's second law in the tangential direction:  

$$ m \frac{d^2 s}{dt^2} = -mg\theta $$
  
where $s = L\theta$ is the arc length displacement. Thus:  

$$ \frac{d^2 (L\theta)}{dt^2} = -g\theta $$
  

$$ L \frac{d^2\theta}{dt^2} = -g\theta $$
  

$$ \frac{d^2\theta}{dt^2} = -\frac{g}{L} \theta $$
  

**Step 2: Identify angular frequency**  
The equation $\frac{d^2\theta}{dt^2} = -\omega^2 \theta$ defines simple harmonic motion. Comparing:  

$$ \omega^2 = \frac{g}{L} $$
  

$$ \omega = \sqrt{\frac{g}{L}} $$
  

**Step 3: Apply to both pendulums**  
- For Pendulum A (length $L$):  
  
$$ \omega_A = \sqrt{\frac{g}{L}} $$
  
- For Pendulum B (length $4L$):  
  
$$ \omega_B = \sqrt{\frac{g}{4L}} = \frac{1}{2} \sqrt{\frac{g}{L}} $$
  

**Step 4: Compute the ratio**  

$$ \frac{\omega_A}{\omega_B} = \frac{\sqrt{\frac{g}{L}}}{\frac{1}{2} \sqrt{\frac{g}{L}}} = \frac{1}{\frac{1}{2}} = 2 $$
  
The ratio is independent of $g$, $m$, and initial displacement (for small angles).

## Answer
$$\boxed{2}$$

------
## Problem 2
##### Background
In the study of wave mechanics, waves are often described mathematically to understand their properties. A common form is the sinusoidal wave, represented as $y(t) = A \sin(\omega t + \phi)$, where $A$ is the amplitude (in meters), $\omega$ is the angular frequency (in rad/s), and $\phi$ is the phase constant (in radians). Here, $y(t)$ denotes the displacement at a fixed point as a function of time $t$. 

##### Knowledge Points Tested
1. **Trigonometric Identity Application**: Using harmonic addition to combine sine and cosine terms into a single sine function.
2. **Wave Parameter Identification**: Extracting angular frequency and phase constant from a wave equation.
3. **Algebraic Manipulation**: Solving systems of equations derived from coefficient comparisons.

##### Intradisciplinary Connections
This problem connects to the broader topic of **oscillatory motion**, where sinusoidal functions model periodic phenomena. It also reinforces **trigonometric identities** from algebra and **wave mechanics** in physics, such as wavelength, frequency, and phase velocity.

##### Interdisciplinary Connections
- **Electrical Engineering**: Similar methods analyze alternating current (AC) circuits, where voltages/currents are sinusoidal.
- **Signal Processing**: Wave decomposition and reconstruction are fundamental in audio and image processing.
- **Astronomy**: Modeling periodic celestial events (e.g., pulsar signals) uses phase and frequency analysis.

##### Real-World Applications
- **Noise-Canceling Headphones**: By analyzing phase constants, engineers design waves that destructively interfere with ambient noise.
- **Seismology**: Identifying wave frequencies helps characterize earthquake tremors.
- **Musical Instrument Tuning**: Matching frequencies and phases ensures harmonic resonance in instruments.

##### Problem Statement
A wave on a string is measured at a fixed point. Its displacement $y(t)$ (in meters) is given by:  
$$ y(t) = \frac{\sqrt{2}}{20} \sin(3\pi t) + \frac{\sqrt{2}}{20} \cos(3\pi t). $$  
Express this wave in the form $y(t) = A \sin(3\pi t + \phi)$, and then determine its angular frequency $\omega$ and phase constant $\phi$.  
- **Answer Requirements**:  
  - $\omega$ must be in radians per second (rad/s).  
  - $\phi$ must be in radians (rad).  
  - Use exact expressions only; no numerical approximations.  
  - For trigonometric functions, use radians and write, e.g., $\sin\left(\frac{\pi}{4}\right)$ instead of evaluating.  
  - Use the notation $\arcsin$, $\arccos$, $\arctan$ for inverse trigonometric functions (do not use $\sin^{-1}$, $\cos^{-1}$, etc.).

## Solution
To express $y(t) = \frac{\sqrt{2}}{20} \sin(3\pi t) + \frac{\sqrt{2}}{20} \cos(3\pi t)$ in the form $y(t) = A \sin(3\pi t + \phi)$, we use the harmonic addition theorem:  

$$ a \sin \theta + b \cos \theta = R \sin(\theta + \phi), $$
  
where $R = \sqrt{a^2 + b^2}$ and $\tan \phi = \frac{b}{a}$. Here, $\theta = 3\pi t$, $a = \frac{\sqrt{2}}{20}$, and $b = \frac{\sqrt{2}}{20}$.  

**Step 1: Compute the amplitude $A$**  
The amplitude $A$ is given by:  

$$ A = \sqrt{a^2 + b^2} = \sqrt{ \left( \frac{\sqrt{2}}{20} \right)^2 + \left( \frac{\sqrt{2}}{20} \right)^2 } = \sqrt{ \frac{2}{400} + \frac{2}{400} } = \sqrt{ \frac{4}{400} } = \sqrt{ \frac{1}{100} } = \frac{1}{10}. $$
  
Thus, $A = 0.1$ m.  

**Step 2: Compute the phase constant $\phi$**  
The phase constant satisfies:  

$$ \tan \phi = \frac{b}{a} = \frac{\frac{\sqrt{2}}{20}}{\frac{\sqrt{2}}{20}} = 1. $$
  
Since both $a > 0$ and $b > 0$, $\phi$ is in the first quadrant:  

$$ \phi = \arctan(1) = \frac{\pi}{4}. $$
  

**Step 3: Verify the expression**  
The wave is now:  

$$ y(t) = 0.1 \sin\left(3\pi t + \frac{\pi}{4}\right). $$
  
This matches the required form.  

**Step 4: Identify angular frequency and phase constant**  
From $y(t) = 0.1 \sin(3\pi t + \pi/4)$:  
- The angular frequency $\omega$ is the coefficient of $t$ in the argument, so $\omega = 3\pi$ rad/s.  
- The phase constant is $\phi = \pi/4$ rad.  

**Conclusion**:  
The angular frequency is $3\pi$ rad/s, and the phase constant is $\pi/4$ rad.

## Answer
$$\boxed{3\pi}$$  
$$\boxed{\frac{\pi}{4}}$$

------
## Problem 3
##### Background
In mechanical systems, springs are often combined to achieve desired stiffness. For instance, vehicle suspensions and exercise equipment use series or parallel spring arrangements to control the restoring force. When springs are connected in series, the effective spring constant decreases, leading to a lower oscillation frequency for the same mass. This problem explores the dynamics of a mass-spring system with two identical springs in series—a configuration that requires deriving the effective spring constant from fundamental principles.

##### Knowledge Points Tested
1. **Hooke's Law**: Relates spring force to displacement.
2. **Series Spring Combinations**: Derivation of the effective spring constant.
3. **Simple Harmonic Motion**: Newton's second law applied to oscillatory systems.
4. **Angular Frequency**: Relationship between spring constant, mass, and oscillation frequency.

##### Intradisciplinary Connections
- **Mechanics**: Force analysis and equilibrium in spring systems.
- **Dynamics**: Equation of motion for oscillatory systems and its solution.
- **Energy Methods**: Potential energy storage in series springs (though not used here, it provides an alternative solution path).

##### Interdisciplinary Connections
- **Engineering**: Design of suspension systems with specific frequency responses.
- **Materials Science**: Effective stiffness of composite materials with serial elastic elements.
- **Biomechanics**: Modeling tendon and ligament systems as series springs.

##### Real-World Applications
- **Vehicle Suspensions**: Series springs absorb road shocks by reducing effective stiffness, improving ride comfort.
- **Elevator Safety Systems**: Shock-absorbing mechanisms use series springs to decelerate falling cabins smoothly.
- **Trampolines**: Multiple springs in series attach the mat to the frame, affecting bounce frequency.

##### Problem Statement
Two identical massless springs, each with spring constant $k$, are connected in series and suspended vertically from a rigid ceiling. A mass $m$ is attached to the free end of the lower spring. The mass is displaced vertically by a small distance and released, initiating simple harmonic motion.  
Derive the angular frequency of oscillation for the mass. Express your answer as an analytic expression in terms of $k$ and $m$.

## Solution
### Step 1: Model the Series Spring System
- Let the displacement of the mass from equilibrium be $y$ (downward positive).  
- The upper spring experiences force $F$ and stretches by $x_1$. By Hooke's law:  
  $$ F = kx_1 \implies x_1 = \frac{F}{k} $$  
- The lower spring experiences the same force $F$ (since springs are massless) and stretches by $x_2$:  
  $$ F = kx_2 \implies x_2 = \frac{F}{k} $$  
- The total displacement $y$ is the sum of individual stretches:  
  $$ y = x_1 + x_2 = \frac{F}{k} + \frac{F}{k} = \frac{2F}{k} $$  

### Step 2: Derive the Effective Spring Constant
- Solve for $F$ in terms of $y$:  
  $$ F = \frac{k}{2} y $$  
- This matches Hooke's law for an equivalent spring: $F = k_{\text{eff}} y$. Thus,  
  $$ k_{\text{eff}} = \frac{k}{2} $$  

### Step 3: Apply Newton's Second Law
- The net force on mass $m$ is the restoring force:  
  $$ F_{\text{net}} = -k_{\text{eff}} y = -\frac{k}{2} y $$  
- Using Newton's second law:  
  $$ m \frac{d^2 y}{dt^2} = -\frac{k}{2} y $$  
- Rearrange to the standard harmonic motion form:  
  $$ \frac{d^2 y}{dt^2} + \frac{k}{2m} y = 0 $$  

### Step 4: Identify the Angular Frequency
- The general equation for simple harmonic motion is:  
  $$ \frac{d^2 y}{dt^2} + \omega^2 y = 0 $$  
- Comparing coefficients:  
  $$ \omega^2 = \frac{k}{2m} $$  
- Solve for the angular frequency $\omega$:  
  $$ \omega = \sqrt{\frac{k}{2m}} $$  

### Conclusion
The derived expression $\omega = \sqrt{\frac{k}{2m}}$ describes the angular frequency of oscillation for mass $m$ attached to two identical springs in series, each with spring constant $k$.

## Answer
$$\boxed{\sqrt{\frac{k}{2m}}}$$

------
# Atwood machine and pulley systems

## Problem 0
##### Background
In modern elevator systems, a counterweight is used to reduce the energy required to lift the cab. Consider an elevator cab of mass $m_1$ and a counterweight of mass $m_2$ ($m_1 > m_2$) connected by a high-strength cable passing over a grooved drive pulley. The pulley, which has mass $M$ and radius $R$, acts as a flywheel to smooth motion. The pulley's moment of inertia is $I = \frac{1}{2} M R^2$ (modeled as a uniform disk), and its axle is frictionless. The cable is massless and does not slip on the pulley. When the system is released from rest, the masses accelerate due to gravity.

##### Knowledge Points Tested
- Newton's second law for linear motion
- Newton's second law for rotational motion ($\tau = I \alpha$)
- Kinematic constraint between linear and angular acceleration ($a = R\alpha$)
- Moment of inertia for continuous mass distributions

##### Intradisciplinary Connections
This problem integrates translational dynamics (masses) with rotational dynamics (pulley), demonstrating how constraints and torques govern coupled motion. It extends the basic Atwood machine by incorporating rotational inertia.

##### Interdisciplinary Connections
The physics of pulley systems is essential in mechanical engineering (e.g., crane design) and biomechanics (e.g., tendon-pulley models in joints). The moment of inertia concept is crucial in aerospace engineering for attitude control systems.

##### Real-World Applications
- Elevators and escalators use counterweighted pulleys to minimize motor load.
- Rock-climbing belay devices employ pulley systems with inertial effects for controlled descent.
- Industrial conveyor belts utilize flywheel pulleys to maintain constant tension.

##### Problem Statement
Derive the magnitude of acceleration $a$ of the elevator cab and counterweight. Express $a$ analytically in terms of $m_1$, $m_2$, $M$, $g$ (acceleration due to gravity), and necessary mathematical constants. The radius $R$ must cancel out in your final expression.  

**Answer Format Requirements:**  
- Use only the symbols $m_1$, $m_2$, $M$, and $g$.  
- Express fractions with \frac{numerator}{denominator} (e.g., \frac{1}{2}).  
- Do not substitute numerical values for constants.  
- Exclude units in the final answer.

## Solution
**Step 1: Define forces and motion**  
Let $a$ be the magnitude of acceleration (same for both masses due to inextensible cable). Assume $m_1$ accelerates downward and $m_2$ upward. Define tensions:  
- $T_1$: tension in cable segment connected to $m_1$  
- $T_2$: tension in cable segment connected to $m_2$ ($T_1 \neq T_2$ due to pulley inertia).  

**Step 2: Apply Newton's second law to masses**  
For $m_1$ (downward motion):  
$$ m_1 g - T_1 = m_1 a \quad \text{(Equation 1)} $$  

For $m_2$ (upward motion):  
$$ T_2 - m_2 g = m_2 a \quad \text{(Equation 2)} $$  

**Step 3: Apply Newton's second law to pulley**  
The pulley experiences torques from $T_1$ and $T_2$. Net torque $\tau_{\text{net}} = (T_1 - T_2)R$ (since $T_1 > T_2$). Rotational inertia $I = \frac{1}{2} M R^2$. Angular acceleration $\alpha$ relates to linear acceleration by $a = R \alpha$ (no slip), so $\alpha = \frac{a}{R}$.  
$$ \tau_{\text{net}} = I \alpha \implies (T_1 - T_2)R = \left( \frac{1}{2} M R^2 \right) \left( \frac{a}{R} \right) $$  
Simplify:  
$$ T_1 - T_2 = \frac{1}{2} M a \quad \text{(Equation 3)} $$  

**Step 4: Solve the system of equations**  
Add Equations 1 and 2:  
$$ (m_1 g - T_1) + (T_2 - m_2 g) = m_1 a + m_2 a $$  
$$ (m_1 - m_2)g - (T_1 - T_2) = (m_1 + m_2)a $$  
Substitute $T_1 - T_2$ from Equation 3:  
$$ (m_1 - m_2)g - \frac{1}{2} M a = (m_1 + m_2)a $$  
Rearrange to isolate terms with $a$:  
$$ (m_1 - m_2)g = (m_1 + m_2)a + \frac{1}{2} M a $$  
$$ (m_1 - m_2)g = a \left( m_1 + m_2 + \frac{1}{2} M \right) $$  
Solve for $a$:  
$$ a = \frac{(m_1 - m_2)g}{m_1 + m_2 + \frac{1}{2} M} $$  
The radius $R$ cancels out as required.

## Answer
$$\boxed{\dfrac{(m_1 - m_2)g}{m_1 + m_2 + \dfrac{1}{2}M}}$$

------
# ballistic pendulum analysis

## Problem 0
##### Background
In forensic science and ballistic testing, the ballistic pendulum is a device used to measure the velocity of projectiles. It consists of a large block of material suspended from rigid rods. When a projectile strikes and embeds into the block, the system swings upward. By measuring the maximum height reached, the projectile's initial velocity can be determined using fundamental principles of mechanics.

##### Knowledge Points Tested
1. Conservation of linear momentum during inelastic collisions.
2. Conservation of mechanical energy in gravitational fields.
3. Algebraic manipulation to derive expressions from physical laws.

##### Intradisciplinary Connections
This problem connects to momentum transfer in collisions, energy conversion between kinetic and potential forms, and the application of Newtonian mechanics to oscillatory systems.

##### Interdisciplinary Connections
The ballistic pendulum links physics to forensic science (crime-scene bullet analysis) and materials engineering (testing impact resistance of substances). The mathematical derivation involves solving systems of equations, relevant to algebra and calculus.

##### Real-World Applications
Forensic experts use similar setups to estimate bullet velocities in criminal investigations. Safety engineers apply these principles to design protective barriers that absorb projectile impacts by converting kinetic energy into potential energy.

##### Problem Statement
A bullet of mass $m$ is fired horizontally into a stationary wooden block of mass $M$ suspended as a pendulum. The bullet embeds itself in the block, and the combined system swings upward, reaching a maximum height $h$ above its initial position. Derive an expression for the initial velocity $v$ of the bullet. Express your answer in terms of $m$, $M$, $h$, and the acceleration due to gravity $g$.  

**Answer Format Requirements:**  
- Provide a single closed-form analytic expression.  
- Use $\frac{numerator}{denominator}$ for fractions and $\sqrt{expression}$ for square roots.  
- Do not substitute numerical values for any constants.  
- Do not include units in the final expression.

## Solution
**Step 1: Apply Conservation of Momentum**  
The collision between the bullet and block is perfectly inelastic since the bullet embeds itself. Let $u$ be the velocity of the combined system immediately after the collision. Conservation of linear momentum in the horizontal direction gives:  

$$
m v + M \cdot 0 = (m + M) u
$$
  
Solving for $u$:  

$$
u = \frac{m v}{m + M}
$$


**Step 2: Apply Conservation of Mechanical Energy**  
After the collision, the system swings upward. At the maximum height $h$, all kinetic energy is converted to gravitational potential energy. Using conservation of mechanical energy:  

$$
\frac{1}{2} (m + M) u^2 = (m + M) g h
$$
  
Divide both sides by $(m + M)$:  

$$
\frac{1}{2} u^2 = g h
$$
  
Solving for $u^2$:  

$$
u^2 = 2 g h
$$


**Step 3: Substitute and Solve for $v$**  
Substitute the expression for $u$ from Step 1 into the equation from Step 2:  

$$
\left( \frac{m v}{m + M} \right)^2 = 2 g h
$$
  
Take the square root of both sides (considering only the positive root since velocity is non-negative):  

$$
\frac{m v}{m + M} = \sqrt{2 g h}
$$
  
Solve for $v$:  

$$
v = \frac{m + M}{m} \sqrt{2 g h}
$$
  
The expression for the initial velocity of the bullet is $\frac{m + M}{m} \sqrt{2 g h}$.

## Answer
$$\boxed{\frac{m + M}{m} \sqrt{2 g h}}$$

------
## Problem 1
##### Background
A ballistic pendulum is a device used to measure the speed of high-velocity projectiles, such as bullets. It consists of a pendulum with a mass $ M $ suspended by a string of length $ L $. When a bullet of mass $ m $ is fired horizontally into the mass $ M $, it embeds itself, and the pendulum swings to a maximum angle $ \theta $ with the vertical. This setup allows the initial bullet speed to be determined using conservation laws, without relying on high-speed timing equipment.

##### Knowledge Points Tested
1. Conservation of linear momentum in inelastic collisions.
2. Conservation of mechanical energy during pendulum motion.
3. Trigonometric relationships for pendulum displacement.
4. Algebraic manipulation to derive expressions from physical principles.

##### Intradisciplinary Connections
- Connects to momentum conservation in collisions (mechanics).
- Relates to energy transformations in oscillatory systems (harmonic motion).
- Illustrates how constraints (string length) define system geometry.

##### Interdisciplinary Connections
- Forensic science: Used historically to measure bullet speeds in crime labs.
- Materials engineering: Models impact absorption in composite materials.
- Biomechanics: Analogous to calculating projectile speeds in biological systems (e.g., predator strikes).

##### Real-World Applications
- Forensic ballistics: Determining muzzle velocity from impact data.
- Automotive safety testing: Measuring collision energy in crash-test dummies.
- Space debris analysis: Estimating impact speeds on spacecraft shielding.

##### Problem Statement
A bullet of mass $ m $ is fired horizontally at an unknown speed $ v $ into a stationary pendulum mass $ M $, which is suspended by a string of length $ L $. The bullet embeds itself in $ M $, and the combined mass $ (m + M) $ swings to a maximum angle $ \theta $ with the vertical. Derive an expression for the initial bullet speed $ v $ in terms of $ m $, $ M $, $ L $, $ \theta $, and the acceleration due to gravity $ g $.  
**Express your final answer as a single analytic expression.**  
**Note:** All physical quantities must remain symbolic. Use exact fractions, square roots, and trigonometric functions without decimal approximations. Follow the notation rules below:  
- Use $ \cos $ for cosine.  
- Write fractions with \frac{numerator}{denominator}.  
- Use \sqrt{expression} for square roots.  
- Omit units in the final answer.

## Solution
### Step 1: Apply conservation of momentum during collision
The collision is perfectly inelastic since the bullet embeds itself. Momentum is conserved horizontally (no external horizontal forces). Let $ u $ be the speed of the combined mass immediately after collision.  
- Initial momentum: $ m v + M \cdot 0 = m v $  
- Final momentum: $ (m + M) u $  
Thus:  

$$ m v = (m + M) u $$
  
Solving for $ u $:  

$$ u = \frac{m v}{m + M} \quad (1) $$


### Step 2: Apply conservation of energy during swing
After the collision, mechanical energy is conserved (no non-conservative forces). The kinetic energy of the combined mass at the lowest point converts to gravitational potential energy at angle $ \theta $.  
- Initial kinetic energy: $ \frac{1}{2} (m + M) u^2 $  
- Final potential energy: $ (m + M) g h $, where $ h $ is the height gained.  
Thus:  

$$ \frac{1}{2} (m + M) u^2 = (m + M) g h $$
  
Cancel $ (m + M) $:  

$$ \frac{1}{2} u^2 = g h \quad (2) $$


### Step 3: Relate height $ h $ to angle $ \theta $
The vertical displacement $ h $ is found using trigonometry. The pendulum rises from its lowest point (A) to the highest point (B), where the string makes angle $ \theta $ with the vertical. The vertical distance from pivot to A is $ L $. At B, this distance is $ L \cos \theta $. Thus:  

$$ h = L - L \cos \theta = L (1 - \cos \theta) \quad (3) $$


### Step 4: Combine equations and solve for $ v $
Substitute (3) into (2):  

$$ \frac{1}{2} u^2 = g L (1 - \cos \theta) $$
  
Substitute $ u $ from (1):  

$$ \frac{1}{2} \left( \frac{m v}{m + M} \right)^2 = g L (1 - \cos \theta) $$
  
Multiply both sides by 2:  

$$ \left( \frac{m v}{m + M} \right)^2 = 2 g L (1 - \cos \theta) $$
  
Take the square root (positive since speed > 0):  

$$ \frac{m v}{m + M} = \sqrt{2 g L (1 - \cos \theta)} $$
  
Solve for $ v $:  

$$ v = \frac{m + M}{m} \sqrt{2 g L (1 - \cos \theta)} $$

## Answer
\[ \boxed{\dfrac{(m + M) \sqrt{2 g L (1 - \cos \theta)}}{m}} \]

------
## Problem 2
##### Background
In forensic science and ballistic testing, the ballistic pendulum is a device used to measure the speed of a projectile, such as a bullet. When a bullet embeds into a pendulum block, the collision is inelastic, meaning kinetic energy is not conserved, though momentum is. The pendulum then swings upward, converting its kinetic energy into gravitational potential energy. This setup allows for the calculation of energy loss during the collision, which is crucial for understanding impact dynamics in fields like material science and safety engineering.

##### Knowledge Points Tested
- Conservation of linear momentum in inelastic collisions.
- Conversion of kinetic energy to gravitational potential energy.
- Fractional energy loss calculation.
- Algebraic manipulation of energy and momentum equations.

##### Intradisciplinary Connections
This problem connects to classical mechanics principles in physics, specifically momentum conservation in collisions (from dynamics) and energy transformations (from work-energy theorems). It also reinforces the concept of isolated systems where external forces (like tension in pendulum strings) do no net work during instantaneous collisions.

##### Interdisciplinary Connections
The analysis applies to forensic ballistics (criminal investigations), automotive crash testing (engineering), and sports science (e.g., analyzing energy absorption in protective gear). The mathematical techniques (algebra, ratios) are fundamental across all quantitative sciences.

##### Real-World Applications
1. **Forensics**: Determining bullet velocity from pendulum rise height in crime labs.
2. **Vehicle Safety**: Simulating inelastic collisions to design crumple zones that dissipate kinetic energy.
3. **Material Testing**: Measuring energy absorption in composite materials during high-impact events.

##### Problem Statement
A bullet of mass $m$ is fired horizontally into a stationary pendulum block of mass $3m$. The bullet embeds completely in the block (inelastic collision), and the combined system swings upward to a maximum height $h$ above its initial position. Derive an expression for the fraction of the initial kinetic energy lost during the collision. Express your answer as a simplified fraction in terms of the given masses. Explicitly state any assumptions made.

**Assumptions**:  
- The pendulum strings remain taut but exert no net horizontal force during the collision.  
- Air resistance and friction at the pivot are negligible during the swing.  
- Gravitational acceleration $g$ is constant.

## Solution
**Step 1: Define variables and apply momentum conservation**  
Let $v$ be the bullet's initial speed. The block is initially stationary. Post-collision, the combined mass ($m + 3m = 4m$) moves with speed $V$. Momentum is conserved horizontally:  
$$ m v + (3m) \cdot 0 = (4m) V $$  
$$ \Rightarrow m v = 4m V $$  
$$ \Rightarrow V = \frac{v}{4} \quad (1) $$  

**Step 2: Apply energy conservation to the swing phase**  
At maximum height $h$, the kinetic energy of the combined system is zero. The initial kinetic energy post-collision converts entirely to gravitational potential energy:  
$$ \frac{1}{2} (4m) V^2 = (4m) g h $$  
$$ \Rightarrow \frac{1}{2} \cdot 4m \cdot V^2 = 4m g h $$  
$$ \Rightarrow 2m V^2 = 4m g h $$  
$$ \Rightarrow V^2 = 2 g h \quad (2) $$  

**Step 3: Express initial kinetic energy ($KE_i$) and post-collision kinetic energy ($KE_f$)**  
Using $v$ from Eq. (1) and $V^2$ from Eq. (2):  
- $KE_i$ (bullet only):  
$$ KE_i = \frac{1}{2} m v^2 = \frac{1}{2} m (4V)^2 = \frac{1}{2} m \cdot 16 V^2 = 8m V^2 $$  
Substitute $V^2 = 2gh$:  
$$ KE_i = 8m \cdot (2gh) = 16mgh $$  
- $KE_f$ (combined mass):  
$$ KE_f = \frac{1}{2} (4m) V^2 = 2m V^2 = 2m \cdot (2gh) = 4mgh $$  

**Step 4: Calculate energy loss and fraction lost**  
- Kinetic energy lost:  
$$ \Delta KE = KE_i - KE_f = 16mgh - 4mgh = 12mgh $$  
- Fraction lost:  
$$ \text{Fraction lost} = \frac{\Delta KE}{KE_i} = \frac{12mgh}{16mgh} = \frac{12}{16} = \frac{3}{4} $$  

The fraction $\frac{3}{4}$ is independent of $g$, $h$, and $m$, depending only on the mass ratio ($m : 3m$).

## Answer
$$\boxed{\dfrac{3}{4}}$$

------
## Problem 3
##### Background
A ballistic pendulum is a device used to measure the speed of projectiles. It consists of a large block of mass $M$ suspended by a cord of length $L$. When a bullet of mass $m$ strikes and embeds into the block, the combined system swings upward to a maximum angle $\theta$ with the vertical. This problem explores the physics of inelastic collisions and energy conservation in pendulum motion.

##### Knowledge Points Tested
1. Conservation of linear momentum in inelastic collisions  
2. Conservation of mechanical energy  
3. Geometric analysis of pendulum displacement  
4. Trigonometric relationships for potential energy calculations  

##### Intradisciplinary Connections
- Connects momentum conservation (collisions) with work-energy principles (pendulum motion)  
- Illustrates how gravitational potential energy relates to angular displacement in oscillatory systems  

##### Interdisciplinary Connections
- Forensic science: Determining bullet speeds in crime scene investigations  
- Mechanical engineering: Designing impact-absorption systems  
- History of science: Original use in 19th-century ballistic measurements  

##### Real-World Applications
- Testing firearm muzzle velocities  
- Crash-test analysis for vehicle safety  
- Space debris impact studies on spacecraft shielding  

##### Problem Statement
A bullet of mass $m$ is fired horizontally into a stationary block of mass $M$ suspended as a pendulum of length $L$. The bullet embeds into the block, and the system swings to a maximum angle $\theta$ with the vertical. Derive an expression for the initial speed $v$ of the bullet in terms of $m$, $M$, $L$, $\theta$, and the acceleration due to gravity $g$.  

**Express your answer as a single analytic expression. Use standard mathematical notation: fractions with \frac{numerator}{denominator}, \sqrt{} for square roots, and \cos for cosine. Do not substitute numerical values.**

## Solution
**Step 1: Conservation of Momentum (Inelastic Collision)**  
Let $v$ be the bullet's initial speed and $V$ be the speed of the block-bullet system immediately after collision. Since the block is initially stationary:  
$$ m v = (M + m) V $$  
Solving for $V$:  
$$ V = \frac{m v}{M + m} \quad (1) $$  

**Step 2: Energy Conservation (Pendulum Swing)**  
The kinetic energy of the block-bullet system converts to gravitational potential energy at the maximum height. Let $h$ be the vertical rise of the center of mass. Then:  
$$ \frac{1}{2} (M + m) V^2 = (M + m) g h $$  
Simplifying:  
$$ \frac{1}{2} V^2 = g h \quad \Rightarrow \quad V^2 = 2 g h \quad (2) $$  

**Step 3: Geometric Height Calculation**  
The height $h$ relates to the angular displacement $\theta$ and cord length $L$. From pendulum geometry:  
$$ h = L (1 - \cos \theta) \quad (3) $$  
Substituting (3) into (2):  
$$ V^2 = 2 g L (1 - \cos \theta) \quad (4) $$  

**Step 4: Combine Equations**  
Substitute expression (1) for $V$ into equation (4):  
$$ \left( \frac{m v}{M + m} \right)^2 = 2 g L (1 - \cos \theta) $$  
Solving for $v^2$:  
$$ v^2 = \frac{2 g L (1 - \cos \theta) (M + m)^2}{m^2} $$  
Take the positive square root (speed magnitude):  
$$ v = \frac{M + m}{m} \sqrt{2 g L (1 - \cos \theta)} $$  

**Final Expression**  
The initial speed of the bullet is:  
$$ v = \frac{M + m}{m} \sqrt{2 g L (1 - \cos \theta)} $$

## Answer
$$\boxed{\frac{M + m}{m} \sqrt{2 g L \left(1 - \cos \theta\right)}}$$

------
## Problem 4
##### Background
A ballistic pendulum is a device used to measure bullet velocities. It consists of a pendulum bob (a block of wood or similar material) suspended by a string. When a bullet strikes and embeds into the bob, the system swings upward. The maximum height $h$ reached depends on the bullet's initial velocity and masses. However, if the string is too short, it may go slack during the swing, causing the pendulum to deviate from circular motion and invalidating standard analysis. This problem explores the minimum string length required to maintain tension throughout the motion when the pendulum reaches height $h$.

##### Knowledge Points Tested
1. Conservation of linear momentum in perfectly inelastic collisions.
2. Conservation of mechanical energy (kinetic and gravitational potential energy).
3. Centripetal force requirement for circular motion at the highest point of the swing.
4. Tension force dynamics in pendulums.

##### Intradisciplinary Connections
- Connects momentum conservation (collisions) with rotational dynamics (pendulum motion).
- Integrates energy concepts with force analysis in curvilinear motion.

##### Interdisciplinary Connections
- Physics and engineering: Designing pendulum systems for ballistic measurements.
- Forensic science: Estimating projectile speeds in impact scenarios.

##### Real-World Applications
- Forensic ballistics: Determining bullet speeds from impact dynamics.
- Mechanical safety systems: Designing pendulum dampers or restraints where slack avoidance is critical.

##### Problem Statement
A bullet of mass $m$ is fired horizontally at velocity $v$ into a stationary pendulum bob of mass $4m$ suspended by a string. The bullet embeds into the bob, and the combined system swings upward, reaching a maximum height $h$ above its lowest point. Determine the minimum string length $L$ such that the string does not go slack at any point during the swing. Express your answer symbolically in terms of $m$, $v$, $h$, $g$ (acceleration due to gravity), and any necessary fundamental constants. Use $g$ for gravity; do not substitute numerical values.  

**Answer Format Instructions:**  
- Provide an analytic expression.  
- Use standard mathematical notation:  
  - Fractions: $\frac{a}{b}$.  
  - Exponents: $x^{2}$, not $x^2$.  
  - Physical constants: Represent $g$ symbolically.  
- The expression must depend only on the given parameters $m$, $v$, $h$, $g$.

## Solution
**Step 1: Apply conservation of momentum to the inelastic collision.**  
Let $V$ be the velocity of the combined system (bullet + bob) immediately after the collision. The initial momentum (bullet only) equals the final momentum (combined mass):  

$$
m \cdot v = (m + 4m) \cdot V \implies mv = 5m V
$$
  
Solving for $V$:  

$$
V = \frac{v}{5}
$$


**Step 2: Apply conservation of energy from right after collision to maximum height.**  
At the lowest point, kinetic energy is $\frac{1}{2}(5m)V^2$, and potential energy is 0 (reference point). At height $h$, kinetic energy is $K_{\text{top}}$, and potential energy is $(5m)gh$. The maximum height $h$ is reached when kinetic energy is minimized but not necessarily zero due to circular motion constraints. Energy conservation gives:  

$$
\frac{1}{2}(5m)V^2 = \frac{1}{2}(5m)v_{\text{top}}^2 + (5m)gh
$$
  
Substitute $V = v/5$:  

$$
\frac{1}{2}(5m)\left(\frac{v}{5}\right)^2 = \frac{5m}{2}v_{\text{top}}^2 + 5mgh
$$
  
Simplify:  

$$
\frac{1}{2} \cdot 5m \cdot \frac{v^2}{25} = \frac{5m}{2}v_{\text{top}}^2 + 5mgh \implies \frac{mv^2}{10} = \frac{5m}{2}v_{\text{top}}^2 + 5mgh
$$
  
Divide both sides by $m$:  

$$
\frac{v^2}{10} = \frac{5}{2}v_{\text{top}}^2 + 5gh \quad \text{(Equation 1)}
$$


**Step 3: Analyze forces at the highest point to prevent slack.**  
At height $h$, the string makes an angle $\theta$ with the vertical. The centripetal force is provided by the net radial component of gravity and tension. To avoid slack, tension $T \geq 0$. The minimum condition is $T = 0$ at the highest point. The centripetal force requirement is:  

$$
(5m)g \cos\theta = \frac{(5m) v_{\text{top}}^2}{L}
$$
  
where $\cos\theta$ relates to $h$ and $L$. From geometry:  

$$
h = L(1 - \cos\theta) \implies \cos\theta = \frac{L - h}{L}
$$
  
Substitute $\cos\theta$:  

$$
(5m)g \cdot \frac{L - h}{L} = \frac{(5m) v_{\text{top}}^2}{L}
$$
  
Simplify (divide both sides by $5m$ and multiply by $L$):  

$$
g(L - h) = v_{\text{top}}^2 \quad \text{(Equation 2)}
$$


**Step 4: Combine energy and force equations.**  
Substitute Equation 2 into Equation 1:  

$$
\frac{v^2}{10} = \frac{5}{2} \left[ g(L - h) \right] + 5gh
$$
  
Simplify the right-hand side:  

$$
\frac{v^2}{10} = \frac{5g}{2}(L - h) + 5gh = \frac{5g}{2}L - \frac{5g}{2}h + 5gh = \frac{5g}{2}L + \frac{5g}{2}h
$$
  
Multiply both sides by 10:  

$$
v^2 = 10 \cdot \frac{5g}{2}(L + h) = 25g(L + h)
$$
  
Solve for $L$:  

$$
L + h = \frac{v^2}{25g} \implies L = \frac{v^2}{25g} - h
$$
  
This is the minimum string length to avoid slack when the pendulum reaches height $h$.

## Answer
$$\boxed{\dfrac{v^{2}}{25g} - h}$$

------
## Problem 5
##### Background
In forensic ballistics, a ballistic pendulum is used to measure bullet velocities. Unlike standard setups where the bullet embeds, modern armor-piercing rounds may penetrate and exit a target block. Consider a pendulum block of mass $M$, suspended by rigid cords, initially at rest. A bullet of mass $m$ is fired horizontally at the block with initial speed $v$. The bullet penetrates the block and exits with exactly half its initial speed, $v/2$. The block then swings upward due to the momentum transfer.

##### Knowledge Points Tested
1. Conservation of linear momentum during the collision phase.
2. Conservation of mechanical energy during the pendulum's upward swing.
3. Algebraic manipulation to derive expressions for velocity and height.

##### Intradisciplinary Connections
- **Mechanics**: Connects to impulse, momentum, and energy principles in inelastic collisions.
- **Dynamics**: Relates to projectile motion concepts through the pendulum's trajectory.
- **Mathematical Modeling**: Requires deriving symbolic relationships from physical laws.

##### Interdisciplinary Connections
- **Forensic Science**: Ballistic pendulums are used to estimate bullet speeds in crime scene investigations.
- **Materials Engineering**: Penetration dynamics inform armor design, where partial energy transfer occurs.
- **Biomechanics**: Models similar momentum-transfer scenarios in biomechanical impacts (e.g., ballistics testing on tissue simulants).

##### Real-World Applications
- **Armor Testing**: Measuring residual bullet speeds after penetration helps evaluate body armor effectiveness.
- **Wildlife Forensics**: Determining poachers' bullet velocities from impact data on suspended animal carcass analogs.
- **Space Debris Mitigation**: Modeling high-velocity impacts on spacecraft shields, where debris may retain partial speed.

##### Problem Statement
A bullet of mass $m$ is fired horizontally with initial speed $v$ at a stationary pendulum block of mass $M$. The bullet penetrates the block and exits with a speed of $v/2$. Derive an expression for the maximum height $h$ that the block rises above its initial position. Express $h$ exclusively in terms of the given symbols: $m$ (bullet mass), $M$ (block mass), $v$ (bullet initial speed), and $g$ (acceleration due to gravity).  

**Answer Format Requirements**:  
- Provide a **single simplified analytic expression** for $h$ using the symbols $m$, $M$, $v$, and $g$.  
- Use fractions with two-field notation (e.g., `\frac{a}{b}`).  
- Do **not** include any numerical values, units, or unevaluated operations.  
- Enclose your final answer in `\boxed{}` as a standalone expression.

## Solution
**Stage 1: Conservation of Momentum During Collision**  
The bullet and block form an isolated system horizontally during penetration. Apply conservation of linear momentum:  
- Initial momentum = momentum of bullet (block is stationary): $m v$.  
- Final momentum = momentum of bullet after exit + momentum of block: $m \cdot (v/2) + M V$, where $V$ is the block's speed immediately after the bullet exits.  
Equating initial and final momentum:  
$$ m v = m \cdot \frac{v}{2} + M V $$  
Solve for $V$:  
$$ m v - \frac{m v}{2} = M V $$  
$$ \frac{m v}{2} = M V $$  
$$ V = \frac{m v}{2 M} $$  

**Stage 2: Conservation of Energy During Pendulum Swing**  
After the bullet exits, the block swings upward. Mechanical energy is conserved (no air resistance or friction):  
- Initial energy (at bottom) = kinetic energy: $\frac{1}{2} M V^2$.  
- Final energy (at maximum height $h$) = gravitational potential energy: $M g h$.  
Equating energies:  
$$ \frac{1}{2} M V^2 = M g h $$  
Solve for $h$:  
$$ h = \frac{V^2}{2 g} $$  
Substitute $V$ from Stage 1:  
$$ h = \frac{1}{2 g} \left( \frac{m v}{2 M} \right)^2 = \frac{1}{2 g} \cdot \frac{m^2 v^2}{4 M^2} = \frac{m^2 v^2}{8 g M^2} $$  
The expression is fully simplified.

## Answer
$$\boxed{\frac{m^{2}v^{2}}{8gM^{2}}}$$

------
# Boyle's law pressure-volume relationships

## Problem 0
##### Background
Scuba divers often observe air bubbles expanding as they rise from the ocean depths. This occurs because the surrounding water pressure decreases, allowing the gas inside the bubble to occupy more space. The behavior of such bubbles can be modeled using fundamental gas laws, assuming constant seawater temperature and ideal gas behavior.

##### Knowledge Points Tested
- Boyle's law: For a fixed amount of gas at constant temperature, pressure and volume are inversely proportional ($P_1 V_1 = P_2 V_2$).
- Hydrostatic pressure: Pressure at depth in a fluid is the sum of atmospheric pressure and pressure from the fluid column ($P = P_{\text{atm}} + \rho g d$).

##### Intradisciplinary Connections
This problem integrates fluid statics (hydrostatic pressure) with gas laws, demonstrating how pressure variations in fluids directly affect gas volume.

##### Interdisciplinary Connections
Connects to oceanography (depth-pressure relationships in seawater) and engineering (safety calculations for underwater operations and diving).

##### Real-World Applications
Predicting bubble expansion is critical for avoiding decompression sickness in divers, designing underwater habitats, and understanding gas exchange in marine ecosystems.

##### Problem Statement
A spherical air bubble forms at a depth $h$ below the surface of the ocean, where its volume is $V_i$. The bubble rises and is observed at a new depth $h'$. The seawater has density $\rho$, atmospheric pressure is $P_{\text{atm}}$, and gravitational acceleration is $g$. The ocean temperature remains constant.  

Derive an expression for the bubble's volume $V_f$ at depth $h'$. Express your answer solely in terms of the given parameters: $V_i$, $P_{\text{atm}}$, $\rho$, $g$, $h$, and $h'$.  

**Answer format instructions**:  
- Provide an analytic expression.  
- Use standard notation: fractions as $\frac{a}{b}$, multiplication as $a \cdot b$ or $a b$.  
- Do **not** substitute numerical values or constants.  
- Use inline fractions only for simple ratios; otherwise, use $\frac{}{}$.  
- Physical units are not required in the final answer.

## Solution
**Step 1: Identify initial and final pressures**  
The pressure at depth $d$ in a fluid is given by hydrostatic pressure formula:  
$$ P(d) = P_{\text{atm}} + \rho g d $$  
- Initial pressure at depth $h$: $P_i = P_{\text{atm}} + \rho g h$  
- Final pressure at depth $h'$: $P_f = P_{\text{atm}} + \rho g h'$  

**Step 2: Apply Boyle's law**  
For a fixed amount of gas at constant temperature, Boyle's law states:  
$$ P_i V_i = P_f V_f $$  

**Step 3: Solve for final volume $V_f$**  
Substitute expressions for $P_i$ and $P_f$:  
$$ (P_{\text{atm}} + \rho g h) V_i = (P_{\text{atm}} + \rho g h') V_f $$  
Rearrange to isolate $V_f$:  
$$ V_f = \frac{(P_{\text{atm}} + \rho g h) V_i}{P_{\text{atm}} + \rho g h'} $$  

**Conclusion**: The expression for the bubble's volume at depth $h'$ is derived as shown.

## Answer
$$\boxed{\dfrac{(P_{\text{atm}} + \rho g h) V_i}{P_{\text{atm}} + \rho g h'}}$$

------
## Problem 1
##### Background
Scuba diving relies on compressed air tanks to supply breathing gas underwater. These tanks are rigid containers with a fixed internal volume. When air is released from the tank, it expands to ambient pressure (sea-level atmospheric pressure). The relationship between pressure and volume follows Boyle's law for ideal gases under constant temperature conditions.

##### Knowledge Points Tested
- Boyle's law and pressure-volume relationships for ideal gases
- Conservation of mass applied to gas systems
- Ideal gas law and its application to variable-pressure scenarios

##### Intradisciplinary Connections
- Connects to thermodynamics (state variables) and fluid mechanics (gas expansion)
- Extends to gas storage calculations in industrial systems (e.g., compressed natural gas tanks)

##### Interdisciplinary Connections
- Environmental science: Estimating gas release volumes in atmospheric studies
- Engineering: Designing pressure vessels and safety valves for gas storage

##### Real-World Applications
- Calculating usable air supply in scuba tanks for dive planning
- Determining gas volumes in medical oxygen tanks during patient treatment
- Industrial gas storage and transfer systems (e.g., HVAC refrigerant handling)

##### Problem Statement
A rigid scuba tank has an internal volume $ V_t $. It is initially pressurized to an absolute pressure $ P_i $. Air is released from the tank until the absolute pressure inside drops to $ P_f $. The released air is measured at sea-level atmospheric pressure $ P_a $, and temperature remains constant. Assume air behaves as an ideal gas.  

Derive an expression for the volume of air released, measured at pressure $ P_a $. Express your answer symbolically in terms of $ V_t $, $ P_i $, $ P_f $, and $ P_a $.

## Solution
**Step 1: Initial and final states of air in the tank**  
- Initial moles of air in tank ($ n_i $):  
  Using the ideal gas law:  
  $$ P_i V_t = n_i RT \implies n_i = \frac{P_i V_t}{RT} $$  
- Final moles of air in tank ($ n_f $) after pressure drop:  
  $$ P_f V_t = n_f RT \implies n_f = \frac{P_f V_t}{RT} $$  

**Step 2: Moles of air released**  
The moles of air released ($ \Delta n $) is the difference:  
$$ \Delta n = n_i - n_f = \frac{P_i V_t}{RT} - \frac{P_f V_t}{RT} = \frac{V_t (P_i - P_f)}{RT} $$  

**Step 3: Volume of released air at pressure $ P_a $**  
Let $ V_{\text{released}} $ be the volume occupied by $ \Delta n $ moles at pressure $ P_a $ (same temperature):  
$$ P_a V_{\text{released}} = \Delta n \cdot RT $$  
Substitute $ \Delta n $:  
$$ P_a V_{\text{released}} = \left( \frac{V_t (P_i - P_f)}{RT} \right) RT $$  
Simplify by canceling $ RT $:  
$$ P_a V_{\text{released}} = V_t (P_i - P_f) $$  
Solve for $ V_{\text{released}} $:  
$$ V_{\text{released}} = \frac{V_t (P_i - P_f)}{P_a} $$  

**Conclusion**  
The volume of air released, measured at atmospheric pressure $ P_a $, is $ \dfrac{V_t (P_i - P_f)}{P_a} $.

## Answer
$$\boxed{\dfrac{V_t \left( P_i - P_f \right)}{P_a}}$$

------
## Problem 2
##### Background
In medical and laboratory settings, syringes are often connected to other containers to form closed systems for precise control of gases. Consider a device where a syringe is connected via a thin tube to a rigid, sealed container. The tube has a valve that can be opened or closed. Initially, the container is evacuated (containing no air), while the syringe contains air. The entire system is maintained at constant temperature, ensuring that Boyle's law applies. Boyle's law states that for a fixed amount of gas at constant temperature, the pressure and volume are inversely related: $ P_1 V_1 = P_2 V_2 $.

##### Knowledge Points Tested
- Boyle's law for ideal gases under constant temperature.
- Conservation of gas mass (amount of substance) in a closed system.
- Analysis of multi-step processes involving gas expansion and compression.
- Application of inverse proportionality between pressure and volume.

##### Intradisciplinary Connections
- **Gas Laws**: This problem extends to combined gas laws when temperature or amount of gas changes (though temperature is constant here).
- **Fluid Mechanics**: Relates to pressure equilibrium in interconnected volumes.
- **Thermodynamics**: Illustrates an isothermal process in an ideal gas, foundational for understanding more complex thermodynamic cycles.

##### Interdisciplinary Connections
- **Medical Technology**: Models syringe systems used in drug delivery or vacuum-assisted devices.
- **Engineering**: Demonstrates principles in designing pneumatic systems, such as those in HVAC or hydraulic controls.
- **Environmental Science**: Analogous to gas behavior in confined ecosystems (e.g., underground cavities or sealed bioreactors).

##### Real-World Applications
- **Medical Devices**: Used in ventilators, where syringes regulate air pressure in patient circuits.
- **Laboratory Equipment**: Applied in vacuum chambers for sample preparation, ensuring precise pressure control.
- **Consumer Products**: Found in spray cans or bicycle pumps, where compressed air stores energy.

##### Problem Statement
A medical device consists of a syringe and a rigid, sealed container connected by a thin tube of negligible volume. The tube has a valve that is initially closed. The syringe has an initial volume $ V_s $, containing air at an initial pressure $ P_i $. The rigid container has a fixed volume $ V_c $ and is initially evacuated (pressure 0 atm). The entire system is kept at constant temperature.  

First, the valve is opened, allowing the air to expand freely into the entire system. Then, without closing the valve, the plunger is compressed to reduce the syringe volume to $ V_s' $ (where $ V_s' < V_s $).  

Derive an expression for the final pressure $ P_f $ in the system in terms of the given symbols: $ P_i $, $ V_s $, $ V_c $, and $ V_s' $.  

Express your final answer as an analytic expression using the provided symbols. Do not substitute numerical values. Ensure all notation follows the guidelines:  
- Use standard LaTeX formatting (e.g., `\frac{}{}` for fractions).  
- Express exponents using `^` with curly braces (e.g., `x^{a+b}`).  
- The answer must be simplified and enclosed in `$$\boxed{...}$$`.

## Solution
### Step-by-Step Derivation

#### Step 1: Analyze the initial state before opening the valve
- The syringe has volume $ V_s $ and pressure $ P_i $.
- The container has volume $ V_c $ and is evacuated, so its pressure is 0 atm.
- The valve is closed, so the gas is confined to the syringe.
- The amount of gas (number of moles, $ n $) is constant and given by the ideal gas law:  
  $$ n = \frac{P_i V_s}{RT} $$  
  where $ R $ is the gas constant and $ T $ is the constant temperature. Since $ T $ is constant, we can use Boyle's law without explicitly involving $ n $, $ R $, or $ T $.

#### Step 2: Calculate the pressure after opening the valve (first expansion)
- When the valve opens, the gas expands to fill the entire system. The total volume becomes:  
  $$ V_{\text{total}} = V_s + V_c $$  
- By Boyle's law, the product of initial pressure and initial volume equals the product of the new pressure and new volume for the same amount of gas at constant temperature:  
  $$ P_i V_s = P_1 (V_s + V_c) $$  
  where $ P_1 $ is the pressure after expansion.
- Solving for $ P_1 $:  
  $$ P_1 = \frac{P_i V_s}{V_s + V_c} $$  

#### Step 3: Analyze the state before compression
- The entire system (syringe + container) now has volume $ V_s + V_c $ and uniform pressure $ P_1 $.
- The amount of gas remains unchanged.

#### Step 4: Calculate the pressure after compressing the syringe
- The plunger is compressed, reducing the syringe volume to $ V_s' $. The container volume $ V_c $ remains fixed, so the new total volume is:  
  $$ V_{\text{new}} = V_s' + V_c $$  
- The gas undergoes a second isothermal process. Applying Boyle's law between the state after expansion (pressure $ P_1 $, volume $ V_s + V_c $) and the final state (pressure $ P_f $, volume $ V_s' + V_c $):  
  $$ P_1 (V_s + V_c) = P_f (V_s' + V_c) $$  
- Substitute the expression for $ P_1 $ from Step 2:  
  $$ \left( \frac{P_i V_s}{V_s + V_c} \right) (V_s + V_c) = P_f (V_s' + V_c) $$  
- Simplify the left side:  
  $$ P_i V_s = P_f (V_s' + V_c) $$  
- Solve for $ P_f $:  
  $$ P_f = \frac{P_i V_s}{V_s' + V_c} $$  

#### Conclusion
The final pressure $ P_f $ is given by the expression $ \frac{P_i V_s}{V_s' + V_c} $.

## Answer
$$\boxed{\frac{P_i V_s}{V_s' + V_c}}$$

------
## Problem 3
##### Background
Weather balloons are essential tools for atmospheric research. As a balloon ascends through Earth's atmosphere, it experiences decreasing external pressure. This expansion is governed by fundamental gas laws derived from the kinetic theory of gases, which describes how molecular motion creates pressure. Understanding these principles allows scientists to predict balloon behavior during ascent, crucial for instrument deployment and atmospheric data collection.

##### Knowledge Points Tested
1. Kinetic theory of gases: Deriving pressure from molecular collisions.
2. Boyle's law: Relationship between pressure and volume at constant temperature.
3. Equilibrium conditions: Internal pressure equals external pressure for a freely expanding balloon.

##### Intradisciplinary Connections
- Thermodynamics: Connection between kinetic energy, temperature, and pressure.
- Fluid statics: Pressure variation with altitude in Earth's atmosphere.

##### Interdisciplinary Connections
- Meteorology: Predicting weather balloon trajectories and instrument payload behavior.
- Aerospace engineering: Designing expandable structures for high-altitude applications.

##### Real-World Applications
- Atmospheric sounding: Weather balloons measure temperature, humidity, and pressure profiles up to 35 km altitude.
- Medical devices: Similar pressure-volume principles govern syringe design and respiratory equipment.

##### Problem Statement
A spherical weather balloon filled with an ideal gas is launched from ground level. The initial atmospheric pressure is $P_0$, and the initial gas volume is $V_0$. The balloon ascends to an altitude where the atmospheric pressure is $P_1$. Assume:
- The gas temperature remains constant due to efficient heat exchange.
- The balloon material allows instantaneous pressure equilibrium with the surroundings.
- Gas molecules have mass $m$, and the gas contains $N$ molecules.

First, derive an expression for pressure $P$ using kinetic theory by considering elastic collisions of gas molecules with the container walls. Start with a cubic container of side length $L$ (volume $V = L^3$). Then, generalize the result to show that $PV = \text{constant}$ for fixed $N$ and temperature $T$.

Using this result, compute the new volume $V_1$ of the balloon at pressure $P_1$. Express $V_1$ analytically in terms of $P_0$, $V_0$, and $P_1$.

## Solution
#### Step 1: Kinetic Theory Derivation of Pressure
Consider a cubic container with side length $L$ and volume $V = L^3$. A gas molecule of mass $m$ moves with velocity component $v_x$ toward the wall perpendicular to the x-axis. Upon elastic collision, its momentum change is $\Delta p_x = -2mv_x$. The time between consecutive collisions with the same wall is $\Delta t = 2L / v_x$. The average force exerted by one molecule on the wall is:

$$
F_{\text{one}} = \frac{\Delta p_x}{\Delta t} = \frac{2mv_x}{2L / v_x} = \frac{mv_x^2}{L}.
$$

For $N$ molecules, the total force in the x-direction is:

$$
F_x = \frac{mN}{L} \overline{v_x^2},
$$

where $\overline{v_x^2}$ is the mean square x-velocity. By symmetry, $\overline{v^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2} = 3\overline{v_x^2}$, so:

$$
F_x = \frac{mN \overline{v^2}}{3L}.
$$

Pressure is force per unit area. With wall area $L^2$:

$$
P = \frac{F_x}{L^2} = \frac{mN \overline{v^2}}{3L^3} = \frac{mN \overline{v^2}}{3V}.
$$


#### Step 2: Relate Pressure to Temperature
The average kinetic energy per molecule is:

$$
\frac{1}{2}m\overline{v^2} = \frac{3}{2}k_B T,
$$

where $k_B$ is Boltzmann's constant and $T$ is absolute temperature. Solving for $m\overline{v^2}$:

$$
m\overline{v^2} = 3k_B T.
$$

Substitute into the pressure equation:

$$
P = \frac{N}{3V} \cdot 3k_B T = \frac{Nk_B T}{V}.
$$

Thus:

$$
PV = Nk_B T.
$$

For fixed $N$ and constant $T$, $PV = \text{constant}$.

#### Step 3: Apply Boyle's Law to Balloon
At ground level:

$$
P_0 V_0 = Nk_B T.
$$

At altitude:

$$
P_1 V_1 = Nk_B T.
$$

Equating the two expressions:

$$
P_0 V_0 = P_1 V_1.
$$

Solving for $V_1$:

$$
V_1 = \frac{P_0 V_0}{P_1}.
$$

This confirms Boyle's law: Volume is inversely proportional to pressure at constant temperature.

## Answer
\[
\boxed{\dfrac{P_0 V_0}{P_1}}
\]

------
# center of mass motion and calculations

## Problem 0
##### Background
In aerospace engineering, the center of mass of a spacecraft is critical for stable orbital maneuvers. Consider a prototype satellite with three thruster modules positioned at key locations: a 4 kg module at the origin (0, 0), a 6 kg module at (3, 0), and a 5 kg module at (0, 4) in a Cartesian coordinate system where units are meters. Precise knowledge of the center of mass ensures the satellite maintains correct orientation during thrust vectoring.

##### Knowledge Points Tested
- Definition and physical interpretation of center of mass
- Application of weighted average formulas in two dimensions
- Vector decomposition of mass distributions

##### Intradisciplinary Connections
- Relates to torque and rotational equilibrium in mechanics
- Extends to moment of inertia calculations for rigid bodies
- Connects to gravitational potential energy in conservative systems

##### Interdisciplinary Connections
- Engineering: Stability analysis of structures under load
- Mathematics: Coordinate geometry and weighted means
- Robotics: Path planning for multi-component systems

##### Real-World Applications
- Satellite attitude control systems
- Aircraft balance and trim calculations
- Biomechanics of human posture and movement

##### Problem Statement
Using the fundamental definition of center of mass, derive the exact coordinates of the center of mass for the three-module satellite system described. Express each coordinate as a simplified fraction. Do not compute numerical approximations. The solution must show all steps starting from first principles, including the governing equations and their dimensional justification.

## Solution
The center of mass $(x_{\text{cm}}, y_{\text{cm}})$ for a system of $n$ point masses is defined as:  
$$x_{\text{cm}} = \frac{\sum_{i=1}^{n} m_i x_i}{\sum_{i=1}^{n} m_i}, \quad y_{\text{cm}} = \frac{\sum_{i=1}^{n} m_i y_i}{\sum_{i=1}^{n} m_i}$$  
where $m_i$ are the masses and $(x_i, y_i)$ are their positions.  

Given:  
- Mass $m_1 = 4  \text{kg}$ at $(x_1, y_1) = (0, 0)$  
- Mass $m_2 = 6  \text{kg}$ at $(x_2, y_2) = (3, 0)$  
- Mass $m_3 = 5  \text{kg}$ at $(x_3, y_3) = (0, 4)$  

**Step 1: Compute total mass $M$**  
$$M = \sum_{i=1}^{3} m_i = m_1 + m_2 + m_3 = 4 + 6 + 5 = 15  \text{kg}$$  

**Step 2: Compute numerator for $x_{\text{cm}}$**  
$$\sum_{i=1}^{3} m_i x_i = m_1 x_1 + m_2 x_2 + m_3 x_3 = (4)(0) + (6)(3) + (5)(0) = 0 + 18 + 0 = 18  \text{kg} \cdot \text{m}$$  

**Step 3: Compute $x_{\text{cm}}$**  
$$x_{\text{cm}} = \frac{\sum m_i x_i}{M} = \frac{18}{15} = \frac{6}{5}  \text{m}$$  

**Step 4: Compute numerator for $y_{\text{cm}}$**  
$$\sum_{i=1}^{3} m_i y_i = m_1 y_1 + m_2 y_2 + m_3 y_3 = (4)(0) + (6)(0) + (5)(4) = 0 + 0 + 20 = 20  \text{kg} \cdot \text{m}$$  

**Step 5: Compute $y_{\text{cm}}$**  
$$y_{\text{cm}} = \frac{\sum m_i y_i}{M} = \frac{20}{15} = \frac{4}{3}  \text{m}$$  

The center of mass coordinates are $\left( \frac{6}{5}, \frac{4}{3} \right)$.

## Answer
$$\boxed{\left( \dfrac{6}{5},\ \dfrac{4}{3} \right)}$$

------
## Problem 1
#### Background
In structural engineering and material science, objects are often designed with non-uniform density to optimize strength, weight, or balance. For example, a cantilever beam in a bridge might have higher density near its support to handle greater stress. Here, we examine a rod with a linearly increasing density profile, a simplified model for such applications.

#### Knowledge Points Tested
1. Definition of center of mass for continuous mass distributions.
2. Integration techniques for calculating total mass and moment integrals.
3. Application of linear mass density functions.

#### Intradisciplinary Connections
This problem connects to rotational dynamics, where the center of mass determines torque and rotational inertia, and to statics, where balance under gravitational forces depends on the center of mass location.

#### Interdisciplinary Connections
- **Engineering**: Calculating center of mass is critical in robotics (e.g., balancing robotic arms) and aerospace (e.g., determining stability of aircraft).
- **Materials Science**: Density gradients are engineered in composite materials to enhance performance under load.

#### Real-World Applications
- Designing baseball bats or golf clubs with variable density to shift the "sweet spot."
- Optimizing the mass distribution in crane booms to prevent tipping.

#### Problem Statement
A rod of length $L$ has a linear mass density $\lambda(x) = kx$, where $x$ is the distance from the left end of the rod, and $k$ is a constant. Determine the position of the center of mass relative to the left end. Express your answer as an analytic expression in terms of $L$.

## Solution
The center of mass $x_{\text{cm}}$ for a continuous object is defined as:
$$
x_{\text{cm}} = \frac{1}{M} \int x  dm,
$$
where $M$ is the total mass of the rod, and $dm$ is the mass element. Given the linear mass density $\lambda(x) = \frac{dm}{dx}$, we express $dm = \lambda(x)  dx = kx  dx$.

**Step 1: Calculate the total mass $M$**  
Integrate $dm$ over the length of the rod:
$$
M = \int_{0}^{L} dm = \int_{0}^{L} kx  dx.
$$
Solve the integral:
$$
M = k \int_{0}^{L} x  dx = k \left[ \frac{x^2}{2} \right]_{0}^{L} = k \left( \frac{L^2}{2} - 0 \right) = \frac{kL^2}{2}.
$$

**Step 2: Calculate the numerator $\int x  dm$**  
Substitute $dm = kx  dx$:
$$
\int x  dm = \int_{0}^{L} x \cdot (kx)  dx = k \int_{0}^{L} x^2  dx.
$$
Solve the integral:
$$
k \int_{0}^{L} x^2  dx = k \left[ \frac{x^3}{3} \right]_{0}^{L} = k \left( \frac{L^3}{3} - 0 \right) = \frac{kL^3}{3}.
$$

**Step 3: Compute $x_{\text{cm}}$**  
Substitute the results from Steps 1 and 2:
$$
x_{\text{cm}} = \frac{\frac{kL^3}{3}}{\frac{kL^2}{2}} = \frac{kL^3}{3} \cdot \frac{2}{kL^2} = \frac{2L}{3}.
$$
The center of mass is located at $\frac{2L}{3}$ from the left end. This result is physically intuitive: since density increases with $x$, the center of mass shifts rightward from the midpoint ($\frac{L}{2}$) to $\frac{2L}{3}$.

## Answer
$$\boxed{\frac{2L}{3}}$$

------
## Problem 2
##### Background
Two masses $m_1$ and $m_2$ are connected by a rigid massless rod, forming a system that can move freely on a horizontal frictionless surface. A force $\vec{F}$ is applied to $m_1$ in a specific direction, causing $m_1$ to experience an instantaneous acceleration of magnitude $a_1$ in that direction. The rod constrains the motion such that internal forces act along its length, but the applied force $\vec{F}$ is perpendicular to the rod. This configuration ensures that the rod transmits no force component to $m_1$ in the direction of $\vec{F}$, simplifying the analysis of center of mass motion.

##### Knowledge Points Tested
1. Center of mass acceleration: $\vec{a}_{\text{cm}} = \frac{\sum \vec{F}_{\text{ext}}}{M_{\text{total}}}$  
2. Newton's second law for individual masses  
3. Role of internal forces in constrained systems (rigid rod)  
4. Vector decomposition of forces and accelerations  

##### Intradisciplinary Connections
- Connects to rotational dynamics (torque and angular acceleration would arise if force were not perpendicular to rod)  
- Relates to systems of particles and conservation laws  
- Extends to rigid body motion concepts  

##### Interdisciplinary Connections
- **Mechanical Engineering**: Force transmission in linked structures (e.g., robotic arms)  
- **Aerospace Engineering**: Thruster placement in spacecraft with multiple modules  
- **Biomechanics**: Muscle forces acting on connected bone segments  

##### Real-World Applications
- Calculating acceleration of a vehicle when force is applied to a trailer hitch  
- Determining thrust distribution in multi-stage rockets  
- Analyzing stress in bridge trusses under load  

##### Problem Statement
Two masses $m_1$ and $m_2$ are connected by a rigid massless rod. When a force $\vec{F}$ is applied to $m_1$ perpendicular to the rod, $m_1$ accelerates with magnitude $a_1$ in the direction of $\vec{F}$. Derive an expression for the magnitude of the center of mass acceleration $a_{\text{cm}}$ in terms of $m_1$, $m_2$, and $a_1$.  

Express your answer as a simplified analytic expression using the given variables. Do not substitute numerical values.

## Solution
**Step 1: Center of mass acceleration definition**  
The acceleration of the center of mass is determined solely by external forces:  
$$ \vec{a}_{\text{cm}} = \frac{\vec{F}_{\text{net, ext}}}{m_1 + m_2} $$  
Since the surface is frictionless and gravity acts vertically (perpendicular to motion), the only external force in the direction of motion is $\vec{F}$ applied to $m_1$. Thus:  
$$ \vec{F}_{\text{net, ext}} = \vec{F} $$  
$$ \vec{a}_{\text{cm}} = \frac{\vec{F}}{m_1 + m_2} \quad (1) $$  

**Step 2: Newton's second law for $m_1$**  
The rigid rod can only exert forces along its length. Since $\vec{F}$ is perpendicular to the rod, the rod exerts **no force component** on $m_1$ in the direction of $\vec{F}$. Therefore, the net force on $m_1$ in the direction of $\vec{F}$ is solely due to $\vec{F}$:  
$$ F = m_1 a_1 \quad (2) $$  

**Step 3: Relate $F$ to $a_{\text{cm}}$**  
Substitute Equation (2) into Equation (1):  
$$ \vec{a}_{\text{cm}} = \frac{m_1 a_1}{m_1 + m_2} $$  
The magnitude of the center of mass acceleration is therefore:  
$$ a_{\text{cm}} = \frac{m_1 a_1}{m_1 + m_2} $$  

**Key Insight**: Internal forces from the rod do not affect the center of mass motion. The rod transmits force to $m_2$, but this only alters individual accelerations, not $a_{\text{cm}}$.

## Answer
$$\boxed{\dfrac{m_{1} a_{1}}{m_{1} + m_{2}}}$$

------
## Problem 3
##### Background
Consider a thin, flexible wire bent into the shape of a semicircle with radius $R$. The wire has a uniform linear mass density, meaning each segment of equal length has the same mass. This semicircular wire is positioned in the $xy$-plane such that its straight edge lies along the $x$-axis from $(-R, 0)$ to $(R, 0)$, and the curved portion is in the upper half-plane ($y \geq 0$). The center of the semicircle is at the origin $(0, 0)$.

##### Knowledge Points Tested
1. Definition of center of mass for continuous mass distributions.
2. Application of symmetry to reduce dimensionality in physics problems.
3. Parametric representation of curves and integration in polar coordinates.
4. Use of trigonometric identities and definite integrals.

##### Intradisciplinary Connections
- **Mechanics**: Connects to rotational motion, as the center of mass is pivotal for analyzing torque and stability.
- **Calculus**: Demonstrates how integration sums infinitesimal contributions to determine bulk properties like mass distribution.
- **Geometry**: Relies on properties of circles and symmetry to simplify the problem.

##### Interdisciplinary Connections
- **Engineering**: Essential for designing stable arches, bridges, or any structure with curved elements where balance affects structural integrity.
- **Astronomy**: Relevant for calculating centers of mass in celestial bodies or orbital systems with symmetric mass distributions.
- **Robotics**: Used to determine balance points in robotic arms or components with curved trajectories.

##### Real-World Applications
- **Architecture**: Calculating the center of mass helps ensure the stability of semicircular arches in buildings.
- **Manufacturing**: Balancing rotating machinery parts (e.g., flywheels or gears) that incorporate semicircular segments.
- **Sports Science**: Analyzing the dynamics of equipment like archery bows or discus throwers where mass distribution impacts performance.

##### Problem Statement
Using the coordinate system described above, derive an expression for the perpendicular distance from the straight edge (the diameter along the $x$-axis) to the center of mass of the semicircular wire. Express your answer **symbolically** in terms of the radius $R$.  

**Answer Format Requirements:**  
- Your final answer must be an analytic expression using the variable $R$.  
- Use $\pi$ for the mathematical constant pi.  
- Do not substitute numerical values or constants.  
- Box your final answer as a single expression.

## Solution
**Step 1: Identify Symmetry and Coordinate System**  
By symmetry, the center of mass must lie on the $y$-axis (the perpendicular bisector of the straight edge). Thus, the $x$-coordinate of the center of mass is $0$, and we only need to compute the $y$-coordinate, denoted $Y_{\text{cm}}$.  

**Step 2: Define Mass Distribution**  
Let $\lambda$ be the uniform linear mass density (mass per unit length). The total length of the wire is half the circumference of a full circle:  
$$ L = \pi R. $$  
The total mass $M$ is:  
$$ M = \lambda L = \lambda \pi R. $$  

**Step 3: Parametrize the Wire**  
Consider a small segment of the wire subtending an angle $d\theta$ at the origin. The arc length $ds$ of this segment is:  
$$ ds = R  d\theta. $$  
The mass $dm$ of this segment is:  
$$ dm = \lambda  ds = \lambda R  d\theta. $$  
The segment is located at angle $\theta$ from the positive $x$-axis, so its Cartesian coordinates are:  
$$ x = R \cos \theta, \quad y = R \sin \theta, \quad \text{for } \theta \in [0, \pi]. $$  

**Step 4: Set Up the Integral for $Y_{\text{cm}}$**  
The $y$-coordinate of the center of mass is given by:  
$$ Y_{\text{cm}} = \frac{1}{M} \int y  dm. $$  
Substitute $y = R \sin \theta$ and $dm = \lambda R  d\theta$:  
$$ Y_{\text{cm}} = \frac{1}{M} \int_{0}^{\pi} (R \sin \theta) (\lambda R  d\theta) = \frac{\lambda R^{2}}{M} \int_{0}^{\pi} \sin \theta  d\theta. $$  

**Step 5: Evaluate the Integral**  
Compute the definite integral:  
$$ \int_{0}^{\pi} \sin \theta  d\theta = \Big[ -\cos \theta \Big]_{0}^{\pi} = (-\cos \pi) - (-\cos 0) = -(-1) - (-1) = 1 + 1 = 2. $$  

**Step 6: Substitute and Simplify**  
Insert the integral result and the expression for $M$:  
$$ Y_{\text{cm}} = \frac{\lambda R^{2}}{M} \cdot 2 = \frac{\lambda R^{2} \cdot 2}{\lambda \pi R} = \frac{2 R^{2}}{\pi R} = \frac{2R}{\pi}. $$  

**Conclusion:**  
The perpendicular distance from the straight edge ($x$-axis) to the center of mass is $\frac{2R}{\pi}$.

## Answer
$$\boxed{\dfrac{2R}{\pi}}$$

------
# combined gas law applications

## Problem 0
##### Background
A student is studying the behavior of a helium-filled balloon. The balloon starts at sea level with an initial volume $ V_i $ at an absolute pressure $ P_i $ and an absolute temperature $ T_i $ (measured in Kelvin). The student then carries the balloon to the top of a mountain. At the mountaintop, the pressure is $ P_1 $ and the temperature is $ T_1 $ (also in Kelvin), and the balloon's volume becomes $ V_1 $. The student then descends back to sea level, where the pressure returns to $ P_i $. However, during the descent, the balloon warms up and reaches a temperature $ T_2 $ (in Kelvin) at sea level.

##### Knowledge Points Tested
- Application of the combined gas law in multi-step processes
- Understanding of absolute temperature in gas laws
- Algebraic manipulation of state variables (pressure, volume, temperature)
- Path independence in ideal gas state changes

##### Intradisciplinary Connections
- Relates to Boyle's law (pressure-volume relationship at constant temperature)
- Connects to Charles's law (volume-temperature relationship at constant pressure)
- Reinforces the ideal gas law framework $ \frac{PV}{T} = \text{constant} $

##### Interdisciplinary Connections
- **Meteorology**: Atmospheric pressure and temperature variations with altitude
- **Engineering**: Design of altitude-sensitive instruments like weather balloons
- **Earth Science**: Thermal dynamics of air masses during vertical displacement

##### Real-World Applications
Weather balloons experience similar pressure and temperature changes during ascent and descent. Accurately predicting volume changes is critical for flight stability and data collection. This principle also applies to:
- Scuba diving air tanks during decompression
- Aircraft cabin pressure regulation systems
- High-altitude scientific payloads

##### Problem Statement
Starting from the initial conditions at sea level (volume $ V_i $, pressure $ P_i $, temperature $ T_i $), the balloon is taken to the mountaintop (pressure $ P_1 $, temperature $ T_1 $) and then brought back to sea level (pressure $ P_i $) with a final temperature $ T_2 $. Derive an expression for the final volume $ V_2 $ of the balloon at sea level using only the parameters $ V_i $, $ T_i $, and $ T_2 $. Explicitly show how intermediate parameters cancel out during derivation.  
**Answer Format Requirement**: Express your final answer as a single analytic expression using only the specified variables. Use $ T_i $ for initial temperature and $ T_2 $ for final temperature.

## Solution
### Step 1: Analyze the ascent (sea level to mountaintop)  
Apply the combined gas law between initial state (i) and mountaintop state (1):  
$$ \frac{P_i V_i}{T_i} = \frac{P_1 V_1}{T_1} $$  
Solve for the mountaintop volume $ V_1 $:  
$$ V_1 = \frac{P_i V_i T_1}{P_1 T_i} \quad \text{(Equation 1)} $$  

### Step 2: Analyze the descent (mountaintop to sea level)  
Apply the combined gas law between mountaintop state (1) and final state (2):  
$$ \frac{P_1 V_1}{T_1} = \frac{P_i V_2}{T_2} $$  
Solve for the final volume $ V_2 $:  
$$ V_2 = \frac{P_1 V_1 T_2}{P_i T_1} \quad \text{(Equation 2)} $$  

### Step 3: Substitute and simplify  
Substitute Equation 1 into Equation 2:  
$$ V_2 = \frac{P_1}{P_i T_1} \cdot T_2 \cdot \left( \frac{P_i V_i T_1}{P_1 T_i} \right) $$  
Cancel common factors:  
- $ P_1 $ in numerator and denominator  
- $ P_i $ in numerator and denominator  
- $ T_1 $ in numerator and denominator  
This simplifies to:  
$$ V_2 = \frac{V_i T_2}{T_i} $$  

### Key observation  
The parameters $ P_1 $, $ P_i $, and $ T_1 $ cancel out, demonstrating that the final volume depends only on:  
- Initial volume $ V_i $  
- Ratio of final to initial absolute temperature $ \frac{T_2}{T_i} $  
This occurs because pressure returns to its initial value $ P_i $, eliminating net pressure effects.

## Answer
$$\boxed{\dfrac{V_i T_2}{T_i}}$$

------
## Problem 1
##### Background
In deep-sea hydrothermal vents, gas bubbles are released from the Earth's crust into the ocean. These bubbles rise through the water column, expanding due to decreasing pressure and changing temperature. Understanding this expansion is critical for predicting gas release in marine environments, volcanic activity monitoring, and diver safety protocols. This problem examines a gas bubble rising from a hydrothermal vent to the ocean surface under idealized conditions.

##### Knowledge Points Tested
- Application of the combined gas law for an ideal gas with constant moles.
- Conversion of temperature to absolute scale (Kelvin) for thermodynamic equations.
- Algebraic manipulation to derive an expression for a final state variable.

##### Intradisciplinary Connections
Connects to fluid statics (pressure-depth relationship), thermodynamics (ideal gas behavior), and oceanography (properties of seawater at depth). Reinforces the interdependence of pressure, volume, and temperature in gaseous systems.

##### Interdisciplinary Connections
- **Chemistry**: Gas laws and mole conservation.
- **Earth Science**: Hydrothermal vent dynamics and deep-ocean pressure gradients.
- **Engineering**: Applications in submersible design and decompression modeling.

##### Real-World Applications
- Predicting gas volume changes in underwater volcanic eruptions.
- Modeling decompression sickness risk in scuba diving.
- Designing containment systems for underwater methane seeps.

##### Problem Statement
A gas bubble is released from a hydrothermal vent at an ocean depth where the absolute pressure is $P_i$, the absolute temperature is $T_i$, and the bubble volume is $V_i$. The bubble rises adiabatically and quickly to the surface, where the absolute pressure is $P_f$ and the absolute temperature is $T_f$. Assume the gas behaves ideally and the amount of gas (number of moles) remains constant. Derive an expression for the volume of the bubble at the surface, $V_f$, in terms of $P_i$, $V_i$, $T_i$, $P_f$, and $T_f$.

## Solution
The combined gas law governs the relationship between pressure, volume, and temperature for a fixed amount of ideal gas:

$$
\frac{P_i V_i}{T_i} = \frac{P_f V_f}{T_f}
$$

This equation holds because the number of moles $n$ is constant, and the ideal gas law ($PV = nRT$) implies that $PV/T$ remains constant when $n$ and $R$ are invariant.

Solving for the final volume $V_f$:
1. Rearrange the equation to isolate $V_f$:
   
$$
   P_i V_i T_f = P_f V_f T_i
   $$

2. Divide both sides by $P_f T_i$:
   
$$
   V_f = \frac{P_i V_i T_f}{P_f T_i}
   $$

The derived expression for the bubble's volume at the surface is $\dfrac{P_i V_i T_f}{P_f T_i}$.

## Answer
$$\boxed{\dfrac{P_i V_i T_f}{P_f T_i}}$$

------
## Problem 2
##### Background  
Car tires are made of rubber, which expands when heated due to its coefficient of volume expansion. The air inside the tire behaves as an ideal gas, so pressure, volume, and temperature changes follow the combined gas law. Gauge pressure (the pressure read on a tire gauge) is the difference between the absolute pressure inside the tire and the atmospheric pressure.

##### Knowledge Points Tested  
1. Conversion between Celsius and Kelvin for gas law applications.  
2. Thermal volume expansion: $V_2 = V_1 [1 + \beta (T_2 - T_1)]$, where $\beta$ is the coefficient of volume expansion.  
3. Combined gas law for an ideal gas: $\frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}$.  
4. Relationship between absolute pressure ($P_{\text{abs}}$), gauge pressure ($P_g$), and atmospheric pressure ($P_{\text{atm}}$): $P_{\text{abs}} = P_g + P_{\text{atm}}$.  

##### Intradisciplinary Connections  
This problem integrates thermal expansion (solids) with gas laws (thermodynamics), illustrating how temperature affects both the container and the contained gas simultaneously.  

##### Interdisciplinary Connections  
The principles apply to automotive engineering (tire safety), materials science (properties of rubber), and thermodynamics (ideal gas behavior).  

##### Real-World Applications  
Proper tire inflation is critical for vehicle safety, fuel efficiency, and tire longevity. Temperature changes cause pressure variations, which can lead to underinflation (increasing rolling resistance) or overinflation (reducing traction and risking blowouts).  

##### Problem Statement  
A car tire is inflated to a gauge pressure of 35.0 psi at an initial temperature of 20.0°C. The atmospheric pressure is 14.7 psi. The temperature rises to 45.0°C, and the tire's volume expands due to the rubber's coefficient of volume expansion $\beta = 1.20 \times 10^{-3} \ \text{°C}^{-1}$. Calculate the new gauge pressure in psi.  

Express your answer to three significant figures. Provide only the numerical value (without units) in your final answer.

## Solution
**Step 1: Convert temperatures to Kelvin**  
Temperatures must be in Kelvin for the gas law:  
- Initial temperature: $T_1 = 20.0 + 273.15 = 293.15 \ \text{K}$  
- Final temperature: $T_2 = 45.0 + 273.15 = 318.15 \ \text{K}$  

**Step 2: Calculate initial absolute pressure**  
Absolute pressure includes atmospheric pressure:  

$$
P_{1,\text{abs}} = P_{g1} + P_{\text{atm}} = 35.0 + 14.7 = 49.7 \ \text{psi}
$$


**Step 3: Determine volume expansion**  
The final volume $V_2$ is given by the thermal expansion formula:  

$$
V_2 = V_1 \left[1 + \beta (T_2^\circ - T_1^\circ)\right]
$$
  
where $T_2^\circ - T_1^\circ = 45.0 - 20.0 = 25.0 \ \text{°C}$. Substitute $\beta$:  

$$
\frac{V_2}{V_1} = 1 + (1.20 \times 10^{-3}) \times 25.0 = 1 + 0.0300 = 1.0300
$$


**Step 4: Apply the combined gas law**  
For a fixed amount of gas:  

$$
\frac{P_{1,\text{abs}} V_1}{T_1} = \frac{P_{2,\text{abs}} V_2}{T_2}
$$
  
Solve for the final absolute pressure $P_{2,\text{abs}}$:  

$$
P_{2,\text{abs}} = P_{1,\text{abs}} \cdot \frac{V_1}{V_2} \cdot \frac{T_2}{T_1} = 49.7 \times \frac{1}{1.0300} \times \frac{318.15}{293.15}
$$


**Step 5: Compute numerical value**  
First, calculate $\frac{318.15}{293.15} \approx 1.08545045$.  
Then, $\frac{1}{1.0300} \approx 0.9708737864$.  
Multiply:  

$$
49.7 \times 0.9708737864 \times 1.08545045 \approx 49.7 \times 1.053759 \approx 52.371 \ \text{psi}
$$
  
(Using intermediate steps: $49.7 \times 0.9708737864 = 48.252427$, then $48.252427 \times 1.08545045 \approx 52.371$.)  

**Step 6: Find new gauge pressure**  

$$
P_{g2} = P_{2,\text{abs}} - P_{\text{atm}} = 52.371 - 14.7 = 37.671 \ \text{psi}
$$
  
Round to three significant figures: **37.7 psi**.

## Answer
$$\boxed{37.7}$$

------
# conservation law applications

## Problem 0
##### Background
In many real-world scenarios, objects move along inclined surfaces that are not fixed. For example, consider a block sliding down a wedge-shaped incline that can freely move on a frictionless horizontal surface. This situation requires analyzing the motion of both the block and the incline using fundamental principles of physics, such as conservation laws. Understanding this system is crucial in mechanical engineering applications, including conveyor systems and amusement park rides.

##### Knowledge Points Tested
- Conservation of mechanical energy
- Conservation of momentum
- Vector decomposition of velocity
- Relative motion in two dimensions

##### Intradisciplinary Connections
This problem connects to Newton's laws of motion by illustrating how constraints and forces influence motion. It also reinforces the concept that energy conservation provides a powerful tool for solving complex dynamics problems without detailed force analysis.

##### Interdisciplinary Connections
The principles involved are foundational in mechanical engineering for designing systems with moving components. In robotics, similar analyses are used for trajectory planning of objects on articulated platforms.

##### Real-World Applications
Understanding the motion of objects on movable inclines is essential in designing safety mechanisms for roller coasters, optimizing material transport on mobile ramps in warehouses, and modeling geological events like landslides on подвижные платформы.

##### Problem Statement
A wedge-shaped incline of mass $M$ is placed on a horizontal frictionless surface. The incline makes an angle $\theta$ with the horizontal. A block of mass $m$ is placed on the frictionless incline and released from rest at a vertical height $h$ above the horizontal surface. Derive an expression for the speed of the block relative to the ground when it reaches the bottom of the incline. Use conservation of energy and momentum principles. Express your answer in terms of $m$, $M$, $g$, $h$, and $\theta$.

## Solution
#### Step 1: Conservation of Horizontal Momentum  
The system starts at rest, so initial horizontal momentum is zero. No external horizontal forces act on the system, so horizontal momentum is conserved. Let $V$ be the speed of the wedge to the left (negative x-direction) when the block reaches the bottom. Let $v_x$ and $v_y$ be the horizontal and vertical components of the block's velocity (with $v_y$ negative since the block moves down). Conservation of horizontal momentum gives:  
$$ m v_x + M (-V) = 0 \implies m v_x = M V \quad (1) $$  

#### Step 2: Relative Velocity Components  
The block moves along the incline, so its velocity relative to the wedge is tangential to the surface. Let $u$ be the speed of the block relative to the wedge. The components of the block's velocity relative to the ground are:  
- Horizontal: $v_x = u \cos\theta - V$ (relative horizontal component minus wedge's velocity)  
- Vertical: $v_y = -u \sin\theta$ (negative for downward motion)  
Substituting into equation (1):  
$$ m (u \cos\theta - V) = M V \implies m u \cos\theta = (M + m) V \implies V = \frac{m u \cos\theta}{M + m} \quad (2) $$  

#### Step 3: Conservation of Mechanical Energy  
Initial mechanical energy is the gravitational potential energy of the block: $m g h$. Final mechanical energy is the kinetic energy of both objects. Using equation (2) for $V$ and the velocity components:  
- Wedge's kinetic energy: $\frac{1}{2} M V^2 = \frac{1}{2} M \left( \frac{m u \cos\theta}{M + m} \right)^2$  
- Block's kinetic energy: $\frac{1}{2} m (v_x^2 + v_y^2) = \frac{1}{2} m \left[ (u \cos\theta - V)^2 + (-u \sin\theta)^2 \right] = \frac{1}{2} m (u^2 - 2 u V \cos\theta + V^2)$  
Total final kinetic energy:  
$$ \frac{1}{2} M \left( \frac{m u \cos\theta}{M + m} \right)^2 + \frac{1}{2} m (u^2 - 2 u V \cos\theta + V^2) $$  
Set equal to initial energy:  
$$ m g h = \frac{1}{2} M \left( \frac{m u \cos\theta}{M + m} \right)^2 + \frac{1}{2} m (u^2 - 2 u V \cos\theta + V^2) $$  
Substitute $V$ from equation (2) and multiply both sides by 2:  
$$ 2 m g h = M \left( \frac{m^2 u^2 \cos^2\theta}{(M + m)^2} \right) + m \left[ u^2 - 2 u \left( \frac{m u \cos\theta}{M + m} \right) \cos\theta + \left( \frac{m u \cos\theta}{M + m} \right)^2 \right] $$  
Simplify the expression in brackets:  
$$ u^2 - \frac{2 m u^2 \cos^2\theta}{M + m} + \frac{m^2 u^2 \cos^2\theta}{(M + m)^2} $$  
Combine all terms:  
$$ 2 m g h = \frac{M m^2 u^2 \cos^2\theta}{(M + m)^2} + m u^2 - \frac{2 m^2 u^2 \cos^2\theta}{M + m} + \frac{m^3 u^2 \cos^2\theta}{(M + m)^2} $$  
Factor $u^2$:  
$$ 2 m g h = u^2 \left[ \frac{M m^2 \cos^2\theta}{(M + m)^2} + m - \frac{2 m^2 \cos^2\theta}{M + m} + \frac{m^3 \cos^2\theta}{(M + m)^2} \right] $$  
Combine the $\cos^2\theta$ terms:  
$$ u^2 \left[ m + \cos^2\theta \left( \frac{M m^2 + m^3}{(M + m)^2} - \frac{2 m^2}{M + m} \right) \right] = u^2 \left[ m + \cos^2\theta \left( \frac{m^2 (M + m)}{(M + m)^2} - \frac{2 m^2}{M + m} \right) \right] $$  
Simplify:  
$$ u^2 \left[ m + \cos^2\theta \left( \frac{m^2}{M + m} - \frac{2 m^2}{M + m} \right) \right] = u^2 \left[ m - \frac{m^2 \cos^2\theta}{M + m} \right] = u^2 m \left[ 1 - \frac{m \cos^2\theta}{M + m} \right] $$  
$$ = u^2 m \left[ \frac{M + m - m \cos^2\theta}{M + m} \right] = u^2 m \left[ \frac{M + m \sin^2\theta}{M + m} \right] $$  
Solve for $u^2$:  
$$ 2 m g h = u^2 m \frac{M + m \sin^2\theta}{M + m} \implies u^2 = \frac{2 g h (M + m)}{M + m \sin^2\theta} \quad (3) $$  

#### Step 4: Speed of the Block Relative to Ground  
The speed $v$ of the block is the magnitude of its velocity vector:  
$$ v = \sqrt{v_x^2 + v_y^2} = \sqrt{ (u \cos\theta - V)^2 + (-u \sin\theta)^2 } = \sqrt{ u^2 \cos^2\theta - 2 u V \cos\theta + V^2 + u^2 \sin^2\theta } = \sqrt{ u^2 + V^2 - 2 u V \cos\theta } $$  
Substitute $V$ from equation (2):  
$$ v = \sqrt{ u^2 + \left( \frac{m u \cos\theta}{M + m} \right)^2 - 2 u \left( \frac{m u \cos\theta}{M + m} \right) \cos\theta } = u \sqrt{ 1 + \frac{m^2 \cos^2\theta}{(M + m)^2} - \frac{2 m \cos^2\theta}{M + m} } $$  
Simplify the expression under the square root:  
$$ 1 - \frac{2 m \cos^2\theta}{M + m} + \frac{m^2 \cos^2\theta}{(M + m)^2} = \frac{ (M + m)^2 - 2 m (M + m) \cos^2\theta + m^2 \cos^2\theta }{(M + m)^2} $$  
The numerator is:  
$$ (M + m)^2 - 2 m (M + m) \cos^2\theta + m^2 \cos^2\theta = M^2 + 2 M m + m^2 - 2 m M \cos^2\theta - 2 m^2 \cos^2\theta + m^2 \cos^2\theta = M^2 + 2 M m + m^2 - 2 m M \cos^2\theta - m^2 \cos^2\theta $$  
Recognize that $M^2 + 2 M m + m^2 = (M + m)^2$, and group:  
$$ (M + m)^2 - 2 m M \cos^2\theta - m^2 \cos^2\theta = M^2 + 2 M m (1 - \cos^2\theta) + m^2 (1 - \cos^2\theta) = M^2 + 2 M m \sin^2\theta + m^2 \sin^2\theta = M^2 + m (2 M + m) \sin^2\theta $$  
Thus,  
$$ v = u \sqrt{ \frac{ M^2 + m (2 M + m) \sin^2\theta }{(M + m)^2} } $$  
Substitute $u^2$ from equation (3):  
$$ v = \sqrt{ \frac{2 g h (M + m)}{M + m \sin^2\theta} } \cdot \sqrt{ \frac{ M^2 + m (2 M + m) \sin^2\theta }{(M + m)^2} } = \sqrt{ \frac{2 g h (M + m)}{M + m \sin^2\theta} \cdot \frac{ M^2 + m (2 M + m) \sin^2\theta }{(M + m)^2} } $$  
Simplify:  
$$ v = \sqrt{ \frac{2 g h \left[ M^2 + m (2 M + m) \sin^2\theta \right] }{ (M + m) (M + m \sin^2\theta) } } $$  
This is the speed of the block relative to the ground.

## Answer
$$\boxed{\sqrt{\frac{2gh\left(M^{2} + m\left(2M + m\right)\sin^{2}\theta\right)}{\left(M + m\right)\left(M + m\sin^{2}\theta\right)}}}$$

------
## Problem 1
##### Background  
In real-world applications, springs often have non-negligible mass, which affects the dynamics of launched objects. Consider a spring-powered device where a spring (spring constant $k$, total mass $M$, uniformly distributed along its length) is attached to a fixed wall at one end and to a block of mass $m$ at the other end. The system rests on a frictionless horizontal surface. When the spring is compressed by a distance $x$ from its equilibrium length and released, both the block and the spring itself gain kinetic energy. To model this, the spring's kinetic energy can be approximated as equivalent to that of a point mass $M/3$ moving at the same speed as the block's endpoint.  

##### Knowledge Points Tested  
- Conservation of mechanical energy  
- Spring potential energy ($\frac{1}{2}kx^2$)  
- Kinetic energy of distributed mass systems (effective mass model)  

##### Intradisciplinary Connections  
- Relates to simple harmonic motion by extending energy conservation to non-ideal springs.  
- Connects to center-of-mass dynamics through the effective mass approximation.  

##### Interdisciplinary Connections  
- **Mechanical engineering**: Accurate modeling of spring-mass systems is essential in vehicle suspensions and mechanical launchers.  
- **Materials science**: Understanding how material distribution affects energy transfer in elastic systems.  

##### Real-World Applications  
- Toy dart guns: Spring mass reduces projectile speed compared to ideal massless models.  
- Industrial machinery: Compression springs in actuators must account for self-mass to predict force output.  

##### Problem Statement  
Using the effective mass model described, derive an expression for the speed $v$ of the block at the exact moment the spring returns to its equilibrium length. Express $v$ in terms of $k$, $m$, $M$, and $x$.

## Solution
**Step 1: Initial energy**  
When compressed by distance $x$, the spring stores potential energy. The block and spring are at rest, so initial kinetic energy is zero. Total initial mechanical energy is:  
$$ E_i = \frac{1}{2} k x^2 $$  

**Step 2: Final energy**  
At equilibrium length, spring potential energy is zero. The block (mass $m$) moves at speed $v$, so its kinetic energy is $\frac{1}{2} m v^2$. The spring (mass $M$) has kinetic energy equivalent to a point mass $M/3$ moving at speed $v$, so its kinetic energy is $\frac{1}{2} \left( \frac{M}{3} \right) v^2$. Total final mechanical energy is:  
$$ E_f = \frac{1}{2} m v^2 + \frac{1}{2} \left( \frac{M}{3} \right) v^2 = \frac{1}{2} v^2 \left( m + \frac{M}{3} \right) $$  

**Step 3: Apply conservation of energy**  
Mechanical energy is conserved (frictionless surface, no non-conservative forces):  
$$ E_i = E_f $$  
$$ \frac{1}{2} k x^2 = \frac{1}{2} v^2 \left( m + \frac{M}{3} \right) $$  

**Step 4: Solve for $v$**  
Multiply both sides by 2:  
$$ k x^2 = v^2 \left( m + \frac{M}{3} \right) $$  
Rewrite the denominator:  
$$ m + \frac{M}{3} = \frac{3m + M}{3} $$  
Substitute and solve for $v^2$:  
$$ k x^2 = v^2 \left( \frac{3m + M}{3} \right) $$  
$$ v^2 = \frac{3k x^2}{3m + M} $$  
Take the square root (positive value for speed):  
$$ v = \sqrt{ \frac{3k x^2}{3m + M} } = x \sqrt{ \frac{3k}{3m + M} } $$

## Answer
$$\boxed{ x \sqrt{ \frac{3k}{3m + M} } }$$

------
## Problem 2
##### Background
In a physics laboratory experiment, two carts are placed on a frictionless linear track. Cart A has mass $2m$ and moves with initial speed $v$, while Cart B has mass $3m$ and moves with initial speed $2v$. The carts are directed toward each other along the same straight line. When they collide, they lock together due to a Velcro attachment, forming a single combined object. This scenario models a perfectly inelastic collision, where kinetic energy is not conserved, but momentum is conserved due to the absence of external forces.

##### Knowledge Points Tested
- Conservation of linear momentum in one dimension
- Analysis of perfectly inelastic collisions
- Vector nature of velocity and momentum (with directional signs)
- Algebraic manipulation of equations involving mass and velocity

##### Intradisciplinary Connections
- Relates to Newton's laws of motion (specifically, the conservation of momentum derived from Newton's third law)
- Connects to work-energy theorem (contrasting inelastic collisions with elastic ones where kinetic energy is conserved)

##### Interdisciplinary Connections
- Engineering: Vehicle crash-test analysis, where cars deform and stick together
- Astronomy: Modeling collisions of celestial bodies in simplified one-dimensional approximations
- Transportation: Designing coupling mechanisms for trains or rail carts

##### Real-World Applications
- Automotive safety testing: Crash simulations measure post-collision velocities to assess safety systems
- Rail transport: Coupling of train cars uses inelastic collisions to minimize jolts
- Sports: Analyzing collisions in contact sports like football or hockey

##### Problem Statement
Define the positive direction as the initial direction of motion of Cart A (mass $2m$). Cart B (mass $3m$) moves in the opposite direction. The carts undergo a perfectly inelastic collision. Derive an expression for the velocity of the combined carts after the collision. Express your answer symbolically in terms of the initial speed $v$. Use a positive sign for motion in Cart A's initial direction and a negative sign for the opposite direction. Provide the final velocity as a simplified fraction.

## Solution
### Step 1: Define the Coordinate System and Initial Conditions
- Assign the positive direction as the initial direction of Cart A.
- Cart A: Mass = $2m$, initial velocity = $+v$
- Cart B: Mass = $3m$, initial velocity = $-2v$ (since it moves opposite to Cart A)

### Step 2: Apply Conservation of Momentum
The total momentum before the collision equals the total momentum after the collision because no external forces act on the system. For a perfectly inelastic collision, both carts move together with a common final velocity $V_f$.  

$$
\text{Total initial momentum} = \text{Total final momentum}
$$


$$
(m_A \cdot v_A) + (m_B \cdot v_B) = (m_A + m_B) \cdot V_f
$$


### Step 3: Substitute Known Values

$$
(2m \cdot v) + (3m \cdot (-2v)) = (2m + 3m) \cdot V_f
$$


### Step 4: Simplify the Equation

$$
(2m \cdot v) + (3m \cdot -2v) = 5m \cdot V_f
$$


$$
2mv - 6mv = 5m V_f
$$


$$
-4mv = 5m V_f
$$


### Step 5: Solve for $V_f$
Divide both sides by $m$ (since $m \neq 0$):  

$$
-4v = 5 V_f
$$


$$
V_f = -\frac{4v}{5}
$$


### Step 6: Interpret the Result
The negative sign indicates the combined velocity is in the direction opposite to Cart A's initial motion (i.e., in Cart B's initial direction). The magnitude is $\frac{4}{5}v$.

## Answer
$$\boxed{-\dfrac{4v}{5}}$$

------
## Problem 3
##### Background
Consider a pendulum system where the pivot is not fixed but mounted on a cart of mass $M$ that can move without friction along a horizontal track. The pendulum bob, of mass $m$, is attached to the cart by a massless, inextensible string of length $L$. Initially, the system is at rest with the string held horizontally. When released, the pendulum swings downward while the cart moves horizontally. This setup introduces additional dynamics because the cart's motion affects the pendulum's energy transformation.

##### Knowledge Points Tested
- Conservation of mechanical energy (gravitational potential to kinetic energy)
- Conservation of linear momentum (horizontal direction)
- Constrained motion analysis
- Energy partitioning in multi-body systems

##### Intradisciplinary Connections
Connects to rotational dynamics (pendulum motion), work-energy theorem, and impulse-momentum principles. Reinforces understanding that mechanical energy conservation holds when non-conservative forces do no work, and momentum conservation applies in the absence of external horizontal forces.

##### Interdisciplinary Connections
Relates to robotics (mobile-base manipulators), vehicle dynamics (cargo stabilization), and biomechanics (gait analysis where limbs act as pendulums on a moving torso). Demonstrates how physics principles underpin control systems in engineering.

##### Real-World Applications
- Inertial propulsion prototypes where pendulum-cart systems convert swinging motion into directed linear momentum.
- Seismic isolation systems in structures, where pendulums dampen horizontal motion.
- Energy-harvesting devices that capture kinetic energy from pendulum motion on moving platforms.

##### Problem Statement
A pendulum bob of mass $m$ is attached by a string of length $L$ to a cart of mass $M$. The cart moves without friction on a horizontal track. Initially, the system is at rest with the string horizontal. The bob is released from this position.  
Using conservation laws, derive an expression for the speed of the bob when it reaches its lowest point (where the string is vertical). Express your answer in terms of $m$, $M$, $L$, and $g$ (acceleration due to gravity).  

##### Answer Format Instructions
- Provide a **single analytic expression** using the variables $m$, $M$, $L$, and $g$.
- Use multiplication operators (e.g., $2 \times g \times L$) or implied multiplication (e.g., $2gL$) consistently.
- Square roots must be written as $\sqrt{...}$.
- No numerical substitutions or unit conversions are needed.

## Solution
**Step 1: Apply conservation of horizontal momentum.**  
Since no external horizontal forces act on the system, the total horizontal momentum remains zero. At the lowest point:  
- Let $V$ = speed of cart (leftward).  
- Let $v_b$ = speed of bob (rightward).  
Conservation equation:  

$$
M V - m v_b = 0 \quad \Rightarrow \quad V = \frac{m}{M} v_b \quad \text{(1)}
$$


**Step 2: Apply conservation of mechanical energy.**  
Gravitational potential energy converts to kinetic energy. Assume the lowest point has zero potential energy.  
- Initial energy: $mgL$ (bob height = $L$ above lowest point).  
- Final energy: $\frac{1}{2} M V^2 + \frac{1}{2} m v_b^2$.  
Conservation equation:  

$$
mgL = \frac{1}{2} M V^2 + \frac{1}{2} m v_b^2 \quad \text{(2)}
$$


**Step 3: Substitute momentum equation into energy equation.**  
Replace $V$ from (1) into (2):  

$$
mgL = \frac{1}{2} M \left( \frac{m}{M} v_b \right)^2 + \frac{1}{2} m v_b^2 = \frac{1}{2} \frac{m^2}{M} v_b^2 + \frac{1}{2} m v_b^2
$$


**Step 4: Simplify and solve for $v_b$.**  
Factor $\frac{1}{2} m v_b^2$:  

$$
mgL = \frac{1}{2} m v_b^2 \left( \frac{m}{M} + 1 \right) = \frac{1}{2} m v_b^2 \left( \frac{m + M}{M} \right)
$$
  
Divide both sides by $m$:  

$$
gL = \frac{1}{2} v_b^2 \left( \frac{m + M}{M} \right)
$$
  
Solve for $v_b^2$:  

$$
v_b^2 = 2gL \left( \frac{M}{m + M} \right)
$$
  
Final speed:  

$$
v_b = \sqrt{ \frac{2gL M}{m + M} }
$$

## Answer
$$\boxed{\sqrt{\frac{2gLM}{m + M}}}$$

------
## Problem 4
##### Background
In forensic science and ballistics, determining the velocity of a projectile after impact is crucial for reconstructing events. When a bullet strikes and embeds itself in a stationary object, the combined system moves together due to conservation of momentum. This scenario models a perfectly inelastic collision, where kinetic energy is not conserved, but momentum is conserved because no external horizontal forces act on the system on a frictionless surface.

##### Knowledge Points Tested
1. Conservation of linear momentum in isolated systems.
2. Analysis of perfectly inelastic collisions.
3. Vector nature of momentum (one-dimensional case).

##### Intradisciplinary Connections
- Connects to work-energy theorem (kinetic energy loss during collision).
- Relates to impulse-momentum theorem for force analysis during impact.

##### Interdisciplinary Connections
- Engineering: Crash-test simulations and vehicle safety design.
- Forensic science: Reconstructing bullet trajectories and impact velocities.

##### Real-World Applications
- Ballistic pendulums for measuring bullet speeds.
- Automotive collision analysis (e.g., stuck debris in moving vehicles).
- Spacecraft docking maneuvers where objects couple together.

##### Problem Statement
A bullet of mass $m$ is fired horizontally with initial speed $v$ at a stationary block of mass $M$ resting on a frictionless surface. The bullet embeds completely in the block, and the system moves as a single unit after the collision. Derive an expression for the final velocity $V$ of the block-bullet system. Express $V$ symbolically in terms of $m$, $M$, and $v$.

## Solution
**Step 1: Identify the conservation principle**  
Since the surface is frictionless and no external horizontal forces act on the bullet-block system during the collision, the total linear momentum is conserved. The vertical forces (gravity and normal force) are balanced and do not affect horizontal momentum.

**Step 2: Define initial and final states**  
- **Initial state** (before collision):  
  - Bullet momentum: $m \cdot v$ (horizontal direction).  
  - Block momentum: $M \cdot 0 = 0$ (stationary).  
  Total initial momentum: $p_{\text{initial}} = mv$.  

- **Final state** (after collision):  
  Combined mass of system: $m + M$.  
  Let $V$ be the final velocity of the combined system.  
  Total final momentum: $p_{\text{final}} = (m + M)V$.

**Step 3: Apply conservation of momentum**  

$$
p_{\text{initial}} = p_{\text{final}}
$$
  

$$
mv = (m + M)V
$$


**Step 4: Solve for $V$**  

$$
V = \frac{mv}{m + M}
$$


**Conclusion**  
The final velocity of the block-bullet system is $\frac{mv}{m + M}$. This expression shows that $V$ is always less than $v$ (since $m + M > m$), consistent with the bullet transferring momentum to a larger mass.

## Answer
\[
\boxed{\dfrac{mv}{m + M}}
\]

------
## Problem 5
##### Background
Roller coasters rely on gravitational potential energy to navigate loops safely. The key to a successful loop is ensuring the car maintains sufficient speed at the top to stay on the track. This problem investigates the minimum starting height required for a frictionless roller coaster car to complete a vertical loop without falling, using fundamental principles of energy conservation and circular motion.

##### Knowledge Points Tested
1. **Conservation of mechanical energy**: Total mechanical energy (kinetic + potential) remains constant in the absence of friction.
2. **Centripetal force**: The net force toward the center of circular motion, given by $m v^2 / r$.
3. **Newton's second law**: Applied to the forces at the top of the loop to establish the critical speed condition.

##### Intradisciplinary Connections
- Connects work-energy concepts (potential and kinetic energy transformations) with rotational dynamics (circular motion constraints).
- Reinforces the relationship between force, acceleration, and energy in conservative systems.

##### Interdisciplinary Connections
- **Engineering**: Critical for designing safe roller coasters and other loop-based rides.
- **Astrophysics**: Similar principles apply to orbital mechanics, where gravitational force provides centripetal acceleration.

##### Real-World Applications
- Roller coaster design: Ensures passenger safety by preventing cars from derailing at the top of loops.
- Amusement park safety standards: Regulatory calculations for minimum drop heights based on loop dimensions.

##### Problem Statement
A roller coaster car of mass $m$ starts from rest at an initial height $H$ above the ground. It slides without friction down a track and enters a vertical circular loop of radius $R$. Derive the expression for the **minimum initial height $H_{\text{min}}$** (in terms of $R$) required for the car to complete the loop without losing contact with the track.  

**Constraints**:  
- Use $g$ for the acceleration due to gravity.  
- Express $H_{\text{min}}$ as a simplified fraction of $R$ (e.g., $\frac{a}{b} R$ where $a$ and $b$ are integers with no common factors).  

**Final Answer Format**:  
- Your answer must be an exact analytic expression in the form $\boxed{\dfrac{a}{b} R}$.  
- Do not substitute numerical values for $g$ or any constants.  
- Use the variable $R$ as specified.

## Solution
**Step 1: Apply conservation of energy**  
The initial mechanical energy (at height $H$) equals the mechanical energy at the top of the loop (height $2R$). With zero initial kinetic energy:  

$$
mgH = \frac{1}{2}mv^2 + mg(2R)
$$
  
Solve for the speed squared at the top of the loop ($v^2$):  

$$
mgH - 2mgR = \frac{1}{2}mv^2 \implies v^2 = 2g(H - 2R)
$$
  
**Equation (1)**: $v^2 = 2g(H - 2R)$

**Step 2: Analyze forces at the top of the loop**  
At the top of the loop, two forces act downward toward the center:  
- Gravitational force: $mg$  
- Normal force: $N$ (exerted by the track)  
The net force provides the centripetal acceleration:  

$$
mg + N = \frac{mv^2}{R}
$$
  
The car loses contact if $N < 0$. The critical case occurs when $N = 0$ (minimum speed to maintain contact):  

$$
mg = \frac{mv_{\text{min}}^2}{R} \implies v_{\text{min}}^2 = gR
$$
  
**Equation (2)**: $v_{\text{min}}^2 = gR$

**Step 3: Combine equations for minimum height**  
At $H = H_{\text{min}}$, the speed at the top is $v_{\text{min}}$. Substitute Equation (2) into Equation (1):  

$$
gR = 2g(H_{\text{min}} - 2R)
$$
  
Solve for $H_{\text{min}}$:  

$$
gR = 2gH_{\text{min}} - 4gR \implies 2gH_{\text{min}} = 5gR \implies H_{\text{min}} = \frac{5}{2}R
$$
  
**Conclusion**: The minimum initial height is $\frac{5}{2}R$.

## Answer
$$\boxed{\dfrac{5}{2}R}$$

------
# constructive and destructive thin film conditions

## Problem 0
##### Background
Thin film interference occurs when light reflects off the two surfaces of a thin layer, causing constructive or destructive interference based on the film's thickness, refractive index, and the light's wavelength and angle of incidence. Soap bubbles are a classic example, where the film has a higher refractive index than air on both sides. When light reflects off the air-film interface, it undergoes a 180° phase change due to the increase in refractive index. However, light reflecting off the film-air interface experiences no phase change. This phase difference must be accounted for in interference conditions.

##### Knowledge Points Tested
- Phase change upon reflection at interfaces
- Path difference and optical path length in thin films
- Snell's law for refraction at boundaries
- Conditions for constructive interference in thin films with symmetric refractive indices
- Minimization of thickness for the smallest non-trivial solution

##### Intradisciplinary Connections
This problem connects to wave optics (interference principles), geometric optics (Snell's law and refraction), and calculus (minimization of thickness). It also reinforces the concept of optical path length, which is fundamental in interferometry and diffraction.

##### Interdisciplinary Connections
Thin-film interference principles are applied in materials science (anti-reflective coatings, optical filters), engineering (design of semiconductor devices and photonic crystals), and biology (structural coloration in animal skins and feathers).

##### Real-World Applications
- **Optical Coatings:** Camera lenses use anti-reflective coatings designed via thin-film interference to minimize glare.
- **Quality Control:** Film thickness monitors in manufacturing rely on interference patterns to measure nanoscale thicknesses.
- **Consumer Products:** Soap bubbles and oil slicks demonstrate interference effects visible in everyday life.

##### Problem Statement
Consider a soap bubble film (refractive index $n$) suspended in air. Monochromatic light of vacuum wavelength $\lambda$ is incident on the film at an angle $\theta$ (in radians) from the normal. Derive an expression for the minimum thickness $d_{\text{min}}$ that results in constructive interference for the reflected light. Assume the refractive index of air is 1. Express your answer symbolically in terms of $\lambda$, $n$, and $\theta$. Use standard mathematical notation: trigonometric functions (e.g., $\sin$, $\cos$), exponents with carets (e.g., $a^{b}$), and fractions with \frac{}{}. Do not evaluate numerical constants.

## Solution
#### Step 1: Identify phase changes
- **First reflection (air-film interface):** Light moves from air (lower refractive index) to film (higher refractive index $n$), causing a **180° phase change**.  
- **Second reflection (film-air interface):** Light moves from film to air (lower refractive index), so **no phase change**.  
- **Net phase difference:** The two reflections have a relative phase difference of 180° ($\lambda/2$ path difference) due to reflection alone.

#### Step 2: Determine the condition for constructive interference
For constructive interference, the path difference must compensate for the phase difference. The optical path length difference for light traveling through the film is $2n d \cos\theta'$, where $\theta'$ is the angle of refraction inside the film.  
- **Phase difference due to path:** $2n d \cos\theta'$  
- **Total phase difference:** Combines the path difference and the 180° reflection phase difference.  
- **Constructive interference occurs when:**  
  $$2n d \cos\theta' = \left(m + \frac{1}{2}\right)\lambda \quad \text{for} \quad m = 0,1,2,\ldots$$  
  Here, $m$ is the order of interference. The term $\frac{1}{2}\lambda$ accounts for the net 180° phase change.

#### Step 3: Relate $\theta'$ to $\theta$ using Snell's law
Snell's law at the air-film interface:  
$$\sin\theta = n \sin\theta'$$  
Solve for $\cos\theta'$:  
$$\cos\theta' = \sqrt{1 - \sin^2\theta'} = \sqrt{1 - \frac{\sin^2\theta}{n^2}} = \frac{\sqrt{n^2 - \sin^2\theta}}{n}$$

#### Step 4: Substitute $\cos\theta'$ into the interference condition
Replace $\cos\theta'$ in the constructive interference equation:  
$$2n d \cdot \frac{\sqrt{n^2 - \sin^2\theta}}{n} = \left(m + \frac{1}{2}\right)\lambda$$  
Simplify:  
$$2 d \sqrt{n^2 - \sin^2\theta} = \left(m + \frac{1}{2}\right)\lambda$$

#### Step 5: Solve for minimum thickness $d_{\text{min}}$
The minimum thickness corresponds to the smallest integer $m$ that yields $d > 0$. For $m = 0$:  
$$2 d_{\text{min}} \sqrt{n^2 - \sin^2\theta} = \frac{\lambda}{2}$$  
Solve for $d_{\text{min}}$:  
$$d_{\text{min}} = \frac{\lambda}{4 \sqrt{n^2 - \sin^2\theta}}$$  
This is the minimum thickness for constructive interference.

## Answer
$$\boxed{\dfrac{\lambda}{4\sqrt{n^{2} - \sin^{2}{\theta}}}}$$

------
## Problem 1
##### Background
Thin film interference occurs when light waves reflect off the top and bottom surfaces of a thin layer, leading to constructive or destructive interference. This phenomenon explains the vibrant colors seen in oil slicks on water. When light reflects off a boundary, a phase change of $\pi$ radians (equivalent to a half-wavelength shift) occurs if the light travels from a medium with a lower refractive index to one with a higher refractive index. No phase change occurs if the light reflects off a boundary to a lower-index medium. For destructive interference in reflected light, the net phase difference between the two reflected waves must be an odd multiple of $\pi$.

##### Knowledge Points Tested
- Phase change upon reflection at an interface.
- Path difference and optical path length in thin films.
- Condition for destructive interference in reflected light.
- Relationship between vacuum wavelength and wavelength in a medium.

##### Intradisciplinary Connections
This problem connects to wave optics, specifically the superposition principle and interference conditions. It also relies on the concept of refractive index from geometric optics.

##### Interdisciplinary Connections
Thin film interference principles are used in materials science for designing anti-reflective coatings and in engineering for quality control of film thicknesses in manufacturing.

##### Real-World Applications
Anti-reflective coatings on camera lenses and eyeglasses use destructive interference to minimize reflections. Similarly, oil spill thickness can be monitored using interference patterns from aerial photography.

##### Problem Statement
An oil slick with refractive index $n_o$ floats on water with refractive index $n_w$. The refractive index of air is 1, and $n_o > n_w$. Monochromatic light of vacuum wavelength $\lambda$ is incident perpendicularly on the oil slick. Determine the minimum non-zero thickness $t_{\text{min}}$ of the oil slick that results in destructive interference for the reflected light. 

Express $t_{\text{min}}$ symbolically as an analytic expression in terms of $n_o$ and $\lambda$. Do not substitute numerical values or physical constants. Ensure your derivation accounts for phase changes and path difference.

## Solution
To find the minimum non-zero thickness $t_{\text{min}}$ for destructive interference in reflected light:

**Step 1: Identify phase changes at interfaces**
- **Air-oil interface**: Light travels from air (refractive index 1) to oil (refractive index $n_o > 1$). Since $1 < n_o$, reflection incurs a phase change of $\pi$.
- **Oil-water interface**: Light travels from oil ($n_o$) to water ($n_w$). Given $n_o > n_w$, reflection occurs from a higher to a lower refractive index, so no phase change occurs.

The net phase difference due to reflections is $\pi$ (only one phase change).

**Step 2: Calculate path difference**
The light ray entering the oil reflects off the oil-water interface and travels back through the oil. The path length difference is twice the thickness of the oil film, $2t$. Since the light travels in oil, the wavelength in oil is $\lambda_o = \lambda / n_o$. The optical path difference is $2n_o t$ (distance multiplied by refractive index).

**Step 3: Determine total phase difference**
The phase difference due to path length is $\delta_{\text{path}} = \frac{2\pi}{\lambda} \times \text{optical path difference} = \frac{2\pi}{\lambda} \times 2n_o t = \frac{4\pi n_o t}{\lambda}$.  
Adding the net reflection phase change of $\pi$, the total phase difference is:

$$
\delta = \delta_{\text{path}} + \pi = \frac{4\pi n_o t}{\lambda} + \pi.
$$


**Step 4: Apply destructive interference condition**
Destructive interference occurs when the total phase difference is an odd multiple of $\pi$:

$$
\delta = (2m+1)\pi, \quad m = 0, 1, 2, \ldots
$$

Substitute $\delta$:

$$
\frac{4\pi n_o t}{\lambda} + \pi = (2m+1)\pi
$$

Divide both sides by $\pi$:

$$
\frac{4 n_o t}{\lambda} + 1 = 2m+1
$$

Solve for $t$:

$$
\frac{4 n_o t}{\lambda} = 2m
$$


$$
t = \frac{2m \lambda}{4 n_o} = \frac{m \lambda}{2 n_o}
$$

The thickness $t$ must be positive. The smallest non-zero $t$ occurs when $m = 1$:

$$
t_{\text{min}} = \frac{(1) \lambda}{2 n_o} = \frac{\lambda}{2 n_o}
$$


The minimum non-zero thickness for destructive interference is $\frac{\lambda}{2 n_o}$.

## Answer
$$\boxed{\dfrac{\lambda}{2n_{o}}}$$

------
## Problem 2
##### Background
Anti-reflective coatings on optical lenses minimize reflection by exploiting destructive interference in thin films. Consider a thin film of material with refractive index $n_f$ and uniform thickness $d$ deposited on a glass substrate with refractive index $n_g$. The film is surrounded by air (refractive index $n_{\text{air}} \approx 1$), with $n_{\text{air}} < n_f < n_g$. Monochromatic light of vacuum wavelength $\lambda$ is normally incident on the film. Due to the refractive index relationships, a phase change of $\pi$ radians occurs upon reflection at both the air-film interface and the film-glass interface.

##### Knowledge Points Tested
1. Phase change upon reflection at an interface based on refractive index comparisons.
2. Path difference and optical path length in thin films.
3. Conditions for destructive interference in reflected light.
4. Derivation of wavelength from interference conditions.

##### Intradisciplinary Connections
This problem connects to wave optics (interference principles), electromagnetic theory (boundary conditions for light waves), and optical materials (refractive indices and phase shifts).

##### Interdisciplinary Connections
- **Materials Science**: Design of thin-film coatings for specific optical properties.
- **Engineering**: Applications in lens manufacturing and photovoltaics to enhance light transmission.
- **Chemistry**: Deposition techniques for uniform thin films.

##### Real-World Applications
Anti-reflective coatings are used on eyeglasses, camera lenses, solar panels, and telescope optics to increase transmission and reduce glare. For example, magnesium fluoride coatings (as described) can achieve >99% transmission for specific wavelengths.

##### Problem Statement
Derive the general condition for destructive interference in the reflected light for the thin film system described above. Then, express the vacuum wavelength $\lambda$ that satisfies this condition in terms of the film's refractive index $n_f$, thickness $d$, and a non-negative integer order $m$ ($m = 0, 1, 2, \dots$). Ensure your derivation explicitly accounts for phase changes and path differences.  
**Final Answer Format**: Provide a single analytic expression for $\lambda$ in terms of $n_f$, $d$, and $m$. Use standard LaTeX notation with two-field fractions (e.g., `\frac{a}{b}`), and avoid numerical substitutions.

## Solution
To derive the condition for destructive interference, consider two rays reflected from the thin film:  
- **Ray 1**: Reflects at the air-film interface. Since $n_f > n_{\text{air}}$, this reflection incurs a phase change of $\pi$ radians.  
- **Ray 2**: Travels through the film, reflects at the film-glass interface (where $n_g > n_f$, so another $\pi$ phase change occurs), and exits back into air.  

Both reflections introduce a $\pi$ phase change, resulting in no net relative phase shift due to reflections. The path difference arises because Ray 2 travels an additional distance of $2d$ within the film (down and back). The optical path difference (OPD) is:  
$$ \text{OPD} = 2n_f d $$  
The phase difference $\delta$ due to this path is:  
$$ \delta = \frac{2\pi}{\lambda} \cdot \text{OPD} = \frac{2\pi}{\lambda} \cdot 2n_f d = \frac{4\pi n_f d}{\lambda} $$  
For destructive interference, the total phase difference must be an odd multiple of $\pi$ (to ensure crest meets trough):  
$$ \delta = (2m + 1)\pi \quad \text{for} \quad m = 0, 1, 2, \dots $$  
Substitute the expression for $\delta$:  
$$ \frac{4\pi n_f d}{\lambda} = (2m + 1)\pi $$  
Divide both sides by $\pi$:  
$$ \frac{4 n_f d}{\lambda} = 2m + 1 $$  
Solve for $\lambda$:  
$$ \lambda = \frac{4 n_f d}{2m + 1} $$  
This is the vacuum wavelength for destructive interference.

## Answer
$$\boxed{\dfrac{4 n_{f} d}{2m+1}}$$

------
# elastic potential energy in springs

## Problem 0
##### Background  
In engineering applications, springs are often designed with non-linear characteristics to achieve specific force-displacement behaviors. While Hooke's Law ($F = -kx$) describes ideal springs, many practical springs exhibit a quadratic deviation from linearity due to material properties or geometric design. Consider a specialized compression spring used in a vehicle's suspension system. When compressed, the restoring force follows the relationship $F(x) = -k_1 x - k_2 x^2$, where $x$ is the displacement from equilibrium, $k_1$ is the primary stiffness coefficient, and $k_2$ is the secondary stiffness coefficient.  

##### Knowledge Points Tested  
- Derivation of elastic potential energy from a variable force function  
- Integration of non-linear force-displacement relationships  
- Energy conservation principles in non-Hookean systems  

##### Intradisciplinary Connections  
- Connects to harmonic motion: Non-linear springs alter oscillation dynamics.  
- Extends Hooke's Law: $k_2 = 0$ reduces to the classical spring energy formula $U = \frac{1}{2} k_1 x^2$.  

##### Interdisciplinary Connections  
- **Material Science**: Explains how atomic bonding anharmonicity causes non-linear elasticity.  
- **Mechanical Engineering**: Applies to vibration dampers in aerospace systems.  

##### Real-World Applications  
- **Automotive suspensions**: Non-linear springs provide smoother rides over large bumps.  
- **Robotics**: Variable-stiffness springs enhance adaptive gripping mechanisms.  

##### Problem Statement  
A non-linear spring obeys the force law $F(x) = -k_1 x - k_2 x^2$, where $x$ is the displacement from its equilibrium length, and $k_1$, $k_2$ are stiffness coefficients. Derive an analytic expression for the elastic potential energy $U$ stored in the spring when compressed by a displacement $d$. Express $U$ solely in terms of $k_1$, $k_2$, and $d$.

## Solution
#### Step 1: Relate force to elastic potential energy  
The elastic potential energy $U$ is defined as the negative work done by the spring force during compression. For a displacement from $x=0$ (equilibrium) to $x=d$:  

$$ U = -\int_{0}^{d} F(x)  dx $$  

#### Step 2: Substitute the given force function  
Insert $F(x) = -k_1 x - k_2 x^2$ into the integral:  

$$ U = -\int_{0}^{d} (-k_1 x - k_2 x^2)  dx = \int_{0}^{d} (k_1 x + k_2 x^2)  dx $$  

#### Step 3: Integrate term by term  
Compute the integral of each component separately:  

$$ \int_{0}^{d} k_1 x  dx = k_1 \left[ \frac{1}{2} x^2 \right]_{0}^{d} = \frac{1}{2} k_1 d^2 $$  

$$ \int_{0}^{d} k_2 x^2  dx = k_2 \left[ \frac{1}{3} x^3 \right]_{0}^{d} = \frac{1}{3} k_2 d^3 $$  

#### Step 4: Combine results  
Sum the integrated terms to obtain the total elastic potential energy:  

$$ U = \frac{1}{2} k_1 d^2 + \frac{1}{3} k_2 d^3 $$  

#### Verification  
- **Dimensional consistency**: Each term has units of energy (Joules).  
- **Boundary check**: If $k_2 = 0$, $U = \frac{1}{2} k_1 d^2$, matching Hooke's Law.  
- **Physical intuition**: Positive $k_2$ increases stored energy for the same $d$, reflecting a "stiffer" spring at large displacements.

## Answer
$$\boxed{\dfrac{1}{2} k_{1} d^{2} + \dfrac{1}{3} k_{2} d^{3}}$$

------
## Problem 1
##### Background  
In modern engineering, shock absorbers are critical for protecting sensitive equipment during impacts. These systems often use springs to convert kinetic energy into elastic potential energy, minimizing damage. For instance, when a drone delivers a package onto a spring-based landing platform, the spring compresses to absorb the impact energy. Understanding the maximum compression is essential for designing such systems to prevent structural failure.

##### Knowledge Points Tested  
1. Conservation of mechanical energy (gravitational potential, elastic potential, and kinetic energy).  
2. Solving quadratic equations derived from energy conservation.  
3. Analyzing systems with combined gravitational and spring forces.  

##### Intradisciplinary Connections  
- Relates to Hooke's law for spring force and the work-energy theorem.  
- Extends to oscillations and simple harmonic motion when the mass rebounds after compression.  

##### Interdisciplinary Connections  
- **Engineering**: Designing shock-absorbing systems for vehicles, aerospace landers, or packaging materials.  
- **Mathematics**: Solving quadratic equations with physical constraints (e.g., rejecting non-physical roots).  

##### Real-World Applications  
- Elevator safety mechanisms that use springs to halt falling cabins.  
- Cushioning systems in athletic shoes or sports equipment to reduce impact forces on joints.  
- Mars rover landing systems that deploy springs to absorb touchdown energy.  

##### Problem Statement  
A package of mass $m$ is released from rest at a height $h$ above the top of a vertical spring (spring constant $k$) that is initially uncompressed. The package falls and lands squarely on the spring. Derive an expression for the maximum compression $x$ of the spring. Ignore air resistance and assume the spring is ideal.  

Express your answer analytically in terms of $m$, $g$ (acceleration due to gravity), $k$, and $h$. Ensure the expression is fully simplified and physically meaningful.

## Solution
**Step 1: Define reference points for energy**  
- Set the gravitational potential energy ($U_g$) reference at the spring's uncompressed position.  
- Initial state: Package at height $h$ above the spring.  
- Final state: Spring compressed by $x$, so the package is at height $-x$ (below the reference).  

**Step 2: Apply conservation of mechanical energy**  
Initial total energy ($E_i$) = Final total energy ($E_f$).  
- Initial kinetic energy = 0 (released from rest).  
- Initial gravitational potential energy = $m g h$.  
- Initial spring potential energy = 0 (spring uncompressed).  
Thus,  
$$ E_i = m g h. $$  

At maximum compression:  
- Kinetic energy = 0 (package momentarily at rest).  
- Gravitational potential energy = $m g (-x) = -m g x$.  
- Spring potential energy = $\frac{1}{2} k x^2$.  
Thus,  
$$ E_f = -m g x + \frac{1}{2} k x^2. $$  

Equate $E_i$ and $E_f$:  
$$ m g h = -m g x + \frac{1}{2} k x^2. $$  

**Step 3: Rearrange into standard quadratic form**  
Bring all terms to one side:  
$$ \frac{1}{2} k x^2 - m g x - m g h = 0. $$  
Multiply through by 2 to eliminate fractions:  
$$ k x^2 - 2 m g x - 2 m g h = 0. \quad (1) $$  

**Step 4: Solve the quadratic equation**  
Equation (1) is quadratic in $x$: $a = k$, $b = -2 m g$, $c = -2 m g h$.  
The quadratic formula gives:  
$$ x = \frac{ -b \pm \sqrt{b^2 - 4 a c} }{2 a}. $$  
Substitute $a$, $b$, and $c$:  
$$ x = \frac{ 2 m g \pm \sqrt{ (-2 m g)^2 - 4 (k) (-2 m g h) } }{2 k}. $$  
Simplify inside the square root:  
$$ (-2 m g)^2 = 4 m^2 g^2, $$  
$$ -4 (k) (-2 m g h) = 8 k m g h, $$  
$$ \therefore \sqrt{4 m^2 g^2 + 8 k m g h} = \sqrt{4 m g (m g + 2 k h)} = 2 \sqrt{m g (m g + 2 k h)}. $$  
Thus,  
$$ x = \frac{ 2 m g \pm 2 \sqrt{m g (m g + 2 k h)} }{2 k} = \frac{ m g \pm \sqrt{m g (m g + 2 k h)} }{k}. $$  

**Step 5: Select the physically valid root**  
- The term $\sqrt{m g (m g + 2 k h)} > m g$ (since $m g + 2 k h > m g$).  
- The solution with "$+$" yields $x > 0$ (compression).  
- The solution with "$-$" yields $x < 0$ (unphysical, as $x$ must be positive).  
Thus, discard the negative root:  
$$ x = \frac{ m g + \sqrt{m g (m g + 2 k h)} }{k}. $$  

**Step 6: Simplify the expression**  
Factor $m g$ inside the square root:  
$$ \sqrt{m g (m g + 2 k h)} = \sqrt{ (m g)^2 + 2 k m g h }. $$  
The final expression is:  
$$ x = \frac{ m g + \sqrt{ (m g)^2 + 2 k m g h } }{k}. $$

## Answer
$$\boxed{ \dfrac{ m g + \sqrt{ \left( m g \right)^{2} + 2 k m g h } }{ k } }$$

------
## Problem 2
##### Background
Elastic potential energy is stored in springs when they are compressed or stretched from their natural length. In practical applications, springs are often combined to achieve specific mechanical properties. For example, in vehicle suspensions, springs in series can provide a smoother ride by reducing the effective stiffness. Here, two springs with different stiffnesses are connected end-to-end (in series), meaning the force experienced by each spring is identical, but their individual compressions may differ.

##### Knowledge Points Tested
- Hooke's law: The force $F$ exerted by a spring is $F = -k x$, where $k$ is the spring constant and $x$ is the displacement from equilibrium.
- Elastic potential energy: The energy stored in a spring is $U = \frac{1}{2} k x^2$.
- Series spring equivalence: For springs in series, the total compression is the sum of individual compressions, while the force is constant throughout.

##### Intradisciplinary Connections
This problem integrates concepts from work-energy principles and force equilibrium. It also connects to oscillations, as the equivalent spring constant determines the frequency of a mass-spring system.

##### Interdisciplinary Connections
- **Mechanical Engineering**: Series springs model shock absorbers in automotive suspensions, where reduced stiffness improves comfort.
- **Biology**: Tendons and ligaments behave like springs in series, storing elastic energy during locomotion.

##### Real-World Applications
- **Exercise Equipment**: Resistance bands with multiple segments use series springs to provide adjustable force profiles.
- **Robotics**: Series elastic actuators (SEAs) employ springs in series with motors to absorb impacts and improve control.

##### Problem Statement
Two ideal springs with spring constants $k_1$ and $k_2$ are connected in series. The system is compressed by a total displacement $d$ (i.e., the reduction in the overall length of the system is $d$). Derive an expression for the total elastic potential energy stored in the system. Express your answer as a single analytic expression in terms of $k_1$, $k_2$, and $d$.

**Format Requirements**:
- Use symbolic parameters only (no numerical substitutions).
- Express the final answer as a simplified fraction or product.
- Ensure all exponents are denoted with `^` and curly braces (e.g., `d^{2}`).

## Solution
**Step 1: Define variables and force equilibrium**  
Let $x_1$ be the compression of spring 1 and $x_2$ be the compression of spring 2. Since the springs are in series:  
$$ d = x_1 + x_2 \quad (1) $$  
The force $F$ is the same in both springs (force equilibrium):  
$$ F = k_1 x_1 = k_2 x_2 \quad (2) $$  

**Step 2: Solve for $x_1$ and $x_2$ in terms of $d$**  
From equation (2):  
$$ x_1 = \frac{F}{k_1}, \quad x_2 = \frac{F}{k_2} $$  
Substitute into equation (1):  
$$ d = \frac{F}{k_1} + \frac{F}{k_2} = F \left( \frac{1}{k_1} + \frac{1}{k_2} \right) = F \left( \frac{k_2 + k_1}{k_1 k_2} \right) $$  
Solve for $F$:  
$$ F = d \cdot \frac{k_1 k_2}{k_1 + k_2} \quad (3) $$  

**Step 3: Express compressions $x_1$ and $x_2$**  
Using equations (2) and (3):  
$$ x_1 = \frac{F}{k_1} = \frac{d}{k_1} \cdot \frac{k_1 k_2}{k_1 + k_2} = d \cdot \frac{k_2}{k_1 + k_2} $$  
$$ x_2 = \frac{F}{k_2} = \frac{d}{k_2} \cdot \frac{k_1 k_2}{k_1 + k_2} = d \cdot \frac{k_1}{k_1 + k_2} $$  

**Step 4: Compute total elastic potential energy**  
The total energy $U$ is the sum of energies in both springs:  
$$ U = \frac{1}{2} k_1 x_1^2 + \frac{1}{2} k_2 x_2^2 $$  
Substitute $x_1$ and $x_2$:  
$$ U = \frac{1}{2} k_1 \left( d \cdot \frac{k_2}{k_1 + k_2} \right)^2 + \frac{1}{2} k_2 \left( d \cdot \frac{k_1}{k_1 + k_2} \right)^2 $$  
$$ U = \frac{1}{2} d^2 \left[ k_1 \left( \frac{k_2^2}{(k_1 + k_2)^2} \right) + k_2 \left( \frac{k_1^2}{(k_1 + k_2)^2} \right) \right] $$  
$$ U = \frac{1}{2} d^2 \cdot \frac{ k_1 k_2^2 + k_2 k_1^2 }{(k_1 + k_2)^2} = \frac{1}{2} d^2 \cdot \frac{ k_1 k_2 (k_1 + k_2) }{(k_1 + k_2)^2} $$  
Simplify:  
$$ U = \frac{1}{2} d^2 \cdot \frac{k_1 k_2}{k_1 + k_2} $$  

**Conclusion**  
The total elastic potential energy is $\frac{1}{2} \frac{k_1 k_2}{k_1 + k_2} d^2$. This matches the energy for a single spring with equivalent spring constant $k_{\text{eq}} = \frac{k_1 k_2}{k_1 + k_2}$.

## Answer
$$\boxed{\dfrac{1}{2} \cdot \dfrac{k_{1} k_{2}}{k_{1} + k_{2}} \cdot d^{2}}$$

------
## Problem 3
##### Background
Springs are essential components in various real-world systems, from vehicle suspension to mechanical watches. When compressed or stretched, they store elastic potential energy. In vertical configurations, such as pogo sticks or industrial shock absorbers, springs interact with gravity during launch phases. This problem explores how gravitational potential energy modifies the conversion of spring energy into kinetic energy compared to frictionless horizontal cases.

##### Knowledge Points Tested
1. Conservation of mechanical energy  
2. Elastic potential energy: $ U_s = \frac{1}{2} k x^2 $  
3. Gravitational potential energy: $ U_g = m g h $  
4. Kinetic energy: $ K = \frac{1}{2} m v^2 $  

##### Intradisciplinary Connections
- Relates to Hooke's law and spring dynamics.  
- Extends energy conservation principles beyond idealized horizontal systems.  

##### Interdisciplinary Connections
- Mechanical engineering: Design of vibration dampers and launch systems.  
- Sports science: Analysis of spring-based equipment like diving boards.  

##### Real-World Applications
Determines launch velocities in vertical spring mechanisms, such as:  
- Trampoline propulsion systems.  
- Industrial presses that use spring recoil.  
- Energy-absorbing buffers in elevator safety systems.  

##### Problem Statement
A vertical spring with spring constant $ k $ is mounted on the floor. A block of mass $ m $ is placed on the spring, compressing it by a distance $ x $ from its natural length. The system is released from rest. Ignore air resistance and friction.  
Derive an expression for the speed $ v $ of the block when the spring returns to its natural length (i.e., when the block just loses contact with the spring).  
Express $ v $ symbolically in terms of $ k $, $ m $, $ x $, and the acceleration due to gravity $ g $. Use $ \sqrt{\cdot} $ for square roots in your final answer.

## Solution
**Step 1: Define reference points for potential energy**  
Set the gravitational potential energy $ U_g = 0 $ at the spring's natural length position (height $ h = 0 $).  

**Step 2: Initial state (spring compressed, block at rest)**  
- Compression distance: $ x $  
- Height of block: $ h_i = -x $ (below reference)  
- Elastic potential energy: $ U_{s,i} = \frac{1}{2} k x^2 $  
- Gravitational potential energy: $ U_{g,i} = m g h_i = m g (-x) = -m g x $  
- Kinetic energy: $ K_i = 0 $ (released from rest)  
- Total initial energy: $ E_i = U_{s,i} + U_{g,i} + K_i = \frac{1}{2} k x^2 - m g x $  

**Step 3: Final state (spring at natural length, block leaving spring)**  
- Height of block: $ h_f = 0 $  
- Elastic potential energy: $ U_{s,f} = 0 $ (spring uncompressed)  
- Gravitational potential energy: $ U_{g,f} = 0 $  
- Kinetic energy: $ K_f = \frac{1}{2} m v^2 $  
- Total final energy: $ E_f = \frac{1}{2} m v^2 $  

**Step 4: Apply conservation of mechanical energy**  
Since no non-conservative forces act:  
$$ E_i = E_f $$  
Substitute expressions:  
$$ \frac{1}{2} k x^2 - m g x = \frac{1}{2} m v^2 $$  

**Step 5: Solve for $ v $**  
Isolate $ v^2 $:  
$$ \frac{1}{2} m v^2 = \frac{1}{2} k x^2 - m g x $$  
Multiply both sides by 2:  
$$ m v^2 = k x^2 - 2 m g x $$  
Divide by $ m $:  
$$ v^2 = \frac{k x^2}{m} - 2 g x $$  
Take the square root (retaining the physical solution):  
$$ v = \sqrt{ \frac{k x^2}{m} - 2 g x } $$

## Answer
$$\boxed{\sqrt{\dfrac{k x^{2}}{m} - 2 g x}}$$

------
## Problem 4
##### Background
In mechanical systems such as vehicle suspensions, elevator safety mechanisms, and building vibration dampers, springs are often arranged in series to manage loads and absorb energy. This problem explores a fundamental two-mass, two-spring system in static equilibrium under gravity. The setup consists of an upper spring (spring 1) attached to a fixed ceiling and mass $m_1$, and a lower spring (spring 2) connecting $m_1$ to mass $m_2$. Both springs obey Hooke's law, and the system is at rest.

##### Knowledge Points Tested
- Application of Newton's second law in static systems.
- Hooke's law for spring force and elastic potential energy.
- Equilibrium conditions for coupled masses.
- Algebraic manipulation of multivariable expressions.

##### Intradisciplinary Connections
This problem integrates concepts from forces, energy, and spring dynamics. It extends the single-spring potential energy formula to a series system, requiring simultaneous equilibrium analysis.

##### Interdisciplinary Connections
The model applies to shock absorption in mechanical engineering (vehicle suspensions), structural stability in civil engineering (building dampers), and load distribution in biomechanics (tendon systems).

##### Real-World Applications
- **Elevator safety springs**: Series springs absorb kinetic energy during emergency stops.
- **Truck suspensions**: Multiple springs distribute load to prevent axle damage.
- **Seismic dampers**: Buildings use stacked spring systems to dissipate earthquake energy.

##### Problem Statement
Two masses, $m_1$ and $m_2$, are suspended vertically in series by two springs:  
- Spring 1 (constant $k_1$) connects the ceiling to $m_1$.  
- Spring 2 (constant $k_2$) connects $m_1$ to $m_2$.  
The system is in static equilibrium under gravity $g$. Derive the total elastic potential energy stored in both springs. Express your answer symbolically in terms of $m_1$, $m_2$, $k_1$, $k_2$, and $g$.  

**Format requirements**:  
- Use $\exp(x)$ for exponentials (e.g., $e^x$ → $\exp(x)$).  
- Express fractions as $\frac{a}{b}$.

## Solution
**Step 1: Analyze forces on $m_2$**  
At equilibrium, the net force on $m_2$ is zero. The spring force upward (from spring 2) balances gravity downward:  
$$k_2 x_2 = m_2 g$$  
where $x_2$ is the extension of spring 2. Solving for $x_2$:  
$$x_2 = \frac{m_2 g}{k_2} \quad (1)$$  

**Step 2: Analyze forces on $m_1$**  
The net force on $m_1$ is zero. Spring 1 exerts an upward force $k_1 x_1$, while gravity ($m_1 g$) and spring 2 (pulling down with force $k_2 x_2$) act downward:  
$$k_1 x_1 = m_1 g + k_2 x_2$$  
Substitute $x_2$ from equation (1):  
$$k_1 x_1 = m_1 g + k_2 \left( \frac{m_2 g}{k_2} \right) = m_1 g + m_2 g$$  
Simplify and solve for $x_1$:  
$$x_1 = \frac{(m_1 + m_2)g}{k_1} \quad (2)$$  

**Step 3: Elastic potential energy in each spring**  
The elastic potential energy $U$ for a spring is $\frac{1}{2} k x^2$. For spring 1:  
$$U_1 = \frac{1}{2} k_1 x_1^2$$  
Substitute $x_1$ from equation (2):  
$$U_1 = \frac{1}{2} k_1 \left( \frac{(m_1 + m_2)g}{k_1} \right)^2 = \frac{1}{2} k_1 \cdot \frac{(m_1 + m_2)^2 g^2}{k_1^2} = \frac{(m_1 + m_2)^2 g^2}{2 k_1}$$  
For spring 2:  
$$U_2 = \frac{1}{2} k_2 x_2^2$$  
Substitute $x_2$ from equation (1):  
$$U_2 = \frac{1}{2} k_2 \left( \frac{m_2 g}{k_2} \right)^2 = \frac{1}{2} k_2 \cdot \frac{m_2^2 g^2}{k_2^2} = \frac{m_2^2 g^2}{2 k_2}$$  

**Step 4: Total elastic potential energy**  
Sum $U_1$ and $U_2$:  
$$U_{\text{total}} = U_1 + U_2 = \frac{(m_1 + m_2)^2 g^2}{2 k_1} + \frac{m_2^2 g^2}{2 k_2}$$  
Factor out $\frac{1}{2}g^2$:  
$$U_{\text{total}} = \frac{1}{2} g^2 \left( \frac{(m_1 + m_2)^2}{k_1} + \frac{m_2^2}{k_2} \right)$$  
This is the symbolic expression for the total elastic potential energy.

## Answer
$$\boxed{\frac{1}{2}g^{2}\left(\frac{\left(m_{1} + m_{2}\right)^{2}}{k_{1}} + \frac{m_{2}^{2}}{k_{2}}\right)}$$

------
# emf in rotating generators

## Problem 0
##### Background
Alternating current (AC) generators operate on electromagnetic induction principles, where mechanical rotation converts to electrical energy. In industrial generators, a multi-turn coil rotates in a uniform magnetic field, inducing a time-varying electromotive force (EMF). The peak EMF is critical for designing generator efficiency and voltage regulation systems in power grids.

##### Knowledge Points Tested
1. Faraday's law of induction: $\varepsilon = -N \frac{d\Phi_B}{dt}$  
2. Magnetic flux through a rotating coil: $\Phi_B = \vec{B} \cdot \vec{A}$  
3. Angular kinematics: relationship between rotational frequency and angular velocity  
4. Trigonometric modeling of time-dependent flux  

##### Intradisciplinary Connections
- Rotational dynamics: angular velocity $\omega$ and frequency $f$  
- Circuit theory: peak voltage in AC systems  
- Vector calculus: dot product in magnetic flux calculation  

##### Interdisciplinary Connections
- Mechanical engineering: torque and rotational energy transfer  
- Environmental science: generator design in wind turbines/hydroelectric plants  
- Industrial design: optimizing coil geometry for maximum power output  

##### Real-World Applications
- Automotive alternators: converting engine rotation to electrical power  
- Renewable energy: wind turbines use rotating coils to generate grid-compatible AC  
- Portable generators: emergency power supply systems  

##### Problem Statement
A rectangular coil with $N$ turns and cross-sectional area $A$ rotates at a constant frequency of $f$ revolutions per minute (rpm) in a uniform magnetic field of magnitude $B$. The magnetic field direction is perpendicular to the coil's axis of rotation. At $t=0$, the coil's plane is perpendicular to the magnetic field. Derive an expression for the peak induced electromotive force (EMF) in the coil.  
Express your answer symbolically in terms of $N$, $A$, $B$, $f$, and fundamental constants. Use $\pi$ explicitly.  

**Answer format requirements**:  
- The final expression must use the given symbols only.  
- Angular functions must be in radians.  
- Use $\exp(\cdot)$ for exponentials; do not use $e^x$.  
- Write fractions as $\frac{a}{b}$.

## Solution
**Step 1: Express angular velocity in rad/s**  
Rotational frequency in Hz (revolutions per second) is:  
$$ f_{\text{Hz}} = \frac{f}{60} $$  
Angular velocity $\omega$ (rad/s) is:  
$$ \omega = 2\pi f_{\text{Hz}} = \frac{2\pi f}{60} = \frac{\pi f}{30} $$  

**Step 2: Model magnetic flux**  
At time $t$, the angle $\theta$ between the magnetic field $\vec{B}$ and the coil's normal is $\theta = \omega t$. Magnetic flux through one turn:  
$$ \Phi_1 = \vec{B} \cdot \vec{A} = BA \cos\theta = BA \cos(\omega t) $$  
Total flux for $N$ turns:  
$$ \Phi_{\text{total}} = N \Phi_1 = NBA \cos(\omega t) $$  

**Step 3: Apply Faraday's law**  
Induced EMF:  
$$ \varepsilon = -\frac{d\Phi_{\text{total}}}{dt} = -\frac{d}{dt} \left[ NBA \cos(\omega t) \right] $$  
Derivative calculation:  
$$ \frac{d}{dt} \cos(\omega t) = -\omega \sin(\omega t) $$  
Thus:  
$$ \varepsilon = -NBA \left( -\omega \sin(\omega t) \right) = NBA\omega \sin(\omega t) $$  

**Step 4: Identify peak EMF**  
The EMF $\varepsilon = NBA\omega \sin(\omega t)$ has amplitude:  
$$ \varepsilon_{\text{peak}} = NBA\omega $$  
Substitute $\omega = \frac{\pi f}{30}$:  
$$ \varepsilon_{\text{peak}} = NBA \left( \frac{\pi f}{30} \right) = \frac{NBA\pi f}{30} $$  

**Conclusion**  
The peak induced EMF is $\frac{NBA\pi f}{30}$.

## Answer
$$\boxed{\dfrac{N B A \pi f}{30}}$$

------
## Problem 1
##### Background  
A generator produces electromotive force (EMF) by rotating a coil within a magnetic field. The maximum EMF depends on the generator's design parameters: the number of coil turns $N$, the coil area $A$, the magnetic field strength $B$, and the rotational (angular) speed $\omega$. Understanding how changes to these parameters affect the EMF is crucial for optimizing generator performance in applications like wind turbines or hydroelectric plants.

##### Knowledge Points Tested  
- Faraday's law of electromagnetic induction.  
- Relationship between magnetic flux and induced EMF.  
- Dependence of maximum EMF on generator parameters.  

##### Intradisciplinary Connections  
Connects to magnetic flux ($\Phi_B = B \cdot A \cos\theta$), angular velocity in rotational motion, and energy conversion principles in electromagnetism.  

##### Interdisciplinary Connections  
Overlaps with mechanical engineering (rotational dynamics) and electrical engineering (power generation systems).  

##### Real-World Applications  
Upgrading generators in renewable energy systems (e.g., increasing wind turbine blade speed or using stronger magnets in hydroelectric generators) to boost voltage output efficiently.  

##### Problem Statement  
A generator initially operates with rotational speed $\omega$ and magnetic field strength $B$, producing a maximum EMF of $\mathcal{E}_{\text{max}}$. During an upgrade, the rotational speed doubles to $2\omega$, and the magnetic field strength triples to $3B$. The number of coil turns $N$ and coil area $A$ remain unchanged.  

Derive an expression for the new maximum EMF, $\mathcal{E}_{\text{new}}$, in terms of the original maximum EMF $\mathcal{E}_{\text{max}}$. Then, find the multiplicative factor $k$ such that $\mathcal{E}_{\text{new}} = k \cdot \mathcal{E}_{\text{max}}$.  

Express $k$ as an exact integer.

## Solution
The maximum EMF for a generator is derived from Faraday's law. The magnetic flux through one coil turn is:  
$$\Phi_B = B \cdot A \cdot \cos(\theta)$$  
where $\theta = \omega t$ (assuming rotation starts when $\theta = 0$). The induced EMF for one turn is:  
$$\mathcal{E}_{\text{1 turn}} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left[ B A \cos(\omega t) \right] = B A \omega \sin(\omega t)$$  
The maximum EMF for one turn occurs when $\sin(\omega t) = 1$:  
$$\mathcal{E}_{\text{1 turn, max}} = B A \omega$$  
For $N$ turns, the maximum EMF is:  
$$\mathcal{E}_{\text{max}} = N \cdot (B A \omega) = N A B \omega \quad (1)$$  

After the upgrade:  
- Magnetic field strength becomes $3B$,  
- Rotational speed becomes $2\omega$.  
The number of turns $N$ and area $A$ are unchanged. Substituting into equation (1):  
$$\mathcal{E}_{\text{new}} = N \cdot A \cdot (3B) \cdot (2\omega) = 6 \cdot (N A B \omega) \quad (2)$$  
From equation (1), $N A B \omega = \mathcal{E}_{\text{max}}$. Substituting this into (2):  
$$\mathcal{E}_{\text{new}} = 6 \cdot \mathcal{E}_{\text{max}}$$  
Thus, the multiplicative factor is:  
$$k = 6$$

## Answer
$$\boxed{6}$$

------
## Problem 2
##### Background
In alternating current (AC) generators, electromagnetic induction converts mechanical rotation into electrical energy. A coil rotating in a uniform magnetic field induces a sinusoidal electromotive force (EMF). This principle powers hydroelectric turbines, where water flow drives rotational motion. The root mean square (RMS) voltage quantifies the effective voltage for power delivery in AC systems.

##### Knowledge Points Tested
1. Faraday's law of electromagnetic induction
2. Relationship between angular velocity and rotational frequency
3. Definition and calculation of RMS values for sinusoidal functions
4. Trigonometric differentiation and simplification techniques

##### Intradisciplinary Connections
Connects to AC circuit analysis, transformer operation, and energy conversion efficiency in electromagnetic systems. Extends to concepts like inductive reactance and impedance in alternating current circuits.

##### Interdisciplinary Connections
- Physics: Conservation of energy in mechanical-to-electrical conversion
- Environmental Science: Sustainable energy generation in hydroelectric plants
- Engineering: Design optimization of generator coils and magnetic circuits

##### Real-World Applications
RMS voltage standardization enables grid compatibility for hydroelectric power. For example, the Hoover Dam generators produce 16,500 V RMS at 60 Hz, stepped up to 230,000 V for transmission. RMS measurements ensure safe voltage levels in household appliances (120 V/240 V RMS).

##### Problem Statement
A hydroelectric turbine drives a generator coil with $N$ turns and cross-sectional area $A$. The coil rotates at frequency $f$ in a uniform magnetic field of strength $B$ directed perpendicular to the axis of rotation. Derive the RMS voltage generated. Express your answer symbolically using $N$, $A$, $f$, $B$, and fundamental constants.

**Answer Format Requirements**:
- Analytic expression in terms of $N$, $A$, $f$, $B$
- Use $\pi$ for pi and $\sqrt{\ }$ for square roots
- No numerical substitutions
- Simplified multiplicative form

## Solution
**Step 1: Magnetic Flux through the Coil**  
The magnetic flux $\Phi$ through a coil with $N$ turns is:  
$$\Phi = NBA \cos \theta$$  
where $\theta$ is the angle between the magnetic field and the coil's normal vector. For constant rotation at frequency $f$:  
$$\theta = \omega t, \quad \omega = 2\pi f$$  
Thus, $\Phi = NBA \cos(2\pi f t)$.

**Step 2: Faraday's Law for Induced EMF**  
Faraday's law states:  
$$\varepsilon = -\frac{d\Phi}{dt}$$  
Differentiate the flux expression:  
$$\frac{d\Phi}{dt} = NBA \cdot \left[-\sin(2\pi f t)\right] \cdot 2\pi f = -2\pi f NBA \sin(2\pi f t)$$  
The induced EMF is:  
$$\varepsilon = - \left(-2\pi f NBA \sin(2\pi f t)\right) = 2\pi f NBA \sin(2\pi f t)$$

**Step 3: Peak Voltage Identification**  
The sinusoidal EMF has peak value:  
$$\varepsilon_{\text{peak}} = 2\pi f NBA$$

**Step 4: RMS Voltage Derivation**  
For any sinusoidal function $V(t) = V_{\text{peak}} \sin(\omega t)$, the RMS value is:  
$$V_{\text{RMS}} = \frac{V_{\text{peak}}}{\sqrt{2}}$$  
Substitute the peak voltage:  
$$\varepsilon_{\text{RMS}} = \frac{2\pi f NBA}{\sqrt{2}}$$

**Step 5: Simplification**  
$$\frac{2}{\sqrt{2}} = \sqrt{2}, \quad \text{so}$$  
$$\varepsilon_{\text{RMS}} = \sqrt{2} \, \pi f NBA$$

**Final Expression**  
The RMS voltage is $\sqrt{2} \pi f NBA$.

## Answer
$$\boxed{\sqrt{2} \pi f N B A}$$

------
## Problem 3
##### Background
In electrical power generation, rotating generators convert mechanical energy into electrical energy using electromagnetic induction. The generator consists of a coil rotating in a uniform magnetic field. The electromotive force (EMF) induced in the coil depends on its geometry, the magnetic field strength, and the rotational speed. Engineers must precisely calculate the rotation speed to achieve a desired voltage output for applications like power grids or renewable energy systems.

##### Knowledge Points Tested
1. Faraday’s law of induction: $\varepsilon = -\frac{d\Phi_B}{dt}$, where $\Phi_B$ is magnetic flux.
2. Magnetic flux through a coil: $\Phi_B = NBA\cos\theta$, with $\theta$ as the angle between the magnetic field and coil normal.
3. Relationship between angular velocity $\omega$ and angular position: $\theta = \omega t$ for constant $\omega$.
4. Trigonometric differentiation: $\frac{d}{dt}[\cos(\omega t)] = -\omega \sin(\omega t)$.
5. Peak EMF derivation: Maximum voltage occurs when $\sin(\omega t) = \pm 1$.

##### Intradisciplinary Connections
- Alternating current (AC) circuits: The generated EMF is sinusoidal, linking to AC voltage and frequency analysis.
- Electromagnetism: Magnetic field interactions and flux changes underpin electric motor and transformer design.

##### Interdisciplinary Connections
- Mechanical engineering: Angular velocity relates to torque and rotational kinetics in turbine design.
- Mathematics: Derivatives of trigonometric functions model time-varying EMF.

##### Real-World Applications
- Wind turbines: Blade rotation speed must be optimized to match grid voltage requirements.
- Hydroelectric generators: Water flow rate controls $\omega$ to maintain consistent voltage output.

##### Problem Statement
A generator coil with $N$ turns rotates in a uniform magnetic field of strength $B$. The area of each turn is $A$. Derive an expression for the angular velocity $\omega$ required to produce a peak EMF of $\varepsilon_0$.  
**Express $\omega$ symbolically in terms of $\varepsilon_0$, $N$, $B$, and $A$.**  
*Ensure all physical constants remain symbolic. Use standard trigonometric and derivative notation.*

## Solution
**Step 1: Express magnetic flux through the coil**  
The magnetic flux $\Phi_B$ through a single loop is $B \cdot A \cdot \cos\theta$, where $\theta$ is the angle between the magnetic field vector and the normal to the coil plane. For a coil with $N$ turns, the total flux is:  
$$\Phi_B = NBA \cos\theta.$$  

**Step 2: Relate angular position to time**  
Since the coil rotates at constant angular velocity $\omega$, $\theta = \omega t$ (assuming $\theta=0$ at $t=0$). Substituting gives:  
$$\Phi_B = NBA \cos(\omega t).$$  

**Step 3: Apply Faraday’s law**  
The induced EMF $\varepsilon$ is the negative rate of change of flux:  
$$\varepsilon = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left[NBA \cos(\omega t)\right].$$  

**Step 4: Compute the derivative**  
Differentiate $\cos(\omega t)$ using the chain rule:  
$$\frac{d}{dt}\left[\cos(\omega t)\right] = -\omega \sin(\omega t).$$  
Thus,  
$$\varepsilon = -NBA \left[-\omega \sin(\omega t)\right] = NBA \omega \sin(\omega t).$$  

**Step 5: Identify peak EMF**  
The maximum value of $\sin(\omega t)$ is $1$, so the peak EMF $\varepsilon_0$ is:  
$$\varepsilon_0 = NBA \omega.$$  

**Step 6: Solve for angular velocity**  
Rearrange the equation to isolate $\omega$:  
$$\omega = \frac{\varepsilon_0}{NBA}.$$

## Answer
$$\boxed{\dfrac{\varepsilon_0}{NBA}}$$

------
## Problem 4
##### Background  
Generators convert mechanical energy into electrical energy using electromagnetic induction. When a coil rotates in a magnetic field, a changing magnetic flux induces an electromotive force (EMF) according to Faraday's law. This principle is fundamental in devices like alternators in cars, wind turbines, and hydroelectric power plants. In this problem, you will derive the magnetic field strength required for a specific generator setup.

##### Knowledge Points Tested  
- Faraday's law of electromagnetic induction  
- Relationship between rotational frequency and angular velocity  
- Derivation of peak EMF in a rotating coil generator  

##### Intradisciplinary Connections  
- Connects to alternating current (AC) circuits: the induced EMF varies sinusoidally with time.  
- Relates to torque and energy conversion in electromechanical systems.  

##### Interdisciplinary Connections  
- **Mathematics**: Angular velocity calculations and trigonometric differentiation.  
- **Engineering**: Design parameters for efficient generator operation.  

##### Real-World Applications  
- Used in renewable energy systems (e.g., wind turbines) to optimize magnetic field strength for maximum power output.  
- Applied in automotive alternators to maintain battery charging voltage.  

##### Problem Statement  
A generator uses a 60-turn coil rotating at 25 revolutions per second in a uniform magnetic field. Each turn has an area of $0.05  \text{m}^2$. The peak EMF induced is $90  \text{V}$. Starting from Faraday's law, derive an expression for the peak EMF and use it to calculate the required magnetic field strength $B$. Express your answer in tesla (T) and provide only the numerical value rounded to three significant figures.  

**Note**:  
- Use $\omega = 2\pi f$ for angular velocity, where $f$ is rotational frequency.  
- The peak EMF occurs when the rate of change of magnetic flux is maximized.

## Solution
#### Step 1: Apply Faraday's law  
Faraday's law states that the induced EMF $\varepsilon$ is the negative rate of change of magnetic flux $\Phi$:  

$$
\varepsilon = -\frac{d\Phi}{dt}
$$
  
For a coil with $N$ turns, the total flux linkage is $\Phi = N \cdot (B A \cos \theta)$, where $\theta$ is the angle between the magnetic field and the normal to the coil's plane.  

#### Step 2: Express $\theta$ as a function of time  
As the coil rotates with angular velocity $\omega$, $\theta = \omega t$. Thus:  

$$
\Phi = N B A \cos(\omega t)
$$
  

#### Step 3: Differentiate $\Phi$ with respect to time  

$$
\frac{d\Phi}{dt} = N B A \cdot (-\omega \sin(\omega t)) = -N B A \omega \sin(\omega t)
$$
  
The induced EMF is:  

$$
\varepsilon = -\left(-N B A \omega \sin(\omega t)\right) = N B A \omega \sin(\omega t)
$$
  

#### Step 4: Identify the peak EMF  
The maximum value of $\sin(\omega t)$ is 1. Thus, the peak EMF $\varepsilon_0$ is:  

$$
\varepsilon_0 = N B A \omega
$$
  

#### Step 5: Substitute $\omega = 2\pi f$  
Given $f = 25  \text{rev/s}$:  

$$
\omega = 2\pi \times 25 = 50\pi  \text{rad/s}
$$
  
So:  

$$
\varepsilon_0 = N B A (50\pi)
$$
  

#### Step 6: Solve for $B$  
Rearrange the equation:  

$$
B = \frac{\varepsilon_0}{N A \cdot 50\pi}
$$
  
Substitute the given values:  
- $\varepsilon_0 = 90  \text{V}$  
- $N = 60$  
- $A = 0.05  \text{m}^2$  

$$
B = \frac{90}{60 \times 0.05 \times 50\pi}
$$
  

#### Step 7: Simplify and compute  
First, compute the denominator:  

$$
60 \times 0.05 = 3, \quad 3 \times 50 = 150, \quad 150 \times \pi \approx 150 \times 3.1416 = 471.24
$$
  

$$
B = \frac{90}{471.24} \approx 0.19099
$$
  
Rounded to three significant figures:  

$$
B \approx 0.191  \text{T}
$$

## Answer
$$\boxed{0.191}$$

------
## Problem 5
##### Background
In alternating current (AC) generators, a coil rotates in a uniform magnetic field, inducing an electromotive force (EMF) due to Faraday's law of induction. The EMF varies sinusoidally with time, characterized by a peak voltage and angular frequency. Understanding the relationship between the coil's rotation and the induced EMF is essential for designing generators used in power plants, wind turbines, and other renewable energy systems.

##### Knowledge Points Tested
1. Faraday's law of induction and its application to a rotating coil.
2. Relationship between angular frequency and linear frequency.
3. Evaluation of sinusoidal functions at specific times.
4. Units and dimensions in electromagnetic contexts.

##### Intradisciplinary Connections
This problem connects to electromagnetic induction, AC circuit theory, and the physics of rotational motion. It also reinforces the derivation of time-dependent EMF expressions from first principles.

##### Interdisciplinary Connections
The principles apply to electrical engineering (generator design), mechanical engineering (rotational dynamics), and environmental science (renewable energy conversion in wind turbines).

##### Real-World Applications
Generators are fundamental in power generation, from hydroelectric dams to wind farms. The frequency of generated electricity (e.g., 50 Hz or 60 Hz) must match grid standards to ensure compatibility with household appliances and industrial machinery.

##### Problem Statement
A generator produces an EMF described by $e(t) = 220 \sin(100\pi t)$ volts.  
(a) Starting from Faraday's law and the geometry of a rotating coil, derive the general expression for the induced EMF $e(t)$ in terms of the number of turns $N$, coil area $A$, magnetic field strength $B$, and angular velocity $\omega$.  
(b) Using the given EMF equation $e(t) = 220 \sin(100\pi t)$, determine the frequency $f$ of the alternating current in hertz.  
(c) Calculate the instantaneous EMF at $t = 0.01$ seconds.  

For part (a), express your answer as an analytic expression. For parts (b) and (c), provide numerical values.  
- **Angles**: Use radians for trigonometric functions.  
- **Final Answer for (c)**: Provide only the numerical value in volts, without units, rounded to five significant figures.

## Solution
### Solution

#### Part (a): Derivation of $e(t)$
Faraday's law states that the induced EMF is the negative rate of change of magnetic flux:  
$$e = -\frac{d\phi_B}{dt}$$  
where $\phi_B$ is the magnetic flux through the coil.  

For a coil with $N$ turns, each of area $A$, rotating in a uniform magnetic field $B$, the flux through one turn at time $t$ is:  
$$\phi_B^{\text{one turn}} = \vec{B} \cdot \vec{A} = BA \cos\theta$$  
Here, $\theta$ is the angle between the magnetic field and the normal to the coil's plane. If the coil rotates with constant angular velocity $\omega$ and $\theta = 0$ at $t=0$, then:  
$$\theta = \omega t$$  
Thus, the flux for one turn is:  
$$\phi_B^{\text{one turn}} = BA \cos(\omega t)$$  
The total flux for $N$ turns is:  
$$\phi_B^{\text{total}} = N \phi_B^{\text{one turn}} = NBA \cos(\omega t)$$  
Applying Faraday's law:  
$$e = -\frac{d}{dt}\left[NBA \cos(\omega t)\right] = -NBA \left[-\omega \sin(\omega t)\right]$$  
Simplifying:  
$$e = NBA \omega \sin(\omega t)$$  
The general expression for the induced EMF is:  
$$e(t) = NBA \omega \sin(\omega t)$$  

#### Part (b): Frequency $f$ in hertz
The given EMF is $e(t) = 220 \sin(100\pi t)$.  
Compare this to the derived form $e(t) = NBA \omega \sin(\omega t)$. The angular frequency $\omega$ is the coefficient of $t$ in the sine function:  
$$\omega = 100\pi \text{ rad/s}$$  
The linear frequency $f$ (in Hz) relates to $\omega$ by:  
$$\omega = 2\pi f$$  
Substituting $\omega$:  
$$100\pi = 2\pi f$$  
Solving for $f$:  
$$f = \frac{100\pi}{2\pi} = 50 \text{ Hz}$$  
The frequency is 50 Hz.  

#### Part (c): Instantaneous EMF at $t = 0.01$ seconds
Substitute $t = 0.01$ into the given EMF equation:  
$$e(0.01) = 220 \sin(100\pi \cdot 0.01) = 220 \sin(\pi)$$  
Since $\sin(\pi) = 0$:  
$$e(0.01) = 220 \times 0 = 0$$  
Rounded to five significant figures, this is 0.0000 volts.

## Answer
$$\boxed{0.0000}$$

------
## Problem 6
##### Background
In an alternating current (AC) generator, a coil rotates in a uniform magnetic field, inducing an electromotive force (EMF) through electromagnetic induction. The maximum EMF depends on the coil's geometry, rotational speed, and magnetic field strength. This problem explores how scaling the coil's size and rotation rate affects the output voltage while keeping the magnetic field constant—a design consideration in real-world generators like those in hydroelectric turbines or portable power units.

##### Knowledge Points Tested
1. Fundamental equation for maximum EMF in a rotating generator coil.
2. Geometric dependence of coil area on diameter (area ∝ diameter²).
3. Proportional reasoning to determine combined effects of parameter changes.
4. Algebraic manipulation of ratios.

##### Intradisciplinary Connections
Connects to Faraday's law of induction, rotational kinematics (angular velocity), and geometry of circular coils. Reinforces understanding of how physical dimensions influence electromagnetic phenomena.

##### Interdisciplinary Connections
- **Engineering:** Generator design trade-offs between size, speed, and voltage output.
- **Mathematics:** Proportional scaling and fractional operations.
- **Environmental Science:** Implications for renewable energy systems where turbine/generator size and rotation rates are constrained by natural resources.

##### Real-World Applications
- Downsizing generators for portable applications (e.g., camping gear) while maintaining voltage by increasing rotation speed.
- Optimizing wind turbine generators where blade length (affecting rotation rate) and generator coil size must be balanced for efficiency.

##### Problem Statement
A generator uses a single circular coil of diameter $d$ rotating at angular velocity $\omega$ in a uniform magnetic field of strength $B$, producing a maximum EMF $\mathcal{E}_0$. The generator is redesigned such that the coil diameter is halved ($d_{\text{new}} = d/2$) and the rotation rate is tripled ($\omega_{\text{new}} = 3\omega$), while $B$ and the number of coil turns remain unchanged.  

Derive the ratio $\frac{\mathcal{E}_{\text{new}}}{\mathcal{E}_0}$, where $\mathcal{E}_{\text{new}}$ is the new maximum EMF. Express your answer as a simplified fraction.  

*Note: The area of a circle is $A = \pi r^2$, where $r$ is the radius.*

## Solution
The maximum EMF in a rotating generator coil is given by:  
$$\mathcal{E}_{\text{max}} = N B A \omega,$$  
where:  
- $N$ = number of turns (constant),  
- $B$ = magnetic field strength (constant),  
- $A$ = cross-sectional area of the coil,  
- $\omega$ = angular velocity of rotation.  

The area $A$ depends on the coil diameter. For a circular coil:  
$$A = \pi \left(\frac{d}{2}\right)^2 = \frac{\pi d^2}{4}.$$  
Thus, the original maximum EMF is:  
$$\mathcal{E}_0 = N B \left(\frac{\pi d^2}{4}\right) \omega = \frac{N B \pi d^2 \omega}{4}.$$  

After redesign:  
- New diameter $d_{\text{new}} = \frac{d}{2}$,  
- New angular velocity $\omega_{\text{new}} = 3\omega$.  

The new area is:  
$$A_{\text{new}} = \pi \left(\frac{d_{\text{new}}}{2}\right)^2 = \pi \left(\frac{d/2}{2}\right)^2 = \pi \left(\frac{d}{4}\right)^2 = \frac{\pi d^2}{16}.$$  
The new maximum EMF is:  
$$\mathcal{E}_{\text{new}} = N B A_{\text{new}} \omega_{\text{new}} = N B \left(\frac{\pi d^2}{16}\right) (3\omega) = \frac{3 N B \pi d^2 \omega}{16}.$$  

The ratio of new to original maximum EMF is:  
$$\frac{\mathcal{E}_{\text{new}}}{\mathcal{E}_0} = \frac{\frac{3 N B \pi d^2 \omega}{16}}{\frac{N B \pi d^2 \omega}{4}} = \frac{3}{16} \times \frac{4}{1} = \frac{12}{16} = \frac{3}{4}.$$  

Thus, the ratio simplifies to $\frac{3}{4}$.

## Answer
$$\boxed{\dfrac{3}{4}}$$

------
## Problem 7
##### Background
Rotating coil generators operate on the principle of electromagnetic induction, as described by Faraday's law. When a coil rotates in a magnetic field, the changing magnetic flux through the coil induces an electromotive force (EMF). This problem explores the design parameters of such a generator, focusing on the relationship between rotational motion, magnetic field strength, and the resulting voltage.

##### Knowledge Points Tested
1. Faraday's law of electromagnetic induction.
2. Magnetic flux and its rate of change.
3. Conversion between rotational speed (revolutions per minute, rpm) and angular velocity (radians per second).
4. Derivation of the peak EMF in a rotating coil generator.

##### Intradisciplinary Connections
This problem connects to alternating current (AC) generation, sinusoidal EMF variation, and the optimization of electromechanical devices. It also reinforces trigonometric functions in modeling rotational dynamics.

##### Interdisciplinary Connections
- **Mathematics**: Angular velocity conversion involves unit analysis and proportionality constants (e.g., $2\pi$ radians per revolution).
- **Engineering**: Coil design parameters (turns, area) directly impact generator efficiency and are critical in power generation systems like wind turbines.

##### Real-World Applications
Generators are used in hydroelectric dams, wind turbines, and automotive alternators. The number of coil turns influences voltage output and is a key design factor in renewable energy systems.

##### Problem Statement
A generator coil rotates at 1800 revolutions per minute (rpm) in a uniform magnetic field of 0.6 tesla (T). The coil has a cross-sectional area of 0.02 square meters (m²). Derive an expression for the peak EMF induced in the coil using Faraday's law and the definition of magnetic flux. Then, use your expression to calculate the number of turns $N$ required to produce a peak EMF of 400 volts (V). 

Round your final answer for $N$ to the nearest whole number, as fractional turns are not physically meaningful. Provide only the numerical value in your answer.

## Solution
The peak EMF is derived from Faraday's law and magnetic flux. The magnetic flux $\Phi_B$ through one turn of the coil is:

$$
\Phi_B = \vec{B} \cdot \vec{A} = BA \cos\theta
$$

where $\theta$ is the angle between the magnetic field and the coil's normal. For a coil rotating at angular velocity $\omega$, $\theta = \omega t$, so:

$$
\Phi_B = BA \cos(\omega t)
$$

By Faraday's law, the induced EMF for one turn is:

$$
\mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt} \left[ BA \cos(\omega t) \right] = BA \omega \sin(\omega t)
$$

The peak EMF for one turn is $BA\omega$. For $N$ turns, the peak EMF $\mathcal{E}_0$ is:

$$
\mathcal{E}_0 = N B A \omega
$$

The rotational speed is given in rpm. Convert 1800 rpm to angular velocity $\omega$ in rad/s:
- Revolutions per second: $ \frac{1800}{60} = 30 $ rev/s.
- Angular velocity: $ \omega = 2\pi \times \text{rev/s} = 2\pi \times 30 = 60\pi $ rad/s.

Substitute known values into the peak EMF equation:
- $\mathcal{E}_0 = 400$ V
- $B = 0.6$ T
- $A = 0.02$ m²
- $\omega = 60\pi$ rad/s

$$
400 = N \times 0.6 \times 0.02 \times 60\pi
$$

Simplify the constants:

$$
0.6 \times 0.02 = 0.012, \quad 0.012 \times 60\pi = 0.72\pi
$$

So:

$$
400 = N \times 0.72\pi
$$

Solve for $N$:

$$
N = \frac{400}{0.72\pi}
$$

Compute numerically:

$$
0.72\pi \approx 0.72 \times 3.1415926535 = 2.26194671132
$$


$$
N = \frac{400}{2.26194671132} \approx 176.8388
$$

Round to the nearest whole number:

$$
N \approx 177
$$

## Answer
$$\boxed{177}$$

------
## Problem 8
##### Background
In a simple alternating current (AC) generator, a rectangular coil with $N$ turns, each of area $A$, rotates at a constant rotational frequency $f$ in a uniform magnetic field of strength $B$. The axis of rotation is perpendicular to the magnetic field direction. The peak electromotive force (EMF) generated depends on these parameters. Initially, the generator produces a peak EMF of 150 V. 

##### Knowledge Points Tested
1. Faraday's law of electromagnetic induction
2. Derivation of peak EMF in a rotating coil generator
3. Proportional relationships between EMF, magnetic field strength, and rotational frequency
4. Algebraic manipulation of percentage changes

##### Intradisciplinary Connections
- Angular frequency ($\omega = 2\pi f$) and its role in sinusoidal EMF generation
- Magnetic flux linkage and its time derivative
- Conservation of energy in electromechanical systems

##### Interdisciplinary Connections
- **Mathematics**: Percentage calculations and multiplicative scaling
- **Engineering**: Design principles of electrical generators and sensitivity analysis
- **Technology**: Optimization of generator output under varying operating conditions

##### Real-World Applications
1. Adjusting turbine speeds in hydroelectric plants to maintain voltage stability when water flow changes
2. Modifying wind turbine blade pitch or rotational speed to compensate for fluctuating wind conditions
3. Regulating backup generators during power grid fluctuations by controlling fuel input (affects frequency) and electromagnet currents (affects $B$-field)

##### Problem Statement
A generator initially produces a peak EMF of 150 V. The rotational frequency $f$ is then increased by 30%, while the magnetic field strength $B$ is simultaneously decreased by 20%. All other parameters ($N$, $A$, coil geometry) remain unchanged. Derive an expression for the new peak EMF in terms of the initial peak EMF and the given percentage changes. Using this expression, compute the numerical value of the new peak EMF. 

**Final Answer Requirements**  
- Express your final answer as an exact number.  
- Do not include units (volts) in your answer.  
- If the result is an integer, write it as such without decimals.

## Solution
### Step 1: Derive the general expression for peak EMF  
The magnetic flux $\Phi$ through a coil with $N$ turns and area $A$ in a uniform magnetic field $B$ is:  
$$\Phi = NBA \cos(\theta)$$  
where $\theta$ is the angle between the magnetic field and the normal to the coil. For a coil rotating with constant angular frequency $\omega = 2\pi f$, $\theta = \omega t$. Thus:  
$$\Phi = NBA \cos(\omega t)$$  
By Faraday's law, the induced EMF $\varepsilon$ is:  
$$\varepsilon = -\frac{d\Phi}{dt} = NBA \omega \sin(\omega t)$$  
The peak EMF $\varepsilon_0$ occurs when $\sin(\omega t) = \pm 1$:  
$$\varepsilon_0 = NBA \omega$$  
Substituting $\omega = 2\pi f$:  
$$\varepsilon_0 = 2\pi NBA f \tag{1}$$  

### Step 2: Express the new peak EMF after changes  
Let $\varepsilon_{0,\text{initial}} = 150  \text{V}$. After changes:  
- New rotational frequency: $f_{\text{new}} = f + 0.3f = 1.3f$  
- New magnetic field: $B_{\text{new}} = B - 0.2B = 0.8B$  
Using equation (1), the new peak EMF is:  
$$\varepsilon_{0,\text{new}} = 2\pi N A B_{\text{new}} f_{\text{new}}$$  
Substitute $B_{\text{new}}$ and $f_{\text{new}}$:  
$$\varepsilon_{0,\text{new}} = 2\pi N A (0.8B) (1.3f)$$  
$$\varepsilon_{0,\text{new}} = (0.8)(1.3) \cdot (2\pi N A B f)$$  
Recognize that $2\pi N A B f = \varepsilon_{0,\text{initial}}$:  
$$\varepsilon_{0,\text{new}} = (0.8 \times 1.3) \cdot \varepsilon_{0,\text{initial}}$$  

### Step 3: Compute the numerical value  
Substitute $\varepsilon_{0,\text{initial}} = 150$:  
$$\varepsilon_{0,\text{new}} = (0.8 \times 1.3) \times 150$$  
First, calculate $0.8 \times 1.3 = 1.04$. Then:  
$$\varepsilon_{0,\text{new}} = 1.04 \times 150 = 156$$  
The new peak EMF is 156 V, but per the answer requirements, we report only the numerical value.

## Answer
$$\boxed{156}$$

------
# energy conservation in oscillators

## Problem 0
##### Background
A block of mass $m$ is attached to a spring with spring constant $k$ on a smooth inclined plane that makes an angle $\theta$ with the horizontal. The other end of the spring is fixed at the top of the incline. When the spring is at its natural (unstretched) length, the block is at position $x = 0$. Due to gravity, the equilibrium position—where the net force on the block is zero—is shifted down the incline. The block is released from rest at $x = 0$ (the natural length position). 

##### Knowledge Points Tested
1. Energy conservation in mechanical systems  
2. Spring potential energy and gravitational potential energy  
3. Quadratic optimization to find extrema  
4. Dynamics of oscillatory systems under constant external forces  

##### Intradisciplinary Connections
This problem connects Hooke's law, Newton's second law, and work-energy theorem. It demonstrates how gravity modifies the equilibrium position of a spring-mass system, extending the concept of simple harmonic motion to inclined planes.

##### Interdisciplinary Connections
- **Mathematics**: Quadratic functions and completing the square to find maxima.  
- **Trigonometry**: Resolving gravitational force components along the incline.  

##### Real-World Applications
Understanding this system is essential for designing suspension systems on mountainous terrain, analyzing seismic dampers in buildings on slopes, and modeling biomechanical systems (e.g., tendon oscillations during inclined motion).

##### Problem Statement
The block is released from rest at $x = 0$ (spring at natural length). Using energy conservation, derive an expression for the maximum speed $v_{\text{max}}$ attained by the block. Express your answer symbolically in terms of $m$, $k$, $g$ (acceleration due to gravity), and $\theta$.  

**Answer Format Requirements**:  
- Provide a closed-form analytic expression.  
- Use $\sin \theta$ for the sine of $\theta$; do not evaluate numerically.  
- Use $\sqrt{\ }$ for square roots and $\frac{a}{b}$ for fractions.  
- Follow standard notation: $\exp(x)$, $\sin$, $\cos$, etc.

## Solution
The total mechanical energy is conserved because the incline is smooth (no friction). Define $x$ as the displacement of the block down the incline from the spring's natural length ($x = 0$).  

**Energy components**:  
- Spring potential energy: $\frac{1}{2} k x^2$  
- Gravitational potential energy: $-mgx \sin \theta$ (height decreases by $x \sin \theta$, so $\Delta U_g = -mg \cdot x \sin \theta$)  
- Kinetic energy: $\frac{1}{2} m v^2$  

Initial conditions at release ($t = 0$):  
- $x = 0$  
- $v = 0$  
Thus, total initial energy $E_{\text{initial}} = 0$.  

At any point during motion, energy conservation gives:  
$$  
E = \frac{1}{2} m v^2 + \frac{1}{2} k x^2 - mgx \sin \theta = 0  
$$  
Solve for $v^2$:  
$$  
\frac{1}{2} m v^2 = -\frac{1}{2} k x^2 + mgx \sin \theta  
$$  
$$  
v^2 = \frac{2}{m} \left( mgx \sin \theta - \frac{1}{2} k x^2 \right) = 2gx \sin \theta - \frac{k}{m} x^2  
$$  
Rewrite $v^2$ as a quadratic function of $x$:  
$$  
v^2 = -\frac{k}{m} \left( x^2 - \frac{2mg \sin \theta}{k} x \right)  
$$  
Complete the square:  
$$  
x^2 - \frac{2mg \sin \theta}{k} x = \left( x - \frac{mg \sin \theta}{k} \right)^2 - \left( \frac{mg \sin \theta}{k} \right)^2  
$$  
Substitute back:  
$$  
v^2 = -\frac{k}{m} \left[ \left( x - \frac{mg \sin \theta}{k} \right)^2 - \left( \frac{mg \sin \theta}{k} \right)^2 \right] = -\frac{k}{m} \left( x - \frac{mg \sin \theta}{k} \right)^2 + \frac{k}{m} \left( \frac{mg \sin \theta}{k} \right)^2  
$$  
Simplify the second term:  
$$  
\frac{k}{m} \cdot \frac{m^2 g^2 \sin^2 \theta}{k^2} = \frac{m g^2 \sin^2 \theta}{k}  
$$  
Thus:  
$$  
v^2 = \frac{m g^2 \sin^2 \theta}{k} - \frac{k}{m} \left( x - \frac{mg \sin \theta}{k} \right)^2  
$$  
The expression $v^2$ is maximized when the subtracted term is zero, i.e., when:  
$$  
x = \frac{mg \sin \theta}{k}  
$$  
This is the equilibrium position (where spring force $kx$ balances the gravitational component $mg \sin \theta$). At this point:  
$$  
v_{\text{max}}^2 = \frac{m g^2 \sin^2 \theta}{k}  
$$  
Take the positive root (speed magnitude):  
$$  
v_{\text{max}} = g \sin \theta \sqrt{\frac{m}{k}}  
$$

## Answer
$$\boxed{g \sin \theta \sqrt{\frac{m}{k}}}$$

------
## Problem 1
##### Background
A pendulum consists of a bob of mass $m$ attached to a fixed pivot by a rigid massless rod of length $L$. The system is in a vertical plane under gravity $g$. To add complexity, a linear spring (spring constant $k$) is attached to the bob and anchored to a fixed point located a distance $h$ directly below the pivot. The spring has its natural length when the pendulum hangs vertically ($\theta = 0$). When released from an initial angle $\theta$, the spring stretches or compresses as the pendulum swings, introducing additional energy storage. Assume $h > L$ to ensure the spring is extended at all angles.

##### Knowledge Points Tested
- Conservation of mechanical energy in multi-potential systems  
- Gravitational potential energy in pendulum systems  
- Elastic potential energy in springs  
- Trigonometric geometry for position-dependent forces  

##### Intradisciplinary Connections
- Relates to simple harmonic motion (pendulum and spring systems)  
- Extends energy methods to hybrid conservative systems  

##### Interdisciplinary Connections
- **Geometry**: Calculating spring extension via coordinate geometry  
- **Physics/Engineering**: Modeling coupled oscillators in structural dynamics  

##### Real-World Applications
- **Seismic Dampers**: Pendulum-like structures with springs dissipate energy in skyscrapers during earthquakes.  
- **Biomechanics**: Muscle-tendon systems act as biological "springs" during limb oscillations.  

##### Problem Statement
The pendulum is released from rest at an angle $\theta$ (measured from the vertical). Using conservation of energy, derive an expression for the speed $v$ of the bob at the lowest point ($\theta = 0$). Express $v$ symbolically in terms of $m$, $g$, $L$, $k$, $h$, and $\theta$ only.  

**Key geometric note**: At angle $\theta$, the spring extension is $\Delta L = \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L)$.

## Solution
**Step 1: Define energy reference points**  
- Gravitational potential energy ($U_g$): Zero at $\theta = 0$ (lowest point).  
- Spring potential energy ($U_s$): Zero at natural length ($\Delta L = 0$), which occurs at $\theta = 0$.  

**Step 2: Initial energy (at release angle $\theta$)**  
- Kinetic energy: $K_i = 0$ (released from rest).  
- Gravitational potential energy: Height above lowest point is $L(1 - \cos\theta)$, so:  
  $$ U_{g,i} = m g L (1 - \cos\theta) $$  
- Spring potential energy: Extension $\Delta L = \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L)$, so:  
  $$ U_{s,i} = \frac{1}{2} k \left[ \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L) \right]^{2} $$  
- Total initial energy:  
  $$ E_i = K_i + U_{g,i} + U_{s,i} = m g L (1 - \cos\theta) + \frac{1}{2} k \left[ \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L) \right]^{2} $$  

**Step 3: Final energy (at $\theta = 0$)**  
- Kinetic energy: $K_f = \frac{1}{2} m v^{2}$.  
- Gravitational potential energy: $U_{g,f} = 0$.  
- Spring potential energy: $U_{s,f} = 0$ (spring at natural length).  
- Total final energy:  
  $$ E_f = \frac{1}{2} m v^{2} $$  

**Step 4: Apply conservation of energy**  
$$ E_i = E_f $$  
$$ m g L (1 - \cos\theta) + \frac{1}{2} k \left[ \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L) \right]^{2} = \frac{1}{2} m v^{2} $$  

**Step 5: Solve for $v$**  
- Multiply both sides by 2:  
  $$ 2 m g L (1 - \cos\theta) + k \left[ \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L) \right]^{2} = m v^{2} $$  
- Divide by $m$:  
  $$ v^{2} = 2 g L (1 - \cos\theta) + \frac{k}{m} \left[ \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L) \right]^{2} $$  
- Take the positive square root (speed is non-negative):  
  $$ v = \sqrt{ 2 g L (1 - \cos\theta) + \frac{k}{m} \left( \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - (h - L) \right)^{2} } $$

## Answer
$$\boxed{\sqrt{2 g L \left(1 - \cos\theta\right) + \frac{k}{m} \left( \sqrt{L^{2} + h^{2} - 2 h L \cos\theta} - \left(h - L\right) \right)^{2}}}$$

------
## Problem 2
#### Background
In a vertical spring-mass system, gravity shifts the equilibrium position from the spring's natural length. When the mass hangs at rest, the spring stretches by a distance $d$ due to the balance between gravity and the spring force. If the system is displaced from this equilibrium and released, it undergoes simple harmonic motion. Here, we consider the scenario where the mass is released from the equilibrium position with an initial kinetic energy $K$, imparting an initial velocity. The goal is to determine the amplitude of oscillation.

#### Knowledge Points Tested
1. **Energy conservation**: Total mechanical energy (kinetic + potential) is conserved in the absence of non-conservative forces.
2. **Effective potential in vertical springs**: The combined effect of spring and gravitational potential simplifies to an effective spring potential centered at the equilibrium position.
3. **Amplitude in harmonic motion**: The maximum displacement from equilibrium, derived from energy considerations.

#### Intradisciplinary Connections
- **Harmonic motion**: Connects to the general treatment of oscillators, emphasizing that gravity only shifts the equilibrium without altering the spring constant or energy dynamics.
- **Work-energy theorem**: Relates initial kinetic energy to the maximum stored potential energy.

#### Interdisciplinary Connections
- **Engineering**: Applications in vibration analysis, vehicle suspension design, and seismic isolation systems.
- **Biology**: Models oscillatory phenomena like the bouncing gait of animals or oscillations in biomechanical systems.

#### Real-World Applications
- **Elevator safety systems**: Vertical springs absorb kinetic energy during emergency stops.
- **Tuned mass dampers**: Used in skyscrapers to counteract oscillations from wind/earthquakes by converting kinetic energy into spring potential energy.

#### Problem Statement
A mass $m$ is attached to a vertical spring with spring constant $k$. At equilibrium, the spring is stretched by a distance $d$ due to gravity. The system is released from this equilibrium position with an initial kinetic energy $K$. Derive an expression for the amplitude $A$ of the resulting oscillation in terms of $m$, $g$ (acceleration due to gravity), $d$, and $K$. Express your answer as an analytic expression using the given symbols. Do not substitute numerical values for any constants.

## Solution
#### Step 1: Equilibrium Condition
At equilibrium, the spring force balances gravity:
$$ mg = kd $$
Solving for the spring constant $k$:
$$ k = \frac{mg}{d} $$

#### Step 2: Total Energy at Release
The total mechanical energy $E$ is conserved. At release (equilibrium position $y = 0$):
- Displacement from equilibrium: $0$
- Kinetic energy: $K$
- Effective spring potential energy: $\frac{1}{2}k(0)^2 = 0$  
Thus, the total energy is:
$$ E = K $$

#### Step 3: Total Energy at Maximum Displacement (Amplitude)
At amplitude $A$:
- Displacement from equilibrium: $A$
- Velocity: $0$ (kinetic energy $= 0$)
- Effective spring potential energy: $\frac{1}{2}kA^2$  
Thus, the total energy is:
$$ E = \frac{1}{2}kA^2 $$

#### Step 4: Energy Conservation
Equate the total energy at release and at amplitude:
$$ \frac{1}{2}kA^2 = K $$

#### Step 5: Solve for Amplitude $A$
$$ A^2 = \frac{2K}{k} $$
$$ A = \sqrt{\frac{2K}{k}} $$

#### Step 6: Substitute $k$ in Terms of Given Parameters
Replace $k$ using $k = \frac{mg}{d}$:
$$ A = \sqrt{\frac{2K}{\frac{mg}{d}}} = \sqrt{\frac{2Kd}{mg}} $$
The amplitude is $\sqrt{\frac{2Kd}{mg}}$.

## Answer
$$\boxed{\sqrt{\frac{2Kd}{mg}}}$$

------
## Problem 3
##### Background
Consider a block of mass $m$ attached to a spring with spring constant $k$ on a frictionless inclined plane. The incline makes an angle $\theta$ with the horizontal, and the spring is aligned parallel to the incline. At equilibrium, the spring is stretched due to gravity. The block is displaced a distance $x_0$ from this equilibrium position and released from rest. This scenario explores energy conservation in an oscillator subject to a constant force field (gravity).

##### Knowledge Points Tested
1. Equilibrium condition for a spring-mass system under a constant force.
2. Conservation of mechanical energy.
3. Spring potential energy and gravitational potential energy.
4. Derivation of maximum kinetic energy by minimizing potential energy.

##### Intradisciplinary Connections
This problem connects to simple harmonic motion by showing how a constant force (gravity) shifts the equilibrium position without altering the oscillator's energy dynamics. It reinforces the concept that the effective spring constant and energy conservation remain unchanged when measured from the new equilibrium.

##### Interdisciplinary Connections
- **Engineering**: Models vibration analysis in vehicles or machinery on sloped surfaces.
- **Earth Science**: Simplifies the study of mass movements (e.g., landslides) on inclined terrains with elastic restoring forces.
- **Biomechanics**: Illustrates energy transfer in tendon-driven motion (e.g., animal locomotion on slopes).

##### Real-World Applications
- **Seismic Dampers**: Buildings in hilly areas use inclined spring systems to absorb earthquake energy.
- **Conveyor Systems**: Springs on inclined conveyors stabilize loads against oscillations.
- **Sports Equipment**: Ski bindings use spring mechanisms that function on slopes to protect against high-impact forces.

##### Problem Statement
A block of mass $m$ is attached to a spring of spring constant $k$ on a frictionless incline angled at $\theta$ to the horizontal. The spring is parallel to the incline. The block is displaced a distance $x_0$ from its equilibrium position and released from rest. Derive an expression for the maximum kinetic energy, $K_{\text{max}}$, attained by the block. Express $K_{\text{max}}$ symbolically in terms of $k$ and $x_0$ only.

**Answer Format Requirements**:
- Provide an analytic expression using only the given symbols.
- Use standard mathematical notation: `\frac{}{}` for fractions, `x_{0}^{2}` for exponents, etc.
- Do not substitute numerical values for any parameter.

## Solution
**Step 1: Equilibrium Condition**  
At equilibrium, the spring force balances the gravitational force component parallel to the incline. Let $\delta$ be the spring stretch at equilibrium:  
$$ k\delta = mg\sin\theta $$  
Solving for $\delta$:  
$$ \delta = \frac{mg\sin\theta}{k} $$

**Step 2: Define Coordinate System**  
Let $x$ be the displacement of the block from the equilibrium position (positive down the incline). The total spring stretch from its natural length is $\delta + x$.

**Step 3: Total Mechanical Energy**  
The total mechanical energy $E$ is conserved and consists of spring potential energy, gravitational potential energy, and kinetic energy. Using the equilibrium position as the reference for gravitational potential energy:  
- Spring potential energy: $\frac{1}{2}k(\delta + x)^2$  
- Gravitational potential energy: $-mgx\sin\theta$ (since moving down the incline reduces potential energy)  
- Kinetic energy: $\frac{1}{2}mv^2$  

Thus:  
$$ E = \frac{1}{2}k(\delta + x)^2 - mgx\sin\theta + \frac{1}{2}mv^2 $$

**Step 4: Simplify the Potential Energy**  
Expand the spring potential energy term:  
$$ E = \frac{1}{2}k(\delta^2 + 2\delta x + x^2) - mgx\sin\theta + \frac{1}{2}mv^2 $$  
Substitute $k\delta = mg\sin\theta$ from Step 1:  
$$ E = \frac{1}{2}k\delta^2 + k\delta x + \frac{1}{2}kx^2 - (k\delta) x + \frac{1}{2}mv^2 $$  
The $k\delta x$ and $-k\delta x$ terms cancel:  
$$ E = \frac{1}{2}k\delta^2 + \frac{1}{2}kx^2 + \frac{1}{2}mv^2 $$  
The term $\frac{1}{2}k\delta^2$ is constant. Thus:  
$$ E = \frac{1}{2}kx^2 + \frac{1}{2}mv^2 + \text{constant} $$

**Step 5: Apply Initial Condition**  
At release ($t=0$), $x = x_0$ and $v = 0$:  
$$ E = \frac{1}{2}kx_0^2 + 0 + \text{constant} $$

**Step 6: Express Kinetic Energy**  
At any point, kinetic energy $K$ is:  
$$ K = E - \frac{1}{2}kx^2 - \text{constant} = \frac{1}{2}kx_0^2 - \frac{1}{2}kx^2 $$  
Maximum kinetic energy occurs when potential energy is minimized, i.e., at $x = 0$:  
$$ K_{\text{max}} = \frac{1}{2}kx_0^2 - \frac{1}{2}k(0)^2 = \frac{1}{2}kx_0^2 $$

**Conclusion**:  
The maximum kinetic energy is $\frac{1}{2}kx_0^2$, independent of $m$ and $\theta$, as the constant force of gravity only shifts the equilibrium without changing the energy available for oscillation.

## Answer
$$\boxed{\dfrac{1}{2} k x_{0}^{2}}$$

------
# equivalent resistance calculations

## Problem 0
##### Background
In electronic circuit design, the delta (Δ) configuration is a common way to connect three resistors in a triangular arrangement. This setup is frequently used in three-phase power systems and filter circuits. Unlike simple series or parallel connections, the equivalent resistance between any two terminals in a delta network requires a more nuanced approach, often involving transformations such as delta-to-star (Δ-Y) conversions or direct application of network analysis techniques.

##### Knowledge Points Tested
1. **Equivalent resistance calculation**: Understanding how to reduce complex resistor networks to a single equivalent resistance.
2. **Delta (Δ) network analysis**: Recognizing and analyzing resistors connected in a triangular topology.
3. **Delta-to-star transformation**: Applying this technique to simplify the network (optional but effective method).

##### Intradisciplinary Connections
This problem connects to Kirchhoff's circuit laws, as the delta configuration can be analyzed using loop equations. It also extends to Thevenin equivalent circuits, where complex networks are reduced to simplified equivalents for analysis.

##### Interdisciplinary Connections
Delta networks appear in mechanical engineering (e.g., truss structure analysis), computer science (graph theory applications), and physics (models of crystal lattices). The mathematical principles involve linear algebra (solving systems of equations) and symmetry considerations.

##### Real-World Applications
Delta configurations are used in:
- **Electrical grids**: Balancing loads in three-phase power transmission.
- **Audio equipment**: Crossover networks in speakers for impedance matching.
- **Sensor arrays**: Resistive touchscreens and strain-gauge bridges where precise equivalent resistance affects measurement accuracy.

##### Problem Statement
Three resistors are connected in a delta (Δ) configuration:  
- $ R_{ab} = 4  \Omega $ between terminals $ a $ and $ b $,  
- $ R_{bc} = 5  \Omega $ between terminals $ b $ and $ c $,  
- $ R_{ca} = 6  \Omega $ between terminals $ c $ and $ a $.  

Calculate the equivalent resistance $ R_{ab}^{\text{eq}} $ between terminals $ a $ and $ b $. Use symbolic derivation first, then substitute the given numerical values. Round your final numerical answer to three significant figures.  
**Instructions for answer formatting**:  
- Express the numerical value only (omit units).  
- Use decimal form (e.g., 2.93, not $ \frac{44}{15} $).  
- Apply standard rounding rules.

## Solution
To find the equivalent resistance $ R_{ab}^{\text{eq}} $ between terminals $ a $ and $ b $ in the delta network, we observe that terminal $ c $ is floating (no external connections). The resistance between $ a $ and $ b $ comprises two parallel paths:  
1. Directly through $ R_{ab} $.  
2. Through the series combination of $ R_{ca} $ and $ R_{bc} $ (via terminal $ c $).  

The equivalent resistance is therefore:  
$$ R_{ab}^{\text{eq}} = R_{ab} \parallel (R_{ca} + R_{bc}) = \frac{ R_{ab} \cdot (R_{ca} + R_{bc}) }{ R_{ab} + R_{ca} + R_{bc} } $$  
This formula arises because resistors $ R_{ab} $ and $ (R_{ca} + R_{bc}) $ are in parallel between nodes $ a $ and $ b $.  

Substitute the given values:  
- $ R_{ab} = 4  \Omega $,  
- $ R_{bc} = 5  \Omega $,  
- $ R_{ca} = 6  \Omega $.  

First, compute the numerator:  
$$ R_{ab} \cdot (R_{ca} + R_{bc}) = 4 \cdot (6 + 5) = 4 \cdot 11 = 44 $$  
Next, compute the denominator:  
$$ R_{ab} + R_{ca} + R_{bc} = 4 + 6 + 5 = 15 $$  
Now, evaluate the fraction:  
$$ R_{ab}^{\text{eq}} = \frac{44}{15} \approx 2.93333... $$  
Round to three significant figures:  
- The digit in the thousandths place is 3, which is less than 5, so we do not round up the hundredths place.  
- Thus, 2.93333... rounds to **2.93**.  

**Note**: The derivation holds for any delta network. Symbolically, with resistances $ A $ (between $ a $-$ b $), $ B $ (between $ b $-$ c $), and $ C $ (between $ c $-$ a $):  
$$ R_{ab}^{\text{eq}} = \frac{A \cdot (B + C)}{A + B + C} $$

## Answer
$$\boxed{2.93}$$

------
## Problem 1
##### Background
In electrical circuits, heating elements are commonly used in appliances like ovens and toasters. These elements convert electrical energy into heat. When connected to a voltage source, each element dissipates power according to the formula $P = \frac{V^2}{R}$, where $P$ is the power, $V$ is the voltage, and $R$ is the resistance. Understanding the combined resistance of multiple elements is essential for circuit design and safety.

##### Knowledge Points Tested
1. Ohm's law and power dissipation in resistors.
2. Calculation of equivalent resistance for parallel circuits.
3. Modeling real-world electrical components using fundamental principles.

##### Intradisciplinary Connections
This problem connects resistor networks to power calculations, illustrating how circuit analysis principles apply to practical electrical systems. It also reinforces the relationship between resistance, voltage, and power.

##### Interdisciplinary Connections
- **Physics**: Energy conversion and thermal dynamics (electrical energy to heat).
- **Engineering**: Circuit design for household appliances, ensuring optimal power distribution.
- **Mathematics**: Algebraic manipulation of fractional expressions and inverse relationships.

##### Real-World Applications
Household appliances like electric ovens often use multiple heating elements connected in parallel to distribute heat evenly. Calculating the equivalent resistance helps determine total current draw, preventing circuit overloads and optimizing energy efficiency.

##### Problem Statement
Three heating elements are designed for use in an industrial oven. When each element is connected individually to a voltage source of magnitude $V$, they consume powers of $3P$, $2P$, and $P$ watts, respectively. The elements are then connected in parallel to the same voltage source $V$. Derive an expression for the equivalent resistance of this parallel combination. Express your answer solely in terms of $V$ and $P$.

## Solution
To determine the equivalent resistance $R_{\text{eq}}$ of the three heating elements connected in parallel, we start by finding the resistance of each element using the power formula. For a resistor connected to voltage $V$, the power dissipated is $P = \frac{V^2}{R}$. Solving for resistance $R$:

- For the first element (power $3P$):  
  $$ R_1 = \frac{V^2}{3P} $$

- For the second element (power $2P$):  
  $$ R_2 = \frac{V^2}{2P} $$

- For the third element (power $P$):  
  $$ R_3 = \frac{V^2}{P} $$

The equivalent resistance $R_{\text{eq}}$ for resistors in parallel is given by:  
$$ \frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} $$

Substitute the expressions for $R_1$, $R_2$, and $R_3$:  
$$ \frac{1}{R_{\text{eq}}} = \frac{1}{\frac{V^2}{3P}} + \frac{1}{\frac{V^2}{2P}} + \frac{1}{\frac{V^2}{P}} $$

Simplify each term:  
$$ \frac{1}{R_{\text{eq}}} = \frac{3P}{V^2} + \frac{2P}{V^2} + \frac{P}{V^2} $$

Combine the terms:  
$$ \frac{1}{R_{\text{eq}}} = \frac{3P + 2P + P}{V^2} = \frac{6P}{V^2} $$

Solve for $R_{\text{eq}}$ by taking the reciprocal:  
$$ R_{\text{eq}} = \frac{V^2}{6P} $$

Thus, the equivalent resistance of the parallel combination is $\frac{V^2}{6P}$.

## Answer
$$\boxed{\dfrac{V^{2}}{6P}}$$

------
## Problem 2
##### Background
In modern electronics, composite materials are often used to create resistors with tailored properties. Consider a circuit component made from a cylindrical rod of length $L$ and cross-sectional area $A$. The rod consists of two parallel conductive paths: 
- Path 1: Made of Material X (resistivity $\rho_1$), occupying a fraction $f$ of the cross-sectional area ($A_1 = fA$).  
- Path 2: Made of Material Y (resistivity $\rho_2$), occupying the remaining fraction $(1-f)$ of the area ($A_2 = (1-f)A$).  

This composite rod behaves like two parallel resistors. It is connected in series with a uniform resistor made of Material Z (resistivity $\rho_3$) with length $L_3$ and cross-sectional area $A$.  

##### Knowledge Points Tested
- Resistance formula: $R = \rho L / A$  
- Equivalent resistance for parallel resistors  
- Equivalent resistance for series resistors  

##### Intradisciplinary Connections
Relates to circuit analysis principles (Kirchhoff's laws) and material properties affecting resistance. Extends to complex resistor networks in circuit design.  

##### Interdisciplinary Connections
Materials science: Role of resistivity in conductor selection. Engineering: Optimization of composite materials for specific electrical properties.  

##### Real-World Applications
Used in precision resistors for electronics, thermistors with temperature-dependent resistance, and multi-layer printed circuit board (PCB) traces.  

##### Problem Statement
Derive the equivalent resistance $R_{\text{eq}}$ of the entire system. Express your answer symbolically in terms of $L$, $A$, $f$, $\rho_1$, $\rho_2$, $\rho_3$, and $L_3$.

## Solution
**Step 1: Resistance of Path 1**  
The resistance of Path 1 (Material X) is:  
$$ R_1 = \rho_1 \frac{L}{A_1} = \rho_1 \frac{L}{fA} $$  

**Step 2: Resistance of Path 2**  
The resistance of Path 2 (Material Y) is:  
$$ R_2 = \rho_2 \frac{L}{A_2} = \rho_2 \frac{L}{(1-f)A} $$  

**Step 3: Equivalent Resistance of Parallel Paths**  
The composite rod has $R_1$ and $R_2$ in parallel. The equivalent resistance $R_{\text{parallel}}$ is:  
$$ \frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \frac{1}{R_2} = \frac{fA}{\rho_1 L} + \frac{(1-f)A}{\rho_2 L} $$  
Simplify the expression:  
$$ \frac{1}{R_{\text{parallel}}} = \frac{A}{L} \left( \frac{f}{\rho_1} + \frac{1-f}{\rho_2} \right) $$  
Thus,  
$$ R_{\text{parallel}} = \frac{L}{A \left( \frac{f}{\rho_1} + \frac{1-f}{\rho_2} \right)} $$  

**Step 4: Resistance of Series Component**  
The series resistor (Material Z) has resistance:  
$$ R_3 = \rho_3 \frac{L_3}{A} $$  

**Step 5: Total Equivalent Resistance**  
The total equivalent resistance is the sum of $R_{\text{parallel}}$ and $R_3$:  
$$ R_{\text{eq}} = R_{\text{parallel}} + R_3 = \frac{L}{A \left( \frac{f}{\rho_1} + \frac{1-f}{\rho_2} \right)} + \rho_3 \frac{L_3}{A} $$  
Factor out $\frac{1}{A}$:  
$$ R_{\text{eq}} = \frac{1}{A} \left[ \frac{L}{\frac{f}{\rho_1} + \frac{1-f}{\rho_2}} + \rho_3 L_3 \right] $$

## Answer
$$\boxed{\dfrac{1}{A} \left( \dfrac{L}{\dfrac{f}{\rho_1} + \dfrac{1-f}{\rho_2}} + \rho_{3} L_{3} \right)}$$

------
## Problem 3
##### Background
In electrical engineering, bridge circuits and symmetric resistor networks are fundamental for designing sensors, measurement systems, and signal processing units. Understanding equivalent resistance in non-standard configurations is essential for analyzing these systems. This problem explores a modified square resistor network where symmetry simplifies complex circuit analysis.

##### Knowledge Points Tested
- Equivalent resistance calculations using parallel/series combinations  
- Circuit simplification via symmetry and node equivalence  
- Effects of short circuits on resistor networks  
- Kirchhoff's laws application  

##### Intradisciplinary Connections
Connects to Thévenin/Norton equivalent circuits, Wheatstone bridge principles, and advanced network analysis techniques like delta-star transformations. Also reinforces fundamental concepts of voltage division and current paths.

##### Interdisciplinary Connections
- **Physics**: Conservation laws (charge/energy) in circuit analysis  
- **Mathematics**: Matrix algebra for solving linear systems (though not required here)  
- **Materials Science**: Resistivity concepts in homogeneous materials  

##### Real-World Applications
- Calibration of strain gauges in structural engineering  
- Null detection in precision resistance measurements  
- Sensor design in biomedical devices (e.g., ECG electrode arrays)  
- Fault simulation in power grid protection systems  

##### Problem Statement
Four identical resistors, each with resistance $R$, form a square network labeled $ABCD$ where resistors occupy sides $AB$, $BC$, $CD$, and $DA$. A zero-resistance wire shorts opposite corners $A$ and $C$. Determine the equivalent resistance between adjacent corners $A$ and $B$. Express your answer as a simplified analytic expression in terms of $R$.

## Solution
**Step 1: Identify circuit modifications**  
The short wire between $A$ and $C$ forces them to the same electric potential, making nodes $A$ and $C$ electrically identical. We merge them into a single node $AC$. The network now has three nodes: $AC$, $B$, and $D$.

**Step 2: Redraw the circuit**  
After merging $A$ and $C$:  
- Resistors originally between $A$-$B$ and $C$-$B$ both connect $AC$ to $B$.  
- Resistors originally between $A$-$D$ and $C$-$D$ both connect $AC$ to $D$.  
- No direct resistor exists between $B$ and $D$.  

**Step 3: Analyze parallel combinations**  
- **Path $AC$ to $B$**: Resistors $AB$ ($R$) and $CB$ ($R$) are in parallel. Equivalent resistance:  
  $$
  R_{AC→B} = \frac{R \times R}{R + R} = \frac{R^2}{2R} = \frac{R}{2}
  $$  
- **Path $AC$ to $D$**: Resistors $AD$ ($R$) and $CD$ ($R$) are in parallel. Equivalent resistance:  
  $$
  R_{AC→D} = \frac{R \times R}{R + R} = \frac{R}{2}
  $$  

**Step 4: Determine equivalent resistance between $A$ and $B$**  
Since $A$ is part of node $AC$, the resistance between $A$ and $B$ is identical to the resistance between $AC$ and $B$. Current flows exclusively through the parallel combination of $AB$ and $CB$, as node $D$ is isolated from $B$. Thus:  
$$
R_{A→B} = R_{AC→B} = \frac{R}{2}
$$  
Node $D$ does not create additional paths between $A$ and $B$ because no resistor connects $B$ and $D$ directly.

## Answer
$$\boxed{\dfrac{R}{2}}$$

------
# ideal gas law and individual gas law applications

## Problem 0
##### Background
In chemistry laboratories, gases produced by chemical reactions are often collected by water displacement. This method involves collecting the gas in an inverted container filled with water, allowing the gas to displace the water. The collected gas is a mixture of the target gas and water vapor. To determine the volume of the target gas alone, we must account for the vapor pressure of water using Dalton's law of partial pressures. This scenario is common in experiments involving hydrogen or oxygen generation.

##### Knowledge Points Tested
- Application of the ideal gas law: $PV = nRT$
- Dalton's law of partial pressures: $P_{\text{total}} = P_{\text{gas}} + P_{\text{vapor}}}$
- Mole concept and stoichiometry in chemical reactions

##### Intradisciplinary Connections
This problem connects gas laws with chemical stoichiometry, illustrating how reaction yields translate to measurable gas volumes. It also reinforces the relationship between temperature, pressure, and volume in gaseous systems.

##### Interdisciplinary Connections
- **Chemistry**: Reaction stoichiometry determines moles of gas produced.
- **Physics**: Partial pressures and ideal gas behavior govern volume calculations.
- **Environmental Science**: Water vapor pressure depends on temperature, reflecting real-world humidity effects.

##### Real-World Applications
- Measuring gas volumes in laboratory synthesis (e.g., hydrogen fuel production).
- Calibrating gas collection systems in industrial chemistry.
- Environmental monitoring of gas emissions using displacement methods.

##### Problem Statement
A chemist generates hydrogen gas ($\mathrm{H_2}$) by reacting zinc metal with sulfuric acid. The balanced reaction is:  

$$
\mathrm{Zn(s) + H_2SO_4(aq) \rightarrow ZnSO_4(aq) + H_2(g)}
$$
  
A mass $m$ of zinc produces hydrogen gas, which is collected by water displacement at temperature $T$. The total pressure above the water is $P_{\text{total}}}$, and the vapor pressure of water at temperature $T$ is $P_v$. The molar mass of zinc is $M_{\text{Zn}}}$, and the universal gas constant is $R$.  

Derive an expression for the volume $V$ of *dry* hydrogen gas collected. Express your answer in terms of $m$, $T$, $P_{\text{total}}}$, $P_v$, $M_{\text{Zn}}}$, and $R$.  

**Note**: The "dry" volume refers to the volume occupied by pure hydrogen gas at the given $T$ and partial pressure, excluding water vapor. Use Dalton's law to isolate the partial pressure of hydrogen.

## Solution
### Step 1: Determine moles of hydrogen gas produced
The reaction stoichiometry shows that 1 mole of zinc ($\mathrm{Zn}$) produces 1 mole of hydrogen gas ($\mathrm{H_2}$):  

$$
\mathrm{Zn \rightarrow H_2}
$$
  
The number of moles of zinc used is:  

$$
n_{\text{Zn}} = \frac{m}{M_{\text{Zn}}}}
$$
  
Thus, the moles of hydrogen gas produced are:  

$$
n_{\mathrm{H_2}} = n_{\text{Zn}} = \frac{m}{M_{\text{Zn}}}}
$$


### Step 2: Apply Dalton's law to find partial pressure of hydrogen
The total pressure $P_{\text{total}}}$ is the sum of the partial pressure of hydrogen ($P_{\mathrm{H_2}}}$) and the vapor pressure of water ($P_v$):  

$$
P_{\text{total}}} = P_{\mathrm{H_2}}} + P_v
$$
  
Solving for $P_{\mathrm{H_2}}}$:  

$$
P_{\mathrm{H_2}}} = P_{\text{total}}} - P_v
$$


### Step 3: Apply the ideal gas law to dry hydrogen gas
The ideal gas law for hydrogen gas is:  

$$
P_{\mathrm{H_2}}} V = n_{\mathrm{H_2}}} R T
$$
  
Substitute the expressions for $P_{\mathrm{H_2}}}$ and $n_{\mathrm{H_2}}}$ from Steps 1 and 2:  

$$
(P_{\text{total}}} - P_v) V = \left( \frac{m}{M_{\text{Zn}}}} \right) R T
$$


### Step 4: Solve for the volume $V$
Rearrange the equation to isolate $V$:  

$$
V = \frac{\frac{m}{M_{\text{Zn}}}} R T}{P_{\text{total}}} - P_v}
$$
  
Simplify the expression:  

$$
V = \frac{m R T}{M_{\text{Zn}}} (P_{\text{total}}} - P_v)
$$
  
This is the volume of dry hydrogen gas at temperature $T$ and partial pressure $P_{\mathrm{H_2}}}$.

## Answer
$$\boxed{\dfrac{m R T}{M_{\text{Zn}} \left( P_{\text{total}} - P_{v} \right)}}$$

------
## Problem 1
##### Background
A horizontal cylinder is divided into two compartments by a frictionless, movable piston. The left compartment contains an ideal gas A, and the right compartment contains an ideal gas B. The total volume of the cylinder is fixed at $6.0  \text{L}$. Initially, a latch holds the piston stationary, with each compartment at $3.0  \text{L}$. The initial pressure in compartment A is $150  \text{kPa}$, and in compartment B is $100  \text{kPa}$. The system is maintained at constant temperature. The latch is released, allowing the piston to move freely until mechanical equilibrium is reached. Then, an external agent slowly moves the piston to reduce the volume of compartment A to $2.0  \text{L}$ and holds it in place. The temperature remains constant throughout.

##### Knowledge Points Tested
1. Application of the ideal gas law for isothermal processes.
2. Mechanical equilibrium condition for a movable piston (equal pressures on both sides at equilibrium).
3. Conservation of mass and volume in a closed system.
4. Step-wise analysis of thermodynamic processes.

##### Intradisciplinary Connections
This problem connects the ideal gas law with mechanical equilibrium principles, requiring students to integrate Boyle's law with force balance concepts. It also demonstrates how multistep processes affect gas behavior, reinforcing the state dependence of ideal gases.

##### Interdisciplinary Connections
The scenario involves principles from mechanics (force balance on the piston) and systems analysis (conservation of volume). It models real-world pneumatic systems where gases interact through movable boundaries, commonly seen in industrial control systems.

##### Real-World Applications
Similar systems are used in hydraulic/pneumatic actuators, internal combustion engines (piston-cylinder assemblies), and medical devices like ventilators. Understanding pressure equilibrium during volume changes is crucial for designing efficient gas-based systems.

##### Problem Statement
After the external agent sets the volume of compartment A to $2.0  \text{L}$ and holds it in place, what is the pressure in compartment A? Calculate the pressure change for gas A from its initial state (before latch release) to the final state, defined as $\Delta P_A = P_{A,\text{final}} - P_{A,\text{initial}}$. Express $\Delta P_A$ in kPa, providing only the numerical value.

## Solution
### Step 1: Analyze equilibrium after latch release
When the latch is released, the piston moves freely until pressures equalize. Let $P_1$ be the equilibrium pressure, and $V_{A1}$ be the volume of compartment A at this stage. The volume of compartment B is $6.0 - V_{A1}$ liters.

For gas A (isothermal process, fixed amount):
$$ P_{A,\text{initial}} V_{A,\text{initial}} = P_1 V_{A1} $$
$$ (150  \text{kPa}) (3.0  \text{L}) = P_1 V_{A1} $$
$$ 450 = P_1 V_{A1} \quad \text{(Equation 1)} $$

For gas B (isothermal process, fixed amount):
$$ P_{B,\text{initial}} V_{B,\text{initial}} = P_1 (6.0 - V_{A1}) $$
$$ (100  \text{kPa}) (3.0  \text{L}) = P_1 (6.0 - V_{A1}) $$
$$ 300 = P_1 (6.0 - V_{A1}) \quad \text{(Equation 2)} $$

Add Equations 1 and 2:
$$ 450 + 300 = P_1 V_{A1} + P_1 (6.0 - V_{A1}) $$
$$ 750 = P_1 (V_{A1} + 6.0 - V_{A1}) $$
$$ 750 = 6.0 P_1 $$
$$ P_1 = \frac{750}{6.0} = 125  \text{kPa} $$

Substitute $P_1$ into Equation 1 to find $V_{A1}$:
$$ 450 = (125) V_{A1} $$
$$ V_{A1} = \frac{450}{125} = 3.6  \text{L} $$

At this intermediate equilibrium, both compartments have a pressure of $125  \text{kPa}$, with compartment A at $3.6  \text{L}$ and compartment B at $2.4  \text{L}$.

### Step 2: Compression of compartment A to $2.0  \text{L}$
The external agent moves the piston to set the volume of compartment A to $2.0  \text{L}$. The volume of compartment B becomes $6.0 - 2.0 = 4.0  \text{L}$. Since the amount of gas in compartment A is fixed and the process is isothermal:

$$ P_1 V_{A1} = P_{A,\text{final}} V_{A,\text{final}} $$
$$ (125  \text{kPa}) (3.6  \text{L}) = P_{A,\text{final}} (2.0  \text{L}) $$
$$ P_{A,\text{final}} = \frac{125 \times 3.6}{2.0} = \frac{450}{2.0} = 225  \text{kPa} $$

### Step 3: Calculate pressure change for gas A
The initial pressure of gas A was $150  \text{kPa}$, and the final pressure is $225  \text{kPa}$. The pressure change is:
$$ \Delta P_A = P_{A,\text{final}} - P_{A,\text{initial}} = 225  \text{kPa} - 150  \text{kPa} = 75  \text{kPa} $$

The pressure change occurs in two stages: first due to pressure equalization (reducing pressure from $150  \text{kPa}$ to $125  \text{kPa}$), then due to compression (increasing pressure to $225  \text{kPa}$).

## Answer
$$\boxed{75}$$

------
## Problem 2
##### Background
The ideal gas law, $PV = nRT$, describes the relationship between pressure ($P$), volume ($V$), and absolute temperature ($T$) for an ideal gas. When the volume and amount of gas remain constant, the law simplifies to a direct proportionality between pressure and absolute temperature. This scenario explores how heating a gas in a rigid container affects its pressure and temperature, with applications in systems like pressurized tanks, automotive engines, and meteorological balloons.

##### Knowledge Points Tested
1. Application of the ideal gas law under constant volume conditions.
2. Conversion between Celsius and Kelvin temperature scales.
3. Algebraic derivation of temperature changes due to pressure variations.

##### Intradisciplinary Connections
This problem connects to Charles's law (volume-temperature relationship at constant pressure) and Boyle's law (pressure-volume relationship at constant temperature), illustrating how the ideal gas law unifies these individual gas laws.

##### Interdisciplinary Connections
The principles are used in chemical engineering (reactor safety), mechanical engineering (internal combustion engines), and environmental science (atmospheric pressure modeling).

##### Real-World Applications
- **Industrial Safety**: Calculating temperature limits for pressurized gas storage to prevent explosions.
- **Meteorology**: Modeling temperature-pressure relationships in weather systems.
- **Automotive Design**: Predicting engine performance under varying thermal conditions.

##### Problem Statement
A fixed amount of an ideal gas is sealed in a rigid container. Initially, the gas has a temperature of $T_i$ degrees Celsius and a pressure of $P_i$. The gas is heated at constant volume until its pressure doubles. Derive an expression for the final temperature, $T_f$, in degrees Celsius, in terms of $T_i$ and the Celsius-to-Kelvin conversion constant $C$.  

*Express your answer as an analytic expression. Use $C$ for the conversion constant and ensure all temperatures are handled in absolute units during derivation.*

## Solution
**Step 1: Convert initial temperature to Kelvin**  
Absolute temperature is required for the ideal gas law. The initial temperature in Kelvin is:  

$$ T_{\mathrm{K},i} = T_i + C $$
  
where $C = 273.15$ is the Celsius-to-Kelvin conversion constant (kept symbolic).

**Step 2: Apply the ideal gas law for initial and final states**  
Since volume ($V$) and moles of gas ($n$) are constant, the ideal gas law gives:  
- Initial state: $ P_i V = n R T_{\mathrm{K},i} $  
- Final state: $ P_f V = n R T_{\mathrm{K},f} $  
where $T_{\mathrm{K},f}$ is the final absolute temperature, and $P_f = 2P_i$ (pressure doubles).  

**Step 3: Relate pressures and temperatures**  
Divide the final-state equation by the initial-state equation:  

$$ \frac{P_f V}{P_i V} = \frac{n R T_{\mathrm{K},f}}{n R T_{\mathrm{K},i}} $$
  
Simplify by canceling $V$, $n$, and $R$:  

$$ \frac{P_f}{P_i} = \frac{T_{\mathrm{K},f}}{T_{\mathrm{K},i}} $$
  
Substitute $P_f = 2P_i$:  

$$ \frac{2P_i}{P_i} = \frac{T_{\mathrm{K},f}}{T_{\mathrm{K},i}} \implies 2 = \frac{T_{\mathrm{K},f}}{T_{\mathrm{K},i}} $$
  
Thus:  

$$ T_{\mathrm{K},f} = 2 T_{\mathrm{K},i} $$
  

**Step 4: Convert final temperature back to Celsius**  

$$ T_f = T_{\mathrm{K},f} - C $$
  
Substitute $T_{\mathrm{K},f} = 2 T_{\mathrm{K},i}$:  

$$ T_f = 2 T_{\mathrm{K},i} - C $$
  
Replace $T_{\mathrm{K},i}$ with $T_i + C$:  

$$ T_f = 2(T_i + C) - C = 2T_i + 2C - C $$
  
Simplify:  

$$ T_f = 2T_i + C $$
  

The final temperature in degrees Celsius is $2T_i + C$.

## Answer
$$\boxed{2T_i + C}$$

------
## Problem 3
##### Background
In the early 19th century, Amedeo Avogadro proposed that equal volumes of gases at the same temperature and pressure contain equal numbers of molecules. This principle revolutionized gas stoichiometry and enabled the determination of relative molecular masses. Modern gas analysis relies on this principle, with applications in environmental monitoring (e.g., identifying pollutants) and industrial gas production. Standard Temperature and Pressure (STP) is defined as 0°C (273 K) and 1 atm, where 1 mole of any ideal gas occupies a volume of $V_m = 22.4$ L.

##### Knowledge Points Tested
- Application of Avogadro's principle to relate volume, moles, and molar mass
- Understanding of STP conditions and molar volume
- Derivation of molar mass from mass-volume measurements

##### Intradisciplinary Connections
- Connects to the ideal gas law ($PV = nRT$) by showing how molar volume at STP is derived from fundamental constants
- Relates to gas density calculations and Dalton's law of partial pressures

##### Interdisciplinary Connections
- **Environmental Science**: Gas identification is crucial for monitoring air quality and greenhouse emissions
- **Engineering**: Used in designing gas storage systems and chemical reactors
- **Forensics**: Applied to identify unknown substances in arson investigations

##### Real-World Applications
- Determining the molar mass of an unknown gas is essential in chemical manufacturing (e.g., quality control of industrial gases) and climate science (e.g., analyzing atmospheric composition from air samples)

##### Problem Statement
A sealed container holds 4.4 g of an unknown pure gas occupying 2.24 L at STP. Using Avogadro's principle and the molar volume of an ideal gas at STP ($V_m$), derive an expression for the molar mass ($M$) of the gas in terms of the given mass ($m$), sample volume ($V$), and molar volume ($V_m$). Then compute $M$ explicitly. Express your final answer as an integer in grams per mole, providing only the numerical value.

## Solution
**Step 1: Relate sample volume to moles using Avogadro's principle**  
Avogadro's principle states that at STP, the ratio of a gas sample's volume to its molar volume equals the number of moles ($n$):  
$$ n = \frac{V}{V_m} $$  
Given:  
- Sample volume $V = 2.24  \text{L}$  
- Molar volume at STP $V_m = 22.4  \text{L/mol}$  

**Step 2: Express molar mass**  
Molar mass ($M$) is defined as mass per mole:  
$$ M = \frac{m}{n} $$  
Substitute the expression for $n$ from Step 1:  
$$ M = \frac{m}{V / V_m} = \frac{m \cdot V_m}{V} $$  
This is the general expression for molar mass in terms of $m$, $V$, and $V_m$.

**Step 3: Substitute values and compute**  
Given:  
- Mass $m = 4.4  \text{g}$  
- $V = 2.24  \text{L}$  
- $V_m = 22.4  \text{L/mol}$  

Substitute into the derived formula:  
$$ M = \frac{(4.4) \cdot (22.4)}{2.24} $$  

Simplify the expression:  
$$ M = \frac{4.4}{2.24} \cdot 22.4 $$  
First, compute $\frac{4.4}{2.24}$:  
$$ \frac{4.4}{2.24} = \frac{44/10}{224/100} = \frac{44}{10} \cdot \frac{100}{224} = \frac{4400}{2240} = \frac{440}{224} = \frac{55}{28} $$  
Now multiply by 22.4:  
$$ M = \left( \frac{55}{28} \right) \cdot 22.4 $$  
Note that $22.4 = \frac{224}{10} = \frac{112}{5}$, so:  
$$ M = \frac{55}{28} \cdot \frac{224}{10} = \frac{55 \cdot 224}{28 \cdot 10} $$  
Simplify by canceling common factors:  
- 224 ÷ 28 = 8  
- 55 and 10 share a factor of 5: 55 ÷ 5 = 11, 10 ÷ 5 = 2  
$$ M = \frac{55 \cdot 8}{10} = \frac{440}{10} = 44  \text{g/mol} $$  

**Verification via moles calculation**  
Number of moles in the sample:  
$$ n = \frac{V}{V_m} = \frac{2.24  \text{L}}{22.4  \text{L/mol}} = 0.100  \text{mol} $$  
Molar mass:  
$$ M = \frac{m}{n} = \frac{4.4  \text{g}}{0.100  \text{mol}} = 44  \text{g/mol} $$  
Both methods yield the same result.

## Answer
$$\boxed{44}$$

------
# instantaneous and average power calculations

## Problem 0
##### Background
In engineering and physics, understanding how power is delivered by time-dependent forces is crucial for designing systems like electric motors, rocket thrusters, or even sports equipment. Consider a block of mass $m$ initially at rest on a frictionless horizontal surface. Starting at $t=0$, a force $F(t) = c t$ is applied in the direction of motion, where $c$ is a constant (with units N/s). This models real-world scenarios where force ramps up linearly, such as in controlled acceleration systems.

##### Knowledge Points Tested
- Newton's second law for time-dependent forces
- Integration to determine velocity from acceleration
- Definition of instantaneous power ($P = \vec{F} \cdot \vec{v}$)

##### Intradisciplinary Connections
Connects to kinematics (velocity/acceleration relationships) and work-energy theorem (since power is the time derivative of work).

##### Interdisciplinary Connections
Relevant to mechanical engineering (actuator design) and control theory (time-dependent system responses).

##### Real-World Applications
Used in elevator systems where smooth acceleration is achieved by linearly increasing motor torque, or in electric vehicles during controlled startup sequences to avoid jerks.

##### Problem Statement
Derive an expression for the instantaneous power $P(T)$ delivered to the block at time $t = T$. Express your answer **solely in terms of** $m$, $c$, and $T$.  

**Answer formatting rules**:  
- Your final expression must be simplified and use the variables $m$, $c$, and $T$ exactly as defined.  
- Use $\frac{}{}$ for fractions.  
- Do **not** substitute numerical values or include units.  
- Example of valid format: $\frac{c^2 T^3}{2m}$

## Solution
**Step 1: Apply Newton's second law**  
The force causes acceleration:  
$$F(t) = m a(t) \implies c t = m \frac{dv}{dt}$$  
Solving for acceleration:  
$$\frac{dv}{dt} = \frac{c t}{m}$$  

**Step 2: Find velocity by integrating acceleration**  
Integrate with initial condition $v(0) = 0$:  
$$\int_0^{v(t)} dv' = \int_0^t \frac{c}{m} t'  dt'$$  
$$v(t) = \frac{c}{m} \int_0^t t'  dt' = \frac{c}{m} \left[ \frac{(t')^2}{2} \right]_0^t$$  
$$v(t) = \frac{c t^2}{2m}$$  

**Step 3: Express instantaneous power**  
Power is force multiplied by velocity:  
$$P(t) = F(t) \cdot v(t) = (c t) \cdot \left( \frac{c t^2}{2m} \right)$$  
$$P(t) = \frac{c^2 t^3}{2m}$$  

**Step 4: Evaluate at $t = T$**  
$$P(T) = \frac{c^2 T^3}{2m}$$  
This is the instantaneous power delivered at time $T$.

## Answer
$$\boxed{\frac{c^{2} T^{3}}{2m}}$$

------
## Problem 1
##### Background
In construction and logistics, cranes are essential for lifting heavy objects. Modern crane systems often employ a two-stage lifting strategy: an initial acceleration phase to reach a desired speed, followed by a constant velocity phase to minimize energy consumption and ensure stability. This problem explores the power requirements of such a crane lifting a crate against gravity, accounting for both acceleration and constant velocity phases. Power calculations must consider the total work done and the time taken, requiring integration of kinematic principles and energy concepts.

##### Knowledge Points Tested
1. Newton's second law for constant force scenarios
2. Kinematic equations under constant acceleration
3. Work-energy theorem and power definitions (instantaneous and average)
4. Displacement and velocity relationships
5. Algebraic manipulation of multivariable expressions

##### Intradisciplinary Connections
- Relates force and motion dynamics to energy transfer (mechanics to thermodynamics)
- Connects constant acceleration kinematics to work calculations
- Demonstrates how power integrates force, displacement, and time variables

##### Interdisciplinary Connections
- **Engineering**: Crane motor specification and energy efficiency optimization
- **Control Systems**: Switching logic between acceleration and constant velocity phases
- **Environmental Science**: Energy consumption analysis in industrial machinery

##### Real-World Applications
- Optimizing elevator systems in high-rise buildings
- Designing warehouse robotic arms for efficient package handling
- Calculating fuel requirements for helicopter lift operations
- Assessing power grid demands for industrial cranes in shipyards

##### Problem Statement
A crane lifts a crate of mass $m$ from rest on the ground. The crane's motor initially applies a constant upward force $F$ (where $F > mg$ and $g$ is the acceleration due to gravity). When the crate reaches speed $v_0$, the crane switches to maintaining constant speed $v_0$. The motion is purely vertical with no air resistance. Determine the average power delivered by the crane's motor during the first $T$ seconds of operation, assuming $T > \frac{mv_0}{F - mg}$ (ensuring the constant-velocity phase has begun). Express your answer analytically in terms of $m$, $g$, $F$, $v_0$, and $T$. Use standard mathematical notation and simplify the expression completely. Do not substitute numerical values for any parameter.

**Answer format requirements**:  
- Express all powers using the caret symbol with braces (e.g., $v_0^2$ as `v_{0}^{2}`)  
- Use `\frac` for fractions (e.g., $\frac{1}{2}$)  
- Omit units in the final boxed answer

## Solution
**Step 1: Determine kinematics during acceleration phase**  
The crate starts at rest. During phase 1 (acceleration phase), the net upward force is $F_{\text{net}} = F - mg$. By Newton's second law:  
$$ a = \frac{F_{\text{net}}}{m} = \frac{F - mg}{m} $$  
Time to reach $v_0$:  
$$ v_0 = a t_1 \implies t_1 = \frac{v_0}{a} = \frac{m v_0}{F - mg} $$  
Displacement during phase 1:  
$$ s_1 = \frac{1}{2} a t_1^2 = \frac{1}{2} \left( \frac{F - mg}{m} \right) \left( \frac{m v_0}{F - mg} \right)^2 = \frac{m v_0^2}{2(F - mg)} $$  

**Step 2: Calculate work done in acceleration phase**  
Work done by crane motor (constant force $F$):  
$$ W_1 = F \cdot s_1 = F \cdot \frac{m v_0^2}{2(F - mg)} = \frac{F m v_0^2}{2(F - mg)} $$  

**Step 3: Determine kinematics during constant-velocity phase**  
Duration of phase 2:  
$$ t_2 = T - t_1 = T - \frac{m v_0}{F - mg} $$  
Displacement during phase 2 (constant velocity $v_0$):  
$$ s_2 = v_0 t_2 = v_0 \left( T - \frac{m v_0}{F - mg} \right) $$  

**Step 4: Calculate work done in constant-velocity phase**  
At constant velocity, net force is zero, so crane force equals weight:  
$$ F_2 = mg $$  
Work done by crane motor:  
$$ W_2 = F_2 \cdot s_2 = mg \cdot v_0 \left( T - \frac{m v_0}{F - mg} \right) $$  

**Step 5: Compute total work and average power**  
Total work done:  
$$ W_{\text{total}} = W_1 + W_2 = \frac{F m v_0^2}{2(F - mg)} + mg v_0 T - \frac{m^2 g v_0^2}{F - mg} $$  
Combine like terms:  
$$ W_{\text{total}} = mg v_0 T + \frac{m v_0^2}{F - mg} \left( \frac{F}{2} - mg \right) $$  
Simplify the coefficient:  
$$ \frac{F}{2} - mg = \frac{F - 2mg}{2} $$  
Thus:  
$$ W_{\text{total}} = mg v_0 T + \frac{m v_0^2 (F - 2mg)}{2(F - mg)} $$  
Average power:  
$$ P_{\text{avg}} = \frac{W_{\text{total}}}{T} = mg v_0 + \frac{m v_0^2 (F - 2mg)}{2T(F - mg)} $$  

**Final simplified expression**:  
The average power delivered by the crane motor over time $T$ is:  
$$ P_{\text{avg}} = mgv_{0} + \frac{mv_{0}^{2}\left(F - 2mg\right)}{2T\left(F - mg\right)} $$

## Answer
$$\boxed{mgv_{0} + \frac{mv_{0}^{2}\left(F - 2mg\right)}{2T\left(F - mg\right)}}$$

------
## Problem 2
##### Background
In automotive engineering, the performance of electric vehicles is often analyzed under constant power output to optimize acceleration profiles. Consider an electric car of mass $ m $ accelerating from rest on a straight horizontal road. The car's motor delivers a constant power $ P $. Air resistance is modeled as a drag force proportional to the car's speed: $ F_{\text{drag}} = -k v $, where $ k $ is the drag coefficient. This force opposes the motion, and rolling resistance is negligible.

##### Knowledge Points Tested
- Instantaneous power: $ P = \vec{F} \cdot \vec{v} $.
- Newton's second law for variable forces.
- Separation of variables in differential equations.
- Work done as the integral of power over time.
- Logarithmic integration and its application in dynamics.

##### Intradisciplinary Connections
This problem connects power and energy concepts with Newtonian mechanics, requiring the setup and solution of a differential equation to model motion under resistive forces. It reinforces the work-energy theorem in non-conservative systems.

##### Interdisciplinary Connections
The drag force model draws from fluid dynamics, while the constant power constraint relates to electrical engineering (battery discharge characteristics) and environmental science (energy efficiency in transportation).

##### Real-World Applications
Constant-power acceleration profiles are used in electric vehicle control systems to maximize range. The drag model approximates real-world aerodynamics, crucial for performance simulations in automotive design and sustainable energy research.

##### Problem Statement
The car starts from rest. Derive an expression for the work done by the motor when the car reaches a speed $ v $. Express your answer symbolically in terms of $ m $, $ k $, $ P $, and $ v $. Ensure the expression is time-independent.  

##### Answer Formatting Rules  
- Provide an analytic expression using $ m $, $ k $, $ P $, and $ v $.  
- Use `\ln` for the natural logarithm (e.g., `\ln(x)`). Do not use `\log` for natural log.  
- Use `\exp(x)` for exponential functions if needed.  
- Keep the expression exact; no numerical approximations.

## Solution
Begin with Newton's second law. The net force along the direction of motion is the motor force $ F_m $ minus the drag force $ k v $:  

$$ m \frac{dv}{dt} = F_m - k v $$
  

The motor delivers constant power $ P $, so:  

$$ P = F_m v \implies F_m = \frac{P}{v} $$
  
Substitute $ F_m $:  

$$ m \frac{dv}{dt} = \frac{P}{v} - k v $$
  

Rearrange to separate variables:  

$$ m  dv = \left( \frac{P}{v} - k v \right) dt $$
  

$$ dt = \frac{m  dv}{\dfrac{P}{v} - k v} = \frac{m v  dv}{P - k v^2} $$
  

Integrate from initial state (rest) to final state (speed $ v $):  

$$ \int_0^t dt = \int_0^v \frac{m v}{P - k v^2}  dv $$
  
The left side is $ t $. For the right side, use the substitution $ u = P - k v^2 $, so $ du = -2k v  dv $ and $ v  dv = -\frac{du}{2k} $. Adjust limits: when $ v = 0 $, $ u = P $; when $ v = v $, $ u = P - k v^2 $.  

$$ t = \int_P^{P - k v^2} \frac{m}{u} \cdot \left( -\frac{du}{2k} \right) = -\frac{m}{2k} \int_P^{P - k v^2} \frac{du}{u} = -\frac{m}{2k} \left[ \ln|u| \right]_P^{P - k v^2} $$
  

$$ t = -\frac{m}{2k} \left( \ln|P - k v^2| - \ln|P| \right) = \frac{m}{2k} \ln \left( \frac{P}{P - k v^2} \right) $$
  

The work done by the motor is the integral of power over time. Since power is constant:  

$$ W = \int_0^t P  dt = P t $$
  
Substitute the expression for $ t $:  

$$ W = P \cdot \frac{m}{2k} \ln \left( \frac{P}{P - k v^2} \right) = \frac{m P}{2k} \ln \left( \frac{P}{P - k v^2} \right) $$
  

This gives the work done as a function of $ v $, independent of time.

## Answer
$$\boxed{\dfrac{m P}{2k} \ln \left( \dfrac{P}{P - k v^{2}} \right)}$$

------
# Lenz's law for induced current direction

## Problem 0
##### Background
A circular loop of radius $R$ is initially entirely within a uniform magnetic field of magnitude $B$, directed perpendicularly into the plane of the loop. The magnetic field occupies the region $x \leq 0$, and the loop is centered at $x = -R$ at $t = 0$. Starting at $t = 0$, the loop is pulled in the positive $x$-direction with constant speed $v$. As the loop exits the field, the magnetic flux through it changes, inducing an electromotive force (EMF) according to Faraday's law. The direction of the induced current is defined as positive when clockwise.

##### Knowledge Points Tested
1. Faraday's law of induction: $\mathcal{E} = -\frac{d\Phi_B}{dt}$, where $\Phi_B$ is the magnetic flux.
2. Magnetic flux calculation: $\Phi_B = \mathbf{B} \cdot \mathbf{A}$ for uniform $\mathbf{B}$ perpendicular to the loop.
3. Geometry of a circular segment to determine the area $A(t)$ inside the magnetic field region.
4. Differentiation of inverse trigonometric functions and application of the chain rule.
5. Lenz's law to determine the direction of induced current.

##### Intradisciplinary Connections
- Related to motional EMF and the Lorentz force law, as the motion of the loop through the field induces an EMF.
- Connects to energy conservation principles, as the work done to pull the loop equals the energy dissipated by the induced current.

##### Interdisciplinary Connections
- Engineering: Models scenarios like extracting sensors from MRI machines or electromagnetic braking systems.
- Mathematics: Involves derivatives, inverse trigonometric functions, and optimization (finding maximum EMF).

##### Real-World Applications
- Magnetic damping in high-speed trains, where loops moving out of magnetic fields generate opposing currents to slow motion.
- Eddy current brakes in roller coasters and industrial equipment, utilizing induced currents for controlled deceleration.

##### Problem Statement
A circular loop of radius $R$ is initially fully immersed in a uniform magnetic field $B$ (directed into the page). At $t = 0$, the loop begins moving with constant velocity $v$ in the $+x$-direction out of the field region $x \leq 0$. Derive the induced EMF $\mathcal{E}(t)$ as a function of time during the exit process ($0 \leq t \leq R/v$), assuming clockwise current is positive. Express $\mathcal{E}(t)$ symbolically in terms of $B$, $R$, $v$, and $t$.  
*Hint: The distance from the center of the loop to the field boundary $x=0$ is $R - v t$ at time $t$.*

## Solution
**Step 1: Define the area inside the magnetic field**  
At time $t$, the center of the loop is at $x = -R + v t$. The distance from the center to the field boundary $x=0$ is $d = R - v t$. The portion of the loop inside $x \leq 0$ is a circular segment. The chord at $x=0$ subtends an angle $2\theta$ at the center, where $\cos \theta = \frac{d}{R} = 1 - \frac{v t}{R}$.  
The area of the circular segment inside the field is:  
$$A(t) = R^2 \cos^{-1}\left(1 - \frac{v t}{R}\right) - (R - v t) \sqrt{R^2 - (R - v t)^2}$$  
*Note: This is the area of the minor segment. Since the loop is exiting, the majority of the loop is inside the field initially, so the area inside the field is the total area minus the minor segment:*  
$$A_{\text{in}}(t) = \pi R^2 - \left[ R^2 \cos^{-1}\left(1 - \frac{v t}{R}\right) - (R - v t) \sqrt{R^2 - (R - v t)^2} \right]$$  
Simplify the expression under the square root:  
$$\sqrt{R^2 - (R - v t)^2} = \sqrt{2 R v t - (v t)^2} = \sqrt{v t (2 R - v t)}$$  
Thus:  
$$A_{\text{in}}(t) = \pi R^2 - R^2 \cos^{-1}\left(1 - \frac{v t}{R}\right) + (R - v t) \sqrt{v t (2 R - v t)}$$

**Step 2: Compute the magnetic flux**  
The magnetic flux through the loop is:  
$$\Phi_B(t) = B \cdot A_{\text{in}}(t) = B \left[ \pi R^2 - R^2 \cos^{-1}\left(1 - \frac{v t}{R}\right) + (R - v t) \sqrt{v t (2 R - v t)} \right]$$  
Since $\mathbf{B}$ is uniform and perpendicular to the loop, the dot product simplifies to $B A_{\text{in}}(t)$.

**Step 3: Apply Faraday's law**  
The induced EMF is:  
$$\mathcal{E} = -\frac{d\Phi_B}{dt} = -B \frac{d}{dt} \left[ \pi R^2 - R^2 \cos^{-1}\left(1 - \frac{v t}{R}\right) + (R - v t) \sqrt{v t (2 R - v t)} \right]$$  
Compute the derivative term by term:  
- $\frac{d}{dt}(\pi R^2) = 0$.  
- Let $u = 1 - \frac{v t}{R}$, so $\frac{du}{dt} = -\frac{v}{R}$. The derivative of $\cos^{-1}(u)$ is $-\frac{1}{\sqrt{1 - u^2}} \frac{du}{dt}$:  
  $$\frac{d}{dt} \left[ \cos^{-1}\left(1 - \frac{v t}{R}\right) \right] = -\frac{1}{\sqrt{1 - \left(1 - \frac{v t}{R}\right)^2}} \left(-\frac{v}{R}\right) = \frac{v}{R} \frac{1}{\sqrt{\frac{2 v t}{R} - \left(\frac{v t}{R}\right)^2}} = \frac{v}{R} \frac{1}{\sqrt{\frac{v t}{R} \left(2 - \frac{v t}{R}\right)}}$$  
  Simplify:  
  $$\sqrt{\frac{v t}{R} \left(2 - \frac{v t}{R}\right)} = \sqrt{\frac{v t (2 R - v t)}{R^2}} = \frac{ \sqrt{v t (2 R - v t)} }{R}$$  
  Thus:  
  $$\frac{d}{dt} \left[ \cos^{-1}\left(1 - \frac{v t}{R}\right) \right] = \frac{v}{R} \cdot \frac{R}{ \sqrt{v t (2 R - v t)} } = \frac{v}{ \sqrt{v t (2 R - v t)} }$$  
- For the last term, let $f(t) = (R - v t) \sqrt{v t (2 R - v t)}$. Use the product rule:  
  $$\frac{df}{dt} = \frac{d}{dt}(R - v t) \cdot \sqrt{v t (2 R - v t)} + (R - v t) \cdot \frac{d}{dt} \left[ \sqrt{v t (2 R - v t)} \right]$$  
  First, $\frac{d}{dt}(R - v t) = -v$.  
  Second, let $g(t) = v t (2 R - v t) = 2 R v t - v^2 t^2$, so $\sqrt{g(t)}$. Then:  
  $$\frac{d}{dt} \sqrt{g(t)} = \frac{1}{2 \sqrt{g(t)}} \cdot g'(t) = \frac{1}{2 \sqrt{v t (2 R - v t)}} \cdot (2 R v - 2 v^2 t) = \frac{v (R - v t)}{ \sqrt{v t (2 R - v t)} }$$  
  Thus:  
  $$\frac{df}{dt} = -v \sqrt{v t (2 R - v t)} + (R - v t) \cdot \frac{v (R - v t)}{ \sqrt{v t (2 R - v t)} } = -v \sqrt{v t (2 R - v t)} + \frac{v (R - v t)^2}{ \sqrt{v t (2 R - v t)} }$$  
  Combine terms:  
  $$\frac{df}{dt} = \frac{ -v \left[ v t (2 R - v t) \right] + v (R - v t)^2 }{ \sqrt{v t (2 R - v t)} } = \frac{ v \left[ -(2 R v t - v^2 t^2) + (R^2 - 2 R v t + v^2 t^2) \right] }{ \sqrt{v t (2 R - v t)} }$$  
  Simplify the numerator:  
  $$-(2 R v t - v^2 t^2) + R^2 - 2 R v t + v^2 t^2 = R^2 - 4 R v t + 2 v^2 t^2$$  
  This is incorrect; recheck:  
  $$-2Rvt + v^2 t^2 + R^2 - 2Rvt + v^2 t^2 = R^2 - 4Rvt + 2v^2 t^2$$  
  However, this does not match the earlier expression. Instead, use the simplified form:  
  $$\frac{df}{dt} = -v \sqrt{v t (2 R - v t)} + \frac{v (R - v t)^2}{\sqrt{v t (2 R - v t)}} = v \left[ \frac{ (R - v t)^2 - v t (2 R - v t) }{ \sqrt{v t (2 R - v t)} } \right]$$  
  Expand the numerator:  
  $$(R^2 - 2 R v t + v^2 t^2) - (2 R v t - v^2 t^2) = R^2 - 4 R v t + 2 v^2 t^2$$  
  Thus:  
  $$\frac{df}{dt} = v \frac{ R^2 - 4 R v t + 2 v^2 t^2 }{ \sqrt{v t (2 R - v t)} }$$  

**Step 4: Combine derivatives**  
The derivative of $\Phi_B$ is:  
$$\frac{d\Phi_B}{dt} = B \left[ -R^2 \cdot \frac{v}{ \sqrt{v t (2 R - v t)} } + \frac{df}{dt} \right] = B \left[ -\frac{R^2 v}{ \sqrt{v t (2 R - v t)} } + v \frac{ R^2 - 4 R v t + 2 v^2 t^2 }{ \sqrt{v t (2 R - v t)} } \right]$$  
Combine the terms over the common denominator:  
$$\frac{d\Phi_B}{dt} = B v \frac{ -R^2 + R^2 - 4 R v t + 2 v^2 t^2 }{ \sqrt{v t (2 R - v t)} } = B v \frac{ -4 R v t + 2 v^2 t^2 }{ \sqrt{v t (2 R - v t)} } = B v \cdot \frac{ 2 v t (v t - 2 R) }{ \sqrt{v t (2 R - v t)} }$$  
Simplify:  
$$2 v t (v t - 2 R) = -2 v t (2 R - v t)$$  
Thus:  
$$\frac{d\Phi_B}{dt} = B v \cdot \frac{ -2 v t (2 R - v t) }{ \sqrt{v t (2 R - v t)} } = -2 B v^{3/2} t \sqrt{2 R - v t} \cdot \frac{ \sqrt{2 R - v t} }{ \sqrt{t} } \cdot \sqrt{v} \quad \text{(incorrect grouping)}$$  
Better:  
$$\frac{ -2 v t (2 R - v t) }{ \sqrt{v t (2 R - v t)} } = -2 \sqrt{v} \cdot \sqrt{t} \cdot \sqrt{2 R - v t}$$  
because:  
$$\frac{ v t (2 R - v t) }{ \sqrt{v t (2 R - v t)} } = \sqrt{v t (2 R - v t)}$$  
But here the numerator is $-2 v t (2 R - v t)$, so:  
$$\frac{ -2 v t (2 R - v t) }{ \sqrt{v t (2 R - v t)} } = -2 \sqrt{v t (2 R - v t)}$$  
Thus:  
$$\frac{d\Phi_B}{dt} = B v \cdot \left( -2 \sqrt{v t (2 R - v t)} \right) = -2 B v \sqrt{v t (2 R - v t)}$$  

**Step 5: Apply Faraday's law for EMF**  
$$\mathcal{E} = -\frac{d\Phi_B}{dt} = - \left[ -2 B v \sqrt{v t (2 R - v t)} \right] = 2 B v \sqrt{v t (2 R - v t)}$$  
Simplify:  
$$\mathcal{E}(t) = 2 B v \sqrt{2 R v t - v^2 t^2} = 2 B v^{3/2} \sqrt{ t (2 R - v t) }$$  
*Direction justification:* At $t > 0$, the flux into the page decreases as the loop exits. By Lenz's law, the induced current opposes this change by creating a magnetic field into the page, which requires a clockwise current (positive as defined).

**Step 6: Final expression**  
The induced EMF is:  
$$\mathcal{E}(t) = 2 B v \sqrt{v t (2 R - v t)}$$  
for $0 \leq t \leq R/v$. At $t = 0$ and $t = R/v$, $\mathcal{E} = 0$; it peaks in between.

## Answer
$$\boxed{2 B v \sqrt{v t \left(2 R - v t\right)}}$$

------
## Problem 1
##### Background
A bar magnet with magnetic moment $m$ moves with constant velocity $v$ toward a stationary circular coil of area $A$ and resistance $R$. The motion occurs along the coil's axis, with the magnet's north pole leading. The magnetic field along the axis of the magnet at a distance $d$ from its center is given by $B = \frac{\mu_0}{4\pi} \frac{2m}{d^3}$, where $\mu_0$ is the permeability of free space. As the magnet approaches, the changing magnetic flux induces an electromotive force (emf) in the coil, resulting in an induced current governed by Faraday's law and Lenz's law.

##### Knowledge Points Tested
1. Faraday's law of induction: relating induced emf to the rate of change of magnetic flux.
2. Lenz's law: determining the direction of induced current to oppose the change in magnetic flux.
3. Magnetic flux calculation for a uniform field perpendicular to a planar coil.
4. Differentiation of the magnetic field expression with respect to distance and time using the chain rule.
5. Relationship between induced emf, current, and resistance (Ohm's law).

##### Intradisciplinary Connections
- Connects magnetic fields of dipoles (bar magnets) to electromagnetic induction.
- Integrates kinematics (constant velocity motion) with time-dependent flux changes.

##### Interdisciplinary Connections
- Calculus: application of the chain rule for differentiation.
- Physics: unification of mechanics (motion) and electromagnetism.

##### Real-World Applications
- Proximity sensors: detecting the approach of metallic objects using induced currents.
- Energy harvesting: converting kinetic energy from motion into electrical energy via electromagnetic induction (e.g., in some wearable devices).
- Eddy current brakes: induced currents create opposing magnetic fields to decelerate moving objects.

##### Problem Statement
Derive an expression for the magnitude of the induced current in the coil at the instant when the magnet is at a distance $d_0$ from the center of the coil. Assume the magnetic field is uniform over the coil's area and perpendicular to its plane. Express your answer symbolically in terms of $m$, $\mu_0$, $v$, $A$, $R$, and $d_0$. Additionally, state the direction of the induced current (clockwise or counterclockwise) when viewed from the magnet's side. For the current magnitude, use the exact symbolic form without numerical substitution.

## Solution
The magnitude of the induced current $I$ is derived using Faraday's law and Ohm's law. The steps are as follows:

1. **Magnetic flux through the coil:**  
   The magnetic field $B$ at distance $d$ is $B = \frac{\mu_0}{4\pi} \frac{2m}{d^3} = \frac{\mu_0 m}{2\pi d^3}$.  
   Since the field is uniform and perpendicular to the coil, the magnetic flux $\Phi_B$ is:  
   $$
   \Phi_B = B \cdot A = \frac{\mu_0 m A}{2\pi d^3}.
   $$

2. **Rate of change of flux with distance:**  
   The magnet moves toward the coil at velocity $v$, so the distance $d$ decreases with time. Thus, $d$ is a function of time $t$:  
   $$
   \frac{dd}{dt} = -v \quad \text{(negative because distance decreases)}.
   $$  
   Differentiate $\Phi_B$ with respect to $d$:  
   $$
   \frac{d\Phi_B}{dd} = \frac{\mu_0 m A}{2\pi} \cdot \left(-3\right) d^{-4} = -\frac{3\mu_0 m A}{2\pi d^4}.
   $$

3. **Rate of change of flux with time (chain rule):**  
   Apply the chain rule:  
   $$
   \frac{d\Phi_B}{dt} = \frac{d\Phi_B}{dd} \cdot \frac{dd}{dt} = \left(-\frac{3\mu_0 m A}{2\pi d^4}\right) \cdot (-v) = \frac{3\mu_0 m A v}{2\pi d^4}.
   $$

4. **Induced emf (Faraday's law):**  
   The magnitude of the induced emf $\mathcal{E}$ is:  
   $$
   \mathcal{E} = \left|\frac{d\Phi_B}{dt}\right| = \frac{3\mu_0 m A v}{2\pi d^4}.
   $$

5. **Induced current (Ohm's law):**  
   The magnitude of the induced current $I$ is:  
   $$
   I = \frac{\mathcal{E}}{R} = \frac{3\mu_0 m A v}{2\pi R d^4}.
   $$  
   At the specific distance $d = d_0$:  
   $$
   I = \frac{3\mu_0 m A v}{2\pi R d_0^4}.
   $$

6. **Direction of induced current (Lenz's law):**  
   The magnet approaches with its north pole leading, increasing the magnetic flux through the coil (as $d$ decreases). To oppose this increase, the induced current must create a magnetic field directed away from the magnet. When viewed from the magnet's side, this requires a **counterclockwise** current in the coil (producing a north pole facing the magnet, inducing repulsion).

## Answer
$$\boxed{\frac{3 \mu_{0} m A v}{2 \pi R d_{0}^{4}}}$$

------
## Problem 2
##### Background
A square loop of wire rotates at a constant angular velocity in a uniform magnetic field. The axis of rotation is perpendicular to the magnetic field direction. As the loop rotates, the magnetic flux through it changes, inducing an electromotive force (EMF) due to electromagnetic induction. This setup models the core principle behind alternating current (AC) generators, which convert mechanical energy into electrical energy.

##### Knowledge Points Tested
1. Faraday's law of electromagnetic induction.
2. Magnetic flux through a planar loop.
3. Lenz's law for determining the direction of induced current (implicit in the sign of EMF).
4. Differentiation of trigonometric functions with respect to time.

##### Intradisciplinary Connections
- Relates to the concept of motional EMF in moving conductors.
- Connects to AC generator design, where rotational motion produces sinusoidal voltage.

##### Interdisciplinary Connections
- **Mathematics**: Differentiation of composite functions (chain rule) and trigonometric identities.
- **Engineering**: Application in designing electrical generators and motors.

##### Real-World Applications
- **AC Generators**: Used in power plants to generate electricity from mechanical rotation (e.g., hydroelectric turbines, wind turbines).
- **Sensors**: Inductive sensors measure rotation speed by detecting induced EMF in rotating coils.

##### Problem Statement
Consider a square loop with side length $a$, rotating at a constant angular velocity $\omega$ in a uniform magnetic field of magnitude $B$. The axis of rotation is perpendicular to $\vec{B}$, and the angle $\theta$ between the magnetic field and the normal to the loop is given by $\theta = \omega t$. Derive an expression for the induced electromotive force (EMF) $\mathcal{E}(t)$ as a function of time. Express your answer symbolically in terms of $a$, $B$, $\omega$, and $t$.  

**Follow these steps**:  
1. Write the expression for magnetic flux $\Phi_B$ through the loop.  
2. Apply Faraday's law to find $\mathcal{E}(t)$.  
3. Simplify the expression to show explicit time dependence.  

**Answer format requirements**:  
- The final answer must be an analytic expression in terms of the given parameters.  
- Use $\sin$ for sine function, and express angles in radians (omit the radian unit).  
- Write all exponents using the caret symbol with braces (e.g., $a^2$ as `a^{2}`).  
- Do **not** include units in the final answer.

## Solution
To derive the induced EMF $\mathcal{E}(t)$, we apply Faraday's law and the definition of magnetic flux.

**Step 1: Magnetic flux $\Phi_B$**  
The magnetic flux through the loop is given by:  

$$
\Phi_B = \vec{B} \cdot \vec{A} = BA \cos\theta,
$$
  
where $A$ is the area of the loop, and $\theta$ is the angle between $\vec{B}$ and the normal to the loop. For a square loop, $A = a^2$. Given $\theta = \omega t$, we substitute:  

$$
\Phi_B = B a^{2} \cos(\omega t).
$$


**Step 2: Apply Faraday's law**  
Faraday's law states that the induced EMF is the negative rate of change of magnetic flux:  

$$
\mathcal{E} = -\frac{d\Phi_B}{dt}.
$$
  
Substitute $\Phi_B = B a^{2} \cos(\omega t)$:  

$$
\mathcal{E} = -\frac{d}{dt} \left[ B a^{2} \cos(\omega t) \right].
$$
  
Since $B$ and $a^{2}$ are constants, we factor them out:  

$$
\mathcal{E} = -B a^{2} \frac{d}{dt} \left[ \cos(\omega t) \right].
$$


**Step 3: Differentiation and simplification**  
Differentiate $\cos(\omega t)$ using the chain rule:  

$$
\frac{d}{dt} \left[ \cos(\omega t) \right] = -\omega \sin(\omega t).
$$
  
Substitute this result:  

$$
\mathcal{E} = -B a^{2} \left[ -\omega \sin(\omega t) \right] = B a^{2} \omega \sin(\omega t).
$$
  
This is the induced EMF as a function of time.

**Direction of induced current (Lenz's law)**:  
The $\sin(\omega t)$ term indicates that the EMF alternates sign, reversing direction periodically. At $t = 0$, $\theta = 0$, and $\Phi_B$ is maximum. As $\theta$ increases, $\Phi_B$ decreases, so the induced current opposes this change by creating a magnetic field in the direction of $\vec{B}$ (consistent with the positive sign when $\sin(\omega t) > 0$).

Thus, the derived expression is:  

$$
\mathcal{E}(t) = B a^{2} \omega \sin(\omega t).
$$

## Answer
$$\boxed{B a^{2} \omega \sin(\omega t)}$$

------
## Problem 3
##### Background
A conducting wire is shaped into an equilateral triangle with side length $a$ and total resistance $R$. The triangle moves at a constant velocity $v$ to the right into a region with a uniform magnetic field $B$ directed perpendicular to the loop's plane (into the page). The magnetic field region is extensive, and the loop is oriented such that one side (the base) is perpendicular to the velocity vector, acting as the leading edge during entry. As the loop enters the field, the immersed area changes, inducing an electromotive force (EMF) and current due to Faraday's law. Lenz's law determines the current direction, with clockwise defined as positive.

##### Knowledge Points Tested
1. Faraday's law of induction: $\mathcal{E} = -\frac{d\Phi_B}{dt}$, where $\Phi_B$ is magnetic flux.
2. Lenz's law for induced current direction.
3. Geometric properties of equilateral triangles and similar figures.
4. Relationship between induced EMF and current: $I = \frac{\mathcal{E}}{R}$.

##### Intradisciplinary Connections
This problem connects changing magnetic flux to geometric transformations (similar triangles) and kinematics (constant velocity). It reinforces how flux change depends on the rate of area variation within the field.

##### Interdisciplinary Connections
Geometry: Calculating the immersed area as a function of penetration depth requires similarity ratios and area scaling. Physics: The scenario models real-world electromagnetic induction in moving conductors, linking mechanics and electromagnetism.

##### Real-World Applications
Similar principles apply in magnetic braking systems, where induced currents oppose motion to decelerate objects (e.g., roller coasters or trains). They are also fundamental in dynamos and generators converting mechanical motion to electrical energy.

##### Problem Statement
The equilateral triangular loop (side $a$, resistance $R$) moves at velocity $v$ into a uniform magnetic field $B$ (into the page). Derive the signed induced current (positive for clockwise) at the instant when exactly half the loop's area is immersed. Express the current in terms of $B$, $v$, $a$, and $R$.

## Solution
**Step 1: Define total area and height of the triangle**  
The area of an equilateral triangle with side length $a$ is:  
$$ A_{\text{total}} = \frac{\sqrt{3}}{4} a^2 $$  
The height $h$ is:  
$$ h = \frac{\sqrt{3}}{2} a $$  

**Step 2: Express immersed area as a function of penetration depth**  
Let $x$ be the distance the base has penetrated into the field at time $t$, so $x = v t$. The immersed region is a smaller triangle similar to the original loop. The similarity ratio is $\frac{x}{h}$, so the base of the immersed triangle is $a \frac{x}{h}$. The immersed area $A$ is:  
$$ A = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \left( a \frac{x}{h} \right) x = \frac{a x^2}{2h} $$  
Substitute $h = \frac{\sqrt{3}}{2} a$:  
$$ A = \frac{a x^2}{2 \cdot \frac{\sqrt{3}}{2} a} = \frac{x^2}{\sqrt{3}} $$  

**Step 3: Solve for $x$ when half the area is immersed**  
Set $A = \frac{1}{2} A_{\text{total}}$:  
$$ \frac{x^2}{\sqrt{3}} = \frac{1}{2} \cdot \frac{\sqrt{3}}{4} a^2 = \frac{\sqrt{3}}{8} a^2 $$  
Solve for $x^2$:  
$$ x^2 = \frac{\sqrt{3}}{8} a^2 \cdot \sqrt{3} = \frac{3}{8} a^2 \implies x = a \sqrt{\frac{3}{8}} = a \frac{\sqrt{6}}{4} $$  

**Step 4: Compute the rate of change of area**  
Differentiate $A$ with respect to time:  
$$ \frac{dA}{dt} = \frac{d}{dt} \left( \frac{x^2}{\sqrt{3}} \right) = \frac{2x}{\sqrt{3}} \frac{dx}{dt} = \frac{2x v}{\sqrt{3}} $$  
Substitute $x = a \frac{\sqrt{6}}{4}$:  
$$ \frac{dA}{dt} = \frac{2}{\sqrt{3}} v \left( a \frac{\sqrt{6}}{4} \right) = \frac{2 a v \sqrt{6}}{4 \sqrt{3}} = \frac{a v \sqrt{6}}{2 \sqrt{3}} = \frac{a v \sqrt{2}}{2} $$  

**Step 5: Apply Faraday's law for induced EMF**  
The magnetic flux $\Phi_B = B A$ (since $B$ is perpendicular to the loop). The induced EMF is:  
$$ \mathcal{E} = -\frac{d\Phi_B}{dt} = -B \frac{dA}{dt} = -B \left( \frac{a v \sqrt{2}}{2} \right) $$  
The magnitude of EMF is $|\mathcal{E}| = B \frac{a v \sqrt{2}}{2}$.  

**Step 6: Determine induced current magnitude**  
$$ |I| = \frac{|\mathcal{E}|}{R} = \frac{B a v \sqrt{2}}{2 R} $$  

**Step 7: Apply Lenz's law for current direction**  
- The magnetic field is directed into the page. As the loop enters, flux into the page increases.  
- Lenz's law states the induced current opposes this change by creating flux out of the page.  
- A current flowing counterclockwise produces flux out of the page (right-hand rule).  
- Since clockwise is defined as positive, the induced current is negative.  

The signed current is:  
$$ I = - \frac{B a v \sqrt{2}}{2 R} $$

## Answer
$$\boxed{-\dfrac{B a v \sqrt{2}}{2 R}}$$

------
## Problem 4
##### Background  
A solenoid is a tightly wound helical coil that produces a nearly uniform magnetic field inside it when an electric current passes through. When the current in the solenoid changes, it induces an electromotive force (EMF) in nearby conductors due to Faraday's law of electromagnetic induction. The direction of the induced current follows Lenz's law, which states that it opposes the change in magnetic flux. In this problem, a loop encircles the solenoid, and we analyze the induced EMF while adhering to a specific sign convention for its direction.

##### Knowledge Points Tested  
1. Magnetic field inside a long solenoid: $ B = \mu_0 n i $, where $ n $ is the turns per unit length.  
2. Magnetic flux linkage for a multi-turn loop: $ \lambda = N \Phi = N B A $.  
3. Faraday's law: $ \mathcal{E} = -\frac{d\lambda}{dt} $.  
4. Lenz's law for determining the direction of induced current.  
5. Sign convention for EMF direction (counterclockwise defined as negative).  

##### Intradisciplinary Connections  
This problem integrates concepts from magnetostatics (solenoid magnetic field) and electromagnetic induction (induced EMF). It also reinforces the relationship between changing currents, magnetic flux, and induced EMF in closed loops.  

##### Interdisciplinary Connections  
The principles apply to electrical engineering (e.g., transformer design) and physics (e.g., particle accelerators where changing magnetic fields induce voltages). Understanding induced EMF is crucial for energy conversion devices like generators.  

##### Real-World Applications  
Solenoids are used in relays, MRI machines, and inductive sensors. The induced EMF phenomenon is exploited in wireless charging pads, where a changing current in a transmitter coil induces EMF in a receiver coil.  

##### Problem Statement  
A long solenoid with $ n $ turns per unit length carries a current that increases linearly from 0 to $ I $ over a time interval $ \Delta t $. A circular loop of area $ A $ with $ N $ turns is positioned concentrically around the solenoid, such that the solenoid's axis is perpendicular to the loop's plane. The magnetic field is uniform across the loop. Adopting the sign convention that a counterclockwise induced EMF (viewed along the solenoid's axis in the direction of the magnetic field) is negative, derive an expression for the induced EMF in the loop. Express your answer symbolically using $ \mu_0 $ (permeability of free space), $ n $, $ A $, $ N $, $ I $, and $ \Delta t $.

## Solution
**Step 1: Magnetic field inside the solenoid**  
The magnetic field magnitude inside a long solenoid is:  
$$ B = \mu_0 n i $$  
where $ i $ is the instantaneous current in the solenoid.  

**Step 2: Magnetic flux linkage for the loop**  
The magnetic flux through one turn of the loop is:  
$$ \Phi = B A = \mu_0 n i A $$  
since the field is uniform and perpendicular to the loop's plane. The flux linkage for $ N $ turns is:  
$$ \lambda = N \Phi = N \mu_0 n i A $$  

**Step 3: Apply Faraday's law**  
The induced EMF is:  
$$ \mathcal{E}_{\text{std}} = -\frac{d\lambda}{dt} = -N \mu_0 n A \frac{di}{dt} $$  
where $ \mathcal{E}_{\text{std}} $ follows the standard sign convention (positive for counterclockwise when viewed along the field direction).  

**Step 4: Rate of change of current**  
The current increases linearly from 0 to $ I $ in time $ \Delta t $, so:  
$$ \frac{di}{dt} = \frac{I}{\Delta t} $$  
Substituting into Faraday's law:  
$$ \mathcal{E}_{\text{std}} = -N \mu_0 n A \frac{I}{\Delta t} $$  

**Step 5: Apply sign convention**  
The problem defines counterclockwise EMF as negative. Since $ \mathcal{E}_{\text{std}} < 0 $, it corresponds to a clockwise-induced EMF in the standard convention. Thus, in the problem's convention:  
- Clockwise EMF (opposite to counterclockwise) is positive.  
- Counterclockwise EMF is negative.  
The induced EMF in the problem's convention is:  
$$ \mathcal{E} = -\mathcal{E}_{\text{std}} = - \left( -N \mu_0 n A \frac{I}{\Delta t} \right) = N \mu_0 n A \frac{I}{\Delta t} $$  
This positive value indicates a clockwise-induced EMF, consistent with Lenz's law: an increasing solenoid current produces an upward magnetic field, so the induced current in the loop creates a downward field (opposing the increase), which requires clockwise current when viewed from above.

## Answer
$$\boxed{N \mu_0 n A \frac{I}{\Delta t}}$$

------
## Problem 5
##### Background
Mutual inductance is a fundamental concept in electromagnetism, describing how a change in current in one coil induces an electromotive force (EMF) in a nearby coil. This phenomenon is governed by Faraday's law of induction and Lenz's law, which together determine the magnitude and direction of the induced EMF. In practical applications, mutual inductance is crucial in devices like transformers, wireless chargers, and induction cooktops.

##### Knowledge Points Tested
1. **Faraday's Law of Induction**: The induced EMF in a secondary coil is proportional to the negative rate of change of magnetic flux linkage, expressed as $\varepsilon = -M \frac{dI}{dt}$, where $M$ is the mutual inductance.
2. **Lenz's Law**: The direction of the induced current opposes the change in magnetic flux that produced it, reflected by the negative sign in Faraday's law.
3. **Derivative Calculation**: Ability to compute the time derivative of a given current function.
4. **Modeling Physical Systems**: Constructing a mathematical model from a real-world scenario involving time-dependent currents.

##### Intradisciplinary Connections
- **Electromagnetic Fields**: Relates to the generation of magnetic fields by currents and their interaction with nearby conductors.
- **Circuit Analysis**: Provides the foundation for understanding induced voltages in coupled circuits, essential in AC circuit theory and transformer design.

##### Interdisciplinary Connections
- **Calculus**: Application of differentiation to model rates of change in physical quantities.
- **Mathematical Modeling**: Using algebraic functions to represent physical phenomena and extracting meaningful parameters.

##### Real-World Applications
- **Transformers**: Mutual inductance enables voltage transformation in power distribution grids, stepping up voltage for efficient long-distance transmission and stepping down for safe household use.
- **Wireless Charging**: Inductive charging pads for electronic devices use mutual inductance to transfer energy without physical connectors.
- **Induction Stoves**: Time-varying currents in coils beneath the cooktop induce eddy currents in metal cookware, generating heat through resistive losses.

##### Problem Statement
Two coaxial circular coils are fixed in position with a mutual inductance of $M = 0.02  \text{H}$. The current in the primary coil varies with time as $I(t) = k t^n$, where $k$ and $n$ are constants. At $t = 1  \text{s}$, the current is $4  \text{A}$, and at $t = 2  \text{s}$, the current is $16  \text{A}$. Determine the induced electromotive force (EMF) in the secondary coil at $t = 1  \text{s}$.  

Express your answer in volts and provide only the numerical value. Ensure the sign reflects Lenz's law.

## Solution
#### Step 1: Determine the current function $I(t)$  
The current is given by $I(t) = k t^n$. Using the conditions at specific times:  
- At $t = 1  \text{s}$, $I(1) = k \cdot (1)^n = k = 4  \text{A}$. Thus, $k = 4$.  
- At $t = 2  \text{s}$, $I(2) = 4 \cdot (2)^n = 16  \text{A}$. Solving for $n$:  
  
$$
  4 \cdot 2^n = 16 \implies 2^n = 4 \implies 2^n = 2^2 \implies n = 2.
  $$
  
Therefore, the current function is $I(t) = 4t^2  \text{A}$.  

#### Step 2: Compute the rate of change of current  
The induced EMF depends on the derivative of the current with respect to time:  

$$
\frac{dI}{dt} = \frac{d}{dt}(4t^2) = 8t  \text{A/s}.
$$
  
At $t = 1  \text{s}$:  

$$
\left. \frac{dI}{dt} \right|_{t=1} = 8 \cdot 1 = 8  \text{A/s}.
$$
  

#### Step 3: Apply Faraday's law  
The induced EMF in the secondary coil is:  

$$
\varepsilon = -M \frac{dI}{dt}.
$$
  
Substitute $M = 0.02  \text{H}$ and $\frac{dI}{dt} = 8  \text{A/s}$ at $t = 1  \text{s}$:  

$$
\varepsilon = -(0.02) \cdot (8) = -0.16  \text{V}.
$$
  
The negative sign indicates that the direction of the induced EMF opposes the increase in primary current, as per Lenz's law.  

#### Final numerical value  
The induced EMF at $t = 1  \text{s}$ is $-0.16  \text{V}$. Since the problem requires only the numerical value in volts:

## Answer
$$\boxed{-0.16}$$

------
# maximum speed and acceleration in simple harmonic motion

## Problem 0
##### Background
In many mechanical systems, such as vehicle suspensions or clock mechanisms, spring-mass systems exhibit simple harmonic motion. Understanding the maximum speed and acceleration is crucial for designing these systems to avoid excessive forces that could cause damage. This problem explores a spring-powered toy car on a frictionless track. When the spring is compressed and released, the car accelerates due to the conversion of spring potential energy to kinetic energy.

##### Knowledge Points Tested
1. Energy conservation in mechanical systems.
2. Relationship between spring potential energy and kinetic energy.
3. Derivation of maximum speed in simple harmonic motion.
4. Algebraic manipulation of physical equations.

##### Intradisciplinary Connections
This problem connects to oscillations and waves (e.g., frequency and period of spring-mass systems) and work-energy theorem applications in mechanics.

##### Interdisciplinary Connections
- **Engineering**: Designing spring mechanisms in robotics or automotive systems.
- **Mathematics**: Solving equations involving squares and square roots.
- **Biology**: Modeling oscillatory motion in biomechanics (e.g., limb movement).

##### Real-World Applications
- **Toys**: Spring-powered cars or launchers.
- **Seismology**: Modeling ground motion during earthquakes as damped harmonic oscillators.
- **Aerospace**: Vibration analysis in spacecraft components.

##### Problem Statement
A toy car of mass $m$ is attached to a spring with spring constant $k$. The car rests on a frictionless horizontal track. The spring is compressed by a distance $A$ from its equilibrium position and released. Derive an expression for the maximum speed $v_{\text{max}}$ attained by the car. Express your answer symbolically in terms of $m$, $k$, and $A$. Do not substitute numerical values. Box your final answer as a single analytic expression.

## Solution
The total mechanical energy in the system is conserved because the track is frictionless and there are no non-conservative forces. At maximum compression (amplitude $A$), the car is momentarily at rest, so its kinetic energy is zero. The total energy is entirely spring potential energy:  
$$ E = \frac{1}{2} k A^2 $$  

At the equilibrium position (spring unstretched), the spring potential energy is zero. The car's kinetic energy is maximized, and this equals the total energy:  
$$ E = \frac{1}{2} m v_{\text{max}}^2 $$  

By conservation of energy:  
$$ \frac{1}{2} k A^2 = \frac{1}{2} m v_{\text{max}}^2 $$  

Solve for $v_{\text{max}}$:  
1. Multiply both sides by 2:  
$$ k A^2 = m v_{\text{max}}^2 $$  
2. Divide both sides by $m$:  
$$ v_{\text{max}}^2 = \frac{k A^2}{m} $$  
3. Take the square root of both sides (considering only the positive root for speed):  
$$ v_{\text{max}} = A \sqrt{\frac{k}{m}} $$  

The maximum speed occurs at the equilibrium position, as expected in simple harmonic motion.

## Answer
$$\boxed{A \sqrt{\frac{k}{m}}}$$

------
## Problem 1
##### Background
A simple pendulum consists of a bob of mass $m$ attached to a string of length $L$, pivoted at a fixed point. When displaced by a small angle $\theta_0$ (in radians) from its equilibrium position and released, the pendulum undergoes simple harmonic motion. This motion arises because the restoring force, which is the tangential component of gravity, is approximately proportional to the displacement for small angles. Understanding the maximum acceleration is crucial for applications like designing pendulum clocks or seismic sensors, where mechanical stress on components must be evaluated.

##### Knowledge Points Tested
1. Derivation of the equation of motion for a simple pendulum using Newton's second law.
2. Application of the small-angle approximation ($\sin\theta \approx \theta$ for $\theta$ in radians) to show simple harmonic motion.
3. Determination of angular frequency $\omega$ from the equation of motion.
4. Calculation of acceleration as the second derivative of displacement and identification of its maximum magnitude.

##### Intradisciplinary Connections
This problem connects to oscillations and waves (e.g., properties of simple harmonic motion), classical mechanics (Newton's laws and forces), and trigonometry (small-angle approximation). It also reinforces the relationship between angular frequency, period, and physical parameters.

##### Interdisciplinary Connections
- **Engineering**: Pendulum dynamics are used in mechanical oscillators for timekeeping and vibration control.
- **Earth Science**: Pendulum principles apply to seismometers that detect ground acceleration during earthquakes.
- **Biology**: Pendulum-like motion models human gait dynamics in biomechanics.

##### Real-World Applications
- **Timekeeping**: Pendulum clocks rely on precise harmonic motion; maximum acceleration determines bearing stresses.
- **Structural Monitoring**: Pendulum-based sensors in buildings measure seismic activity by detecting maximum accelerations.
- **Amusement Rides**: Swing designs use pendulum motion to ensure accelerations remain within safe limits.

##### Problem Statement
Consider a simple pendulum of length $L$ with a bob of mass $m$. The pendulum is displaced by a small angle $\theta_0$ (in radians) from its equilibrium position and released from rest. Assume the small-angle approximation holds, and neglect air resistance and friction.

1. Derive the equation of motion for the pendulum bob and show that it describes simple harmonic motion. Express the angular frequency $\omega$ in terms of $g$ and $L$.
2. Using the simple harmonic motion model, derive the acceleration $a(t)$ of the bob as a function of time.
3. Hence, derive an expression for the maximum magnitude of the acceleration $a_{\text{max}}$ experienced by the bob.

Express $a_{\text{max}}$ symbolically in terms of the acceleration due to gravity $g$ and $\theta_0$.

## Solution
#### Step 1: Derive the equation of motion and angular frequency
The forces acting on the bob are gravity ($mg$ downward) and tension ($T$ along the string). The tangential component of gravity provides the restoring force. For an angular displacement $\theta$, this component is $-mg \sin\theta$ (negative because it opposes the displacement). Using the small-angle approximation $\sin\theta \approx \theta$:

$$ F_{\text{tangential}} \approx -mg\theta $$

By Newton's second law, the tangential acceleration $a_t = L \ddot\theta$ relates to the tangential force:

$$ m L \ddot\theta = -mg\theta $$

Divide both sides by $m$:

$$ L \ddot\theta = -g\theta $$

Rearrange to standard simple harmonic form:

$$ \ddot\theta + \frac{g}{L} \theta = 0 $$

This is the equation of simple harmonic motion with angular frequency $\omega$:

$$ \omega = \sqrt{\frac{g}{L}} $$

#### Step 2: Derive the acceleration as a function of time
The general solution for the angular displacement in simple harmonic motion is $\theta(t) = \theta_0 \cos(\omega t)$, since the bob is released from rest at $\theta = \theta_0$ when $t=0$. The linear displacement along the arc is $s(t) = L \theta(t)$. The acceleration $a(t)$ is the second derivative of $s(t)$:

$$ a(t) = \frac{d^2 s}{dt^2} = L \frac{d^2\theta}{dt^2} $$

First, compute $\ddot\theta$:

$$ \dot\theta = \frac{d}{dt} [\theta_0 \cos(\omega t)] = -\theta_0 \omega \sin(\omega t) $$
$$ \ddot\theta = \frac{d}{dt} [-\theta_0 \omega \sin(\omega t)] = -\theta_0 \omega^2 \cos(\omega t) $$

Substitute into $a(t)$:

$$ a(t) = L [-\theta_0 \omega^2 \cos(\omega t)] = -\omega^2 L \theta_0 \cos(\omega t) $$

#### Step 3: Find the maximum magnitude of acceleration
The magnitude of acceleration is:

$$ |a(t)| = \left| -\omega^2 L \theta_0 \cos(\omega t) \right| = \omega^2 L \theta_0 \left| \cos(\omega t) \right| $$

The maximum value of $\left| \cos(\omega t) \right|$ is 1. Thus, the maximum acceleration magnitude is:

$$ a_{\text{max}} = \omega^2 L \theta_0 $$

Substitute $\omega^2 = \frac{g}{L}$:

$$ a_{\text{max}} = \left( \frac{g}{L} \right) L \theta_0 = g \theta_0 $$

The maximum acceleration occurs when $\cos(\omega t) = \pm 1$, which corresponds to the endpoints of the motion ($\theta = \pm \theta_0$), where the speed is zero and the tangential acceleration is maximized.

## Answer
$$\boxed{g \theta_{0}}$$

------
## Problem 2
##### Background
In automotive engineering, the suspension system of a car is often modeled as a spring-mass system to analyze ride comfort and stability. When a car hits a bump, the wheel (modeled as a point mass) undergoes vertical oscillations that can be described as simple harmonic motion (SHM). The maximum acceleration experienced by the wheel determines the forces transmitted to the chassis and passengers, making it critical for vehicle design.

##### Knowledge Points Tested
1. Application of Newton's second law to derive the equation of motion for a spring-mass system.
2. Identification of SHM parameters (angular frequency, period, amplitude).
3. Relationship between acceleration, displacement, and angular frequency in SHM.
4. Derivation of maximum acceleration using amplitude and period.

##### Intradisciplinary Connections
This problem connects to the broader study of oscillatory systems, including energy conservation (kinetic and potential energy exchanges) and resonance phenomena. It also reinforces differential equations governing harmonic motion.

##### Interdisciplinary Connections
- **Engineering**: Suspension design principles in automotive engineering rely on SHM to optimize spring constants and damping.
- **Biology**: Biomechanical systems (e.g., walking gaits) exhibit similar oscillatory behavior.
- **Geophysics**: Seismic waves propagate as harmonic oscillations through Earth's layers.

##### Real-World Applications
- **Vehicle Safety**: Excessive acceleration in suspension systems causes passenger discomfort and structural fatigue. Calculating $a_{\text{max}}$ helps engineers select appropriate springs.
- **Electronics**: MEMS accelerometers use SHM principles to measure vibration in devices like smartphones.
- **Civil Engineering**: Bridge oscillations under wind loads are modeled using SHM to prevent resonance-induced failures.

##### Problem Statement
A car's wheel, modeled as a point mass attached to a suspension spring, undergoes vertical simple harmonic motion after hitting a bump. The oscillation has amplitude $A$ and period $T$. Starting from Newton's second law, derive the equation of motion for the wheel. Use this result to find an expression for the maximum magnitude of the wheel's acceleration, $a_{\text{max}}$, in terms of $A$ and $T$.

## Solution
**Step 1: Apply Newton's second law**  
The restoring force from the spring is $F = -kx$, where $k$ is the spring constant and $x$ is the displacement from equilibrium. By Newton's second law:  

$$
F = ma \implies -kx = m \frac{d^2x}{dt^2}
$$
  
Rearranging gives the equation of motion:  

$$
\frac{d^2x}{dt^2} + \frac{k}{m}x = 0
$$


**Step 2: Identify angular frequency**  
The general solution is $x(t) = A \cos(\omega t + \phi)$, where $\omega$ is the angular frequency. Substituting into the equation of motion:  

$$
\frac{d^2x}{dt^2} = -A \omega^2 \cos(\omega t + \phi) = -\omega^2 x
$$
  
Comparing with $\frac{d^2x}{dt^2} = -\frac{k}{m}x$, we get:  

$$
\omega^2 = \frac{k}{m}
$$


**Step 3: Relate period to angular frequency**  
The period $T$ is the time for one full cycle:  

$$
T = \frac{2\pi}{\omega} \implies \omega = \frac{2\pi}{T}
$$


**Step 4: Derive acceleration**  
Acceleration is the second derivative of position:  

$$
a = \frac{d^2x}{dt^2} = -\omega^2 x = -\omega^2 A \cos(\omega t + \phi)
$$
  
The magnitude of acceleration is $ |a| = \omega^2 A |\cos(\omega t + \phi)| $. The maximum value occurs when $|\cos(\omega t + \phi)| = 1$:  

$$
a_{\text{max}} = \omega^2 A
$$


**Step 5: Substitute for $\omega$**  
Using $\omega = \frac{2\pi}{T}$:  

$$
a_{\text{max}} = \left( \frac{2\pi}{T} \right)^2 A = \frac{4\pi^2 A}{T^2}
$$
  
This is the maximum magnitude of acceleration.

## Answer
\[
\boxed{\dfrac{4\pi^{2} A}{T^{2}}}
\]

------
## Problem 3
##### Background
In automotive engineering, the suspension system of a car uses springs to absorb shocks from road irregularities. When a car hits a bump, the wheel undergoes vertical oscillations that can be modeled as simple harmonic motion (SHM). For a wheel oscillating with amplitude $A$, engineers must analyze the relationship between displacement and velocity to design effective shock absorbers. The maximum speed occurs at equilibrium, while speed decreases as the wheel moves toward maximum displacement. Understanding when the speed drops to specific fractions of its maximum value is critical for predicting forces on suspension components.

##### Knowledge Points Tested
1. Velocity-displacement relationship in SHM: $v = \omega \sqrt{A^2 - x^2}$
2. Maximum speed in SHM: $v_{\text{max}} = A\omega$
3. Algebraic manipulation of energy conservation equations.

##### Intradisciplinary Connections
Connects to energy conservation in oscillatory systems, where kinetic energy is maximum at equilibrium and potential energy is maximum at extremes. Relates to Hooke's law for spring forces and the derivation of SHM equations from Newton's second law.

##### Interdisciplinary Connections
Bridges physics (mechanics and oscillations) with mechanical engineering (suspension design). Requires understanding of kinematic relationships used in control systems for vehicle stability.

##### Real-World Applications
Determining critical displacements in suspension systems helps engineers avoid resonant frequencies, reduce wear on components, and improve ride comfort. Similar analysis applies to seismic dampers in buildings, pendulum clocks, and MEMS oscillators in electronics.

##### Problem Statement
A car's wheel oscillates vertically with simple harmonic motion after hitting a bump. The oscillation has amplitude $A$. Derive an expression for the displacement $x$ (measured from equilibrium) at which the wheel's speed is exactly half its maximum speed. Express your answer symbolically in terms of $A$.  
*Note: Your final expression must be simplified and use the exact form.*

## Solution
In SHM, the velocity $v$ at displacement $x$ is given by:  
$$ v = \omega \sqrt{A^2 - x^2} $$  
where $\omega$ is the angular frequency and $A$ is the amplitude.  

The maximum speed $v_{\text{max}}$ occurs at the equilibrium position ($x = 0$):  
$$ v_{\text{max}} = \omega A $$  

We seek the displacement $x$ where the speed is half the maximum speed:  
$$ v = \frac{1}{2} v_{\text{max}} $$  
Substitute the expressions for $v$ and $v_{\text{max}}$:  
$$ \omega \sqrt{A^2 - x^2} = \frac{1}{2} (\omega A) $$  

Divide both sides by $\omega$ (assuming $\omega \neq 0$):  
$$ \sqrt{A^2 - x^2} = \frac{1}{2} A $$  

Square both sides to eliminate the square root:  
$$ A^2 - x^2 = \left( \frac{1}{2} A \right)^2 $$  
$$ A^2 - x^2 = \frac{1}{4} A^2 $$  

Solve for $x^2$:  
$$ x^2 = A^2 - \frac{1}{4} A^2 $$  
$$ x^2 = \frac{3}{4} A^2 $$  

Take the square root of both sides:  
$$ x = \pm \sqrt{\frac{3}{4}} A $$  
$$ x = \pm \frac{\sqrt{3}}{2} A $$  

Thus, the displacement $x$ where the speed is half the maximum speed is $\pm \frac{\sqrt{3}}{2} A$. This corresponds to two symmetric points on either side of equilibrium.

## Answer
$$\boxed{\pm \frac{\sqrt{3}}{2} A}$$

------
# motion with changing acceleration

## Problem 0
##### Background
In advanced transportation systems, such as magnetic levitation (maglev) trains, propulsion can be engineered to provide precisely controlled acceleration profiles. Suppose a maglev pod undergoes testing where its acceleration increases quadratically with time to simulate high-speed launch conditions. This scenario allows engineers to model displacement without relying on constant acceleration assumptions.

##### Knowledge Points Tested
1. Relationship between acceleration, velocity, and displacement via integration  
2. Application of initial conditions in kinematics  
3. Polynomial integration techniques  
4. Dimensional analysis for physical consistency  

##### Intradisciplinary Connections
- Connects to Newton's second law ($F = ma$) where force profiles may produce quadratic acceleration.  
- Extends constant-acceleration kinematics to general calculus-based motion analysis.  

##### Interdisciplinary Connections
- **Engineering**: Used in designing acceleration profiles for high-speed transit.  
- **Applied Mathematics**: Demonstrates how integration transforms rate functions into cumulative quantities.  

##### Real-World Applications
Predicting stopping distances for vehicles with non-linear braking systems, modeling rocket launches with time-dependent thrust, and simulating particle trajectories in electrostatic fields with position-dependent forces.  

##### Problem Statement
A maglev pod starts from rest at position $x = 0$ and time $t = 0$. Its acceleration is given by $a(t) = c t^{2}$, where $c$ is a positive constant with units $\text{m/s}^4$. Derive an expression for the pod's displacement $s$ at time $\tau$ (where $\tau > 0$). Express $s$ symbolically in terms of $c$ and $\tau$.  

**Answer Format Requirements**:  
- Your final expression must use the variables $c$ and $\tau$.  
- Use standard mathematical notation:  
  - Write fractions as $\frac{a}{b}$ (e.g., $\frac{3c\tau^4}{8}$).  
  - Use $\exp(\cdot)$ for exponential functions if needed.  
  - Explicitly state exponents with $^$ and braces (e.g., $\tau^{4}$).  
- Do not substitute numerical values or constants.

## Solution
**Step 1: Relate acceleration to velocity**  
Acceleration is the derivative of velocity with respect to time:  

$$
a(t) = \frac{dv}{dt} = c t^{2}
$$
  
Integrate both sides to find velocity $v(t)$:  

$$
\int dv = \int c t^{2}  dt
$$
  

$$
v(t) = c \cdot \frac{t^{3}}{3} + C_1
$$
  
where $C_1$ is the integration constant.  

**Step 2: Apply initial condition for velocity**  
The pod starts from rest, so $v(0) = 0$:  

$$
v(0) = c \cdot \frac{(0)^{3}}{3} + C_1 = 0 \implies C_1 = 0
$$
  
Thus:  

$$
v(t) = \frac{c t^{3}}{3}
$$
  

**Step 3: Relate velocity to displacement**  
Velocity is the derivative of displacement with respect to time:  

$$
v(t) = \frac{ds}{dt} = \frac{c t^{3}}{3}
$$
  
Integrate both sides to find displacement $s(t)$:  

$$
\int ds = \int \frac{c t^{3}}{3}  dt
$$
  

$$
s(t) = \frac{c}{3} \cdot \frac{t^{4}}{4} + C_2 = \frac{c t^{4}}{12} + C_2
$$
  
where $C_2$ is another integration constant.  

**Step 4: Apply initial condition for displacement**  
At $t = 0$, $s(0) = 0$:  

$$
s(0) = \frac{c (0)^{4}}{12} + C_2 = 0 \implies C_2 = 0
$$
  
Thus:  

$$
s(t) = \frac{c t^{4}}{12}
$$
  

**Step 5: Evaluate displacement at time $\tau$**  
Substitute $t = \tau$:  

$$
s(\tau) = \frac{c \tau^{4}}{12}
$$
  

**Dimensional Verification**:  
- $c$ has units $\text{m/s}^4$, $\tau$ has units $\text{s}$.  
- $c \tau^{4}$ has units $\text{m/s}^4 \cdot \text{s}^4 = \text{m}$, which matches displacement units.  
The expression is physically consistent.

## Answer
$$\boxed{\dfrac{c\tau^{4}}{12}}$$

------
## Problem 1
##### Background
In many physical systems, an object experiences a drag force proportional to its velocity, leading to acceleration that depends linearly on velocity. This occurs in scenarios like a small object moving through a viscous fluid at low Reynolds numbers, where the resistive force follows Stokes' law. Consider an object moving in a straight line with initial velocity $v_0$. The acceleration is given by $a(v) = -k v$, where $k > 0$ is a constant characterizing the damping strength. This acceleration opposes the direction of motion, causing the velocity to decrease over time.

##### Knowledge Points Tested
1. Application of Newton's second law to velocity-dependent acceleration.
2. Use of the chain rule in kinematics: $a = \frac{dv}{dt} = v \frac{dv}{dx}$.
3. Separation of variables in differential equations.
4. Definite integration to relate velocity change to distance traveled.

##### Intradisciplinary Connections
- Connects to kinematics with non-constant acceleration and damped harmonic motion (without oscillation).
- Extends concepts of work-energy theorem when forces are velocity-dependent.

##### Interdisciplinary Connections
- **Fluid Dynamics**: Models drag force in viscous fluids (Stokes' law).
- **Electrical Engineering**: Analogous to RC circuit discharge, where voltage decays exponentially.

##### Real-World Applications
- Predicting stopping distances for vehicles in highly viscous environments (e.g., submarines in water).
- Modeling sedimentation rates of particles in chemical engineering.
- Designing air-resistance systems for parachutes at low speeds.

##### Problem Statement
An object moves along a straight line with acceleration given by $a(v) = -k v$, where $k$ is a positive constant. The object starts with velocity $v_0$ at position $x=0$. Derive an expression for the distance $x$ traveled by the object as its velocity decreases from $v_0$ to $v_1$ (where $0 < v_1 < v_0$). Express your answer as an analytic expression in terms of $k$, $v_0$, and $v_1$.  
**Note**: Your derivation must explicitly show the differential equation setup, separation of variables, and integration steps. Use the chain rule to relate acceleration to velocity and position.

## Solution
Start with the given acceleration:  
$$ a(v) = -k v $$  
Acceleration is defined as $a = \frac{dv}{dt}$. Using the chain rule, express acceleration in terms of velocity and position:  
$$ a = \frac{dv}{dt} = \frac{dv}{dx} \cdot \frac{dx}{dt} = v \frac{dv}{dx} $$  
Substitute the given expression for $a$:  
$$ v \frac{dv}{dx} = -k v $$  
Since $v > 0$ during the motion (as $v_1 > 0$), divide both sides by $v$:  
$$ \frac{dv}{dx} = -k $$  
Separate variables to integrate:  
$$ dv = -k  dx $$  
Integrate both sides. The velocity changes from $v_0$ to $v_1$, and the position changes from $0$ to $x$:  
$$ \int_{v_0}^{v_1} dv = -k \int_{0}^{x} dx $$  
Evaluate the integrals:  
$$ \left. v \right|_{v_0}^{v_1} = -k \left. x \right|_{0}^{x} $$  
$$ v_1 - v_0 = -k (x - 0) $$  
Solve for $x$:  
$$ v_1 - v_0 = -k x $$  
$$ x = \frac{v_0 - v_1}{k} $$  
The distance traveled is $\frac{v_0 - v_1}{k}$.

## Answer
$$\boxed{\dfrac{v_0 - v_1}{k}}$$

------
## Problem 2
##### Background
A rocket is launched vertically upward from ground level. During the powered phase, the rocket's net acceleration (accounting for both engine thrust and gravity) is given as a function of time. This acceleration decreases linearly until the engine cuts off when the net acceleration becomes zero. After cutoff, the rocket coasts under the influence of gravity alone. The acceleration due to gravity, denoted as $g$, acts downward and is constant. Understanding rocket motion with variable acceleration is crucial in aerospace engineering for trajectory optimization.

##### Knowledge Points Tested
1. Integration of acceleration to obtain velocity and position functions.
2. Solving for the time when a specific condition (acceleration = 0) occurs.
3. Application of kinematics under constant acceleration (after cutoff).
4. Determination of maximum height by analyzing velocity zero-crossing.

##### Intradisciplinary Connections
Connects to kinematics in one dimension, calculus applications in physics, and the transition between variable and constant acceleration regimes within mechanics.

##### Interdisciplinary Connections
Involves solving differential equations (mathematics) and models real-world rocket propulsion systems (engineering). The variable acceleration reflects fuel consumption dynamics.

##### Real-World Applications
Used in spacecraft launch trajectory design, such as for satellites or crewed missions, where engine cutoff timing directly impacts payload altitude and reentry profiles. Also applicable to model-based control systems in vertical takeoff vehicles.

##### Problem Statement
A rocket is launched vertically upward from ground level with an initial velocity of zero. The net acceleration during the powered phase is $a(t) = 40 - 5t$ m/s², where $t$ is time in seconds. The engine cuts off when the net acceleration becomes zero. After cutoff, gravity acts with constant acceleration magnitude $g$ downward. Determine the maximum height $H$ reached by the rocket. Express $H$ symbolically in terms of $g$.

## Solution
**Phase 1: Powered Ascent (from $t=0$ to engine cutoff)**  
The engine cuts off when $a(t) = 0$:  
$$40 - 5t_c = 0 \implies t_c = 8 \text{ seconds}$$  
Velocity $v(t)$ is the integral of acceleration $a(t)$:  
$$v(t) = \int (40 - 5t)  dt = 40t - \frac{5}{2}t^2 + C$$  
Initial condition: $v(0) = 0 \implies C = 0$, so:  
$$v(t) = 40t - \frac{5}{2}t^2$$  
Position $s(t)$ is the integral of velocity $v(t)$:  
$$s(t) = \int \left(40t - \frac{5}{2}t^2\right)  dt = 20t^2 - \frac{5}{6}t^3 + D$$  
Initial condition: $s(0) = 0 \implies D = 0$, so:  
$$s(t) = 20t^2 - \frac{5}{6}t^3$$  
At $t_c = 8$ s:  
$$v_c = 40(8) - \frac{5}{2}(8)^2 = 320 - 160 = 160 \text{ m/s}$$  
$$s_c = 20(8)^2 - \frac{5}{6}(8)^3 = 1280 - \frac{2560}{3} = \frac{2560}{3} \text{ m}$$  

**Phase 2: Coasting Ascent (after $t_c$)**  
Initial velocity $u = v_c = 160$ m/s (upward), initial height $s_c = \frac{2560}{3}$ m, acceleration $a = -g$.  
At maximum height $H$, velocity $v = 0$. Using the kinematics equation:  
$$v^2 = u^2 + 2a\Delta s \implies 0 = (160)^2 + 2(-g)\left(H - s_c\right)$$  
Solve for $H$:  
$$0 = 25600 - 2g\left(H - \frac{2560}{3}\right)$$  
$$2g\left(H - \frac{2560}{3}\right) = 25600$$  
$$H - \frac{2560}{3} = \frac{25600}{2g} = \frac{12800}{g}$$  
$$H = \frac{2560}{3} + \frac{12800}{g}$$  

The maximum height $H$ is $\frac{2560}{3} + \frac{12800}{g}$ meters.

## Answer
$$\boxed{\dfrac{2560}{3} + \dfrac{12800}{g}}$$

------
## Problem 3
##### Background  
In automotive testing, engineers often program vehicles with adaptive acceleration profiles to simulate real-world driving conditions. One such test involves a vehicle whose acceleration is designed to decrease linearly with distance traveled. This scenario models situations where external factors (like regenerative braking in electric cars or varying terrain) cause the acceleration to change based on position rather than time.  

##### Knowledge Points Tested  
1. Kinematic equations with acceleration as a function of position.  
2. Application of the chain rule: $ a = v \frac{dv}{dx} $.  
3. Solving separable first-order differential equations.  
4. Definite integration with initial conditions.  

##### Intradisciplinary Connections  
This problem connects to the work-energy theorem, as the solution can alternatively be derived using energy methods. It also extends to oscillations, where position-dependent acceleration leads to simple harmonic motion (though not in this specific case).  

##### Interdisciplinary Connections  
- **Mathematics**: Solving differential equations via separation of variables.  
- **Engineering**: Modeling and control systems for autonomous vehicles.  
- **Computer Science**: Numerical integration techniques used in vehicle simulation software.  

##### Real-World Applications  
Position-dependent acceleration profiles are used in:  
- Electric vehicle regenerative braking systems, where deceleration increases as the vehicle approaches a stop.  
- Roller coaster design, where acceleration depends on track elevation.  
- Aerospace testing, where rocket thrust varies with altitude.  

##### Problem Statement  
A test vehicle starts from rest at $ x = 0 $ m. Its acceleration decreases linearly with position according to $ a(x) = A - Bx $, where $ A = 12  \text{m/s}^2 $ and $ B = 0.5  \text{m/s}^2\text{ per meter} $. Derive the velocity of the vehicle at $ x = 10  \text{m} $.  

Express your answer in meters per second (m/s). Provide only the numerical value rounded to three significant figures.

## Solution
#### Step 1: Relate acceleration to velocity using the chain rule  
Acceleration is defined as $ a = \frac{dv}{dt} $. To express it in terms of position $ x $, apply the chain rule:  

$$ a = \frac{dv}{dt} = \frac{dv}{dx} \cdot \frac{dx}{dt} = v \frac{dv}{dx} $$
  
Given $ a(x) = A - Bx $, this becomes:  

$$ v \frac{dv}{dx} = A - Bx $$
  
where $ A = 12  \text{m/s}^2 $ and $ B = 0.5  \text{m/s}^2\text{ per meter} $.  

#### Step 2: Separate variables and integrate  
Separate variables $ v $ and $ x $:  

$$ v  dv = (A - Bx)  dx $$
  
Integrate both sides. The left side integrates from $ v = 0 $ (initial rest) to $ v $, and the right side from $ x = 0 $ to $ x $:  

$$ \int_{0}^{v} v'  dv' = \int_{0}^{x} (A - Bx')  dx' $$
  
Compute the integrals:  

$$ \left[ \frac{(v')^2}{2} \right]_{0}^{v} = \left[ Ax' - \frac{B}{2} (x')^2 \right]_{0}^{x} $$
  

$$ \frac{v^2}{2} - 0 = \left( Ax - \frac{B}{2} x^2 \right) - (0) $$
  

$$ \frac{v^2}{2} = Ax - \frac{B}{2} x^2 $$
  

#### Step 3: Solve for velocity  
Multiply both sides by 2:  

$$ v^2 = 2Ax - B x^2 $$
  
Take the positive square root (since the vehicle moves in the positive $ x $-direction):  

$$ v = \sqrt{2Ax - B x^2} $$
  

#### Step 4: Substitute given values  
Evaluate at $ x = 10  \text{m} $:  

$$ v = \sqrt{2 \cdot 12 \cdot 10 - 0.5 \cdot (10)^2} $$
  

$$ v = \sqrt{240 - 0.5 \cdot 100} $$
  

$$ v = \sqrt{240 - 50} $$
  

$$ v = \sqrt{190} $$
  

#### Step 5: Compute numerical value  
Calculate $ \sqrt{190} $:  

$$ \sqrt{190} \approx 13.784048 $$
  
Round to three significant figures:  

$$ v \approx 13.8  \text{m/s} $$

## Answer
$$\boxed{13.8}$$

------
## Problem 4
##### Background
In physics, oscillatory motion often arises when an object experiences a restoring force proportional to its displacement from equilibrium. A classic example is a spring-mass system, where Hooke's law governs the force. However, this problem explores motion where acceleration is directly specified as a function of position, leading to a differential equation that models harmonic oscillation. Such models appear in seismology (ground motion during earthquakes), molecular dynamics (vibrations in diatomic molecules), and mechanical engineering (suspension systems).

##### Knowledge Points Tested
1. Solving second-order linear homogeneous differential equations with constant coefficients.
2. Applying initial conditions to determine arbitrary constants in general solutions.
3. Recognizing the mathematical structure of simple harmonic motion from acceleration-position relationships.

##### Intradisciplinary Connections
This problem connects to energy conservation in oscillatory systems. The total mechanical energy (kinetic + potential) remains constant, which can be verified by integrating the equation of motion. It also relates to the superposition principle in linear systems, as the solution combines sine and cosine functions.

##### Interdisciplinary Connections
- **Mathematics**: Direct application of ordinary differential equation (ODE) solution techniques and characteristic equations.
- **Engineering**: Models vibrations in structures and materials under elastic deformation.
- **Biology**: Describes oscillatory phenomena like heartbeat cycles or neural oscillations when linearized.

##### Real-World Applications
- **Seismometers**: Measure ground acceleration during seismic events using pendulum-based systems obeying similar equations.
- **Atomic Force Microscopy (AFM)**: Cantilevers experience harmonic motion when probing surface forces.
- **Vehicle Suspension**: Shock absorbers exhibit damped harmonic motion, with this problem representing the idealized undamped case.

##### Problem Statement
A particle moves along the x-axis under an acceleration defined by $ a(x) = -16x $  m/s², where $ x $ is the displacement from the origin in meters. At time $ t = 0 $, the particle is displaced to $ x = 0.2 $  m and released from rest (initial velocity $ v_0 = 0 $  m/s). Derive the position function $ x(t) $ for $ t \geq 0 $.  

Express your final answer as an analytic expression in terms of $ t $ (time in seconds). Use exact fractions and symbols; do not substitute numerical values for constants. Write trigonometric functions in unevaluated form (e.g., $ \cos(4t) $), and express all coefficients as simplified fractions. Angle units are radians; omit the degree symbol.

## Solution
The acceleration is given as a function of position:  
$$ a(x) = \frac{d^2x}{dt^2} = -16x $$  
Rearranging yields the harmonic motion equation:  
$$ \frac{d^2x}{dt^2} + 16x = 0 $$  
This is a second-order linear homogeneous differential equation with constant coefficients. The characteristic equation is:  
$$ r^2 + 16 = 0 $$  
Solving for $ r $:  
$$ r^2 = -16 \implies r = \pm 4i $$  
The general solution is:  
$$ x(t) = C_1 \cos(4t) + C_2 \sin(4t) $$  
where $ C_1 $ and $ C_2 $ are constants determined by initial conditions.  

**Apply initial conditions:**  
1. At $ t = 0 $, $ x(0) = 0.2 $:  
$$ x(0) = C_1 \cos(0) + C_2 \sin(0) = C_1 \cdot 1 + C_2 \cdot 0 = C_1 = \frac{1}{5} $$  
(since $ 0.2 = \frac{1}{5} $).  

2. Initial velocity $ v(0) = 0 $. First, find velocity by differentiating $ x(t) $:  
$$ v(t) = \frac{dx}{dt} = -4C_1 \sin(4t) + 4C_2 \cos(4t) $$  
At $ t = 0 $:  
$$ v(0) = -4C_1 \sin(0) + 4C_2 \cos(0) = 0 + 4C_2 \cdot 1 = 4C_2 $$  
Set $ v(0) = 0 $:  
$$ 4C_2 = 0 \implies C_2 = 0 $$  

Substitute $ C_1 = \frac{1}{5} $ and $ C_2 = 0 $ into the general solution:  
$$ x(t) = \frac{1}{5} \cos(4t) $$  
This describes the position as a function of time.

## Answer
$$\boxed{\dfrac{1}{5}\cos\left(4t\right)}$$

------
# Ohm's law and resistance calculations

## Problem 0
##### Background
In electrical engineering, resistors are often made from homogeneous materials, but composite resistors with segments of different materials are used for specialized applications. Consider a cylindrical resistor of total length $L$ and uniform cross-sectional area $A$. The resistor is formed by joining two different materials in series: the first segment (length $L/2$) has resistivity $\rho_1$, and the second segment (length $L/2$) has resistivity $\rho_2$. A potential difference $V$ is applied across the entire length, causing a current $I$ to flow. Understanding how to derive the total resistance from fundamental principles illustrates the application of Ohm's law and series resistance concepts.

##### Knowledge Points Tested
- Ohm's law: $V = IR$
- Resistance formula: $R = \rho \frac{L}{A}$ for a uniform conductor
- Equivalent resistance for resistors in series: $R_{\text{eq}} = R_1 + R_2$

##### Intradisciplinary Connections
- Connects microscopic resistivity ($\rho$) to macroscopic resistance ($R$).
- Extends series circuit analysis to continuous materials.

##### Interdisciplinary Connections
- Materials science: resistivity depends on material properties.
- Mathematics: algebraic manipulation and derivation.

##### Real-World Applications
- Used in designing precision resistors, thermistors, and multifunctional electronic components where material properties vary along the current path.

##### Problem Statement
A composite resistor consists of two cylindrical segments of equal length $L/2$ and cross-sectional area $A$, with resistivities $\rho_1$ and $\rho_2$, connected in series. When a potential difference of $V = 12\,\text{V}$ is applied across the entire resistor, a current of $I = 0.4\,\text{A}$ flows through it.  

Derive an expression for the total resistance $R$ of the composite resistor in terms of $\rho_1$, $\rho_2$, $L$, and $A$. This is the final answer to be boxed.

## Solution
### Step 1: Define resistance of each segment  
The resistance of a uniform conductor is given by $R = \rho \frac{L}{A}$.  
- For the first segment (length $L_1 = L/2$, resistivity $\rho_1$):  
  $$ R_1 = \rho_1 \frac{L_1}{A} = \rho_1 \frac{L/2}{A} = \frac{\rho_1 L}{2A} $$  
- For the second segment (length $L_2 = L/2$, resistivity $\rho_2$):  
  $$ R_2 = \rho_2 \frac{L_2}{A} = \rho_2 \frac{L/2}{A} = \frac{\rho_2 L}{2A} $$  

### Step 2: Determine total resistance  
Since the segments are in series, the total resistance is the sum:  
$$ R = R_1 + R_2 = \frac{\rho_1 L}{2A} + \frac{\rho_2 L}{2A} $$  

### Step 3: Simplify the expression  
Factor out common terms:  
$$ R = \frac{L}{2A} (\rho_1 + \rho_2) $$  

### Verification using given values  
The problem provides $V = 12\,\text{V}$ and $I = 0.4\,\text{A}$. By Ohm's law:  
$$ R = \frac{V}{I} = \frac{12}{0.4} = 30\,\Omega $$  
This numerical value depends only on $V$ and $I$, confirming that the derived expression for $R$ is consistent with the fundamental law. However, the final answer is the symbolic expression, as required.

## Answer
$$\boxed{\dfrac{L(\rho_{1} + \rho_{2})}{2A}}$$

------
## Problem 1
##### Background
In electronic circuit design, resistors are often connected in parallel to achieve a desired equivalent resistance. This configuration ensures that the voltage across each resistor is the same, while the total current is the sum of the currents through each resistor. The equivalent resistance of parallel resistors is always less than the smallest individual resistance. This principle is critical in applications like power distribution systems, where parallel connections allow multiple devices to operate at the same voltage.

##### Knowledge Points Tested
1. Ohm's law: $V = IR$, where $V$ is voltage, $I$ is current, and $R$ is resistance.
2. Kirchhoff's current law (KCL): The sum of currents entering a junction equals the sum leaving.
3. Equivalent resistance for parallel resistors: The reciprocal of the equivalent resistance equals the sum of the reciprocals of individual resistances.

##### Intradisciplinary Connections
- Conductance ($G = 1/R$), which is additive in parallel circuits, provides an alternative approach to resistance calculations.
- The concept extends to capacitors in series and resistors in series-parallel networks.

##### Interdisciplinary Connections
- **Physics**: Thermal resistance networks in heat transfer follow analogous parallel/series rules.
- **Engineering**: Power management in electrical grids uses parallel resistor configurations to balance loads.

##### Real-World Applications
- Household wiring systems connect appliances in parallel to maintain uniform voltage.
- Electronic devices like smartphones use parallel resistors in integrated circuits for current division and signal processing.

##### Problem Statement
Three identical resistors, each with resistance $R = 6  \Omega$, are connected in parallel. Derive an expression for the equivalent resistance $R_{\text{eq}}$ using Ohm's law and Kirchhoff's current law. Then, compute the numerical value of $R_{\text{eq}}$ in ohms.  
**Express your final answer as a numerical value only, without units.**

## Solution
#### Step 1: Define the circuit setup
- Three resistors with resistances $R_1 = R_2 = R_3 = R = 6  \Omega$ are connected in parallel.
- A voltage $V$ is applied across the combination, causing a total current $I$ to flow from the source.

#### Step 2: Apply Ohm's law to each resistor
The current through each resistor is:  

$$
I_1 = \frac{V}{R_1}, \quad I_2 = \frac{V}{R_2}, \quad I_3 = \frac{V}{R_3}.
$$


#### Step 3: Apply Kirchhoff's current law (KCL)
At the junction where the total current $I$ splits:  

$$
I = I_1 + I_2 + I_3.
$$
  
Substituting the expressions from Step 2:  

$$
I = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} = V \left( \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} \right).
$$


#### Step 4: Define the equivalent resistance
The equivalent resistance $R_{\text{eq}}$ satisfies $V = I R_{\text{eq}}}$. Rearranging:  

$$
I = \frac{V}{R_{\text{eq}}}}.
$$


#### Step 5: Equate expressions for total current
From Steps 3 and 4:  

$$
\frac{V}{R_{\text{eq}}}} = V \left( \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} \right).
$$
  
Dividing both sides by $V$ (assuming $V \neq 0$):  

$$
\frac{1}{R_{\text{eq}}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}.
$$


#### Step 6: Substitute identical resistances
Since $R_1 = R_2 = R_3 = R$:  

$$
\frac{1}{R_{\text{eq}}}} = \frac{1}{R} + \frac{1}{R} + \frac{1}{R} = \frac{3}{R}.
$$
  
Thus:  

$$
R_{\text{eq}} = \frac{R}{3}.
$$


#### Step 7: Compute numerical value
Given $R = 6  \Omega$:  

$$
R_{\text{eq}} = \frac{6}{3} = 2.
$$
  
The equivalent resistance is $2  \Omega$.

## Answer
$$\boxed{2}$$

------
## Problem 2
##### Background
A battery's electromotive force (emf) is its ideal voltage output, but real batteries have internal resistance that affects circuit behavior. When current flows, the terminal voltage (voltage available to the external circuit) is reduced due to energy dissipation within the battery. Consider a battery with an emf of $E = 20\,\text{V}$. When connected solely to a $30\,\Omega$ resistor, it draws a current of $0.6\,\text{A}$. Now, this same battery is connected to a series combination of a $15\,\Omega$ resistor and a $25\,\Omega$ resistor.

##### Knowledge Points Tested
- Ohm's law: $V = IR$
- Terminal voltage of a battery: $V_{\text{terminal}} = E - Ir$, where $r$ is the internal resistance
- Equivalent resistance in series circuits: $R_{\text{eq}} = R_1 + R_2$
- Current conservation in series circuits

##### Intradisciplinary Connections
This problem integrates Kirchhoff's voltage law (KVL) with Ohm's law, demonstrating how internal resistance modifies the effective voltage supplied to external components. It reinforces the concept that resistance is additive in series and current is uniform throughout a series path.

##### Interdisciplinary Connections
Internal resistance is critical in electrochemistry (battery design) and engineering (power systems). Understanding voltage drop due to internal resistance ensures accurate modeling in robotics (battery life estimation) and renewable energy systems (solar cell efficiency).

##### Real-World Applications
- **Electric vehicles**: Battery internal resistance reduces available voltage under load, affecting motor performance and range.
- **Portable electronics**: Smartphones and laptops experience reduced operating voltage as batteries age, leading to unexpected shutdowns.
- **Power grids**: Transformers and generators have internal resistance, causing voltage drops during high-demand periods.

##### Problem Statement
A battery has an emf of $20\,\text{V}$. When connected to a standalone $30\,\Omega$ resistor, it produces a current of $0.6\,\text{A}$. The same battery is then connected to a series combination of a $15\,\Omega$ resistor and a $25\,\Omega$ resistor. Determine the current (in amperes) through the $15\,\Omega$ resistor.  

Express your answer as an exact fraction. Do not include units in your final answer.

## Solution
##### Step 1: Determine the battery's internal resistance
- The terminal voltage $V_{\text{terminal}}$ when connected to the $30\,\Omega$ resistor is given by Ohm's law:  
  $$ V_{\text{terminal}} = I_1 R_1 $$  
  Substituting the values $I_1 = 0.6\,\text{A}$ and $R_1 = 30\,\Omega$:  
  $$ V_{\text{terminal}} = (0.6)(30) = 18\,\text{V} $$
- The terminal voltage also equals the emf minus the voltage drop across the internal resistance $r$:  
  $$ V_{\text{terminal}} = E - I_1 r $$  
  Rearranging for $r$:  
  $$ 18 = 20 - (0.6)r $$  
  $$ (0.6)r = 20 - 18 = 2 $$  
  $$ r = \frac{2}{0.6} = \frac{20}{6} = \frac{10}{3}\,\Omega $$  

##### Step 2: Calculate the equivalent resistance of the series circuit
- The external resistors ($15\,\Omega$ and $25\,\Omega$) are in series, so their equivalent resistance $R_{\text{eq}}$ is:  
  $$ R_{\text{eq}} = R_2 + R_3 = 15 + 25 = 40\,\Omega $$  

##### Step 3: Find the total current in the series circuit
- The total resistance of the circuit includes the external equivalent resistance and the internal resistance:  
  $$ R_{\text{total}} = R_{\text{eq}} + r = 40 + \frac{10}{3} = \frac{120}{3} + \frac{10}{3} = \frac{130}{3}\,\Omega $$  
- The total current $I$ is determined by Ohm's law applied to the entire circuit:  
  $$ I = \frac{E}{R_{\text{total}}} = \frac{20}{\frac{130}{3}} = 20 \times \frac{3}{130} = \frac{60}{130} = \frac{6}{13}\,\text{A} $$  

##### Step 4: Identify the current through the $15\,\Omega$ resistor
- In a series circuit, the current is uniform throughout. Thus, the current through the $15\,\Omega$ resistor equals the total current:  
  $$ I_{15\,\Omega} = I = \frac{6}{13}\,\text{A} $$

## Answer
$$\boxed{\dfrac{6}{13}}$$

------
## Problem 3
##### Background
Copper wires are fundamental components in electrical circuits, known for their excellent conductivity. In practical applications, wires often undergo mechanical processes like stretching, which alters their dimensions while conserving volume. This problem explores how such changes affect electrical resistance, combining concepts from material science and circuit theory.

##### Knowledge Points Tested
- Ohm's law and the resistance formula: $R = \rho \frac{L}{A}$  
- Volume conservation in deformable solids  
- Series and parallel resistor combinations  

##### Intradisciplinary Connections
Connects resistivity (microscopic property) to resistance (macroscopic circuit element) and extends to energy dissipation in conductors.

##### Interdisciplinary Connections
Material science: Volume conservation during deformation.  
Geometry: Relationships between length and cross-sectional area.

##### Real-World Applications
Understanding resistance changes in stretched wires is crucial for designing strain gauges, overhead power lines, and flexible electronics where mechanical stress alters electrical behavior.

##### Problem Statement
A copper wire with resistivity $\rho$ has an initial length $L_0$ and initial cross-sectional area $A_0$. The wire is stretched uniformly until its length becomes $2L_0$. After stretching, it is cut into three equal-length pieces. Two pieces are connected in series, and this series combination is connected in parallel with the third piece. Derive an expression for the total resistance $R_{\text{total}}$ of this arrangement.  
Express $R_{\text{total}}$ symbolically in terms of $\rho$, $L_0$, and $A_0$. Simplify your answer to a single fractional expression.  
**Follow these notation rules:**  
- Use $\rho$, $L_0$, $A_0$ as given.  
- For fractions, use $\frac{a}{b}$ syntax.  
- No numerical substitutions or approximations.

## Solution
**Step 1: Determine cross-sectional area after stretching**  
Volume conservation implies:  
$$A_0 L_0 = A_{\text{new}} \cdot (2L_0)$$  
Solving for the new area $A_{\text{new}}$:  
$$A_{\text{new}} = \frac{A_0 L_0}{2L_0} = \frac{A_0}{2}$$  

**Step 2: Calculate resistance of the full stretched wire**  
Using $R = \rho \frac{L}{A}$:  
$$R_{\text{stretched}} = \rho \frac{2L_0}{A_{\text{new}}} = \rho \frac{2L_0}{A_0 / 2} = \rho \cdot 2L_0 \cdot \frac{2}{A_0} = \frac{4\rho L_0}{A_0}$$  

**Step 3: Find resistance of one piece after cutting**  
Each piece has length $\frac{1}{3}$ of the stretched wire:  
$$L_{\text{piece}} = \frac{1}{3} \cdot 2L_0 = \frac{2L_0}{3}$$  
Cross-sectional area remains $A_{\text{new}} = \frac{A_0}{2}$. Thus:  
$$R_{\text{piece}} = \rho \frac{L_{\text{piece}}}{A_{\text{new}}} = \rho \frac{2L_0 / 3}{A_0 / 2} = \rho \cdot \frac{2L_0}{3} \cdot \frac{2}{A_0} = \frac{4\rho L_0}{3A_0}$$  

**Step 4: Compute series resistance of two pieces**  
$$R_{\text{series}} = R_{\text{piece}} + R_{\text{piece}} = 2 \cdot \frac{4\rho L_0}{3A_0} = \frac{8\rho L_0}{3A_0}$$  

**Step 5: Compute total resistance of parallel combination**  
The parallel combination has $R_{\text{series}}$ and $R_{\text{piece}}$:  
$$\frac{1}{R_{\text{total}}}} = \frac{1}{R_{\text{series}}} + \frac{1}{R_{\text{piece}}} = \frac{1}{\frac{8\rho L_0}{3A_0}} + \frac{1}{\frac{4\rho L_0}{3A_0}} = \frac{3A_0}{8\rho L_0} + \frac{3A_0}{4\rho L_0}$$  
Find a common denominator ($8\rho L_0$):  
$$\frac{3A_0}{8\rho L_0} + \frac{6A_0}{8\rho L_0} = \frac{9A_0}{8\rho L_0}$$  
Thus:  
$$R_{\text{total}} = \frac{8\rho L_0}{9A_0}$$

## Answer
$$\boxed{\dfrac{8\rho L_{0}}{9A_{0}}}$$

------
# order of magnitude estimations

## Problem 0
##### Background
Raindrops form when water vapor condenses in the atmosphere. A typical raindrop has a diameter of about 2 mm. Water has a density of 1000 kg/m³, and its molecular composition (H₂O) gives it a molar mass of 18 g/mol. Avogadro's constant, which relates the number of molecules to the amount of substance, is 6.02 × 10²³ molecules per mole. Order-of-magnitude estimation is a fundamental skill in science and engineering for approximating quantities when precise values are impractical.

##### Knowledge Points Tested
1. Volume of a sphere  
2. Density-mass-volume relationship  
3. Molar mass and Avogadro's constant for molecular counting  
4. Scientific notation and order-of-magnitude estimation  
5. Logarithmic rounding to determine the nearest power of 10  

##### Intradisciplinary Connections
This problem connects fluid mechanics (raindrop formation) to molecular chemistry (Avogadro's constant) and dimensional analysis (unit conversions). It demonstrates how macroscopic properties (density) bridge to microscopic scales (molecular count).

##### Interdisciplinary Connections
Physics provides the density and spherical model, chemistry supplies the molar mass and Avogadro's constant, and mathematics enables logarithmic rounding for order-of-magnitude estimation. This reflects real-world problem-solving across disciplines.

##### Real-World Applications
- **Meteorology**: Estimating cloud droplet concentrations for weather modeling.  
- **Nanotechnology**: Scaling molecular quantities for material design.  
- **Environmental Science**: Modeling pollutant dispersion in precipitation.  

##### Problem Statement
Using the provided typical values:  
- Raindrop diameter $d = 2  \text{mm}$  
- Water density $\rho = 1000  \text{kg/m}^3$  
- Molar mass of water $M = 18  \text{g/mol}$  
- Avogadro's constant $N_A = 6.02 \times 10^{23}  \text{mol}^{-1}$  

Derive an expression for the number of water molecules $N$ in a raindrop. Compute $N$ numerically, then determine its order of magnitude by rounding the base-10 logarithm of $N$ to the nearest integer. Your final answer must be this integer exponent.  

**Instructions for answer formatting**:  
- Use $\log_{10}$ for base-10 logarithms (e.g., $\log_{10}(100) = 2$).  
- Round the logarithm to the nearest integer (e.g., 20.49 rounds to 20; 20.50 rounds to 21).  
- Provide only the integer exponent in the boxed answer.

## Solution
**Step 1: Convert units and compute volume**  
- Diameter $d = 2  \text{mm} = 2 \times 10^{-3}  \text{m}$  
- Radius $r = d/2 = 1 \times 10^{-3}  \text{m}$  
- Volume of spherical raindrop:  
  
$$
  V = \frac{4}{3} \pi r^3 = \frac{4}{3} \pi (1 \times 10^{-3})^3 = \frac{4}{3} \pi \times 10^{-9}  \text{m}^3
  $$
  

**Step 2: Compute mass**  
- Density $\rho = 1000  \text{kg/m}^3$  
- Mass $m = \rho V = 1000 \times \frac{4}{3} \pi \times 10^{-9} = \frac{4000}{3} \pi \times 10^{-9}  \text{kg}$  

**Step 3: Convert mass to moles**  
- Molar mass $M = 18  \text{g/mol} = 0.018  \text{kg/mol}$  
- Moles $n = \frac{m}{M} = \frac{\frac{4000}{3} \pi \times 10^{-9}}{0.018} = \frac{4000 \pi \times 10^{-9}}{3 \times 0.018} = \frac{4000 \pi \times 10^{-9}}{0.054}$  
- Simplify:  
  
$$
  n = \frac{4000}{0.054} \pi \times 10^{-9} = 74,\!074.\overline{074} \pi \times 10^{-9} \approx 7.4074 \times 10^4 \times \pi \times 10^{-9} = 7.4074 \pi \times 10^{-5}  \text{mol}
  $$
  
- Numerical evaluation: $n \approx 7.4074 \times 3.1416 \times 10^{-5} \approx 2.327 \times 10^{-4}  \text{mol}$  

**Step 4: Compute number of molecules**  
- $N = n \times N_A = 2.327 \times 10^{-4} \times 6.02 \times 10^{23}$  
- Calculate:  
  
$$
  2.327 \times 6.02 = 14.00854 \quad \Rightarrow \quad N = 14.00854 \times 10^{-4+23} = 1.400854 \times 10^{20}
  $$
  
- Thus, $N \approx 1.401 \times 10^{20}$  

**Step 5: Determine order of magnitude**  
- Compute $\log_{10}(N) = \log_{10}(1.401 \times 10^{20}) = \log_{10}(1.401) + 20$  
- $\log_{10}(1.401) \approx 0.1465$ (since $10^{0.1465} \approx 1.401$)  
- $\log_{10}(N) \approx 20.1465$  
- Round to nearest integer: $20.1465 \to 20$  

**Conclusion**  
The order of magnitude exponent is 20, meaning $N \sim 10^{20}$.

## Answer
$$\boxed{20}$$

------
## Problem 1
##### Background
Order of magnitude estimation is a fundamental skill in physics and engineering, allowing us to approximate physical quantities using reasonable assumptions and basic principles. This technique is particularly valuable for understanding phenomena where precise measurements are unavailable or impractical, such as in biological systems.

##### Knowledge Points Tested
- Kinetic energy formula: $ KE = \frac{1}{2} m v^2 $
- Order of magnitude estimation using powers of 10
- Unit conversions (implicitly through estimation)
- Critical thinking in model-building for real-world systems

##### Intradisciplinary Connections
- Mechanics: Application of kinetic energy concepts
- Scientific notation: Expressing very large or very small numbers
- Dimensional analysis: Verifying consistency of energy units

##### Interdisciplinary Connections
- Biology: Relating insect physiology to physical capabilities
- Aeronautical engineering: Understanding lift and drag forces in flight
- Environmental science: Energy transfer in ecosystems

##### Real-World Applications
- Designing micro-air vehicles (MAVs) inspired by insect flight
- Estimating energy requirements for pest control systems
- Modeling energy flow in food chains (e.g., bats consuming mosquitoes)
- Developing impact-resistant materials for small-scale collisions

##### Problem Statement
Estimate the order of magnitude of the kinetic energy of a flying mosquito. To solve this problem:
1. Estimate the typical mass $ m $ of a mosquito in kilograms.
2. Estimate the typical flying speed $ v $ of a mosquito in meters per second.
3. Compute the kinetic energy using $ KE = \frac{1}{2} m v^2 $.
4. Express your final answer as $ 10^{k} $ joules, where $ k $ is an integer representing the order of magnitude.

Your solution should include:
- Justification for your mass and speed estimates
- All calculations in scientific notation
- Explicit consideration of the factor $ \frac{1}{2} $ in the energy calculation
- Final answer in the exact form $ 10^{k} $

Note: Use the following conventions:
- Express all powers of 10 using the caret notation (e.g., $ 10^{-6} $)
- Do not substitute numerical values for physical constants
- Assume standard SI units (kilograms, meters, seconds)

## Solution
### Step 1: Estimate the mass of a mosquito
Mosquitoes are small insects. Based on biological knowledge:
- A typical mosquito has a mass around 1-2 milligrams.
- Convert to kilograms: 1 milligram = $ 10^{-3} $ grams = $ 10^{-6} $ kg.
- We use $ m \sim 10^{-6} $ kg as the order of magnitude estimate.

### Step 2: Estimate the flying speed
Observations of mosquito flight:
- Mosquitoes fly at approximately 1-2 miles per hour.
- Convert to SI units: 1 mph ≈ 0.45 m/s, so 1-2 mph ≈ 0.5-1 m/s.
- We use $ v \sim 10^{0} $ m/s = 1 m/s as the order of magnitude estimate.

### Step 3: Compute kinetic energy
Apply the kinetic energy formula:
$$ KE = \frac{1}{2} m v^2 $$

Substitute the estimates:
- $ m = 10^{-6} $ kg
- $ v = 10^{0} $ m/s
- $ v^2 = (10^{0})^2 = 10^{0} $ m²/s²

Now compute:
$$ KE = \frac{1}{2} \times (10^{-6}) \times (10^{0}) = \frac{1}{2} \times 10^{-6} $$

### Step 4: Simplify and determine order of magnitude
Simplify the expression:
$$ \frac{1}{2} \times 10^{-6} = 0.5 \times 10^{-6} = 5 \times 10^{-7} \text{ joules} $$

Express in scientific notation:
- $ 5 \times 10^{-7} = 10^{\log_{10}(5)} \times 10^{-7} $
- $ \log_{10}(5) \approx 0.7 $, so $ 10^{0.7} \times 10^{-7} = 10^{-6.3} $

Determine the order of magnitude:
- The value $ 10^{-6.3} $ lies between $ 10^{-7} $ and $ 10^{-6} $
- Compare distances: 
  - To $ 10^{-7} $: $ |5 \times 10^{-7} - 10^{-7}| = 4 \times 10^{-7} $
  - To $ 10^{-6} $: $ |5 \times 10^{-7} - 10^{-6}| = 5 \times 10^{-7} $
- Since $ 4 \times 10^{-7} < 5 \times 10^{-7} $, $ 10^{-7} $ is closer

### Step 5: Final expression
The factor $ \frac{1}{2} $ reduces the energy by approximately half, confirming the kinetic energy is closer to $ 10^{-7} $ J than $ 10^{-6} $ J. Thus, the order of magnitude is:
$$ \boxed{10^{-7}} $$

## Answer
$$\boxed{10^{-7}}$$

------
## Problem 2
##### Background
Blood is a vital fluid in the human circulatory system, responsible for transporting oxygen, nutrients, hormones, and waste products. The volume of blood in an individual varies based on age, body mass, and health. Adults typically have about 5 liters of blood, while children and infants have less. The global human population exceeds 8 billion, distributed across various age groups. Order-of-magnitude estimations simplify complex real-world quantities by focusing on the power of ten that best represents the scale, useful in resource planning, medical supply logistics, and ecological studies.

##### Knowledge Points Tested
- Order-of-magnitude estimation
- Weighted averages in population demographics
- Scientific notation and exponent manipulation
- Unit consistency in volume calculations

##### Intradisciplinary Connections
Connects to biology (blood volume per capita), statistics (weighted averages for age groups), and arithmetic operations (multiplication, addition, scientific notation). Reinforces understanding of how demographic distributions affect aggregate quantities.

##### Interdisciplinary Connections
- **Biology/Medicine**: Blood volume norms across age groups and implications for transfusion medicine.
- **Demography**: Population structure and growth trends.
- **Environmental Science**: Estimating resource use (e.g., water or iron content) linked to blood volume.

##### Real-World Applications
- Planning blood donation drives and emergency stockpiles.
- Estimating pharmaceutical demand (e.g., iron supplements for anemia).
- Modeling disease spread through blood-borne pathogens.

##### Problem Statement
Using the following data, estimate the order of magnitude of the total blood volume in all humans alive today, expressed in liters:
- Current world population: $ P = 8.0 \times 10^9 $
- Fraction of population under 15 years old: $ f_c = 0.25 $
- Average blood volume for a person under 15: $ V_c = 2.5  \text{liters} $
- Average blood volume for a person 15 or older: $ V_a = 5.0  \text{liters} $

Compute the total blood volume in scientific notation (form $ a \times 10^b $ with $ 1 \leq a < 10 $) and report the order of magnitude, defined as the exponent $ b $.  
Your final answer is $ b $.

## Solution
**Step 1: Calculate subpopulations**  
- Population under 15:  
  $$ N_c = f_c \times P = 0.25 \times 8.0 \times 10^9 = 2.0 \times 10^9 $$  
- Population 15 or older:  
  $$ N_a = (1 - f_c) \times P = 0.75 \times 8.0 \times 10^9 = 6.0 \times 10^9 $$  

**Step 2: Compute blood volume per group**  
- Blood volume from under-15 group:  
  $$ V_{\text{children}} = N_c \times V_c = (2.0 \times 10^9) \times 2.5 = 5.0 \times 10^9  \text{liters} $$  
- Blood volume from 15-or-older group:  
  $$ V_{\text{adults}} = N_a \times V_a = (6.0 \times 10^9) \times 5.0 = 3.0 \times 10^{10}  \text{liters} $$  

**Step 3: Sum total blood volume**  
$$ V_{\text{total}} = V_{\text{children}} + V_{\text{adults}} = 5.0 \times 10^9 + 3.0 \times 10^{10} = 3.5 \times 10^{10}  \text{liters} $$  

**Step 4: Express in scientific notation and extract order of magnitude**  
The total blood volume is $ 3.5 \times 10^{10} $ liters. Here, $ a = 3.5 $ (satisfying $ 1 \leq a < 10 $) and $ b = 10 $. The order of magnitude is the exponent $ b $.  

**Conclusion**  
The order of magnitude of the total blood volume is 10.

## Answer
$$\boxed{10}$$

------
## Problem 3
##### Background
Newton's law of universal gravitation describes the attractive force between two masses. This force is fundamental to understanding celestial mechanics, such as the interaction between Earth and the Moon. Order of magnitude estimation simplifies complex calculations by focusing on the powers of 10 in scientific notation, enabling quick approximations of physical quantities without precise arithmetic.

##### Knowledge Points Tested
1. Application of Newton's law of universal gravitation: $F = \frac{G M_e M_m}{d^2}$  
2. Order of magnitude estimation using scientific notation  
3. Arithmetic operations with exponents  

##### Intradisciplinary Connections
This problem connects to kinematics (orbital motion) and energy conservation (gravitational potential energy) within physics. Understanding gravitational force is essential for analyzing satellite trajectories and tidal forces.

##### Interdisciplinary Connections
- **Astronomy**: Estimating forces between celestial bodies  
- **Mathematics**: Exponent rules and scientific notation  
- **Geophysics**: Modeling Earth-Moon interactions that influence tides  

##### Real-World Applications
Accurate gravitational force estimates are crucial for space mission planning (e.g., Apollo missions), satellite deployment, and understanding tidal patterns that affect coastal ecosystems and renewable energy systems like tidal power plants.

##### Problem Statement
Estimate the order of magnitude of the gravitational force between Earth and the Moon using Newton's law of universal gravitation and the following approximate values:  
- Gravitational constant: $G \approx 6.67 \times 10^{-11}  \text{N} \cdot \text{m}^2 / \text{kg}^2$  
- Mass of Earth: $M_e \approx 6.0 \times 10^{24}  \text{kg}$  
- Mass of Moon: $M_m \approx 7.0 \times 10^{22}  \text{kg}$  
- Average Earth-Moon distance: $d \approx 4.0 \times 10^8  \text{m}$  

Perform the following steps:  
1. Express all quantities in scientific notation.  
2. Compute the numerator $G M_e M_m$ and denominator $d^2$ separately, keeping track of exponents.  
3. Combine results to find $F$, then determine its order of magnitude by rounding to the nearest power of 10.  

Express the final order of magnitude as $10^X$ (where $X$ is an integer). For the final answer box, provide **only the expression $10^X$** (e.g., $10^{15}$). Do not include units or additional text.

## Solution
The gravitational force is given by Newton's law:  
$$ F = \frac{G M_e M_m}{d^2} $$  

Substitute the given values:  
$$ F = \frac{(6.67 \times 10^{-11}) \times (6.0 \times 10^{24}) \times (7.0 \times 10^{22})}{(4.0 \times 10^8)^2} $$  

**Step 1: Compute the numerator $G M_e M_m$**  
- Multiply the coefficients: $6.67 \times 6.0 \times 7.0 = 6.67 \times 42 = 280.14$  
- Add the exponents: $-11 + 24 + 22 = 35$  
- Numerator: $280.14 \times 10^{35} = 2.8014 \times 10^2 \times 10^{35} = 2.8014 \times 10^{37}$  

**Step 2: Compute the denominator $d^2$**  
- $(4.0 \times 10^8)^2 = 4.0^2 \times (10^8)^2 = 16.0 \times 10^{16} = 1.60 \times 10^{17}$  

**Step 3: Calculate $F$**  
- $F = \frac{2.8014 \times 10^{37}}{1.60 \times 10^{17}} = \frac{2.8014}{1.60} \times 10^{37-17} = 1.750875 \times 10^{20}$  

**Step 4: Determine the order of magnitude**  
- $F \approx 1.75 \times 10^{20} \text{N}$  
- The exponent is 20. To decide whether to round to $10^{20}$ or $10^{21}$, compare $1.75$ to $\sqrt{10} \approx 3.16$ (the geometric mean between $10^0$ and $10^1$). Since $1.75 < 3.16$, the order of magnitude is $10^{20}$.  

*Note: Order of magnitude is defined as the nearest power of 10. Here, $1.75 \times 10^{20}$ is closer to $10^{20}$ than to $10^{21}$ because $1.75 < 5$ (the arithmetic midpoint in logarithmic space is $10^{20.5} \approx 3.16 \times 10^{20}$).*

## Answer
$$\boxed{10^{20}}$$

------
## Problem 4
##### Background  
The human heart is a vital organ that pumps blood throughout the body, and its beating rate varies significantly with age, activity, and health. Unlike simplified models that assume a constant average heart rate, a more accurate estimation accounts for developmental stages. This problem explores a refined model to estimate the total number of heartbeats over a typical human lifespan, incorporating age-dependent heart rate variations.

##### Knowledge Points Tested  
- Unit conversions (years to minutes).  
- Multiplication and summation of large numbers.  
- Scientific notation and logarithmic scaling for order of magnitude.  
- Critical estimation using real-world physiological data.  

##### Intradisciplinary Connections  
Connects to human biology (cardiac physiology and developmental stages) and mathematics (exponents, logarithms, and summation).  

##### Interdisciplinary Connections  
Integrates biology (heart rate variability and lifespan stages) with mathematical modeling (order of magnitude estimation and multi-stage summation).  

##### Real-World Applications  
Order of magnitude estimations are essential in fields like biomedical engineering (e.g., designing pacemaker battery life) and actuarial science (e.g., assessing lifetime health metrics). For instance, such estimates inform the durability requirements for implantable medical devices.  

##### Problem Statement  
A typical human lifespan is divided into four stages with distinct average heart rates:  
- **Infancy (first year)**: 120 beats per minute.  
- **Childhood (ages 1–10)**: 90 beats per minute.  
- **Adulthood (ages 10–50)**: 70 beats per minute.  
- **Senior years (ages 50–80)**: 75 beats per minute.  

The durations of each stage are:  
- Infancy: 1 year.  
- Childhood: 9 years.  
- Adulthood: 40 years.  
- Senior years: 30 years.  

Assume 365 days per year, 24 hours per day, and 60 minutes per hour.  
1. Calculate the total number of heartbeats over the entire lifespan.  
2. Find the order of magnitude of this number, defined as the exponent $k$ in $10^k$ that is closest to the total. To determine $k$, compute the base-10 logarithm of the total and round it to the nearest integer.  

**Instructions for the final answer**:  
- Express the order of magnitude $k$ as a single integer.  
- Do not include any units or additional text.  
- Use scientific notation and logarithmic calculations as needed.

## Solution
#### Step 1: Calculate minutes per year  
First, compute the number of minutes in one year:  

$$
\text{Minutes per year} = 365 \times 24 \times 60 = 365 \times 1440 = 525,600
$$
  

#### Step 2: Calculate heartbeats for each stage  
- **Infancy (1 year)**:  
  
$$
  \text{Heartbeats}_{\text{infancy}} = 120 \times 525,600 = 63,072,000
  $$
  
- **Childhood (9 years)**:  
  
$$
  \text{Heartbeats}_{\text{childhood}} = 90 \times 9 \times 525,600 = 90 \times 4,730,400 = 425,736,000
  $$
  
- **Adulthood (40 years)**:  
  
$$
  \text{Heartbeats}_{\text{adulthood}} = 70 \times 40 \times 525,600 = 70 \times 21,024,000 = 1,471,680,000
  $$
  
- **Senior years (30 years)**:  
  
$$
  \text{Heartbeats}_{\text{senior}} = 75 \times 30 \times 525,600 = 75 \times 15,768,000 = 1,182,600,000
  $$
  

#### Step 3: Sum the heartbeats  
Add the heartbeats from all stages:  

$$
\begin{align*}
\text{Total} &= 63,072,000 + 425,736,000 + 1,471,680,000 + 1,182,600,000 \\
&= 63,072,000 + 425,736,000 = 488,808,000 \\
&+ 1,471,680,000 = 1,960,488,000 \\
&+ 1,182,600,000 = 3,143,088,000
\end{align*}
$$
  
Thus, the total number of heartbeats is $3,143,088,000$.  

#### Step 4: Express in scientific notation and compute logarithm  
Convert to scientific notation:  

$$
3,143,088,000 = 3.143088 \times 10^9
$$
  
Compute the base-10 logarithm:  

$$
\log_{10}(3.143088 \times 10^9) = \log_{10}(3.143088) + \log_{10}(10^9) \approx 0.4973 + 9 = 9.4973
$$
  

#### Step 5: Determine the order of magnitude  
Round $9.4973$ to the nearest integer:  

$$
9.4973 \approx 9 \quad \text{(since the fractional part 0.4973 < 0.5)}
$$
  
The order of magnitude is 9.

## Answer
$$\boxed{9}$$

------
# position calculations from velocity data

## Problem 0
##### Background
In automotive engineering, the motion of vehicles is often analyzed to optimize performance and safety. One common scenario involves calculating the displacement of a car based on its velocity profile. While constant-velocity cases are straightforward, real-world situations often involve changing velocities due to traffic, terrain, or engine performance. Here, we explore a more realistic model where velocity changes over time, requiring integration to determine displacement—a fundamental skill in kinematics and calculus.

##### Knowledge Points Tested
1. Understanding displacement as the integral of velocity with respect to time.
2. Setting up and evaluating definite integrals for exponential velocity functions.
3. Applying initial conditions to solve motion problems.
4. Handling exponential decay models in physical contexts.

##### Intradisciplinary Connections
- **Calculus**: Integration techniques for exponential functions.
- **Physics**: Kinematics in one dimension, velocity-displacement relationships.
- **Differential Equations**: Exponential decay as a solution to linear differential equations (e.g., motion with drag proportional to velocity).

##### Interdisciplinary Connections
- **Environmental Science**: Modeling pollutant dispersion in fluids (similar exponential decay).
- **Economics**: Depreciation of assets over time (exponential decay models).
- **Electrical Engineering**: Discharge of capacitors in RC circuits (same mathematical form).

##### Real-World Applications
- **Automotive Safety Testing**: Calculating stopping distances for vehicles with anti-lock braking systems (exponential deceleration).
- **Aerospace**: Determining the displacement of rockets during stage separation (velocity decay profiles).
- **Sports Science**: Analyzing sprinter performance under fatigue (velocity decay over race duration).

##### Problem Statement
A test car starts from position $x = 0$ at time $t = 0$. Its velocity $v(t)$ (in m/s) decreases exponentially due to mechanical resistance and is given by:

$$
v(t) = v_0 \exp\left(-\frac{t}{\tau}\right),
$$

where $v_0$ is the initial velocity (in m/s), $\tau$ is a time constant (in seconds), and $t$ is time (in seconds). Derive an expression for the car's displacement $x(T)$ at time $t = T$. Express your answer symbolically in terms of $v_0$, $\tau$, and $T$.

**Answer Formatting Instructions**:
- Provide an **analytic expression** using $v_0$, $\tau$, and $T$.
- Use $\exp(\cdot)$ for exponential functions (e.g., $\exp(x)$, not $e^x$).
- Do not substitute numerical values for any parameters.
- Displacement must be in meters, so express the answer as a numerical coefficient times the given symbols.

## Solution
To find the displacement $x(T)$ at time $t = T$, integrate the velocity function $v(t)$ from $t = 0$ to $t = T$:

$$
x(T) = \int_{0}^{T} v(t)  dt = \int_{0}^{T} v_0 \exp\left(-\frac{t}{\tau}\right)  dt.
$$


Factor out the constant $v_0$:

$$
x(T) = v_0 \int_{0}^{T} \exp\left(-\frac{t}{\tau}\right)  dt.
$$


Use the substitution $u = -\frac{t}{\tau}$. Then, $du = -\frac{1}{\tau} dt$, so $dt = -\tau  du$.  
- When $t = 0$, $u = 0$.  
- When $t = T$, $u = -\frac{T}{\tau}$.  

Rewrite the integral in terms of $u$:

$$
\int \exp\left(-\frac{t}{\tau}\right)  dt = \int \exp(u) (-\tau)  du = -\tau \int \exp(u)  du.
$$


The antiderivative of $\exp(u)$ is $\exp(u)$:

$$
-\tau \int \exp(u)  du = -\tau \exp(u) + C = -\tau \exp\left(-\frac{t}{\tau}\right) + C,
$$

where $C$ is the constant of integration.

Apply the definite integral limits from $t = 0$ to $t = T$:

$$
\int_{0}^{T} \exp\left(-\frac{t}{\tau}\right)  dt = \left[ -\tau \exp\left(-\frac{t}{\tau}\right) \right]_{0}^{T}.
$$


Evaluate at the bounds:

$$
\left[ -\tau \exp\left(-\frac{T}{\tau}\right) \right] - \left[ -\tau \exp\left(-\frac{0}{\tau}\right) \right] = -\tau \exp\left(-\frac{T}{\tau}\right) + \tau \exp(0).
$$


Since $\exp(0) = 1$:

$$
\int_{0}^{T} \exp\left(-\frac{t}{\tau}\right)  dt = \tau \left(1 - \exp\left(-\frac{T}{\tau}\right)\right).
$$


Substitute back into the expression for $x(T)$:

$$
x(T) = v_0 \cdot \tau \left(1 - \exp\left(-\frac{T}{\tau}\right)\right).
$$


The displacement at time $T$ is:

$$
x(T) = v_0 \tau \left(1 - \exp\left(-\frac{T}{\tau}\right)\right).
$$


This result is consistent with the physical interpretation:  
- At $T = 0$, $x(0) = 0$ (starting point).  
- As $T \to \infty$, $x(T) \to v_0 \tau$ (finite displacement due to exponential decay).

## Answer
$$\boxed{v_0 \tau \left(1 - \exp\left(-\frac{T}{\tau}\right)\right)}$$

------
## Problem 1
##### Background
In automotive testing, engineers often study a vehicle's motion to optimize performance. Consider a test car starting from rest at the origin of a straight track. The car's acceleration increases linearly with time due to an experimental engine profile. At $t = 0$, the acceleration is $a_0$, and at $t = T$, the car's velocity is measured as $V$. This scenario models real-world systems where acceleration changes continuously, such as rocket launches or electric vehicle speed trials.

##### Knowledge Points Tested
- Deriving velocity from acceleration via integration.
- Computing position change by integrating velocity.
- Applying initial conditions to determine constants.
- Performing definite integration with polynomial functions.

##### Intradisciplinary Connections
Connects to fundamental kinematics (velocity-acceleration-position relationships) and calculus (integration techniques), forming the basis for analyzing non-uniform motion in physics.

##### Interdisciplinary Connections
- **Engineering**: Modeling vehicle dynamics and control systems.
- **Mathematics**: Solving differential equations and evaluating definite integrals.
- **Data Science**: Interpreting motion data to predict position changes.

##### Real-World Applications
Used in automotive safety testing (e.g., calculating stopping distances), aerospace trajectory planning, and robotics path optimization.

##### Problem Statement
A car starts from rest at position $x = 0$. Its acceleration increases linearly with time as $a(t) = k \cdot t + a_0$, where $a_0$ is the initial acceleration at $t = 0$. At time $t = T$, the car's velocity is $V$. Find the change in the car's position $\Delta x$ from time $t = t_1$ to $t = t_2$. Express $\Delta x$ symbolically in terms of $a_0$, $T$, $V$, $t_1$, and $t_2$.  
**Answer Format Requirements**:  
- Provide an analytic expression using the given symbols.  
- Use explicit fractions (e.g., $\frac{1}{2}$).  
- Do not substitute numerical values or simplify constants.

## Solution
The change in position $\Delta x$ is the definite integral of velocity $v(t)$ from $t_1$ to $t_2$:  

$$
\Delta x = \int_{t_1}^{t_2} v(t)  dt
$$
  
First, derive $v(t)$. Acceleration $a(t)$ is the derivative of velocity, so:  

$$
v(t) = \int a(t)  dt = \int (k \cdot t + a_0)  dt = \frac{k}{2} t^2 + a_0 t + C
$$
  
The car starts from rest at $t = 0$, so $v(0) = 0$:  

$$
v(0) = \frac{k}{2}(0)^2 + a_0(0) + C = 0 \implies C = 0
$$
  
Thus, $v(t) = \frac{k}{2} t^2 + a_0 t$.  
At $t = T$, $v(T) = V$:  

$$
V = \frac{k}{2} T^2 + a_0 T
$$
  
Solve for $k$:  

$$
\frac{k}{2} T^2 = V - a_0 T \implies k = \frac{2(V - a_0 T)}{T^2}
$$
  
Substitute $k$ into $v(t)$:  

$$
v(t) = \frac{1}{2} \left( \frac{2(V - a_0 T)}{T^2} \right) t^2 + a_0 t = \frac{(V - a_0 T)}{T^2} t^2 + a_0 t
$$
  
Now integrate $v(t)$ from $t_1$ to $t_2$:  

$$
\Delta x = \int_{t_1}^{t_2} \left( \frac{(V - a_0 T)}{T^2} t^2 + a_0 t \right)  dt
$$
  
Split the integral:  

$$
\Delta x = \frac{V - a_0 T}{T^2} \int_{t_1}^{t_2} t^2  dt + a_0 \int_{t_1}^{t_2} t  dt
$$
  
Evaluate the integrals:  

$$
\int_{t_1}^{t_2} t^2  dt = \left[ \frac{t^3}{3} \right]_{t_1}^{t_2} = \frac{t_2^3 - t_1^3}{3}, \quad \int_{t_1}^{t_2} t  dt = \left[ \frac{t^2}{2} \right]_{t_1}^{t_2} = \frac{t_2^2 - t_1^2}{2}
$$
  
Substitute:  

$$
\Delta x = \frac{V - a_0 T}{T^2} \cdot \frac{t_2^3 - t_1^3}{3} + a_0 \cdot \frac{t_2^2 - t_1^2}{2}
$$
  
Simplify:  

$$
\Delta x = \frac{(V - a_0 T)(t_2^3 - t_1^3)}{3 T^2} + \frac{a_0 (t_2^2 - t_1^2)}{2}
$$
  
This is the symbolic expression for the position change.

## Answer
$$
\boxed{\dfrac{(V - a_{0} T) (t_{2}^{3} - t_{1}^{3})}{3 T^{2}} + \dfrac{a_{0} (t_{2}^{2} - t_{1}^{2})}{2}}
$$

------
## Problem 2
##### Background
In autonomous vehicle testing, engineers collect velocity data at discrete time intervals to analyze motion. The displacement of the vehicle during a time interval is the integral of its velocity, but continuous data is often unavailable. The trapezoidal rule provides a numerical estimate by approximating the area under the velocity-time curve using linear segments between data points. This method is essential in robotics, navigation systems, and experimental physics where sensor data is sampled at discrete times.

##### Knowledge Points Tested
1. Fundamental theorem of calculus: Displacement as the integral of velocity.
2. Numerical integration using the trapezoidal rule for non-uniform or discrete data.
3. Interpretation of velocity-time graphs and area calculations.
4. Algebraic manipulation of summation formulas for integration.

##### Intradisciplinary Connections
- **Calculus**: Direct application of integration techniques to kinematics.
- **Physics**: Kinematic analysis of motion using sampled data.
- **Data Analysis**: Estimating physical quantities from discrete measurements.

##### Interdisciplinary Connections
- **Robotics**: Path planning and position estimation for autonomous systems.
- **Geomatics**: GPS and sensor data processing for displacement calculations.
- **Computer Science**: Algorithm design for numerical integration in simulations.

##### Real-World Applications
- Autonomous drones use velocity data from accelerometers to estimate position changes during flight.
- Sports science analyzes athlete movement via wearable sensors.
- Seismology processes ground velocity readings to determine displacement during earthquakes.

##### Problem Statement
An autonomous delivery drone moves in a straight line. Its velocity $v$ (in m/s) is recorded at three times:  
- $t = 0$ s, $v = 5$ m/s  
- $t = 2$ s, $v = 9$ m/s  
- $t = 4$ s, $v = 1$ m/s  

Using the trapezoidal rule, estimate the drone's displacement (in meters) from $t = 0$ to $t = 4$ seconds. The trapezoidal rule for $n$ subintervals is:  
$$ \Delta s \approx \frac{1}{2} \sum_{i=1}^{n} (t_i - t_{i-1})(v_i + v_{i-1}) $$  
where $(t_0, v_0)$, $(t_1, v_1)$, ..., $(t_n, v_n)$ are the data points.  

Express your answer as an exact number. Provide only the numerical value (without units) in the boxed answer.

## Solution
The displacement $\Delta s$ is estimated using the trapezoidal rule with the given data points: $(t_0, v_0) = (0, 5)$, $(t_1, v_1) = (2, 9)$, $(t_2, v_2) = (4, 1)$. This divides the interval $[0, 4]$ into $n = 2$ subintervals.

Applying the trapezoidal rule formula:  
$$ \Delta s \approx \frac{1}{2} \sum_{i=1}^{2} (t_i - t_{i-1})(v_i + v_{i-1}) $$  

**Step 1: Calculate the first subinterval ($i = 1$)**  
- Time difference: $t_1 - t_0 = 2 - 0 = 2$ s  
- Velocity sum: $v_1 + v_0 = 9 + 5 = 14$ m/s  
- Contribution: $\frac{1}{2} \times 2 \times 14 = \frac{1}{2} \times 28 = 14$ m  

**Step 2: Calculate the second subinterval ($i = 2$)**  
- Time difference: $t_2 - t_1 = 4 - 2 = 2$ s  
- Velocity sum: $v_2 + v_1 = 1 + 9 = 10$ m/s  
- Contribution: $\frac{1}{2} \times 2 \times 10 = \frac{1}{2} \times 20 = 10$ m  

**Step 3: Sum the contributions**  
$$ \Delta s \approx 14 + 10 = 24 \text{ m} $$  

The estimated displacement is 24 meters.

## Answer
$$\boxed{24}$$

------
## Problem 3
##### Background  
In aerospace engineering, spacecraft often perform controlled descents onto planetary surfaces. During the final landing phase, retro-rockets fire to decelerate the vehicle. Consider a Mars lander with initial downward velocity $v_0$ at $t = 0$. The rockets provide constant deceleration $a$, so its velocity (in m/s) is $v(t) = v_0 - a t$ (positive direction downward). The lander starts at position $s(0) = 0$ and stops when $v(t) = 0$. Understanding the stopping distance is critical for mission safety and fuel planning.

##### Knowledge Points Tested  
- Integration of velocity to find displacement  
- Solving for the time when velocity becomes zero  
- Applying definite integrals to compute distance traveled under constant acceleration  

##### Intradisciplinary Connections  
- Connects to kinematics equations for motion under constant acceleration.  
- Extends to optimization problems in trajectory design.  

##### Interdisciplinary Connections  
- **Aerospace Engineering**: Calculating landing distances for spacecraft.  
- **Control Systems**: Real-time velocity management during descent.  

##### Real-World Applications  
- Used in Mars rover landings (e.g., Perseverance) to ensure safe touchdown velocities.  
- Applied in drone delivery systems for precision landing on moving targets.  

##### Problem Statement  
A Mars lander descends with velocity $v(t) = v_0 - a t$, where $v_0$ is the initial velocity and $a$ is the constant deceleration magnitude. Determine the total distance traveled by the lander from $t = 0$ until it stops. Express your answer symbolically in terms of $v_0$ and $a$.

## Solution
**Step 1: Find the stopping time**  
The lander stops when $v(t) = 0$:  

$$
v_0 - a t_{\text{stop}} = 0 \implies t_{\text{stop}} = \frac{v_0}{a}.
$$


**Step 2: Set up the position integral**  
Distance traveled is the integral of velocity from $t = 0$ to $t = t_{\text{stop}}$:  

$$
s(t_{\text{stop}}) = \int_0^{t_{\text{stop}}} v(t)  dt = \int_0^{v_0 / a} (v_0 - a t)  dt.
$$


**Step 3: Evaluate the integral**  
Compute the antiderivative:  

$$
\int (v_0 - a t)  dt = v_0 t - \frac{1}{2} a t^2.
$$
  
Apply the limits:  

$$
\left[ v_0 t - \frac{1}{2} a t^2 \right]_0^{v_0 / a} = \left( v_0 \cdot \frac{v_0}{a} - \frac{1}{2} a \cdot \left( \frac{v_0}{a} \right)^2 \right) - (0) = \frac{v_0^2}{a} - \frac{1}{2} a \cdot \frac{v_0^2}{a^2} = \frac{v_0^2}{a} - \frac{v_0^2}{2a}.
$$
  
Combine terms:  

$$
\frac{2v_0^2 - v_0^2}{2a} = \frac{v_0^2}{2a}.
$$
  
Thus, the distance traveled is $\frac{v_0^2}{2a}$.

## Answer
$$\boxed{\dfrac{v_{0}^{2}}{2a}}$$

------
## Problem 4
##### Background
In rocket science, engineers often model the velocity of a rocket during its initial ascent phase to predict its trajectory. The velocity function provides critical data for determining the rocket's position over time, which is essential for mission planning and safety. Here, we consider a rocket launched vertically from ground level, with its velocity described by a quadratic function of time.

##### Knowledge Points Tested
- Integration of velocity to obtain displacement (position)
- Application of definite integrals with initial conditions
- Handling polynomial functions in kinematics

##### Intradisciplinary Connections
- Relates to acceleration (derivative of velocity) and jerk (derivative of acceleration)
- Extends to motion under non-constant acceleration, beyond standard constant-acceleration equations

##### Interdisciplinary Connections
- Physics: Kinematics in one dimension
- Engineering: Trajectory modeling in aerospace systems
- Mathematics: Fundamental theorem of calculus

##### Real-World Applications
- Predicting rocket altitude for stage separation or parachute deployment
- Estimating maximum height in sounding rocket experiments
- Validating telemetry data from launch vehicles

##### Problem Statement
A rocket is launched vertically from ground level. Its vertical velocity at time $t$ is given by $v(t) = a t - b t^{2}$, where $a$ and $b$ are positive constants with units of m/s² and m/s³ respectively. Determine the height $H$ of the rocket at time $T$. Express $H$ in terms of $a$, $b$, and $T$.

## Solution
The height $H$ at time $T$ is the displacement from the initial position (ground level). Since velocity is the derivative of position with respect to time, position is the integral of velocity. Given the initial condition that the rocket starts at ground level, we have $s(0) = 0$. Thus:
$$ H = s(T) = \int_{0}^{T} v(t)  dt = \int_{0}^{T} (a t - b t^{2})  dt $$

Split the integral into two terms:
$$ \int_{0}^{T} (a t - b t^{2})  dt = a \int_{0}^{T} t  dt - b \int_{0}^{T} t^{2}  dt $$

Evaluate each integral separately. The antiderivative of $t$ is $\frac{t^{2}}{2}$, and the antiderivative of $t^{2}$ is $\frac{t^{3}}{3}$:
$$ \int_{0}^{T} t  dt = \left[ \frac{t^{2}}{2} \right]_{0}^{T} = \frac{T^{2}}{2} - \frac{0^{2}}{2} = \frac{T^{2}}{2} $$
$$ \int_{0}^{T} t^{2}  dt = \left[ \frac{t^{3}}{3} \right]_{0}^{T} = \frac{T^{3}}{3} - \frac{0^{3}}{3} = \frac{T^{3}}{3} $$

Substitute these results back:
$$ a \cdot \frac{T^{2}}{2} - b \cdot \frac{T^{3}}{3} = \frac{a T^{2}}{2} - \frac{b T^{3}}{3} $$

Therefore, the height at time $T$ is $\frac{a T^{2}}{2} - \frac{b T^{3}}{3}$.

## Answer
$$\boxed{\dfrac{a T^{2}}{2} - \dfrac{b T^{3}}{3}}$$

------
# relationship between linear and angular quantities

## Problem 0
##### Background
In many mechanical systems, such as engines or rotating machinery, understanding the motion of points on rotating bodies is crucial. Consider a disk, like a flywheel in an engine, rotating at a constant speed. The linear velocity of any point on its rim depends on its distance from the center and the angular speed of rotation, but its components vary based on the point's angular position. This problem explores how to mathematically describe this relationship.

##### Knowledge Points Tested
1. Relationship between linear velocity ($v$) and angular velocity ($\omega$): $v = R\omega$.
2. Angular position as a function of time: $\theta = \theta_0 + \omega t$.
3. Vector decomposition of velocity in Cartesian coordinates.
4. Differentiation of trigonometric functions to obtain velocity components.

##### Intradisciplinary Connections
This problem connects rotational kinematics (angular velocity, angular displacement) with linear kinematics (velocity components) and calculus (differentiation of position functions).

##### Interdisciplinary Connections
- **Engineering**: Essential for analyzing stresses in rotating components like turbine blades or gears.
- **Robotics**: Used in trajectory planning for robotic arms with rotational joints.
- **Animation/Graphics**: Applied to simulate realistic motion of rotating objects in virtual environments.

##### Real-World Applications
- **Automotive**: Calculating the velocity of points on a rotating tire for traction analysis.
- **Aerospace**: Determining blade-tip velocities in jet engines to avoid supersonic shock waves.
- **Manufacturing**: Optimizing cutting speeds at different radii on a rotating tool in CNC machining.

##### Problem Statement
A disk of radius $R$ rotates counterclockwise with a constant angular speed $\omega$ about a fixed axis through its center. At time $t = 0$, a point $P$ on the rim is at an angle $\phi$ from the positive $x$-axis. Derive an expression for the $x$-component of the linear velocity of point $P$ at an arbitrary time $t$. Express your answer in terms of $R$, $\omega$, $\phi$, and $t$.  
*Use standard mathematical notation:  
- Angles are in radians.  
- Use $\sin$, $\cos$, etc., and leave arguments unevaluated (e.g., $\sin(\phi + \omega t)$).  
- Express fractions using $\frac{a}{b}$.*

## Solution
The linear velocity of a point on a rotating rigid body is tangent to its circular path. Its magnitude is $v = R\omega$, but its components depend on the angular position.  

**Step 1: Express angular position as a function of time**  
The angular position $\theta$ of point $P$ at time $t$ is:  
$$\theta(t) = \phi + \omega t$$  
since the disk rotates counterclockwise at constant angular speed $\omega$, and $\phi$ is the initial angle.

**Step 2: Write the position coordinates**  
The Cartesian coordinates of point $P$ are:  
$$x(t) = R \cos(\theta(t)) = R \cos(\phi + \omega t)$$  
$$y(t) = R \sin(\phi + \omega t)$$  

**Step 3: Differentiate to find velocity components**  
The $x$-component of velocity is the derivative of $x(t)$ with respect to time:  
$$v_x = \frac{dx}{dt} = \frac{d}{dt} \left[ R \cos(\phi + \omega t) \right]$$  
Apply the chain rule:  
$$v_x = R \cdot \left[ -\sin(\phi + \omega t) \right] \cdot \frac{d}{dt}(\phi + \omega t)$$  
Since $\phi$ is constant and $\frac{d}{dt}(\omega t) = \omega$:  
$$v_x = -R \omega \sin(\phi + \omega t)$$  

**Conclusion**  
The $x$-component of the linear velocity of point $P$ at time $t$ is:  
$$\boxed{-R \omega \sin(\phi + \omega t)}$$

## Answer
$$\boxed{-R \omega \sin(\phi + \omega t)}$$

------
## Problem 1
##### Background
In automotive engineering, the motion of a vehicle is directly linked to the rotation of its wheels. When a car accelerates linearly, its tires rotate without slipping—a fundamental concept in kinematics. This scenario allows us to connect linear quantities (like speed and acceleration) to angular quantities (like angular speed and angular acceleration) through the tire's geometry.

##### Knowledge Points Tested
- Relationship between linear velocity and angular velocity: $v = r\omega$
- Relationship between linear acceleration and angular acceleration: $a = r\alpha$
- Kinematic equations for motion with constant acceleration
- Concept of rolling without slipping

##### Intradisciplinary Connections
- Extends linear kinematics (e.g., $v = u + at$) to rotational kinematics (e.g., $\omega_f = \omega_i + \alpha t$)
- Reinforces the parallel between translational and rotational dynamics

##### Interdisciplinary Connections
- **Mechanical Engineering**: Tire design and traction control systems rely on angular acceleration calculations to prevent slipping.
- **Robotics**: Wheeled robots use similar principles for navigation and stability control.

##### Real-World Applications
- **Anti-lock Braking Systems (ABS)**: Sensors monitor wheel angular acceleration to detect slippage and modulate braking force.
- **Performance Testing**: Automotive engineers measure angular acceleration to optimize acceleration profiles and powertrain efficiency.

##### Problem Statement
A car starts from rest and accelerates in a straight line with constant linear acceleration. Its tires roll without slipping. After a time $t$, the car reaches a linear speed $v$. The radius of each tire is $r$.  

Derive an expression for the angular acceleration $\alpha$ of the tires during this acceleration. Express your answer in terms of $v$, $t$, and $r$.

## Solution
**Step 1: Identify key relationships**  
Since the tires roll without slipping, the linear acceleration $a$ of the car is related to the angular acceleration $\alpha$ of the tires by:  
$$ a = r \alpha $$  

**Step 2: Apply linear kinematics**  
The car starts from rest ($\text{initial speed } u = 0$) and reaches speed $v$ after time $t$ with constant acceleration. Using the kinematic equation:  
$$ v = u + at $$  
Substitute $u = 0$:  
$$ v = at $$  
Solve for linear acceleration $a$:  
$$ a = \frac{v}{t} $$  

**Step 3: Relate linear and angular acceleration**  
Substitute $a = \frac{v}{t}$ into $a = r \alpha$:  
$$ \frac{v}{t} = r \alpha $$  
Solve for angular acceleration $\alpha$:  
$$ \alpha = \frac{v}{r t} $$

## Answer
$$\boxed{\dfrac{v}{r t}}$$

------
## Problem 2
##### Background
In many mechanical systems, such as industrial flywheels or rotating machinery, understanding the connection between linear and angular motion is crucial. Consider a solid disc, like a grinding wheel, that accelerates from rest. A point on its rim moves with both angular and linear characteristics. The angular quantities (like angular velocity and acceleration) are intrinsically linked to the linear quantities (like tangential velocity) via the disc's radius.

##### Knowledge Points Tested
- Conversion between linear and angular velocity: $v = R\omega$
- Rotational kinematics under constant acceleration: $\omega^2 = \omega_0^2 + 2\alpha\theta$
- Angular displacement calculation: $\theta = 2\pi \times \text{rotations}$

##### Intradisciplinary Connections
This problem integrates concepts from uniform circular motion (tangential velocity) and rotational dynamics (angular acceleration). It reinforces how rotational kinematics parallels linear kinematics, with angular displacement ($\theta$), angular velocity ($\omega$), and angular acceleration ($\alpha$) corresponding to their linear counterparts.

##### Interdisciplinary Connections
- **Engineering**: Essential for designing rotating systems (e.g., turbines, centrifuges).
- **Robotics**: Critical for programming joint rotations in robotic arms.
- **Sports Science**: Analyzes rotational motion in discus throw or figure skating.

##### Real-World Applications
- **Automotive Industry**: Calculating the acceleration of brake discs or drivetrain components.
- **Manufacturing**: Optimizing the spin-up time of lathes or CNC machines.
- **Energy Sector**: Modeling flywheel energy storage systems where angular acceleration affects efficiency.

##### Problem Statement
A solid disc of radius $R$ starts from rest ($\omega_0 = 0$) and undergoes constant angular acceleration. After completing exactly 3 full rotations, a point on its rim reaches a linear (tangential) velocity $v$. Derive an expression for the disc's angular acceleration $\alpha$ in terms of $v$ and $R$. Express your answer as a simplified analytic expression using the given symbols only.

## Solution
**Step 1: Relate linear velocity to angular velocity**  
The linear (tangential) velocity $v$ of a point on the rim is related to the angular velocity $\omega$ by:  
$$ v = R \omega $$  
At the end of 3 rotations, $\omega$ is the final angular velocity, so:  
$$ \omega = \frac{v}{R} $$  

**Step 2: Calculate angular displacement**  
One full rotation equals $2\pi$ radians. Thus, 3 rotations give:  
$$ \theta = 3 \times 2\pi = 6\pi \text{ radians} $$  

**Step 3: Apply rotational kinematics**  
The kinematic equation for rotational motion under constant acceleration, starting from rest ($\omega_0 = 0$), is:  
$$ \omega^2 = \omega_0^2 + 2\alpha\theta $$  
Substitute $\omega_0 = 0$, $\omega = v/R$, and $\theta = 6\pi$:  
$$ \left( \frac{v}{R} \right)^2 = (0)^2 + 2\alpha(6\pi) $$  
Simplify:  
$$ \frac{v^2}{R^2} = 12\pi \alpha $$  

**Step 4: Solve for angular acceleration**  
Isolate $\alpha$:  
$$ \alpha = \frac{v^2}{12\pi R^2} $$  
This is the expression for angular acceleration in terms of $v$ and $R$.

## Answer
$$\boxed{\dfrac{v^{2}}{12\pi R^{2}}}$$

------
## Problem 3
##### Background
Flywheels are mechanical energy storage devices that rely on rotational motion. In engineering applications like regenerative braking systems, flywheel rims experience significant centripetal forces. Understanding the link between linear motion at the rim and rotational properties is essential for designing efficient systems that avoid material stress failures.

##### Knowledge Points Tested
1. Definition of centripetal acceleration: $a_c = r \omega^2$
2. Relationship between diameter and radius: $r = d/2$
3. Algebraic manipulation to solve for angular velocity $\omega$

##### Intradisciplinary Connections
- Connects to kinematics of uniform circular motion and rotational dynamics.
- Reinforces dimensional analysis (e.g., verifying units of $\omega$ as rad/s).

##### Interdisciplinary Connections
- Materials Science: Centripetal acceleration determines tensile stress in flywheel materials.
- Mechanical Engineering: Critical for designing energy storage systems in electric vehicles and industrial machinery.

##### Real-World Applications
- Flywheel batteries in hybrid vehicles store kinetic energy during braking.
- Industrial punch presses use flywheels to deliver high torque; angular velocity affects production speed.
- Centrifuges in medical labs rely on precise $\omega$ control to separate substances.

##### Problem Statement
A flywheel has a diameter $d$. The centripetal acceleration at its rim is $a_c$. Derive an expression for the angular velocity $\omega$ of the flywheel in terms of $d$ and $a_c$.  

**Express your final answer as an analytic expression using the symbols $d$ and $a_c$.** Ensure the expression is simplified and radical-free in the denominator. Do not substitute numerical values.

## Solution
**Step 1: Relate diameter to radius**  
The radius $r$ is half the diameter:  
$$ r = \frac{d}{2} $$

**Step 2: Apply the centripetal acceleration formula**  
Centripetal acceleration $a_c$ is given by:  
$$ a_c = r \omega^2 $$  
Substitute the expression for $r$:  
$$ a_c = \left( \frac{d}{2} \right) \omega^2 $$

**Step 3: Solve for $\omega^2$**  
Rearrange the equation to isolate $\omega^2$:  
$$ \omega^2 = \frac{a_c}{\frac{d}{2}} = \frac{2a_c}{d} $$

**Step 4: Solve for $\omega$**  
Take the square root of both sides. Since angular velocity is positive:  
$$ \omega = \sqrt{\frac{2a_c}{d}} $$  

**Simplification note:**  
The expression $\sqrt{\frac{2a_c}{d}}$ is already simplified, with no radicals in the denominator.

## Answer
$$\boxed{\sqrt{\frac{2a_{c}}{d}}}$$

------
## Problem 4
##### Background
In the study of rotational motion, the relationship between linear and angular quantities is fundamental. When an object like a wheel rolls without slipping, every point on its rim moves such that the linear distance traveled equals the arc length traversed. This principle is critical in designing mechanical systems, from bicycles to industrial gears, ensuring accurate motion transfer and energy efficiency.

##### Knowledge Points Tested
- Conversion between angular displacement (in revolutions) and radians.
- Relationship between linear displacement $s$ and angular displacement $\theta$ for rolling without slipping: $s = r \theta$.
- Algebraic manipulation to solve for an unknown quantity.

##### Intradisciplinary Connections
This problem connects to kinematics (linear and angular motion) and dynamics (torque and rotational inertia), forming a basis for understanding more complex systems like coupled rotations in gear trains or planetary motion approximations.

##### Interdisciplinary Connections
- **Engineering**: Wheel design in vehicles requires precise radius calculations to synchronize speedometers and odometers.
- **Robotics**: Wheel radius determination is essential for path planning and control algorithms in mobile robots.
- **Mathematics**: Unit conversions (revolutions to radians) and solving equations with exact symbolic expressions.

##### Real-World Applications
- **Transportation**: Bicycle wheel calibration affects distance tracking and gear ratios.
- **Manufacturing**: Conveyor belt systems use rollers of specific radii to control linear feed rates.
- **Sports Science**: Optimizing wheelchair wheel radii for Paralympic racing based on stride-length equivalents.

##### Problem Statement
A bicycle wheel rolls without slipping along a straight path. During its motion, it completes exactly 10 revolutions while covering a linear distance of 15.7 meters. Determine the radius $r$ of the wheel. Express your answer as an exact fraction in terms of $\pi$. Provide only the numerical coefficient (without units) in the boxed answer.

*Note: 15.7 meters is exactly $\frac{157}{10}$ meters. Do not substitute numerical values for $\pi$.*

## Solution
**Step 1: Convert angular displacement to radians**  
Given 10 revolutions, and knowing 1 revolution = $2\pi$ radians:  

$$
\theta = 10 \times 2\pi = 20\pi \text{ radians}.
$$


**Step 2: Apply the rolling-without-slipping condition**  
For rolling without slipping, the linear distance traveled $s$ is related to the angular displacement $\theta$ and radius $r$ by:  

$$
s = r \theta.
$$
  
Substitute $s = 15.7  \text{m} = \frac{157}{10}  \text{m}$ and $\theta = 20\pi$ radians:  

$$
\frac{157}{10} = r \times 20\pi.
$$


**Step 3: Solve for the radius $r$**  
Isolate $r$:  

$$
r = \frac{\frac{157}{10}}{20\pi} = \frac{157}{10 \times 20\pi} = \frac{157}{200\pi}.
$$
  
This is the exact expression for the radius in meters. The numerical coefficient (without units) is $\frac{157}{200\pi}$.

**Final Answer**  
The radius of the wheel is $\frac{157}{200\pi}$ meters. As required, only the numerical expression is boxed.

## Answer
$$\boxed{\dfrac{157}{200\pi}}$$

------
# satellite orbital speed and period

## Problem 0
##### Background
Satellites in orbit around Earth must maintain specific speeds to stay in a stable circular path. The orbital speed depends on the distance from Earth's center and the planet's gravitational influence. Understanding this involves Newton's law of gravitation and centripetal acceleration, which together govern circular motion under gravity.

##### Knowledge Points Tested
1. Newton's law of universal gravitation: $F_g = G \frac{M m}{r^2}$, where $F_g$ is the gravitational force, $G$ is the gravitational constant, $M$ is Earth's mass, $m$ is the satellite's mass, and $r$ is the distance between centers.
2. Centripetal force for circular motion: $F_c = \frac{m v^2}{r}$, where $v$ is the orbital speed.
3. Equating gravitational force to centripetal force for a stable orbit.
4. Expressing orbital speed in terms of Earth's surface gravity $g$ and radius $R$, using $g = \frac{G M}{R^2}$.

##### Intradisciplinary Connections
This problem connects to Kepler's laws of planetary motion, energy conservation in orbits, and geostationary satellite calculations.

##### Interdisciplinary Connections
- **Aerospace Engineering**: Satellite deployment and orbital mechanics.
- **Geophysics**: Gravitational field variations and their effect on satellite trajectories.

##### Real-World Applications
Calculating orbital speeds is essential for:
- Launching communication satellites (e.g., GPS, Starlink).
- Maintaining the International Space Station's orbit.
- Planning interplanetary missions using gravitational assists.

##### Problem Statement
A satellite is in a circular orbit at a height $h$ above Earth's surface.  
(a) Starting from Newton's law of gravitation, derive an expression for the orbital speed $v$ in terms of $G$ (gravitational constant), $M$ (Earth's mass), $R$ (Earth's radius), and $h$.  
(b) Rewrite $v$ in terms of $g$ (acceleration due to gravity at Earth's surface), $R$, and $h$ using the relationship $g = \frac{G M}{R^2}$.  
(c) Using the expression from part (b), calculate $v$ for $h = 500 \text{ km}$. Use $R = 6370 \text{ km}$ and $g = 9.80 \text{ m/s}^2$.  
Convert all distances to meters, express the final numerical answer in meters per second in scientific notation, and round to three significant figures. Provide only the numerical value for part (c).

## Solution
#### Part (a): Derivation in terms of $G$, $M$, $R$, and $h$
For a stable circular orbit, the gravitational force provides the centripetal force:  
$$ G \frac{M m}{r^2} = \frac{m v^2}{r} $$  
where $r$ is the distance from Earth's center to the satellite, so $r = R + h$. Cancel $m$ (satellite mass) from both sides:  
$$ G \frac{M}{r^2} = \frac{v^2}{r} $$  
Multiply both sides by $r$:  
$$ G \frac{M}{r} = v^2 $$  
Take the square root to solve for $v$:  
$$ v = \sqrt{\frac{G M}{r}} $$  
Substitute $r = R + h$:  
$$ v = \sqrt{\frac{G M}{R + h}} $$  

#### Part (b): Rewriting in terms of $g$, $R$, and $h$
Given $g = \frac{G M}{R^2}$, solve for $G M$:  
$$ G M = g R^2 $$  
Substitute into the expression from part (a):  
$$ v = \sqrt{\frac{g R^2}{R + h}} $$  
Simplify:  
$$ v = R \sqrt{\frac{g}{R + h}} $$  

#### Part (c): Numerical calculation for $h = 500 \text{ km}$
- Convert heights to meters:  
  $R = 6370 \text{ km} = 6370 \times 10^3 \text{ m} = 6.370 \times 10^6 \text{ m}$  
  $h = 500 \text{ km} = 500 \times 10^3 \text{ m} = 5.000 \times 10^5 \text{ m}$  
- Compute $R + h$:  
  $R + h = 6.370 \times 10^6 + 5.000 \times 10^5 = 6.870 \times 10^6 \text{ m}$  
- Substitute into $v = R \sqrt{\frac{g}{R + h}}$:  
  $$ v = (6.370 \times 10^6) \sqrt{\frac{9.80}{6.870 \times 10^6}} $$  
- Simplify the fraction inside the square root:  
  $$ \frac{9.80}{6.870 \times 10^6} = 1.42649 \times 10^{-6} $$  
- Compute the square root:  
  $$ \sqrt{1.42649 \times 10^{-6}} = \sqrt{1.42649} \times \sqrt{10^{-6}} = 1.19436 \times 10^{-3} $$  
- Multiply by $R$:  
  $$ v = (6.370 \times 10^6) \times (1.19436 \times 10^{-3}) = 7610.077 \text{ m/s} $$  
- Round to three significant figures:  
  $7610$ has four significant figures. Express in scientific notation: $7.610 \times 10^3$. Rounding to three significant figures gives $7.61 \times 10^3 \text{ m/s}$.  
The numerical value is $7.61 \times 10^3$.

## Answer
$$\boxed{7.61 \times 10^{3}}$$

------
## Problem 1
##### Background
A geostationary satellite orbits Earth such that it remains fixed above a specific point on the equator. This requires its orbital period to precisely match Earth's rotational period relative to the fixed stars (a sidereal day). However, common timekeeping uses the solar day (24 hours), defined as the time between consecutive solar noons. The difference arises because Earth orbits the Sun while rotating, causing the solar day to be longer than the sidereal day. The tropical year ($T_{year}$) is the time for Earth to complete one orbit around the Sun relative to the Sun.

##### Knowledge Points Tested
1. Definition of geostationary orbit: orbital period equals Earth's sidereal rotational period.
2. Relationship between sidereal day, solar day, and tropical year.
3. Algebraic derivation of time period relations.

##### Intradisciplinary Connections
- Orbital mechanics: circular motion and synchronization with planetary rotation.
- Astronomy: sidereal vs. solar time systems and Earth's orbital motion.

##### Interdisciplinary Connections
- Geodesy: precise time measurement for satellite positioning.
- Chronometry: historical development of calendars based on solar/sidereal discrepancies.

##### Real-World Applications
Geostationary satellites enable global communications (e.g., TV broadcasting, weather monitoring) by maintaining fixed positions relative to ground stations. Their orbital periods must account for the sidereal/solar difference to avoid positional drift.

##### Problem Statement
Derive an expression for the orbital period $T$ of a geostationary satellite in terms of Earth's solar day ($T_{solar}$) and tropical year ($T_{year}$). Use only the given symbols in your final analytic expression.  
*Hint: Consider that in one tropical year, Earth completes one fewer solar-day rotation than sidereal-day rotation due to its orbital motion.*

## Solution
#### Step 1: Establish Key Relationships  
Let $T_{sidereal}$ be Earth's sidereal rotational period (the geostationary orbital period). The solar day ($T_{solar}$) and tropical year ($T_{year}$) are given.  
- In one tropical year, Earth completes $\frac{T_{year}}{T_{sidereal}}$ sidereal rotations (relative to fixed stars).  
- In the same duration, Earth completes $\frac{T_{year}}{T_{solar}}$ solar rotations (relative to the Sun).  

#### Step 2: Relate Sidereal and Solar Rotations  
As Earth orbits the Sun, the direction to the Sun changes. After one full orbit (tropical year), Earth has rotated one extra time relative to fixed stars compared to rotations relative to the Sun:  
$$ \frac{T_{year}}{T_{sidereal}} = \frac{T_{year}}{T_{solar}} + 1 $$  
This equation arises because Earth must rotate $360^\circ$ extra to compensate for its orbital revolution.  

#### Step 3: Solve for $T_{sidereal}$  
Rearrange the equation:  
$$ \frac{T_{year}}{T_{sidereal}} - \frac{T_{year}}{T_{solar}} = 1 $$  
Factor $T_{year}$:  
$$ T_{year} \left( \frac{1}{T_{sidereal}} - \frac{1}{T_{solar}} \right) = 1 $$  
Isolate the reciprocal terms:  
$$ \frac{1}{T_{sidereal}} - \frac{1}{T_{solar}} = \frac{1}{T_{year}} $$  
$$ \frac{1}{T_{sidereal}} = \frac{1}{T_{solar}} + \frac{1}{T_{year}} $$  

#### Step 4: Express $T_{sidereal}$ Analytically  
Combine the right-hand side:  
$$ \frac{1}{T_{sidereal}} = \frac{T_{year} + T_{solar}}{T_{solar} \, T_{year}} $$  
Invert both sides:  
$$ T_{sidereal} = \frac{T_{solar} \, T_{year}}{T_{solar} + T_{year}} $$  
Since the geostationary orbital period $T = T_{sidereal}$, the final expression is:  
$$ T = \frac{T_{solar} \, T_{year}}{T_{solar} + T_{year}} $$

## Answer
$$\boxed{\frac{T_{solar} \, T_{year}}{T_{solar} + T_{year}}}$$

------
## Problem 2
##### Background
Satellites orbiting Earth must maintain a specific speed to stay in a stable circular orbit. This speed depends on the satellite's altitude due to the balance between gravitational pull and the centripetal force required for circular motion. Engineers often need to determine orbital parameters like altitude when designing satellite missions for Earth observation or communication.

##### Knowledge Points Tested
- Newton's law of universal gravitation
- Centripetal acceleration in circular motion
- Algebraic manipulation to derive expressions
- Relationship between orbital speed, radius, and gravitational acceleration

##### Intradisciplinary Connections
- Connects to Kepler's laws of planetary motion
- Extends to energy conservation in orbital mechanics (kinetic and potential energy)
- Relates to gravitational field theory and central forces

##### Interdisciplinary Connections
- **Aerospace Engineering:** Satellite deployment and trajectory calculations
- **Geophysics:** Analysis of Earth's gravitational field variations
- **Data Science:** Computational modeling of orbital dynamics

##### Real-World Applications
- Designing satellite constellations for GPS or global internet coverage
- Predicting re-entry trajectories for space debris
- Planning lunar or Mars missions using gravitational assists

##### Problem Statement
A satellite is in a circular orbit around Earth with an orbital speed $v$. Derive an expression for its altitude $h$ above Earth's surface. Use the following symbolic constants:  
- $v$ = orbital speed of the satellite  
- $R$ = radius of Earth  
- $g$ = acceleration due to gravity at Earth's surface  

Express $h$ exclusively in terms of $v$, $R$, and $g$. Ensure your final expression is simplified and boxed.  
*Note: Altitude $h$ is measured from Earth's surface to the satellite.*

## Solution
**Step 1: Gravitational force equals centripetal force**  
For a satellite of mass $m$ in circular orbit at distance $r$ from Earth's center:  

$$
\frac{GMm}{r^2} = \frac{mv^2}{r}
$$
  
where $G$ is the gravitational constant and $M$ is Earth's mass. Simplify by canceling $m$:  

$$
\frac{GM}{r} = v^2 \quad (1)
$$
  

**Step 2: Relate $GM$ to $g$ and $R$**  
At Earth's surface, gravitational acceleration $g$ is:  

$$
g = \frac{GM}{R^2} \implies GM = gR^2 \quad (2)
$$
  

**Step 3: Substitute (2) into (1)**  
Replace $GM$ in equation (1):  

$$
\frac{gR^2}{r} = v^2
$$
  
Solve for $r$:  

$$
r = \frac{gR^2}{v^2} \quad (3)
$$
  

**Step 4: Express altitude $h$**  
The orbital radius $r$ is the sum of Earth's radius $R$ and altitude $h$:  

$$
r = R + h \quad (4)
$$
  
Substitute (4) into (3):  

$$
R + h = \frac{gR^2}{v^2}
$$
  
Solve for $h$:  

$$
h = \frac{gR^2}{v^2} - R
$$
  

**Step 5: Simplify the expression**  
Factor out $R$:  

$$
h = R \left( \frac{gR}{v^2} - 1 \right)
$$
  
This is the altitude in terms of $v$, $R$, and $g$.

## Answer
\[
\boxed{R \left( \frac{g R}{v^{2}} - 1 \right)}
\]

------
## Problem 3
##### Background
The space elevator is a proposed megastructure that would transport materials from Earth's surface to geostationary orbit using a cable anchored to Earth and extending beyond geostationary altitude. This concept relies on understanding orbital mechanics, particularly the relationship between orbital velocity, radius, and Earth's rotation. At geostationary orbit, an object's orbital period matches Earth's sidereal rotation period $T$, making it appear stationary relative to the surface. For other points along the cable, the motion differs from a natural orbit.

##### Knowledge Points Tested
1. Relationship between linear velocity, angular velocity, and radius: $v = \omega r$.
2. Centripetal force requirement for circular motion: $F_c = \frac{mv^2}{r}$.
3. Newton's law of universal gravitation: $F_g = \frac{GMm}{r^2}$.
4. Equating gravitational force to centripetal force for orbital velocity derivation.

##### Intradisciplinary Connections
- Kepler's third law: The square of the orbital period is proportional to the cube of the semi-major axis, applicable to geostationary orbit derivation.
- Conservation of energy in gravitational fields.

##### Interdisciplinary Connections
- Aerospace engineering: Space elevator design involves material science and structural dynamics to withstand tension and gravitational forces.
- Celestial navigation: Understanding angular velocity and orbital periods is essential for satellite positioning.

##### Real-World Applications
- Geostationary satellites are used for telecommunications, weather monitoring, and broadcasting due to their fixed position relative to Earth.
- Space elevators could revolutionize space travel by reducing launch costs, though current materials lack sufficient tensile strength.

##### Problem Statement
Earth (mass $M$) rotates with a sidereal period $T$. The gravitational constant is $G$. Consider a space elevator extending from Earth's surface to beyond geostationary orbit. The cable rotates with Earth, so any point at distance $r$ from Earth's center moves with angular velocity $\omega$.  

(a) Derive the linear speed $v$ of a point on the elevator at distance $r$ in terms of $\omega$ and $r$. Then express $\omega$ in terms of $T$.  
(b) Derive the orbital velocity $v_{\text{orbit}}$ required for a natural circular orbit at distance $r$ (without the elevator) in terms of $G$, $M$, and $r$.  
(c) At geostationary radius $r_g$, the elevator's linear speed equals the orbital velocity. Use this to derive $r_g$ in terms of $G$, $M$, and $T$.  
(d) For a point on the elevator at $r < r_g$, compute $v_{\text{orbit}}^2 - v^2$ (difference of squared velocities) in terms of $G$, $M$, $T$, and $r$.  

Express all answers analytically. Use $\pi$ explicitly. For part (d), combine constants where possible.

## Solution
#### Solution for (a)
The linear speed $v$ for circular motion with angular velocity $\omega$ at radius $r$ is:  
$$ v = \omega r $$  
Earth completes one full rotation of $2\pi$ radians in sidereal period $T$, so:  
$$ \omega = \frac{2\pi}{T} $$  
Thus,  
$$ v = \left( \frac{2\pi}{T} \right) r $$  

#### Solution for (b)
For a satellite in circular orbit at radius $r$, gravitational force provides centripetal force:  
$$ \frac{GMm}{r^2} = \frac{m v_{\text{orbit}}^2}{r} $$  
Cancel $m$ and solve for $v_{\text{orbit}}$:  
$$ \frac{GM}{r^2} = \frac{v_{\text{orbit}}^2}{r} $$  
$$ v_{\text{orbit}}^2 = \frac{GM}{r} $$  
$$ v_{\text{orbit}} = \sqrt{\frac{GM}{r}} $$  

#### Solution for (c)
At $r_g$, the elevator's linear speed equals orbital velocity:  
$$ \text{Elevator speed } v = \omega r_g = \frac{2\pi r_g}{T} $$  
$$ \text{Orbital velocity } v_{\text{orbit}} = \sqrt{\frac{GM}{r_g}} $$  
Set equal:  
$$ \frac{2\pi r_g}{T} = \sqrt{\frac{GM}{r_g}} $$  
Square both sides:  
$$ \left( \frac{2\pi r_g}{T} \right)^2 = \frac{GM}{r_g} $$  
$$ \frac{4\pi^2 r_g^2}{T^2} = \frac{GM}{r_g} $$  
Multiply both sides by $r_g$:  
$$ \frac{4\pi^2 r_g^3}{T^2} = GM $$  
Solve for $r_g$:  
$$ r_g^3 = \frac{GM T^2}{4\pi^2} $$  
$$ r_g = \sqrt[3]{\frac{GM T^2}{4\pi^2}} $$  

#### Solution for (d)
From (b), orbital velocity squared at $r$ is:  
$$ v_{\text{orbit}}^2 = \frac{GM}{r} $$  
From (a), elevator speed squared at $r$ is:  
$$ v^2 = \left( \frac{2\pi r}{T} \right)^2 = \frac{4\pi^2 r^2}{T^2} $$  
Compute the difference:  
$$ v_{\text{orbit}}^2 - v^2 = \frac{GM}{r} - \frac{4\pi^2 r^2}{T^2} $$  
This is the required expression in terms of $G$, $M$, $T$, and $r$.

## Answer
For (a):  
$$\boxed{v = \frac{2\pi r}{T}}$$  

For (b):  
$$\boxed{v_{\text{orbit}} = \sqrt{\frac{GM}{r}}}$$  

For (c):  
$$\boxed{r_g = \sqrt[3]{\frac{G M T^{2}}{4\pi^{2}}}}}$$  

For (d):  
$$\boxed{v_{\text{orbit}}^{2} - v^{2} = \frac{GM}{r} - \frac{4\pi^{2} r^{2}}{T^{2}}}}$$

------
# sonic boom and Mach number effects

## Problem 0
##### Background  
When an aircraft travels faster than the speed of sound, it generates a conical shock wave known as a Mach cone. The sonic boom occurs when this shock wave reaches an observer on the ground. The time delay between the aircraft passing directly overhead and the sonic boom being heard depends on the aircraft's speed, altitude, and the speed of sound. This problem explores the relationship between these quantities to determine the Mach number, defined as the ratio of the aircraft's speed to the speed of sound.

##### Knowledge Points Tested  
- Understanding of supersonic motion and the Mach cone geometry.  
- Application of the Pythagorean theorem to relate distances in the Mach cone.  
- Derivation of the Mach number using time delay, altitude, and the speed of sound.  

##### Intradisciplinary Connections  
Connects to wave propagation (shock waves) and kinematics (relative motion in two dimensions).  

##### Interdisciplinary Connections  
Relates to aeronautical engineering (supersonic flight dynamics) and earth science (atmospheric properties affecting sound speed).  

##### Real-World Applications  
Determining aircraft speed from sonic boom observations is used in aerospace testing, noise regulation compliance for supersonic flights, and military reconnaissance.  

##### Problem Statement  
A jet flies at a constant altitude $h$ and passes directly overhead an observer on the ground. The sonic boom is heard by the observer a time $t$ after the jet passes overhead. The speed of sound in air is $c$. Derive an expression for the Mach number $M$ of the jet in terms of $h$, $t$, and $c$. Ensure your final expression is simplified and boxed.  

**Answer Format Instructions**  
- Express the Mach number $M$ as a single analytic expression in terms of the given symbols $h$, $t$, and $c$.  
- Use $\sqrt{\cdot}$ for square roots and express fractions with $\frac{}{}$.  
- Do **not** substitute numerical values for any parameter.

## Solution
#### Step 1: Model the Mach Cone Geometry  
When the jet passes directly overhead at point $A$, the observer is at $O$. After time $t$, the jet moves horizontally to point $B$, covering a distance $v t$, where $v$ is the jet's speed. The sonic boom heard at time $t$ originates from the shock wave emitted when the jet was at point $A$. This shock wave travels radially outward at speed $c$, covering a distance $c t$ to reach $O$.  

The triangle $AOB$ forms a right triangle:  
- $AO = h$ (altitude, vertical leg).  
- $AB = v t$ (horizontal distance traveled by the jet).  
- $BO = c t$ (distance traveled by the shock wave, hypotenuse).  

#### Step 2: Apply the Pythagorean Theorem  
In $\triangle AOB$, the relationship is:  
$$(c t)^2 = (v t)^2 + h^2$$  

#### Step 3: Solve for the Jet's Speed $v$  
Rearrange the equation to isolate $v$:  
$$(v t)^2 = (c t)^2 - h^2$$  
$$v^2 t^2 = c^2 t^2 - h^2$$  
$$v^2 = c^2 - \frac{h^2}{t^2}$$  
$$v = \sqrt{c^2 - \frac{h^2}{t^2}} \quad \text{(taking the positive root as speed)}$$  

#### Step 4: Express the Mach Number $M$  
The Mach number $M$ is defined as $M = v / c$. Substitute the expression for $v$:  
$$M = \frac{1}{c} \sqrt{c^2 - \frac{h^2}{t^2}}$$  
Simplify the expression:  
$$M = \sqrt{\frac{c^2 - \frac{h^2}{t^2}}{c^2}} = \sqrt{\frac{c^2}{c^2} - \frac{h^2}{c^2 t^2}} = \sqrt{1 - \left(\frac{h}{c t}\right)^2}$$  

#### Final Expression  
The Mach number is:  
$$M = \sqrt{1 - \left(\frac{h}{c t}\right)^2}$$  
This is valid when $c t > h$ (i.e., the shock wave reaches the observer within the model).

## Answer
$$\boxed{\sqrt{1 - \left(\frac{h}{c t}\right)^2}}$$

------
## Problem 1
##### Background
When an object moves through a fluid faster than the speed of sound in that fluid, it generates a conical shock wave known as a Mach cone. This phenomenon is responsible for the sonic boom heard when a supersonic aircraft passes overhead. The half-angle of this cone, called the Mach angle, depends on the ratio of the object's speed to the speed of sound, known as the Mach number.

##### Knowledge Points Tested
- Wave propagation and superposition  
- Geometry of shock wave formation  
- Definition and application of Mach number  
- Inverse trigonometric functions in physical contexts  

##### Intradisciplinary Connections
- Relates to wave interference, Doppler effect, and compressible fluid dynamics in physics.  
- Connects to aerodynamic drag and sound barrier concepts in aviation physics.  

##### Interdisciplinary Connections
- Aerospace engineering: Shock wave analysis for aircraft design.  
- Mathematics: Geometric derivation using right-triangle trigonometry.  
- Earth science: Propagation of pressure waves in the atmosphere.  

##### Real-World Applications
- Predicting sonic boom intensity and ground impact zones for supersonic aircraft.  
- Designing stealth features in military aviation to minimize shock wave detection.  
- Analyzing meteor entries into Earth's atmosphere, where hypersonic speeds generate intense shock waves.  

##### Problem Statement
A fighter aircraft flies horizontally through stationary air at a constant supersonic speed $v$. The speed of sound in air is $c$ (where $v > c$). At time $t = 0$, the aircraft is at point $A$. By time $t > 0$, it reaches point $B$, where the distance $AB = vt$. During this interval, the sound wave emitted at $A$ expands as a sphere of radius $ct$ centered at $A$.  

A tangent line drawn from $B$ touches this sphere at point $C$, forming angle $\theta$ between the line $BC$ and the aircraft's direction of motion $AB$. This $\theta$ is the Mach angle.  

Using geometric properties of the sphere and tangent, derive an expression for $\theta$ in terms of the Mach number $M = v/c$. Express your answer using the inverse sine function (denoted by $\arcsin$) and simplify.

## Solution
##### Step 1: Establish the geometric relationship
Consider the sphere centered at $A$ with radius $ct$ and the tangent from $B$ to point $C$. Since $BC$ is tangent to the sphere, the radius $AC$ is perpendicular to $BC$ at $C$. Thus, $\triangle ABC$ is a right-angled triangle with the right angle at $C$.  

- Length $AB = vt$ (distance traveled by aircraft)  
- Length $AC = ct$ (radius of sound wave sphere)  
- Length $BC$ is the tangent segment (magnitude irrelevant for angle derivation).  

##### Step 2: Apply trigonometry to $\triangle ABC$
In $\triangle ABC$, focus on the vertex at $B$:  
- The side opposite to $\theta$ is $AC = ct$.  
- The hypotenuse is $AB = vt$.  

The sine of $\theta$ is:  

$$
\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{AC}{AB} = \frac{ct}{vt} = \frac{c}{v}.
$$


##### Step 3: Express in terms of Mach number
The Mach number is defined as $M = v/c$. Substitute:  

$$
\sin \theta = \frac{c}{v} = \frac{1}{M}.
$$


##### Step 4: Solve for $\theta$
Take the inverse sine of both sides:  

$$
\theta = \arcsin\left(\frac{1}{M}\right).
$$


##### Conclusion
The Mach angle $\theta$ depends solely on the Mach number $M$ and is given by $\theta = \arcsin(1/M)$.

## Answer
$$\boxed{\arcsin\left(\frac{1}{M}\right)}$$

------
## Problem 2
##### Background
When an aircraft travels faster than the speed of sound, it generates a conical shock wave known as a Mach cone. The half-angle of this cone, called the Mach angle $\theta$, is defined by $\sin \theta = 1/M$, where $M > 1$ is the Mach number. An observer on the ground experiences a sonic boom when this shock wave passes over them. The time delay between the aircraft passing directly overhead and the sonic boom being heard arises because the shock wave must travel from the point of emission to the observer. This problem explores the derivation of this time delay.

##### Knowledge Points Tested
- Mach angle definition and geometry of the Mach cone
- Trigonometric relationships in right triangles
- Kinematics of constant-velocity motion
- Relating sound propagation to aircraft motion
- Algebraic manipulation of derived expressions

##### Intradisciplinary Connections
This problem connects to wave phenomena (shock waves), aerodynamics (supersonic flight), and kinematics (relative motion). It extends the concept of the Doppler effect to supersonic regimes and integrates geometric principles with time-distance calculations.

##### Interdisciplinary Connections
The physics of sonic booms intersects with aerospace engineering (aircraft design and noise mitigation) and environmental science (assessing boom impact on communities). Mathematical tools include trigonometry, algebra, and dimensional analysis.

##### Real-World Applications
Understanding sonic boom timing is crucial for supersonic flight planning over populated areas. Recent developments in commercial supersonic travel (e.g., NASA's X-59 QueSST project) rely on accurate boom prediction models to minimize ground-level disturbances.

##### Problem Statement
An aircraft flies horizontally at a constant altitude $h$ with a constant Mach number $M > 1$. The speed of sound in air is $c$. At time $t = 0$, the aircraft passes directly over an observer on the ground. Derive an expression for the time delay $\Delta t$ between the aircraft passing overhead and the observer hearing the sonic boom. Express $\Delta t$ symbolically in terms of $h$, $M$, and $c$.  
Ensure your final answer is simplified and uses only the given parameters.  
**Format requirements**:  
- Use $\sqrt{\cdot}$ for square roots and $\frac{}{}$ for fractions.  
- Angles in trigonometric functions must be in radians (but none appear in the final answer).  
- Do **not** substitute numerical values or physical constants.

## Solution
### Step-by-Step Derivation

#### Step 1: Define key variables
- Let $v = Mc$ be the aircraft's speed.  
- The Mach angle $\theta$ satisfies $\sin \theta = \frac{1}{M}$.  
- When the sonic boom is heard, the shock wave was emitted when the aircraft was at point $A$, horizontally displaced by distance $d$ from the observer's position.  
- At the emission time, the aircraft is at $(-d, h)$, and the observer is at $(0, 0)$.  
- The straight-line distance from $A$ to the observer is $s = \sqrt{d^2 + h^2}$.

#### Step 2: Relate $d$ and $h$ using the Mach angle
The Mach cone geometry gives:  
$$\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{d}{s} = \frac{1}{M}$$  
Thus:  
$$s = M d \quad (1)$$  

Using the Pythagorean theorem:  
$$s^2 = d^2 + h^2 \quad (2)$$  

Substitute (1) into (2):  
$$(M d)^2 = d^2 + h^2$$  
$$M^2 d^2 = d^2 + h^2$$  
$$d^2 (M^2 - 1) = h^2$$  
Solve for $d$:  
$$d = \frac{h}{\sqrt{M^2 - 1}} \quad (3)$$  
(The positive root is used since distance is non-negative.)

#### Step 3: Express the distance $s$
From (1) and (3):  
$$s = M \cdot \frac{h}{\sqrt{M^2 - 1}} = \frac{M h}{\sqrt{M^2 - 1}} \quad (4)$$  

#### Step 4: Determine emission and arrival times
- Let $t_e$ be the time when the shock wave is emitted (before $t=0$).  
- At $t_e$, the aircraft is at $(-d, h)$.  
- The aircraft reaches $(0, h)$ at $t = 0$. The time to travel distance $d$ at speed $v = Mc$ is:  
$$\Delta t_{\text{aircraft}} = \frac{d}{Mc} = -\kern-1pt t_e \quad (\text{since } t_e < 0)$$  
Thus:  
$$t_e = -\frac{d}{Mc} \quad (5)$$  

- The shock wave travels distance $s$ at speed $c$. The arrival time $t_a$ is:  
$$t_a = t_e + \frac{s}{c} \quad (6)$$  

#### Step 5: Compute the time delay $\Delta t$
The delay is the difference between the arrival time $t_a$ and the overhead time ($t=0$):  
$$\Delta t = t_a - 0 = t_e + \frac{s}{c}$$  
Substitute (5):  
$$\Delta t = -\frac{d}{Mc} + \frac{s}{c} = \frac{1}{c} \left( s - \frac{d}{M} \right) \quad (7)$$  

Substitute (3) and (4) into (7):  
$$\Delta t = \frac{1}{c} \left( \frac{M h}{\sqrt{M^2 - 1}} - \frac{1}{M} \cdot \frac{h}{\sqrt{M^2 - 1}} \right) = \frac{h}{c \sqrt{M^2 - 1}} \left( M - \frac{1}{M} \right)$$  
Simplify the term in parentheses:  
$$M - \frac{1}{M} = \frac{M^2 - 1}{M}$$  
Thus:  
$$\Delta t = \frac{h}{c \sqrt{M^2 - 1}} \cdot \frac{M^2 - 1}{M} = \frac{h}{c} \cdot \frac{\sqrt{M^2 - 1}}{M}$$  
(The cancellation uses $M^2 - 1 = (\sqrt{M^2 - 1})^2$.)

#### Final expression:  
$$\Delta t = \frac{h \sqrt{M^2 - 1}}{c M}$$

## Answer
$$\boxed{\frac{h \sqrt{M^{2} - 1}}{c M}}$$

------
# surface tension and capillary action

## Problem 0
##### Background
Surface tension is a property of liquids that causes their surfaces to behave like elastic membranes. In soap bubbles, surface tension plays a crucial role in maintaining the spherical shape and creating an internal pressure greater than the external atmospheric pressure. A soap bubble differs from a simple liquid droplet because it has two surfaces (an inner and an outer air-liquid interface) connected by a thin film of soap solution. The excess pressure inside a bubble counteracts the contracting force of surface tension.

##### Knowledge Points Tested
1. Fundamental principles of surface tension
2. Force balance in fluid systems
3. Pressure difference across curved interfaces
4. Mathematical modeling of physical systems

##### Intradisciplinary Connections
This problem connects to fluid statics (pressure relationships), molecular physics (intermolecular forces causing surface tension), and geometry (spherical systems).

##### Interdisciplinary Connections
- **Biology/Medicine**: Similar pressure dynamics exist in pulmonary alveoli.
- **Materials Science**: Principles apply to foam stability and emulsification.
- **Meteorology**: Relates to droplet formation in clouds.

##### Real-World Applications
1. Industrial foam production (firefighting, insulation)
2. Medical technologies (contrast-enhanced ultrasound)
3. Microfluidics (lab-on-a-chip bubble valves)
4. Detergent formulation (surface-active agents)

##### Problem Statement
A spherical soap bubble with radius $R$ floats in air. The soap solution has surface tension $\sigma$. Derive the expression for excess pressure $\Delta P$ inside the bubble by analyzing force equilibrium on a hemispherical section. Consider both surfaces of the soap film and the direction of forces. Express $\Delta P$ exclusively in terms of $\sigma$ and $R$.  
Provide your answer as a simplified analytic expression.

## Solution
**Step 1: Force balance setup**  
Consider a soap bubble cut along its equatorial plane into two hemispheres. Analyze forces on one hemisphere:  
- Excess pressure $\Delta P$ acts perpendicular to the circular cross-section (area $\pi R^2$), pushing the hemisphere outward.  
- Surface tension acts tangentially along the circumference ($2\pi R$) of the cut. Since the bubble has two surfaces (inner and outer), both contribute to the total contracting force.

**Step 2: Calculate pressure force**  
The force due to excess pressure is:  
$$ F_{\text{pressure}} = \Delta P \times \text{cross-sectional area} = \Delta P \cdot \pi R^2 $$  
This force acts outward perpendicular to the equatorial plane.

**Step 3: Calculate surface tension force**  
Surface tension $\sigma$ acts along the circumference. For a given surface:  
- Force = $\sigma \times \text{circumference length} = \sigma \cdot 2\pi R$  
Since there are two surfaces (inner and outer) and both pull inward:  
$$ F_{\text{tension}} = 2 \times (\sigma \cdot 2\pi R) = 4\pi \sigma R $$  
The factor of 2 accounts for the double surface of the soap film.

**Step 4: Apply equilibrium condition**  
For the hemisphere to remain stationary:  
$$ \text{Outward force} = \text{Inward force} $$  
$$ \Delta P \cdot \pi R^2 = 4\pi \sigma R $$  

**Step 5: Solve for $\Delta P$**  
$$ \Delta P = \frac{4\pi \sigma R}{\pi R^2} = \frac{4\sigma}{R} $$  
The expression simplifies to $\Delta P = 4\sigma / R$.

**Key principles used**:  
- Surface tension force proportional to contact length  
- Pressure force proportional to area  
- Force equilibrium in static systems  
- Double-surface contribution in soap films

## Answer
$$\boxed{\dfrac{4\sigma}{R}}$$

------
## Problem 1
##### Background  
Capillary action is a phenomenon where liquids spontaneously rise or fall in narrow tubes due to intermolecular forces between the liquid and tube walls. This effect is crucial in natural systems like plant xylem and technological applications such as microfluidic devices. When a capillary tube is inclined, the height of liquid rise along the tube depends on the angle of inclination, requiring a balance between surface tension and gravitational forces.

##### Knowledge Points Tested  
1. **Surface tension and capillary action**: Understanding how surface tension drives liquid rise.  
2. **Force balance**: Resolving forces in an inclined system using trigonometry.  
3. **Young-Laplace equation**: Relating pressure difference across a curved interface to surface tension and curvature.  
4. **Hydrostatic pressure**: Calculating pressure due to a liquid column.  

##### Intradisciplinary Connections  
- **Fluid mechanics**: Applies the Young-Laplace equation for pressure difference and hydrostatic pressure.  
- **Statics**: Uses force equilibrium to balance surface tension and gravitational forces.  

##### Interdisciplinary Connections  
- **Materials science**: Contact angle dependence reflects wetting properties at solid-liquid interfaces.  
- **Biology**: Models capillary rise in inclined plant vessels for nutrient transport.  

##### Real-World Applications  
- **Lab-on-a-chip devices**: Precise control of fluid flow in inclined microchannels.  
- **Soil science**: Predicting water movement in sloped porous media.  

##### Problem Statement  
A capillary tube of inner radius $ r $ is dipped into a liquid reservoir at an angle $ \theta $ (measured from the horizontal). The liquid has density $ \rho $, surface tension $ \sigma $, and contact angle $ \phi $ with the tube material. Derive an expression for the height $ h $ (the distance along the tube from the reservoir level to the meniscus) to which the liquid rises.  

Express $ h $ as an analytic expression in terms of $ r $, $ \theta $, $ \phi $, $ \sigma $, $ \rho $, and $ g $ (acceleration due to gravity).  

**Answer format requirements**:  
- Use standard mathematical notation: $ \sin $, $ \cos $, $ \exp $, etc.  
- Angles are in radians; omit degree symbols.  
- Simplify the expression.  
- Provide only the analytic expression in the final answer box.

## Solution
**Step 1: Pressure difference due to curved meniscus**  
The Young-Laplace equation gives the pressure difference $ \Delta P $ across a spherical meniscus:  

$$ \Delta P = \frac{2\sigma}{R} $$
  
where $ R $ is the radius of curvature. For a contact angle $ \phi $ and tube radius $ r $, the geometry yields:  

$$ R = \frac{r}{\cos \phi} $$
  
Substituting $ R $:  

$$ \Delta P = \frac{2\sigma \cos \phi}{r} $$
  

**Step 2: Hydrostatic pressure balance**  
The pressure difference $ \Delta P $ is balanced by the hydrostatic pressure from the vertical component of the liquid column. The vertical height is $ h \sin \theta $ (since $ \theta $ is the angle from the horizontal), so:  

$$ \Delta P = \rho g (h \sin \theta) $$
  

**Step 3: Equate pressures and solve for $ h $**  
Set the expressions for $ \Delta P $ equal:  

$$ \frac{2\sigma \cos \phi}{r} = \rho g h \sin \theta $$
  
Solve for $ h $:  

$$ h = \frac{2\sigma \cos \phi}{\rho g r \sin \theta} $$
  
This expression describes the rise along the tube, accounting for inclination via $ \sin \theta $.  

**Verification for vertical case**:  
When $ \theta = 90^\circ $, $ \sin \theta = 1 $, recovering Jurin’s law: $ h = \frac{2\sigma \cos \phi}{\rho g r} $.

## Answer
\[ \boxed{\dfrac{2\sigma \cos\phi}{\rho g r \sin\theta}} \]

------
## Problem 2
##### Background
Surface tension is a property of liquids that causes their surfaces to behave like elastic membranes. This phenomenon is crucial in capillary action, droplet formation, and various industrial processes like inkjet printing. When a liquid droplet breaks into smaller droplets, work must be done against surface tension to create additional surface area. Mercury, with its high surface tension, provides an excellent model system for studying these effects.

##### Knowledge Points Tested
- Surface energy and its relationship to surface tension
- Conservation of volume during droplet fragmentation
- Geometric properties of spheres
- Work-energy principle in fluid interfaces

##### Intradisciplinary Connections
Connects to fluid statics (Laplace pressure), thermodynamics (minimum energy principles), and intermolecular forces (origin of surface tension).

##### Interdisciplinary Connections
Relevant to materials science (nanoparticle synthesis), biomedical engineering (drug delivery microdroplets), and aerospace engineering (propellant management in microgravity).

##### Real-World Applications
- Precision medicine: Calculating energy requirements for breaking therapeutic droplets in targeted drug delivery systems.
- Metallurgy: Determining energy costs in mercury-catalyzed reactions.
- Environmental science: Modeling oil spill dispersion dynamics.

##### Problem Statement
Consider a spherical mercury droplet of radius $R$ with surface tension $\sigma$. It undergoes a process where it breaks into $n$ identical smaller spherical droplets. Derive an expression for the work $W$ required to achieve this transformation. Use your expression to calculate $W$ when $R = 3  \text{mm}$, $\sigma = 0.465  \text{N/m}$, and $n = 8$.  

Provide only the numerical value of your final answer in joules, rounded to four significant figures.

## Solution
The work done against surface tension equals the increase in surface energy. The initial surface area $A_i$ of the droplet is:  
$$ A_i = 4\pi R^2 $$  

After breaking into $n$ identical droplets, each has radius $r$. By conservation of volume:  
$$ \frac{4}{3}\pi R^3 = n \cdot \frac{4}{3}\pi r^3 $$  
Solving for $r$:  
$$ R^3 = n r^3 \implies r = R \cdot n^{-1/3} $$  

The final surface area $A_f$ is:  
$$ A_f = n \cdot 4\pi r^2 = 4\pi n (R^2 n^{-2/3}) = 4\pi R^2 n^{1/3} $$  

The change in surface area $\Delta A$ is:  
$$ \Delta A = A_f - A_i = 4\pi R^2 n^{1/3} - 4\pi R^2 = 4\pi R^2 (n^{1/3} - 1) $$  

The work done $W$ is:  
$$ W = \sigma \Delta A = 4\pi \sigma R^2 (n^{1/3} - 1) $$  

For the given values:  
- $R = 3  \text{mm} = 0.003  \text{m}$  
- $\sigma = 0.465  \text{N/m}$  
- $n = 8$  

First, compute $n^{1/3}$:  
$$ 8^{1/3} = 2 $$  

Substitute into the expression:  
$$ W = 4\pi (0.465) (0.003)^2 (2 - 1) $$  
$$ W = 4\pi (0.465) (9 \times 10^{-6}) (1) $$  
$$ W = 4\pi (0.465) (9 \times 10^{-6}) $$  
$$ W = (4)(9 \times 10^{-6})(0.465)\pi $$  
$$ W = (3.6 \times 10^{-5})(0.465)\pi $$  
$$ W = 1.674 \times 10^{-5} \pi $$  

Using $\pi \approx 3.1416$:  
$$ W \approx 1.674 \times 10^{-5} \times 3.1416 \approx 5.259 \times 10^{-5} $$  

Rounded to four significant figures:  
$$ W = 5.259 \times 10^{-5}  \text{J} $$

## Answer
$$\boxed{5.259 \times 10^{-5}}$$

------
## Problem 3
##### Background
Capillary action is a fascinating phenomenon where liquids spontaneously rise in narrow spaces, such as thin tubes or between closely spaced surfaces, due to intermolecular forces. This effect is governed by surface tension and the liquid's contact angle with the solid surface. While the capillary rise in cylindrical tubes is well-known, the behavior between parallel plates is equally important in applications like microfluidics, soil moisture analysis, and the design of lab-on-a-chip devices.

##### Knowledge Points Tested
1. Fundamental principles of surface tension and capillary action
2. Force balance analysis for capillary rise in non-cylindrical geometries
3. Mathematical derivation of the capillary height equation for parallel plates
4. Application of contact angle in Young's equation

##### Intradisciplinary Connections
- Fluid statics: Pressure differences and hydrostatic equilibrium
- Wetting phenomena: Relationship between contact angle, adhesive, and cohesive forces
- Interfacial thermodynamics: Surface energy minimization principles

##### Interdisciplinary Connections
- Materials science: Design of hydrophilic/hydrophobic surfaces
- Biomedical engineering: Microfluidic drug delivery systems
- Environmental science: Water movement in soil fissures

##### Real-World Applications
- Inkjet printing technology: Precise control of ink flow between printhead components
- Medical diagnostics: Capillary-driven blood plasma separation in portable test devices
- Geotechnical engineering: Predicting water seepage in rock fractures

##### Problem Statement
Two infinitely long parallel glass plates are vertically oriented and partially immersed in a reservoir of water. The plates are separated by a distance $d$. The water has density $\rho$, surface tension $\gamma$, and forms a contact angle $\theta$ with the glass. Derive an expression for the height $h$ to which water rises between the plates due to capillary action. Assume atmospheric pressure is constant above the reservoir and ignore edge effects. Express $h$ symbolically using only the given parameters: $d$, $\rho$, $\gamma$, $\theta$, and gravitational acceleration $g$.  
*Instruction for final answer*:  
- Use standard mathematical notation with explicit operators (e.g., $\cos\theta$, not $\cos{\theta}$).  
- Express trigonometric functions with angles in degrees but omit the degree symbol.  
- Use $\exp(x)$ for exponentials and $\ln$ for natural logarithms.  
- Provide the expression in simplest algebraic form.

## Solution
To derive the capillary rise height $h$ between two parallel plates, we analyze the forces acting on the water column. The key principles are:  
1. **Capillary pressure difference**: Results from surface tension and curvature at the air-water interface.  
2. **Hydrostatic equilibrium**: The upward capillary force balances the weight of the raised water column.  

**Step 1: Determine the meniscus shape and pressure difference**  
The air-water interface between parallel plates forms a cylindrical meniscus (radius $R$ in the horizontal plane). The pressure difference $\Delta P$ across this curved surface is given by the Young-Laplace equation for a cylindrical surface:  
$$ \Delta P = \frac{\gamma}{R} $$  
where $R$ is the radius of curvature.  

**Step 2: Relate radius of curvature to plate separation and contact angle**  
For parallel plates separated by distance $d$, the radius of curvature $R$ relates to the contact angle $\theta$ and plate separation. From the geometry of the meniscus:  
$$ R = \frac{d}{2 \cos\theta} $$  
This follows because the contact angle $\theta$ is measured from the vertical plate surface to the tangent of the meniscus, and the meniscus spans half the plate separation ($d/2$) in the horizontal direction. Substituting into the pressure difference equation:  
$$ \Delta P = \frac{\gamma}{R} = \frac{\gamma}{\left( \frac{d}{2 \cos\theta} \right)} = \frac{2\gamma \cos\theta}{d} $$  

**Step 3: Apply hydrostatic equilibrium**  
The capillary pressure difference $\Delta P$ supports the hydrostatic pressure of the water column of height $h$:  
$$ \Delta P = \rho g h $$  
Equating the expressions from Steps 2 and 3:  
$$ \rho g h = \frac{2\gamma \cos\theta}{d} $$  

**Step 4: Solve for capillary rise height $h$**  
Rearranging the equation:  
$$ h = \frac{2\gamma \cos\theta}{\rho g d} $$  
This is the symbolic expression for the capillary rise height between two parallel plates.

## Answer
$$\boxed{\dfrac{2\gamma\cos\theta}{\rho g d}}$$

------
# transformer turn ratios

## Problem 0
##### Background
Transformers are essential devices in electrical engineering that transfer electrical energy between circuits via electromagnetic induction. The key principle is Faraday's law of induction, which states that the induced electromotive force (EMF) in a coil is proportional to the rate of change of magnetic flux linkage. In a transformer, an alternating current in the primary winding creates a time-varying magnetic flux in the core, inducing a voltage in the secondary winding. The turn ratio (primary turns to secondary turns) determines the voltage transformation.

##### Knowledge Points Tested
1. Application of Faraday's law of induction to derive transformer voltage relationships.
2. Relationship between RMS voltage and peak voltage in sinusoidal AC circuits.
3. Dependence of induced voltage on the number of coil turns.

##### Intradisciplinary Connections
This problem connects electromagnetic theory (Faraday's law, magnetic flux) with AC circuit analysis (RMS voltage, sinusoidal waveforms) and transformer operation.

##### Interdisciplinary Connections
Transformer principles are foundational in power engineering (electricity distribution), electronics (power supplies), and physics (electromagnetic induction).

##### Real-World Applications
Step-down transformers reduce high-voltage AC from power grids (e.g., 220 V RMS) to safer levels for household electronics (e.g., phone chargers, LED lighting), minimizing energy loss during transmission.

##### Problem Statement
A transformer with an iron core operates at a frequency $f$. The magnetic flux through the core varies sinusoidally as $\Phi(t) = \Phi_{\text{max}} \cos(2\pi f t)$, where $\Phi_{\text{max}}$ is the peak flux. The primary winding has $N_p = 400$ turns and is connected to an AC source with an RMS voltage $V_p = 220$ V. The secondary winding has $N_s = 100$ turns.  

Starting from Faraday's law, derive a general expression for the RMS secondary voltage $V_s$ in terms of $N_p$, $N_s$, and $V_p$. Then, compute the numerical value of $V_s$ in volts.  

**Final Answer Requirements**:  
- Derive the expression symbolically before substituting numerical values.  
- Express the final numerical answer as an integer.  
- Box only the numerical result.

## Solution
**Step 1: Apply Faraday's law to the primary winding**  
Faraday's law states that the induced EMF in a coil is $\mathcal{E} = -N \frac{d\Phi}{dt}$. For the primary winding:  

$$
\mathcal{E}_p = -N_p \frac{d}{dt} \left[ \Phi_{\text{max}} \cos(2\pi f t) \right] = N_p \Phi_{\text{max}} \cdot 2\pi f \sin(2\pi f t).
$$
  
The amplitude of $\mathcal{E}_p$ is $N_p \Phi_{\text{max}} \cdot 2\pi f$. The RMS voltage $V_p$ relates to the amplitude by:  

$$
V_p = \frac{\text{Amplitude of } \mathcal{E}_p}{\sqrt{2}} = \frac{N_p \Phi_{\text{max}} \cdot 2\pi f}{\sqrt{2}}.
$$
  
Rearranging for $\Phi_{\text{max}}$:  

$$
\Phi_{\text{max}} = \frac{V_p \sqrt{2}}{2\pi f N_p}. \quad (1)
$$


**Step 2: Apply Faraday's law to the secondary winding**  
For the secondary winding:  

$$
\mathcal{E}_s = -N_s \frac{d\Phi}{dt} = N_s \Phi_{\text{max}} \cdot 2\pi f \sin(2\pi f t).
$$
  
The RMS secondary voltage $V_s$ is:  

$$
V_s = \frac{\text{Amplitude of } \mathcal{E}_s}{\sqrt{2}} = \frac{N_s \Phi_{\text{max}} \cdot 2\pi f}{\sqrt{2}}. \quad (2)
$$


**Step 3: Derive the relationship between $V_s$ and $V_p$**  
Substitute $\Phi_{\text{max}}$ from equation (1) into equation (2):  

$$
V_s = \frac{N_s \cdot 2\pi f}{\sqrt{2}} \cdot \left( \frac{V_p \sqrt{2}}{2\pi f N_p} \right) = \frac{N_s}{N_p} V_p.
$$
  
The frequency $f$ and peak flux $\Phi_{\text{max}}$ cancel out, yielding:  

$$
V_s = V_p \cdot \frac{N_s}{N_p}.
$$


**Step 4: Compute the numerical value**  
Substitute $V_p = 220$ V, $N_p = 400$, and $N_s = 100$:  

$$
V_s = 220 \cdot \frac{100}{400} = 220 \cdot \frac{1}{4} = 55 \text{ V}.
$$
  
The RMS secondary voltage is 55 V.

## Answer
$$\boxed{55}$$

------
## Problem 1
##### Background
Transformers are essential devices in electrical engineering that step up or step down alternating voltages and currents using electromagnetic induction. They consist of two coils (primary and secondary) wound around a common magnetic core. The turn ratio, defined as the ratio of the number of turns in the primary coil to the secondary coil, determines the voltage and current transformation. In this problem, you will derive the secondary current by modeling the relationship between wire length and turn ratio in a toroidal transformer.

##### Knowledge Points Tested
1. Derivation of the number of turns from wire length and core geometry.
2. Application of the ideal transformer equations: voltage ratio $\frac{V_p}{V_s} = \frac{N_p}{N_s}$ and power conservation $V_p I_p = V_s I_s$.
3. Current transformation $\frac{I_s}{I_p} = \frac{N_p}{N_s}$ in ideal transformers (no losses, perfect coupling).

##### Intradisciplinary Connections
This problem connects turn ratio concepts to Faraday's law of induction (voltage induction) and Ampère's law (magnetic flux linkage). It also reinforces geometric modeling of coils and proportional reasoning.

##### Interdisciplinary Connections
- **Geometry**: Calculating the number of turns using circumference and wire length.
- **Materials Science**: Ideal core assumptions (infinite permeability, zero hysteresis loss) simplify magnetic behavior.
- **Energy Conservation**: Power balance between input and output circuits.

##### Real-World Applications
Toroidal transformers are used in audio equipment, power supplies, and medical devices due to their compact size and low electromagnetic interference. Engineers select wire lengths to achieve specific turn ratios for voltage/current transformation in these applications.

##### Problem Statement
A toroidal transformer has an iron core with mean radius $r$. The primary coil is wound uniformly with a copper wire of total length $L_p$, and the secondary coil is wound uniformly with a copper wire of total length $L_s$. The windings are tight and cover the entire core. Assume ideal conditions (no energy losses, perfect magnetic coupling, and negligible wire resistance). When the primary coil carries an alternating current of $I_p$ (root mean square, rms), derive an expression for the secondary current $I_s$ (rms) in terms of $I_p$, $L_p$, and $L_s$.

## Solution
### Step 1: Model the number of turns  
The core is toroidal with mean radius $r$, so the average circumference of each turn is $2\pi r$. For a tightly wound uniform coil:  
- Number of turns in primary coil: $N_p = \frac{L_p}{2\pi r}$  
- Number of turns in secondary coil: $N_s = \frac{L_s}{2\pi r}$  

### Step 2: Derive the turn ratio  
The turn ratio is the ratio of primary to secondary turns:  
$$ \frac{N_p}{N_s} = \frac{L_p / (2\pi r)}{L_s / (2\pi r)} = \frac{L_p}{L_s} $$  
This simplifies to $\frac{N_p}{N_s} = \frac{L_p}{L_s}$.  

### Step 3: Apply ideal transformer equations  
For an ideal transformer:  
1. **Power conservation**: Input power equals output power:  
   $$ V_p I_p = V_s I_s $$  
   where $V_p$ and $V_s$ are primary and secondary voltages (rms).  
2. **Voltage ratio**: Proportional to turn ratio:  
   $$ \frac{V_p}{V_s} = \frac{N_p}{N_s} $$  

Substitute the voltage ratio into the power equation:  
$$ \left( \frac{N_p}{N_s} V_s \right) I_p = V_s I_s $$  
Divide both sides by $V_s$ (assuming $V_s \neq 0$):  
$$ \frac{N_p}{N_s} I_p = I_s $$  

### Step 4: Substitute the turn ratio  
From Step 2, $\frac{N_p}{N_s} = \frac{L_p}{L_s}$. Thus:  
$$ I_s = I_p \cdot \frac{L_p}{L_s} $$  
This is the expression for the secondary current.

## Answer
$$\boxed{I_p \cdot \frac{L_p}{L_s}}$$

------
## Problem 2
##### Background
Transformers are essential components in electrical power systems, enabling efficient transmission and distribution of electricity by stepping voltages up or down. They operate on the principle of electromagnetic induction, where a changing magnetic field in the primary coil induces a voltage in the secondary coil. The turn ratio between the coils determines the voltage transformation.

##### Knowledge Points Tested
1. Faraday’s law of electromagnetic induction.
2. Relationship between voltage and turns ratio in an ideal transformer.
3. Algebraic manipulation of ratios.

##### Intradisciplinary Connections
This problem connects to electromagnetic induction principles, alternating current (AC) circuits, and energy conservation in transformers.

##### Interdisciplinary Connections
Physics principles applied in electrical engineering for designing power grids, electronics (e.g., power adapters), and renewable energy systems (e.g., wind turbine voltage step-up).

##### Real-World Applications
- Power transmission: Step-up transformers increase voltage to reduce energy loss during long-distance transmission.
- Consumer electronics: Step-down transformers in chargers convert 120V/240V AC to safer voltages (e.g., 5V for USB devices).
- Industrial machinery: Transformers isolate control circuits from high-voltage lines.

##### Problem Statement
An ideal transformer is designed to step up voltage for a solar power grid. The secondary coil has $N_s$ turns and outputs an RMS voltage of $V_s$. The primary coil is connected to an RMS voltage source $V_p$. Due to a labeling error, only the secondary coil's turn count ($N_s = 800$) and the output voltage ($V_s = 480  \text{V}$) are legible on the schematic. The input voltage is verified as $V_p = 120  \text{V}$.  

Using Faraday’s law of induction, derive the general relationship between the turn ratio and voltages in an ideal transformer. Hence, determine the number of turns $N_p$ in the primary coil.  

Express $N_p$ as an exact integer.

## Solution
### Step 1: Apply Faraday’s Law to the Primary Coil  
Faraday’s law states that the induced electromotive force (EMF) in a coil is proportional to the rate of change of magnetic flux linkage. For the primary coil with $N_p$ turns:  

$$
\mathcal{E}_p = -N_p \frac{d\phi_B}{dt}
$$
  
where $\phi_B$ is the magnetic flux through a single turn. In an ideal transformer, the primary coil’s applied voltage $V_p$ equals the magnitude of the induced EMF $\mathcal{E}_p$ (neglecting resistance and leakage flux). Thus:  

$$
V_p = \left| \mathcal{E}_p \right| = N_p \left| \frac{d\phi_B}{dt} \right| \quad (1)
$$
  

### Step 2: Apply Faraday’s Law to the Secondary Coil  
For the secondary coil with $N_s$ turns, the induced EMF is:  

$$
\mathcal{E}_s = -N_s \frac{d\phi_B}{dt}
$$
  
The output voltage $V_s$ equals the magnitude of $\mathcal{E}_s$:  

$$
V_s = \left| \mathcal{E}_s \right| = N_s \left| \frac{d\phi_B}{dt} \right| \quad (2)
$$
  

### Step 3: Derive the Turn Ratio Relationship  
Divide equation (2) by equation (1) to eliminate $\left| \frac{d\phi_B}{dt} \right|$:  

$$
\frac{V_s}{V_p} = \frac{N_s \left| \frac{d\phi_B}{dt} \right|}{N_p \left| \frac{d\phi_B}{dt} \right|} = \frac{N_s}{N_p}
$$
  
Rearranging gives the fundamental transformer equation:  

$$
\frac{V_s}{V_p} = \frac{N_s}{N_p} \quad (3)
$$
  

### Step 4: Solve for $N_p$  
Substitute the given values into equation (3):  

$$
\frac{480}{120} = \frac{800}{N_p}
$$
  
Simplify the voltage ratio:  

$$
4 = \frac{800}{N_p}
$$
  
Solve for $N_p$:  

$$
N_p = \frac{800}{4} = 200
$$
  

### Conclusion  
The primary coil has $200$ turns. This result follows directly from the proportional relationship between voltages and turns in an ideal transformer, derived from Faraday’s law.

## Answer
$$\boxed{200}$$

------
## Problem 3
##### Background
Transformers are essential devices in electrical engineering that transfer electrical energy between circuits through electromagnetic induction. They are commonly used to step up or step down voltages in power distribution systems. Real transformers experience energy losses due to factors like resistive heating in windings and magnetic hysteresis, resulting in efficiencies below 100%. Efficiency ($\eta$) is defined as the ratio of output power to input power, expressed as a percentage.

##### Knowledge Points Tested
1. Definition and calculation of transformer efficiency.
2. Relationship between primary and secondary power in non-ideal transformers.
3. Derivation of secondary current using power conservation principles.

##### Intradisciplinary Connections
This problem connects to electromagnetic induction, AC circuit theory, and electrical power calculations. It extends the ideal transformer model to account for real-world energy losses.

##### Interdisciplinary Connections
- **Physics**: Conservation of energy and power dissipation concepts.
- **Engineering**: Practical design considerations for electrical machines and power systems.

##### Real-World Applications
Transformers are critical in power grids (e.g., stepping down high-voltage transmission lines to household voltages) and consumer electronics (e.g., phone chargers). Understanding efficiency impacts energy conservation and thermal management in these systems.

##### Problem Statement
A step-down transformer operates with an efficiency of $\eta = 90\%$. The primary winding has a voltage of $V_p = 200  \text{V}$ and carries a current of $I_p = 5  \text{A}$. The secondary winding supplies a voltage of $V_s = 50  \text{V}$.  

Derive an expression for the secondary current $I_s$ in terms of $\eta$, $V_p$, $I_p$, and $V_s$. Then compute the numerical value of $I_s$.  

Express your final answer as a numerical value in amperes, rounded to three significant figures. Provide only the numerical value in your answer.

## Solution
The efficiency $\eta$ is defined as:  
$$  
\eta = \frac{P_{\text{out}}}{P_{\text{in}}}} \times 100\%  
$$  
where $P_{\text{in}}$ is the input power to the primary side and $P_{\text{out}}$ is the output power from the secondary side.  

The input power is:  
$$  
P_{\text{in}} = V_p I_p  
$$  
The output power is:  
$$  
P_{\text{out}} = V_s I_s  
$$  
Substitute these expressions into the efficiency equation:  
$$  
\eta = \frac{V_s I_s}{V_p I_p} \times 100\%  
$$  
Solve for $I_s$:  
1. Divide both sides by 100% to convert $\eta$ to a decimal fraction:  
$$  
\frac{\eta}{100} = \frac{V_s I_s}{V_p I_p}  
$$  
2. Rearrange to isolate $I_s$:  
$$  
I_s = \frac{\eta}{100} \cdot \frac{V_p I_p}{V_s}  
$$  
This is the general expression for $I_s$.  

Now substitute the given numerical values:  
- $\eta = 90$  
- $V_p = 200  \text{V}$  
- $I_p = 5  \text{A}$  
- $V_s = 50  \text{V}$  

$$  
I_s = \frac{90}{100} \cdot \frac{200 \times 5}{50}  
$$  
Simplify step by step:  
- $\frac{90}{100} = 0.90$  
- $200 \times 5 = 1000$  
- $\frac{1000}{50} = 20$  
- $0.90 \times 20 = 18.0$  

The secondary current is $18.0  \text{A}$, rounded to three significant figures.

## Answer
$$\boxed{18.0}$$

------
## Problem 4
##### Background
Transformers are devices that transfer electrical energy between circuits through electromagnetic induction. In an ideal transformer, the ratio of the secondary voltage to the primary voltage equals the ratio of the number of turns in the secondary coil to the primary coil. However, real transformers have internal resistances in the coils, which cause voltage drops and power losses. These losses mean the ideal transformer equation does not directly apply, and energy conservation must be used to model the system accurately.

##### Knowledge Points Tested
1. Ideal transformer voltage and current relationships: $ \frac{V_s}{V_p} = \frac{N_s}{N_p} $ and $ \frac{I_s}{I_p} = \frac{N_p}{N_s} $.
2. Ohm's law and power dissipation in resistors.
3. Conservation of energy: input power equals the sum of power dissipated in internal resistances and power delivered to the load.
4. Solving quadratic equations derived from physical principles.

##### Intradisciplinary Connections
This problem connects electromagnetic induction (transformer operation) with circuit analysis (resistive losses and voltage drops) and energy conservation principles.

##### Interdisciplinary Connections
The analysis of non-ideal transformers is crucial in electrical engineering for designing efficient power distribution systems and electronic devices.

##### Real-World Applications
Transformers are used in power adapters for laptops and phone chargers (step-down) and in electrical grids (step-up for transmission, step-down for consumption). Internal resistances model copper losses in real transformers, affecting efficiency.

##### Problem Statement
A non-ideal transformer has a primary coil with 300 turns and an internal resistance of 10 Ω. The secondary coil has an internal resistance of 0.5 Ω and is connected to a load resistor of 8 Ω. The primary coil is connected to an AC source of 120 V (rms). The voltage across the load resistor (output voltage) is exactly one-fourth of the source voltage (input voltage).  

Using the principle of conservation of energy (i.e., the power input from the source equals the total power dissipated in the internal resistances plus the power delivered to the load), determine the number of turns in the secondary coil.  

Express your answer as an exact expression. Do not evaluate numerically or use decimal approximations.

## Solution
We denote:
- $ N_p = 300 $ (turns in primary coil),
- $ R_p = 10 \, \Omega $ (primary internal resistance),
- $ R_s = 0.5 \, \Omega $ (secondary internal resistance),
- $ R_L = 8 \, \Omega $ (load resistance),
- $ V_p = 120 \, \text{V} $ (source voltage, rms),
- $ V_L = \frac{V_p}{4} = 30 \, \text{V} $ (output voltage across load, given).

The goal is to find $ N_s $, the number of turns in the secondary coil.

**Step 1: Express currents using load voltage and transformer relations.**  
The current in the secondary coil, $ I_s $, flows through the load resistor:  
$$ V_L = I_s R_L \implies I_s = \frac{V_L}{R_L} = \frac{30}{8} = \frac{15}{4} \, \text{A}. $$  

For an ideal transformer, the current ratio is:  
$$ \frac{I_s}{I_p} = \frac{N_p}{N_s} \implies I_p = I_s \frac{N_s}{N_p} = \frac{15}{4} \cdot \frac{N_s}{300} = \frac{N_s}{80} \, \text{A}. $$  

**Step 2: Apply conservation of energy.**  
Input power from source: $ P_{\text{in}} = V_p I_p $.  
Power dissipated in primary internal resistance: $ P_{R_p} = I_p^2 R_p $.  
Power dissipated in secondary internal resistance: $ P_{R_s} = I_s^2 R_s $.  
Power delivered to load: $ P_L = V_L I_s $.  

Conservation of energy:  
$$ V_p I_p = I_p^2 R_p + I_s^2 R_s + V_L I_s. $$  

**Step 3: Substitute known values and simplify.**  
Plug in $ V_p = 120 $, $ V_L = 30 $, $ I_s = \frac{15}{4} $, and $ I_p = \frac{N_s}{80} $:  
$$ 120 \cdot \frac{N_s}{80} = \left( \frac{N_s}{80} \right)^2 \cdot 10 + \left( \frac{15}{4} \right)^2 \cdot 0.5 + 30 \cdot \frac{15}{4}. $$  

Simplify each term:  
- Left side: $ \frac{120 N_s}{80} = \frac{3N_s}{2} $.  
- First term on right: $ \frac{10 N_s^2}{6400} = \frac{N_s^2}{640} $.  
- Second term on right: $ \left( \frac{225}{16} \right) \cdot 0.5 = \frac{225}{32} $.  
- Third term on right: $ 30 \cdot \frac{15}{4} = \frac{450}{4} = \frac{225}{2} $.  

Equation becomes:  
$$ \frac{3N_s}{2} = \frac{N_s^2}{640} + \frac{225}{32} + \frac{225}{2}. $$  

**Step 4: Combine constants and clear denominators.**  
Combine the constant terms:  
$$ \frac{225}{32} + \frac{225}{2} = \frac{225}{32} + \frac{225 \cdot 16}{32} = \frac{225 + 3600}{32} = \frac{3825}{32}. $$  

Multiply both sides by 640 to eliminate denominators (LCM of 2, 640, 32):  
$$ 640 \cdot \frac{3N_s}{2} = 640 \cdot \frac{N_s^2}{640} + 640 \cdot \frac{3825}{32} $$  
$$ 320 \cdot 3N_s = N_s^2 + 20 \cdot 3825 $$  
$$ 960 N_s = N_s^2 + 76,\!500. $$  

Rearrange into standard quadratic form:  
$$ N_s^2 - 960 N_s + 76,\!500 = 0. $$  

**Step 5: Solve the quadratic equation.**  
Use the quadratic formula:  
$$ N_s = \frac{960 \pm \sqrt{(-960)^2 - 4 \cdot 1 \cdot 76,\!500}}{2} = \frac{960 \pm \sqrt{921,\!600 - 306,\!000}}{2} = \frac{960 \pm \sqrt{615,\!600}}{2}. $$  

Simplify the discriminant:  
$$ \sqrt{615,\!600} = \sqrt{100 \cdot 6156} = 10 \sqrt{6156}. $$  
Factor $ 6156 $: $ 6156 = 4 \cdot 1539 = 4 \cdot 9 \cdot 171 = 4 \cdot 9 \cdot 9 \cdot 19 = 2^2 \cdot 3^4 \cdot 19 $, so  
$$ \sqrt{6156} = \sqrt{2^2 \cdot (3^2)^2 \cdot 19} = 2 \cdot 3^2 \sqrt{19} = 18 \sqrt{19}. $$  
Thus,  
$$ \sqrt{615,\!600} = 10 \cdot 18 \sqrt{19} = 180 \sqrt{19}. $$  

Solutions:  
$$ N_s = \frac{960 \pm 180 \sqrt{19}}{2} = 480 \pm 90 \sqrt{19}. $$  

**Step 6: Select the physically meaningful solution.**  
Since the transformer is step-down ($ V_L < V_p $), $ N_s < N_p = 300 $.  
- $ 90 \sqrt{19} \approx 90 \cdot 4.3589 = 392.301 $.  
- $ 480 + 392.301 = 872.301 > 300 $ (invalid, exceeds primary turns).  
- $ 480 - 392.301 = 87.699 \approx 88 $ (valid, less than 300).  

Thus, $ N_s = 480 - 90 \sqrt{19} $.

## Answer
$$\boxed{480 - 90\sqrt{19}}$$

------
## Problem 5
##### Background
Transformers are crucial components in electrical power distribution and electronic devices, enabling efficient voltage conversion through electromagnetic induction. An ideal transformer, with no energy losses, obeys specific relationships between the number of turns in its primary and secondary windings, voltages, and currents. This problem explores how the turn ratio affects current flow in the context of a practical energy delivery system.

##### Knowledge Points Tested
- Ideal transformer principles: voltage and current relationships based on turn ratios.
- Power conservation in transformers (input power equals output power).
- Application of symbolic derivation to real-world electrical systems.

##### Intradisciplinary Connections
- Connects to concepts in electromagnetism (Faraday's law of induction) and AC circuit analysis.
- Reinforces understanding of energy transfer and impedance matching in electrical engineering.

##### Interdisciplinary Connections
- Physics: Conservation of energy and electromagnetic theory.
- Engineering: Design of electrical grids, power supplies, and electronic devices.
- Environmental science: Efficient energy distribution reduces waste and supports sustainable practices.

##### Real-World Applications
- Power adapters for laptops/phones use step-down transformers (e.g., 120 V AC to 12 V DC) with specific turn ratios to safely deliver current.
- Electric grids employ transformers to minimize current (and resistive losses) during long-distance transmission by stepping up voltage.

##### Problem Statement
An ideal transformer has a primary-to-secondary turn ratio of $a:1$, meaning $\frac{N_p}{N_s} = a$, where $N_p$ and $N_s$ are the number of turns in the primary and secondary windings, respectively. The secondary winding delivers a current $I_s$ to a resistive load.  
Using the principles of ideal transformers and power conservation, derive an expression for the primary current $I_p$ in terms of $a$ and $I_s$.

## Solution
### Step 1: State the ideal transformer voltage relationship  
For an ideal transformer, the ratio of primary voltage ($V_p$) to secondary voltage ($V_s$) equals the turn ratio:  
$$ \frac{V_p}{V_s} = \frac{N_p}{N_s} = a \quad \Rightarrow \quad V_p = a V_s \tag{1} $$

### Step 2: Apply power conservation  
An ideal transformer has no energy losses, so input power equals output power:  
$$ V_p I_p = V_s I_s \tag{2} $$  
where $I_p$ is the primary current and $I_s$ is the secondary current.

### Step 3: Substitute the voltage relationship into the power equation  
Substitute $V_p = a V_s$ from equation (1) into equation (2):  
$$ (a V_s) I_p = V_s I_s \tag{3} $$

### Step 4: Solve for the primary current $I_p$  
Assuming $V_s \neq 0$ (valid for a loaded transformer), divide both sides of equation (3) by $V_s$:  
$$ a I_p = I_s \tag{4} $$  
Rearrange to isolate $I_p$:  
$$ I_p = \frac{I_s}{a} \tag{5} $$  

### Conclusion  
The primary current $I_p$ is inversely proportional to the turn ratio $a$, given the secondary current $I_s$. This reflects how a step-down transformer ($a > 1$) reduces voltage but increases current in the secondary, while the primary current is smaller than the secondary current by the factor $a$.

## Answer
$$\boxed{\dfrac{I_s}{a}}$$

------
## Problem 6
##### Background
Transformers operate on the principle of electromagnetic induction, where a changing magnetic field in a primary coil induces a voltage in a secondary coil. The turn ratio between coils determines the voltage transformation. This problem explores the fundamental derivation of the turn ratio relationship using Faraday's law and applies it to a real-world step-down transformer used in power adapters for electronic devices.

##### Knowledge Points Tested
1. Faraday's law of electromagnetic induction
2. Relationship between induced voltage and number of coil turns
3. Sinusoidal flux variation in transformer cores
4. Root-mean-square (rms) voltage calculations for AC systems

##### Intradisciplinary Connections
Connects to AC circuit analysis, magnetic flux linkage, and power transfer efficiency in electrical systems. Extends to transformer efficiency calculations and inductive reactance.

##### Interdisciplinary Connections
Physics: Electromagnetic field theory  
Engineering: Power distribution system design  
Materials Science: Core material selection to minimize hysteresis losses

##### Real-World Applications
Step-down transformers are critical in:  
- Power adapters for laptops and smartphones (converting 240V mains to 5-12V)  
- Voltage reduction for industrial control circuits  
- Isolation transformers for safety in medical equipment

##### Problem Statement
An ideal transformer core experiences sinusoidal magnetic flux $\phi(t) = \phi_0 \sin(2\pi ft)$, where $\phi_0$ is the peak flux, $f$ is the AC frequency, and $t$ is time. The primary coil has $N_p$ turns, while the secondary has $N_s = 60$ turns. The primary is connected to a 240 V (rms) AC source, and the secondary outputs 12 V (rms).

a) Apply Faraday's law to derive the instantaneous induced EMF $e_p(t)$ in the primary coil.  
b) Find the amplitude $E_p$ of $e_p(t)$.  
c) Using the relationship $V_{rms} = E/\sqrt{2}$ for sinusoidal voltages, express $V_{p,rms}$ in terms of $f$, $N_p$, and $\phi_0$.  
d) Repeat steps (a)-(c) for the secondary coil to obtain $V_{s,rms}$.  
e) Derive the turn ratio relationship $\frac{N_p}{N_s} = \frac{V_{p,rms}}{V_{s,rms}}$.  
f) Calculate $N_p$ for the given voltages and $N_s$.  

Express $N_p$ as an integer in your final answer.

## Solution
#### Part (a): Primary Coil Instantaneous EMF
Faraday's law states:  
$$e_p = -N_p \frac{d\phi}{dt}$$  
Given $\phi(t) = \phi_0 \sin(2\pi ft)$:  
$$\frac{d\phi}{dt} = \phi_0 \cdot 2\pi f \cos(2\pi ft)$$  
Substitute into Faraday's law:  
$$e_p(t) = -N_p \cdot 2\pi f \phi_0 \cos(2\pi ft)$$  

#### Part (b): Primary EMF Amplitude
The amplitude is the coefficient of the trigonometric function:  
$$E_p = 2\pi f N_p \phi_0$$  

#### Part (c): Primary RMS Voltage
For sinusoidal waveforms:  
$$V_{p,rms} = \frac{E_p}{\sqrt{2}} = \frac{2\pi f N_p \phi_0}{\sqrt{2}} = \sqrt{2} \pi f N_p \phi_0$$  

#### Part (d): Secondary Coil Analysis
Applying Faraday's law to the secondary coil:  
$$e_s(t) = -N_s \frac{d\phi}{dt} = -N_s \cdot 2\pi f \phi_0 \cos(2\pi ft)$$  
Amplitude:  
$$E_s = 2\pi f N_s \phi_0$$  
RMS voltage:  
$$V_{s,rms} = \frac{E_s}{\sqrt{2}} = \sqrt{2} \pi f N_s \phi_0$$  

#### Part (e): Turn Ratio Derivation
Divide the primary and secondary RMS voltages:  
$$\frac{V_{p,rms}}{V_{s,rms}} = \frac{\sqrt{2} \pi f N_p \phi_0}{\sqrt{2} \pi f N_s \phi_0} = \frac{N_p}{N_s}$$  
Thus:  
$$\frac{N_p}{N_s} = \frac{V_{p,rms}}{V_{s,rms}}$$  

#### Part (f): Numerical Calculation
Given:  
- $V_{p,rms} = 240\text{ V}$  
- $V_{s,rms} = 12\text{ V}$  
- $N_s = 60$  

Using the derived relationship:  
$$\frac{N_p}{60} = \frac{240}{12} = 20$$  
Solve for $N_p$:  
$$N_p = 20 \times 60 = 1200$$

## Answer
$$\boxed{1200}$$

------
# vector addition and subtraction methods

## Problem 0
##### Background
In aviation and navigation, understanding the combined effect of an aircraft's propulsion and wind conditions is crucial for determining actual displacement. This problem involves vector addition to compute the net displacement of an aircraft affected by crosswinds during a two-leg journey. The aircraft's velocity relative to the air and the wind velocity must be combined to determine the true path over the ground.

##### Knowledge Points Tested
- Vector decomposition into components
- Vector addition and subtraction
- Magnitude calculation using the Pythagorean theorem
- Application of relative velocity concepts

##### Intradisciplinary Connections
Connects to trigonometry (resolving vectors into components) and kinematics (displacement as a function of velocity and time).

##### Interdisciplinary Connections
Relevant to aeronautical engineering (aircraft navigation) and meteorology (wind impact on motion).

##### Real-World Applications
Pilots use these calculations to correct for wind drift during flight planning. Search-and-rescue operations rely on accurate displacement predictions to locate targets.

##### Problem Statement
An aircraft flies with constant airspeed $V_A$ relative to the air. During its journey, a steady wind blows with velocity $\vec{V_W}$ km/h due east. The flight consists of two legs:  
1. Leg 1: The aircraft heads $\theta$ degrees north of east for time $T_1$ hours.  
2. Leg 2: The aircraft heads $\phi$ degrees south of west for time $T_2$ hours.  

Determine the magnitude of the aircraft's total displacement from its starting point at the end of both legs. Use a coordinate system where east is the positive $x$-direction and north is the positive $y$-direction.  
Express your answer as an analytic expression in terms of $V_A$, $V_W$, $\theta$, $\phi$, $T_1$, and $T_2$.  
**Required notation:**  
- Use $\sin$, $\cos$ with angles in degrees (omit ° symbol).  
- Express powers using $a^{b}$.  
- Simplify all trigonometric expressions where possible.

## Solution
### Step 1: Resolve velocities into components  
**Aircraft velocity relative to air (Leg 1):**  
- $x$-component: $V_{A1x} = V_A \cos \theta$  
- $y$-component: $V_{A1y} = V_A \sin \theta$  

**Aircraft velocity relative to air (Leg 2):**  
- $x$-component: $V_{A2x} = V_A \cos (180^\circ + \phi) = V_A (-\cos \phi)$  
- $y$-component: $V_{A2y} = V_A \sin (180^\circ + \phi) = V_A (-\sin \phi)$  

**Wind velocity ($\vec{V_W}$):**  
- $x$-component: $V_{Wx} = V_W$  
- $y$-component: $V_{Wy} = 0$  

### Step 2: Compute ground velocity for each leg  
Ground velocity = aircraft velocity relative to air + wind velocity.  

**Leg 1 ground velocity:**  
- $x$-component: $V_{G1x} = V_{A1x} + V_{Wx} = V_A \cos \theta + V_W$  
- $y$-component: $V_{G1y} = V_{A1y} + V_{Wy} = V_A \sin \theta$  

**Leg 2 ground velocity:**  
- $x$-component: $V_{G2x} = V_{A2x} + V_{Wx} = -V_A \cos \phi + V_W$  
- $y$-component: $V_{G2y} = V_{A2y} + V_{Wy} = -V_A \sin \phi$  

### Step 3: Calculate displacement components  
Displacement = velocity × time.  

**Leg 1 displacement:**  
- $\Delta x_1 = V_{G1x} \cdot T_1 = (V_A \cos \theta + V_W) T_1$  
- $\Delta y_1 = V_{G1y} \cdot T_1 = (V_A \sin \theta) T_1$  

**Leg 2 displacement:**  
- $\Delta x_2 = V_{G2x} \cdot T_2 = (-V_A \cos \phi + V_W) T_2$  
- $\Delta y_2 = V_{G2y} \cdot T_2 = (-V_A \sin \phi) T_2$  

### Step 4: Total displacement components  
- Total $\Delta x = \Delta x_1 + \Delta x_2 = (V_A \cos \theta + V_W) T_1 + (-V_A \cos \phi + V_W) T_2$  
- Total $\Delta y = \Delta y_1 + \Delta y_2 = (V_A \sin \theta) T_1 + (-V_A \sin \phi) T_2$  

### Step 5: Magnitude of total displacement  
$$|\text{Displacement}| = \sqrt{ (\Delta x)^2 + (\Delta y)^2 }$$  
Substitute expressions:  
$$\Delta x = V_A T_1 \cos \theta - V_A T_2 \cos \phi + V_W (T_1 + T_2)$$  
$$\Delta y = V_A T_1 \sin \theta - V_A T_2 \sin \phi$$  
Thus,  
$$|\text{Displacement}| = \sqrt{ \left[ V_A (T_1 \cos \theta - T_2 \cos \phi) + V_W (T_1 + T_2) \right]^2 + \left[ V_A (T_1 \sin \theta - T_2 \sin \phi) \right]^2 }$$

## Answer
$$\boxed{\sqrt{ \left( V_A (T_1 \cos \theta - T_2 \cos \phi) + V_W (T_1 + T_2) \right)^{2} + \left( V_A (T_1 \sin \theta - T_2 \sin \phi) \right)^{2} }}$$

------
## Problem 1
#### Background
In aviation, an aircraft's navigation must account for both its intended airspeed and the wind's influence. The airspeed vector represents the aircraft's velocity relative to the air, while the wind vector indicates the air's motion relative to the ground. The resultant ground velocity is the vector sum of these two. This problem explores how to compute the magnitude of this resultant when the vectors are oriented at specific angles relative to a reference direction (e.g., due east).

#### Knowledge Points Tested
- Resolution of vectors into Cartesian components.
- Vector addition using component-wise summation.
- Magnitude calculation from orthogonal components.
- Trigonometric identities for simplifying expressions.

#### Intradisciplinary Connections
Connects to projectile motion (kinematics), force equilibrium (dynamics), and coordinate transformations (linear algebra).

#### Interdisciplinary Connections
- **Engineering**: Used in control systems for autonomous drones.
- **Meteorology**: Modeling wind effects on flight paths.
- **Game Development**: Simulating realistic movement in physics engines.

#### Real-World Applications
Pilots use this calculation to adjust headings for crosswinds during takeoff/landing. Sailors apply it to navigate currents, and it is critical in designing guidance systems for self-driving cars encountering lateral forces.

#### Problem Statement
An aircraft has an airspeed vector of magnitude $ A $ directed at an angle $ \alpha $ above the positive $ x $-axis (east). A wind blows with velocity of magnitude $ W $ at an angle $ \beta $ below the positive $ x $-axis. Derive the magnitude of the aircraft's resultant velocity relative to the ground. Express your answer symbolically in terms of $ A $, $ W $, $ \alpha $, and $ \beta $.  

**Answer Format Requirements**:  
- Use degrees for angles and omit the degree symbol (e.g., $\sin(30)$, not $\sin(30^\circ)$).  
- Employ standard notation: $\cos$, $\sin$, $\sqrt{}$.  
- The expression must be simplified and enclosed in $\boxed{}$.

## Solution
**Step 1: Resolve vectors into components**  
The airspeed vector $ \vec{A} $ has:  
- $ x $-component: $ A \cos \alpha $  
- $ y $-component: $ A \sin \alpha $  

The wind vector $ \vec{W} $ (below the $ x $-axis) has:  
- $ x $-component: $ W \cos \beta $  
- $ y $-component: $ -W \sin \beta $ (negative due to downward direction)  

**Step 2: Sum components for resultant vector $ \vec{R} = \vec{A} + \vec{W} $**  
- $ R_x = A \cos \alpha + W \cos \beta $  
- $ R_y = A \sin \alpha - W \sin \beta $  

**Step 3: Compute magnitude $ |\vec{R}| $**  

$$
|\vec{R}| = \sqrt{ R_x^2 + R_y^2 } = \sqrt{ (A \cos \alpha + W \cos \beta)^2 + (A \sin \alpha - W \sin \beta)^2 }
$$


**Step 4: Expand and simplify**  

$$
\begin{align*}
|\vec{R}|^2 &= (A \cos \alpha + W \cos \beta)^2 + (A \sin \alpha - W \sin \beta)^2 \\
&= A^2 \cos^2 \alpha + 2 A W \cos \alpha \cos \beta + W^2 \cos^2 \beta + A^2 \sin^2 \alpha - 2 A W \sin \alpha \sin \beta + W^2 \sin^2 \beta \\
&= A^2 (\cos^2 \alpha + \sin^2 \alpha) + W^2 (\cos^2 \beta + \sin^2 \beta) + 2 A W (\cos \alpha \cos \beta - \sin \alpha \sin \beta) \\
&= A^2 + W^2 + 2 A W \cos(\alpha + \beta) \quad [\text{using} \ \cos(a+b) = \cos a \cos b - \sin a \sin b]
\end{align*}
$$
  
Thus,  

$$
|\vec{R}| = \sqrt{ A^2 + W^2 + 2 A W \cos(\alpha + \beta) }
$$

## Answer
$$\boxed{\sqrt{ A^{2} + W^{2} + 2 A W \cos(\alpha + \beta) }}$$

------
## Problem 2
##### Background
In physics and engineering, vector addition is fundamental for analyzing forces acting on objects. This problem involves combining two forces with different magnitudes and directions to find the net force's direction, using trigonometric principles and component resolution.

##### Knowledge Points Tested
- Vector decomposition into Cartesian components
- Trigonometric functions for directional angles
- Vector addition and subtraction
- Inverse tangent function for direction calculation

##### Intradisciplinary Connections
Connects to kinematics (velocity vectors), equilibrium analysis, and projectile motion, where vector addition determines net motion or force.

##### Interdisciplinary Connections
- **Navigation**: Pilots and sailors use vector addition to adjust for wind/current drift.
- **Robotics**: Path planning requires vector resolution for motor control.
- **Civil Engineering**: Structural load analysis combines forces from multiple directions.

##### Real-World Applications
- **Construction Cranes**: Calculating net force on loads from multiple cables.
- **Weather Forecasting**: Modeling wind vectors to predict storm paths.
- **Aviation**: Determining aircraft heading when accounting for crosswinds.

##### Problem Statement
Two forces act on an object:  
- Force A: 20 N directed north  
- Force B: 35 N directed 40° west of south  

Determine the direction of the resultant force relative to south. Express your answer as an angle in degrees west of south, rounded to one decimal place. Do not include the degree symbol or the word "degrees" in your final answer.

## Solution
**Step 1: Define the coordinate system**  
- Positive $x$-axis: East  
- Positive $y$-axis: North  

**Step 2: Resolve Force A (20 N north) into components**  
- $F_{Ax} = 0$ N (no east-west component)  
- $F_{Ay} = 20$ N (entirely north)  

**Step 3: Resolve Force B (35 N, 40° west of south) into components**  
- South is the negative $y$-direction; west is the negative $x$-direction.  
- The angle from south is 40°, so:  
  - South component: $F_{B,\text{south}} = 35 \cos(40^\circ)$  
  - West component: $F_{B,\text{west}} = 35 \sin(40^\circ)$  
- In Cartesian coordinates:  
  
$$
  F_{Bx} = -35 \sin(40^\circ) \quad \text{(negative for west)}  
  $$
  
  
$$
  F_{By} = -35 \cos(40^\circ) \quad \text{(negative for south)}  
  $$
  

**Step 4: Calculate resultant force components**  
- $x$-component (east-west):  
  
$$
  R_x = F_{Ax} + F_{Bx} = 0 + (-35 \sin(40^\circ)) = -35 \sin(40^\circ)  
  $$
  
- $y$-component (north-south):  
  
$$
  R_y = F_{Ay} + F_{By} = 20 + (-35 \cos(40^\circ)) = 20 - 35 \cos(40^\circ)  
  $$
  

**Step 5: Determine direction relative to south**  
- The resultant vector lies in the third quadrant ($R_x < 0$, $R_y < 0$), meaning it points southwest.  
- Let $\phi$ be the angle west of south. Then:  
  
$$
  \tan(\phi) = \frac{|R_x|}{|R_y|} = \frac{35 \sin(40^\circ)}{35 \cos(40^\circ) - 20}  
  $$
  
  since $R_y$ is negative, $|R_y| = -(20 - 35 \cos(40^\circ)) = 35 \cos(40^\circ) - 20$.  
- Solve for $\phi$:  
  
$$
  \phi = \arctan\left( \frac{35 \sin(40^\circ)}{35 \cos(40^\circ) - 20} \right)  
  $$
  

**Step 6: Numerical evaluation**  
- $\sin(40^\circ) \approx 0.6428$, $\cos(40^\circ) \approx 0.7660$:  
  
$$
  \text{Numerator} = 35 \times 0.6428 = 22.498  
  $$
  
  
$$
  \text{Denominator} = 35 \times 0.7660 - 20 = 26.81 - 20 = 6.81  
  $$
  
  
$$
  \tan(\phi) = \frac{22.498}{6.81} \approx 3.3037  
  $$
  
  
$$
  \phi = \arctan(3.3037) \approx 73.1^\circ \quad \text{(using calculator in degree mode)}  
  $$
  
- Rounded to one decimal place: $\phi = 73.1^\circ$.  

**Conclusion**: The resultant force is directed $73.1^\circ$ west of south.

## Answer
$$\boxed{73.1}$$

------
# velocity selector operation

## Problem 0
##### Background
A velocity selector is a device used in particle physics to filter charged particles by their speed. It employs perpendicular electric and magnetic fields; only particles with a specific velocity pass through undeflected. The electric field is generated by a parallel-plate capacitor with plate separation $d$ and voltage $V$, while the magnetic field is produced by a solenoid with $n$ turns per unit length carrying current $I$. The fields are mutually perpendicular and perpendicular to the particle's direction of motion. A proton enters this velocity selector.

##### Knowledge Points Tested
1. Electric field magnitude in a parallel-plate capacitor.
2. Magnetic field magnitude inside an ideal solenoid.
3. Force balance on a charged particle in crossed electric and magnetic fields.
4. Derivation of the condition for undeflected motion.

##### Intradisciplinary Connections
- Connects concepts from electrostatics (capacitors), magnetostatics (solenoids), and electromagnetism (Lorentz force).
- Extends the principle of uniform circular motion in magnetic fields to balanced linear motion.

##### Interdisciplinary Connections
- **Engineering:** Design of particle beam filters in accelerators and mass spectrometers.
- **Chemistry:** Isotope separation techniques relying on velocity-dependent forces.
- **Biology:** Applications in radiation therapy targeting with charged particles.

##### Real-World Applications
- Mass spectrometry for identifying chemical compositions.
- Particle accelerators like the Large Hadron Collider (LHC) for selecting specific particle energies.
- Medical devices such as proton therapy machines for cancer treatment.

##### Problem Statement
A proton moves through a velocity selector where the electric field is generated by a parallel-plate capacitor with plate separation $d$ and applied voltage $V$. The magnetic field is produced by a solenoid with $n$ turns per unit length carrying current $I$. The permeability of free space is $\mu_0$. Derive an expression for the proton's undeflected speed $v$ in terms of $V$, $d$, $n$, $I$, and $\mu_0$. Express your final answer as an analytic expression using the given symbols.

## Solution
To find the undeflected speed of the proton, we must ensure the electric and magnetic forces balance exactly. The Lorentz force on a charged particle is given by:
$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$$
For undeflected motion, the net force perpendicular to the velocity must be zero:
$$F_{\text{net}} = 0 \quad \Rightarrow \quad |q|E = |q|vB \sin\theta$$
Since $\vec{E}$, $\vec{B}$, and $\vec{v}$ are mutually perpendicular, $\theta = 90^\circ$ and $\sin\theta = 1$. Thus:
$$E = vB \quad \Rightarrow \quad v = \frac{E}{B}$$

Now, express $E$ and $B$ using the given parameters.  
**Electric field $E$ in the capacitor:**  
For a parallel-plate capacitor with plate separation $d$ and voltage $V$:
$$E = \frac{V}{d}$$

**Magnetic field $B$ in the solenoid:**  
For an ideal solenoid with $n$ turns per unit length and current $I$:
$$B = \mu_0 n I$$

Substitute these expressions into the velocity equation:
$$v = \frac{E}{B} = \frac{\frac{V}{d}}{\mu_0 n I} = \frac{V}{d \mu_0 n I}$$

The charge $q$ and mass of the proton do not appear in the final expression because the forces depend linearly on $q$, which cancels out in the balance equation. Thus, the undeflected speed is:
$$v = \frac{V}{d \mu_0 n I}$$

## Answer
$$\boxed{\dfrac{V}{d \mu_{0} n I}}$$

------
## Problem 1
##### Background
In a velocity selector, charged particles pass through perpendicular electric and magnetic fields to filter particles by velocity. The standard condition for undeflected motion balances electric and magnetic forces. However, real-world selectors may have misaligned components or require precise targeting. This problem explores how an electron's trajectory through a selector relates to its speed when it must hit a specific point.

##### Knowledge Points Tested
1. Lorentz force: $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$
2. Vector decomposition of forces and velocities
3. Uniform motion under zero net force
4. Kinematics of multi-dimensional motion

##### Intradisciplinary Connections
Connects electromagnetic force concepts with kinematics and vector algebra. Extends the velocity selector principle by incorporating spatial constraints on particle trajectories.

##### Interdisciplinary Connections
Applies to mass spectrometry (chemistry) where velocity selection identifies particles, and accelerator physics where beam targeting is essential. Involves vector mathematics from linear algebra.

##### Real-World Applications
- Particle beam focusing in cathode ray tubes (CRTs)
- Precision ion implantation in semiconductor manufacturing
- Particle filtering in space radiation detectors

##### Problem Statement
An electron enters a velocity selector at point $(0, 0, 0)$. The selector has uniform electric field $\vec{E} = E \hat{\imath}$ and uniform magnetic field $\vec{B} = B \hat{\jmath}$, where $E > 0$ and $B > 0$ are constants. The electron exits undeflected (net force $\vec{0}$ throughout) at point $(0, D, L)$. The electron has charge $-e$ and mass $m_e$. Derive the electron's speed $v$ in terms of $E$, $B$, $D$, and $L$ only.

##### Note
"Undeflected" means the net force on the electron is exactly zero at all times. Express the speed as a simplified analytic expression using the given symbols.

## Solution
**Step 1: Analyze forces using Lorentz force law**  
The Lorentz force on an electron ($q = -e$) is:
$$
\vec{F} = -e(\vec{E} + \vec{v} \times \vec{B})
$$
Given $\vec{E} = E \hat{\imath}$ and $\vec{B} = B \hat{\jmath}$:
- Electric force: $-eE \hat{\imath}$  
- Magnetic force: $-e(\vec{v} \times \vec{B})$  

Compute $\vec{v} \times \vec{B}$ for $\vec{v} = (v_x, v_y, v_z)$:
$$
\vec{v} \times \vec{B} = 
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k} \\
v_x & v_y & v_z \\
0 & B & 0 \\
\end{vmatrix}
= \hat{\imath}(v_y \cdot 0 - v_z \cdot B) - \hat{\jmath}(v_x \cdot 0 - v_z \cdot 0) + \hat{k}(v_x \cdot B - v_y \cdot 0) = -B v_z \hat{\imath} + B v_x \hat{k}
$$
Thus, magnetic force: $-e(-B v_z \hat{\imath} + B v_x \hat{k}) = eB v_z \hat{\imath} - eB v_x \hat{k}$  

**Total force components**:  
- $x$-component: $-eE + eB v_z$  
- $y$-component: $0$  
- $z$-component: $-eB v_x$  

**Step 2: Apply undeflected condition (net force $\vec{0}$)**  
Set each force component to zero:  
1. $x$-direction: $-eE + eB v_z = 0 \implies v_z = \frac{E}{B}$  
2. $z$-direction: $-eB v_x = 0 \implies v_x = 0$  
3. $y$-direction: $0$ (always satisfied)  

**Step 3: Relate motion to exit point $(0, D, L)$**  
- Velocity components: $v_x = 0$, $v_y$ unknown, $v_z = E/B$  
- Motion equations (constant velocity):  
  - $x(t) = 0$  
  - $y(t) = v_y t$  
  - $z(t) = (E/B) t$  
At exit time $t_f$:  
- $z(t_f) = L \implies (E/B) t_f = L \implies t_f = \frac{B L}{E}$  
- $y(t_f) = D \implies v_y t_f = D \implies v_y \left(\frac{B L}{E}\right) = D \implies v_y = \frac{D E}{B L}$  

**Step 4: Compute speed**  
Speed $v$ is the magnitude of $\vec{v}$:
$$
v = \sqrt{v_x^2 + v_y^2 + v_z^2} = \sqrt{0 + \left(\frac{D E}{B L}\right)^2 + \left(\frac{E}{B}\right)^2} = \frac{E}{B} \sqrt{\left(\frac{D}{L}\right)^2 + 1}
$$

## Answer
$$\boxed{\dfrac{E}{B} \sqrt{1 + \left( \dfrac{D}{L} \right)^{2}}}$$

------
## Problem 2
##### Background
Velocity selectors are crucial devices in particle physics and mass spectrometry, used to filter charged particles by their speed. They employ perpendicular electric and magnetic fields. Particles pass undeflected only when the electric and magnetic forces balance exactly. Alpha particles (helium nuclei) have a charge of $+2e$ and mass $m$, making them ideal for studying fundamental force interactions. In a new experimental setup for cosmic ray analysis, alpha particles must be isolated from background radiation using a velocity selector.

##### Knowledge Points Tested
1. Lorentz force law for charged particles in electromagnetic fields.
2. Vector cross product application in magnetic force calculations.
3. Equilibrium condition for linear motion under perpendicular forces.
4. Algebraic manipulation to derive physical quantities from fundamental principles.

##### Intradisciplinary Connections
This problem integrates concepts from electrostatics (electric force $q\vec{E}$), magnetostatics (magnetic force $q\vec{v} \times \vec{B}$), and kinematics (uniform linear motion). It reinforces the vector nature of electromagnetic forces and their dependence on particle charge and velocity.

##### Interdisciplinary Connections
- **Engineering**: Velocity selectors are used in mass spectrometers for chemical analysis and radiation detection systems.
- **Space Science**: Similar principles apply in designing instruments for measuring solar wind particle velocities in satellites.
- **Medical Physics**: Targeted alpha therapy for cancer treatment requires precise control of particle beams using electromagnetic fields.

##### Real-World Applications
1. **Particle Accelerators**: Tuning electric fields to isolate specific ion beams.
2. **Environmental Monitoring**: Detecting alpha-emitting pollutants in air samples.
3. **Nuclear Safety**: Filtering alpha particles in radiation-hardened sensors for reactor monitoring.

##### Problem Statement
Consider alpha particles (charge $+2e$, mass $m$) moving with speed $v$ along the positive $x$-axis. They enter a velocity selector region with a uniform magnetic field $\vec{B} = (0, 0, B)$ aligned parallel to the $z$-axis and a perpendicular uniform electric field $\vec{E} = (0, E_y, 0)$ along the $y$-axis. Derive an analytic expression for the electric field strength $E_y$ required for the particles to pass through undeflected. Express $E_y$ symbolically in terms of the given parameters $v$, $B$, and fundamental constants.  

**Answer Format Requirements**:  
- Your final expression must use only the variables $v$, $B$, and physical constants explicitly defined in the problem.  
- Write fractions with \frac\{numerator\}\{denominator\} and square roots with \sqrt\{\}.  
- Do **not** substitute numerical values or evaluate constants.  
- Omit units in the final expression.

## Solution
**Step 1: Lorentz Force Analysis**  
The net force $\vec{F}_{\text{net}}$ on a charged particle in electromagnetic fields is given by the Lorentz force law:  

$$
\vec{F}_{\text{net}} = q(\vec{E} + \vec{v} \times \vec{B})
$$
  
For alpha particles, charge $q = +2e$.  

**Step 2: Force Components**  
Given:  
- Velocity $\vec{v} = (v, 0, 0)$  
- Magnetic field $\vec{B} = (0, 0, B)$  
- Electric field $\vec{E} = (0, E_y, 0)$  

The magnetic force component:  

$$
\vec{v} \times \vec{B} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
v & 0 & 0 \\
0 & 0 & B
\end{vmatrix} = \hat{i}(0 \cdot B - 0 \cdot 0) - \hat{j}(v \cdot B - 0 \cdot 0) + \hat{k}(v \cdot 0 - 0 \cdot 0) = (0, -vB, 0)
$$
  
Thus,  

$$
q(\vec{v} \times \vec{B}) = (+2e) \cdot (0, -vB, 0) = (0, -2evB, 0)
$$
  

The electric force component:  

$$
q\vec{E} = (+2e) \cdot (0, E_y, 0) = (0, 2eE_y, 0)
$$
  

**Step 3: Net Force Equilibrium**  
For undeflected motion, $\vec{F}_{\text{net}} = 0$ in all directions. The $y$-component must satisfy:  

$$
F_{\text{net},y} = 2eE_y + (-2evB) = 2e(E_y - vB) = 0
$$
  
Since $2e \neq 0$,  

$$
E_y - vB = 0
$$
  

**Step 4: Solve for Electric Field**  
Rearranging the equation:  

$$
E_y = vB
$$
  
This is the required electric field strength. The expression is independent of charge and mass because both forces scale linearly with $q$, which cancels out.  

**Conclusion**  
The electric field strength $E_y$ that allows alpha particles to pass undeflected depends only on the particle speed $v$ and magnetic field strength $B$.

## Answer
$$\boxed{vB}$$

------
## Problem 3
##### Background
Velocity selectors are essential tools in particle physics and analytical chemistry, used to filter charged particles by their speed. They employ perpendicular electric and magnetic fields, where particles experience opposing forces. Only particles with a specific velocity travel undeflected when the forces balance. This principle is fundamental in devices like mass spectrometers and particle accelerators.  

##### Knowledge Points Tested
- Force balance on charged particles in crossed electric and magnetic fields  
- Dependence of selected velocity on field strengths  
- Algebraic manipulation of physical equations  

##### Intradisciplinary Connections
- Electric field fundamentals (Coulomb's law, uniform fields)  
- Magnetic force on moving charges (Lorentz force)  
- Newtonian mechanics (equilibrium conditions)  

##### Interdisciplinary Connections
- **Engineering:** Design of particle-beam instruments  
- **Materials Science:** Ion implantation in semiconductor manufacturing  
- **Medicine:** Radiation therapy targeting with charged particles  

##### Real-World Applications
- **Mass Spectrometry:** Isolating ions by velocity before mass analysis  
- **Spacecraft Shielding:** Deflecting cosmic rays using field configurations  
- **Plasma Confinement:** Controlling charged particle streams in fusion reactors  

##### Problem Statement
A velocity selector uses perpendicular uniform electric and magnetic fields with magnitudes $E$ and $B$, respectively. Particles with charge $q$ and velocity $v$ pass undeflected when the electric force exactly cancels the magnetic force.  
The magnetic field strength is reduced to $B/2$ while the electric field $E$ remains constant. Starting from fundamental force principles, derive the factor $\kappa$ by which the selected velocity changes, defined as $\kappa = v_{\text{new}} / v_{\text{original}}$.  
Express $\kappa$ as an exact rational number.

## Solution
**Step 1: Establish force balance condition**  
For undeflected motion, the electric force ($F_E = qE$) and magnetic force ($F_B = qvB$) must be equal in magnitude and opposite in direction:  
$$ qE = qvB $$  

**Step 2: Solve for original velocity**  
Divide both sides by $q$ (assuming $q \neq 0$):  
$$ E = vB $$  
Rearrange for the original velocity $v_{\text{original}}$:  
$$ v_{\text{original}} = \frac{E}{B} \quad (1) $$  

**Step 3: Apply field changes**  
The electric field remains $E$, but the magnetic field becomes $B_{\text{new}} = B/2$. The new force balance equation is:  
$$ qE = q v_{\text{new}} \left(\frac{B}{2}\right) $$  

**Step 4: Solve for new velocity**  
Divide both sides by $q$:  
$$ E = v_{\text{new}} \cdot \frac{B}{2} $$  
Solve for $v_{\text{new}}$:  
$$ v_{\text{new}} = \frac{2E}{B} \quad (2) $$  

**Step 5: Determine the factor $\kappa$**  
Using equations (1) and (2), compute the ratio:  
$$ \kappa = \frac{v_{\text{new}}}{v_{\text{original}}} = \frac{2E/B}{E/B} = \frac{2E}{B} \cdot \frac{B}{E} = 2 $$

## Answer
$$\boxed{2}$$

------
## Problem 4
##### Background
A velocity selector is a device used to filter charged particles by their velocity. It employs perpendicular electric and magnetic fields. Particles passing through experience opposing forces: the electric force and the magnetic force. When these forces balance, particles travel undeflected. This principle is foundational in devices like mass spectrometers, which analyze particle composition in fields such as nuclear physics and chemistry.

##### Knowledge Points Tested
1. Lorentz force: The combined electric and magnetic force on a moving charge, $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$.
2. Equilibrium condition: Net force zero ($\vec{F}_{\text{net}} = 0$) for undeflected motion.
3. Vector cross product: The magnetic force magnitude when $\vec{v} \perp \vec{B}$ is $qvB$.
4. Directional analysis: Forces must oppose for cancellation.

##### Intradisciplinary Connections
This problem integrates concepts from electromagnetism, including field-particle interactions and vector forces, which are extended in topics like cyclotron motion and Hall effect.

##### Interdisciplinary Connections
- **Engineering**: Velocity selectors are used in particle accelerator design.
- **Chemistry/biology**: Applied in mass spectrometry for isotopic analysis.
- **Materials science**: Helps characterize charged particle beams in thin-film deposition.

##### Real-World Applications
- **Medical imaging**: Isotope separation in PET scan tracer production.
- **Space technology**: Plasma velocity filters in satellite thrusters.
- **Environmental science**: Analyzing atmospheric ions in pollution studies.

##### Problem Statement
A deuteron (mass $2m_p$, charge $+e$) moves with velocity $\vec{v}$ perpendicular to a uniform magnetic field of magnitude $B$. An electric field $\vec{E}$, perpendicular to both $\vec{v}$ and $\vec{B}$, is applied. The deuteron passes through undeflected. Derive the magnitude of the electric field $E$ in terms of $v$ and $B$.

Express your answer as an analytic expression using only the variables $v$ and $B$.

## Solution
The deuteron remains undeflected when the net force is zero. The forces acting are:
- Electric force: $\vec{F}_e = q\vec{E} = e\vec{E}$ (since charge is $+e$).
- Magnetic force: $\vec{F}_m = q(\vec{v} \times \vec{B}) = e(\vec{v} \times \vec{B})$.

Given $\vec{v} \perp \vec{B}$, the magnitude of $\vec{F}_m$ is $evB$. The direction of $\vec{F}_m$ follows the right-hand rule. For the forces to oppose:
- $\vec{F}_e$ and $\vec{F}_m$ must be antiparallel. The electric field is oriented such that $\vec{F}_e$ opposes $\vec{F}_m$.

**Equilibrium condition**: Magnitudes of forces are equal:
$$ F_e = F_m $$
$$ eE = evB $$

Divide both sides by $e$ (since $e \neq 0$):
$$ E = vB $$

Thus, the electric field magnitude is the product of the speed $v$ and magnetic field $B$.  
**Note**: The result is independent of mass ($2m_p$) and charge ($e$) because both forces scale linearly with charge, and mass does not affect the force balance for constant velocity.

## Answer
$$\boxed{vB}$$

------
## Problem 5
##### Background
A velocity selector is a device used in scientific instruments like mass spectrometers to select particles of a specific velocity. It employs perpendicular electric and magnetic fields. Particles pass through without deflection when the electric force and the magnetic force on the particle are equal in magnitude and opposite in direction. This problem explores the configuration required for a negatively charged particle moving eastward while experiencing an upward electric force.

##### Knowledge Points Tested
1. Force on a charged particle in an electric field: $\vec{F}_e = q \vec{E}$.
2. Force on a moving charge in a magnetic field: $\vec{F}_m = q (\vec{v} \times \vec{B})$.
3. Vector cross product and right-hand rule conventions.
4. Equilibrium condition for forces in a velocity selector.

##### Intradisciplinary Connections
This problem connects electric and magnetic forces within electromagnetism, requiring vector analysis and coordinate system navigation. It extends to applications in particle dynamics and field theory.

##### Interdisciplinary Connections
Velocity selectors are pivotal in chemistry (mass spectrometry for compound analysis), biology (isotope separation in medical imaging), and engineering (particle beam focusing in accelerators).

##### Real-World Applications
- **Mass Spectrometry**: Identifying molecular structures by filtering ions by velocity.
- **Particle Accelerators**: Selecting charged particles at specific speeds for collision experiments.
- **Medical Diagnostics**: Isolating radioactive isotopes for targeted cancer treatments.

##### Problem Statement
A negatively charged particle with charge $-|q|$ moves eastward with velocity $\vec{v} = v \hat{\imath}$ in a velocity selector. The electric field $\vec{E}$ is configured to exert an upward force on the particle. Assume a right-handed coordinate system where:  
- $\hat{\imath}$ points east (positive $x$-direction),  
- $\hat{\jmath}$ points upward (positive $y$-direction),  
- $\hat{k}$ points north (positive $z$-direction).  

The magnetic field $\vec{B}$ is perpendicular to both $\vec{v}$ and $\vec{E}$. Derive the expression for the ratio $B_z / |\vec{B}|$, where $B_z$ is the $z$-component of $\vec{B}$ and $|\vec{B}|$ is its magnitude. Express your answer as an exact number.  
*Hint: Consider the vector nature of the magnetic force and equilibrium conditions.*

## Solution
**Step 1: Express forces using given conditions**  
- Charge: $q = -|q|$.  
- Velocity: $\vec{v} = v \hat{\imath}$.  
- Electric force is upward: $\vec{F}_e = F_e \hat{\jmath}$ ($F_e > 0$).  
- Electric field relation: $\vec{F}_e = q \vec{E} \implies \vec{E} = \frac{\vec{F}_e}{q} = \frac{F_e \hat{\jmath}}{-|q|} = -\frac{F_e}{|q|} \hat{\jmath}$.  
Thus, $\vec{E}$ is downward (negative $y$-direction).  

**Step 2: Apply equilibrium condition**  
Net force is zero for no deflection:  
$$
\vec{F}_e + \vec{F}_m = 0 \implies \vec{F}_m = -\vec{F}_e = -F_e \hat{\jmath}.
$$

**Step 3: Write magnetic force**  
$$
\vec{F}_m = q (\vec{v} \times \vec{B}) = -|q| (v \hat{\imath} \times \vec{B}).
$$
Set equal to $-F_e \hat{\jmath}$:  
$$
-|q| v (\hat{\imath} \times \vec{B}) = -F_e \hat{\jmath} \implies |q| v (\hat{\imath} \times \vec{B}) = F_e \hat{\jmath}. \quad (1)
$$

**Step 4: Expand cross product**  
Let $\vec{B} = B_x \hat{\imath} + B_y \hat{\jmath} + B_z \hat{k}$. Using cross-product identities:  
$$
\hat{\imath} \times \hat{\imath} = 0, \quad \hat{\imath} \times \hat{\jmath} = \hat{k}, \quad \hat{\imath} \times \hat{k} = -\hat{\jmath}.
$$
Thus:  
$$
\hat{\imath} \times \vec{B} = B_x (\hat{\imath} \times \hat{\imath}) + B_y (\hat{\imath} \times \hat{\jmath}) + B_z (\hat{\imath} \times \hat{k}) = 0 + B_y \hat{k} - B_z \hat{\jmath} = -B_z \hat{\jmath} + B_y \hat{k}.
$$
Substitute into (1):  
$$
|q| v (-B_z \hat{\jmath} + B_y \hat{k}) = F_e \hat{\jmath}.
$$

**Step 5: Equate vector components**  
- $\hat{\jmath}$-component: $-|q| v B_z = F_e \implies B_z = -\frac{F_e}{|q| v}$.  
- $\hat{k}$-component: $|q| v B_y = 0 \implies B_y = 0$.  

**Step 6: Apply perpendicularity constraint**  
$\vec{B}$ is perpendicular to $\vec{v}$ (east, $\hat{\imath}$) and $\vec{E}$ (downward, $-\hat{\jmath}$), so $\vec{B}$ must be parallel to $\hat{k}$ (north-south). Thus, $B_x = 0$, and $\vec{B} = B_z \hat{k}$. Magnitude is $|\vec{B}| = |B_z| = \left| -\frac{F_e}{|q|v} \right| = \frac{F_e}{|q|v}$ (since $F_e, |q|, v > 0$).  

**Step 7: Compute the ratio**  
$$
\frac{B_z}{|\vec{B}|} = \frac{-\frac{F_e}{|q|v}}{\frac{F_e}{|q|v}} = -1.
$$

## Answer
$$\boxed{-1}$$

------
## Problem 6
##### Background
A velocity selector is a device used in particle physics that employs perpendicular electric and magnetic fields to filter charged particles by their velocity. Particles traveling at a specific speed pass through undeflected, while others are deflected. After selection, particles can be analyzed further in a uniform magnetic field where they undergo circular motion due to the magnetic force acting perpendicular to their velocity.

##### Knowledge Points Tested
1. Force balance in velocity selectors: electric force vs. magnetic force.
2. Magnetic force as a centripetal force in uniform circular motion.
3. Derivation of the radius of curvature for charged particles in a magnetic field.

##### Intradisciplinary Connections
This problem connects concepts from electrostatics (electric force), magnetism (magnetic force on moving charges), and mechanics (centripetal acceleration in circular motion).

##### Interdisciplinary Connections
Velocity selectors are foundational in mass spectrometry (chemistry/biology for isotope separation) and particle physics (detector systems like Wien filters).

##### Real-World Applications
- **Mass Spectrometry:** Determining mass-to-charge ratios of ions.
- **Particle Accelerators:** Beam focusing and velocity filtering.
- **Spacecraft Shielding:** Simulating cosmic ray behavior using crossed fields.

##### Problem Statement
A particle of mass $m$ and charge $q$ (where $q$ can be positive or negative) passes undeflected through a velocity selector with a uniform electric field of magnitude $E$ and a uniform magnetic field of magnitude $B_s$, where the fields are perpendicular to each other and to the particle's velocity. Immediately after, the particle enters a region with a uniform magnetic field of magnitude $B_c$ (where $B_c = B_s$) and no electric field. The particle moves perpendicular to this magnetic field in a circular path.  

Derive an expression for the radius $r$ of the circular path in terms of $m$, $|q|$, $E$, and $B_s$.  
Express your answer as an analytic expression using the given symbols. Use $\left| q \right|$ for the magnitude of charge, and follow standard mathematical notation:  
- Use $\frac{a}{b}$ for fractions.  
- Use $B_s^{2}$ for the square of $B_s$.  
- Do not substitute numerical values or constants.

## Solution
#### Step 1: Velocity Selector Condition  
In the velocity selector, the particle is undeflected, so the net force is zero. The electric force ($F_e$) and magnetic force ($F_m$) must balance:  

$$ F_e = |q| E \quad \text{(magnitude)} $$
  

$$ F_m = |q| v B_s \quad \text{(magnitude, since } \vec{v} \perp \vec{B_s}\text{)} $$
  
Setting forces equal:  

$$ |q| E = |q| v B_s $$
  
Divide both sides by $|q|$ (assuming $q \neq 0$):  

$$ E = v B_s $$
  
Solve for velocity $v$:  

$$ v = \frac{E}{B_s} $$
  

#### Step 2: Circular Motion in Magnetic Field  
In the region with only magnetic field $B_c = B_s$, the magnetic force provides the centripetal force for circular motion:  

$$ F_m = \frac{m v^2}{r} $$
  
The magnitude of the magnetic force is:  

$$ F_m = |q| v B_c = |q| v B_s \quad \text{(since } B_c = B_s\text{)} $$
  
Equate to centripetal force:  

$$ |q| v B_s = \frac{m v^2}{r} $$
  

#### Step 3: Solve for Radius $r$  
Cancel $v$ (assuming $v \neq 0$):  

$$ |q| B_s = \frac{m v}{r} $$
  
Rearrange:  

$$ r = \frac{m v}{|q| B_s} $$
  
Substitute $v = \frac{E}{B_s}$ from Step 1:  

$$ r = \frac{m}{|q| B_s} \cdot \frac{E}{B_s} = \frac{m E}{|q| B_s^{2}} $$
  
Thus, the radius is:  

$$ r = \frac{m E}{\left| q \right| B_s^{2}} $$

## Answer
\[ \boxed{\dfrac{m E}{\left| q \right| B_s^{2}}} \]

------
## Problem 7
#### Background
A velocity selector, also known as a Wien filter, is a device used in particle physics to isolate charged particles with a specific velocity. It employs perpendicular electric and magnetic fields to exert opposing forces on moving charges. When these forces balance, particles with the target velocity travel undeflected through the device. This problem explores the fundamental principles behind such a selector, focusing on the derivation of the magnetic field strength required for equilibrium.

#### Knowledge Points Tested
1. Force balance between electric and magnetic fields on a moving charge.
2. Relationship between electric field, potential difference, and plate separation in a parallel plate capacitor.
3. Application of Newton's second law for steady-state motion with zero net force.

#### Intradisciplinary Connections
- Electrostatics: Uniform electric fields in capacitors.
- Magnetism: Magnetic force on moving charges (Lorentz force).
- Dynamics: Equilibrium conditions in particle motion.

#### Interdisciplinary Connections
- Engineering: Design of particle beam selectors in mass spectrometers.
- Technology: Applications in medical isotope separation and particle accelerator systems.

#### Real-World Applications
Velocity selectors are critical components in mass spectrometry for isotopic analysis, radiation therapy devices for targeting specific ion velocities, and space probe instruments for analyzing cosmic ray compositions.

#### Problem Statement
A velocity selector consists of two parallel conducting plates separated by a distance $d$. A potential difference $V$ is applied across the plates, generating a uniform electric field. A uniform magnetic field of magnitude $B$ is applied perpendicularly to both the electric field and the initial velocity vector of incoming protons. Each proton has charge $e$ and mass $m_p$.  

Derive an expression for the magnetic field $B$ that allows protons with velocity $v$ to pass through the selector without deflection. Express your answer symbolically in terms of $V$, $v$, and $d$.  

**Formatting Instructions**:  
- The final answer must be an analytic expression.  
- Use fractions, multiplication, and division operations as needed.  
- Do not substitute numerical values or physical constants.  
- Express all multiplication explicitly with $\cdot$ or via juxtaposition (e.g., $V / (v d)$).

## Solution
**Step 1: Identify forces acting on the proton**  
The electric force ($\vec{F}_e$) and magnetic force ($\vec{F}_m$) must balance for zero deflection. Given:  
- Electric field $\vec{E}$ is uniform and perpendicular to the plates.  
- Magnetic field $\vec{B}$ is uniform and perpendicular to both $\vec{E}$ and the proton's velocity $\vec{v}$.  

The magnitudes of the forces are:  
- Electric force: $F_e = eE$ (direction depends on charge and $\vec{E}$)  
- Magnetic force: $F_m = evB$ (direction follows the right-hand rule, opposing $\vec{F}_e$)  

**Step 2: Apply the equilibrium condition**  
For no deflection, net force perpendicular to $\vec{v}$ is zero:  
$$ F_e = F_m $$  
Substitute force expressions:  
$$ eE = evB $$  

**Step 3: Relate electric field to given parameters**  
The electric field $E$ between parallel plates is:  
$$ E = \frac{V}{d} $$  
Substitute this into the force-balance equation:  
$$ e \cdot \frac{V}{d} = evB $$  

**Step 4: Solve for $B$**  
Divide both sides by $e$ (since $e \neq 0$):  
$$ \frac{V}{d} = vB $$  
Rearrange to isolate $B$:  
$$ B = \frac{V}{v d} $$  

**Conclusion**  
The magnetic field strength required for protons to pass undeflected is $B = \frac{V}{v d}$.

## Answer
$$\boxed{\dfrac{V}{v \cdot d}}$$

------
## Problem 8
##### Background
In particle physics experiments, a velocity selector uses perpendicular electric and magnetic fields to filter charged particles by velocity. This device is essential in applications like mass spectrometry and electron microscopy. When particles enter the selector with the correct velocity, the electric and magnetic forces balance, allowing them to travel undeflected. For electrons, this principle enables precise control of particle beams in vacuum systems.

##### Knowledge Points Tested
- Force balance on charged particles in crossed electric and magnetic fields
- Relating kinetic energy to particle velocity and mass
- Vector nature of electromagnetic forces (Lorentz force law)

##### Intradisciplinary Connections
Connects to electromagnetism (field interactions), mechanics (force equilibrium), and particle dynamics (uniform motion under balanced forces). Extends to cyclotron motion and mass spectrometry when magnetic fields act alone.

##### Interdisciplinary Connections
Used in chemistry for isotope separation (mass spectrometry), engineering for electron beam focusing (cathode-ray tubes), and medical physics for radiation therapy systems.

##### Real-World Applications
- **Electron Microscopes:** Velocity selectors prepare monoenergetic electron beams for high-resolution imaging.
- **Particle Accelerators:** Selectors filter particles before injection into acceleration stages.
- **Spacecraft Shielding:** Simulated in labs to study cosmic-ray deflection mechanisms.

##### Problem Statement
An electron (mass $m_e$, charge $-e$) enters a velocity selector with perpendicular uniform electric and magnetic fields. The electric field has magnitude $E$ and the magnetic field has magnitude $B$. Derive the kinetic energy $K$ of electrons that pass through the selector without deflection. Express $K$ symbolically in terms of $E$, $B$, $m_e$, and fundamental constants.  
*Note: Assume non-relativistic mechanics and exact perpendicularity of fields and initial velocity.*

## Solution
**Step 1: Force balance condition**  
For undeflected motion, the net force on the electron must be zero. The Lorentz force gives:  
$$\vec{F}_{\text{net}} = q(\vec{E} + \vec{v} \times \vec{B}) = 0$$  
With $q = -e$ and $\vec{E} \perp \vec{B} \perp \vec{v}$, the magnitudes satisfy:  
$$eE = evB \quad \text{(since forces oppose)}$$  
Solving for velocity $v$:  
$$v = \frac{E}{B} \quad (1)$$  

**Step 2: Kinetic energy expression**  
Non-relativistic kinetic energy is:  
$$K = \frac{1}{2} m_e v^2 \quad (2)$$  
Substitute $v$ from (1) into (2):  
$$K = \frac{1}{2} m_e \left( \frac{E}{B} \right)^2$$  

**Step 3: Final expression**  
Simplify the equation:  
$$K = \frac{1}{2} m_e \frac{E^2}{B^2}$$  
This is the kinetic energy for undeflected electrons.

## Answer
$$\boxed{\dfrac{m_{e} E^{2}}{2 B^{2}}}$$

------
# vertical circular motion problems

## Problem 0
##### Background
Vertical circular motion is a fundamental concept in mechanics, with applications ranging from amusement park rides to athletic training. Consider a high-performance drone light show where a drone (modeled as a point mass $m$) is attached to a central pivot by a lightweight, inextensible string of length $r$. The drone executes vertical circles while maintaining tautness in its tether. If the string goes slack at the top position, the drone loses its controlled trajectory. Understanding the minimum speed requirement at the top is critical for designing fail-safe mechanisms in such dynamic systems.

##### Knowledge Points Tested
- Newton's second law for circular motion
- Centripetal force and its relation to tension
- Critical speed conditions in vertical circular motion
- Free-body diagrams at specific trajectory points

##### Intradisciplinary Connections
- Connects to conservation of mechanical energy (for full-circle analysis)
- Relates to torque and rotational dynamics through tension variations
- Extends to non-uniform circular motion concepts

##### Interdisciplinary Connections
- **Engineering**: Safety calculations for roller coaster loops and centrifuges
- **Aerospace**: Tethered satellite systems requiring constant tension
- **Sports Science**: Analysis of hammer throw or gymnastic bar releases

##### Real-World Applications
- Designing centrifuges for astronaut training that simulate high-g environments
- Calculating minimum launch speeds for loop-the-loop maneuvers in autonomous drone racing
- Ensuring structural integrity of pendulum rides at theme parks

##### Problem Statement
A drone of mass $m$ is attached to a fixed point by a string of length $r$ and moves in a vertical circle. Derive the minimum speed $v_{\text{min}}$ the drone must have at the highest point of the circle to prevent the string from going slack. Express your answer symbolically in terms of the acceleration due to gravity $g$ and the radius $r$.  
**Format Requirements**:  
- Use $g$ for gravity and $r$ for radius.  
- The final expression must be simplified and boxed.  
- Do **not** substitute numerical values or constants.

## Solution
**Step 1: Identify forces at the top of the circle**  
At the highest point of the vertical circle, two forces act on the drone:  
- Gravitational force: $mg$ downward (toward Earth's center).  
- Tension force: $T$ downward (along the string toward the pivot).  
Both forces act toward the center of the circle, providing the centripetal force.  

**Step 2: Apply Newton's second law**  
The net centripetal force equals mass times centripetal acceleration:  
$$ T + mg = \frac{mv^2}{r} $$  
where $v$ is the speed at the top, and $\frac{v^2}{r}$ is the centripetal acceleration.  

**Step 3: Condition for preventing slack**  
The string goes slack when tension $T \leq 0$. The minimum speed $v_{\text{min}}$ occurs when tension is exactly zero:  
$$ T = 0 $$  
Substitute into the force equation:  
$$ 0 + mg = \frac{mv_{\text{min}}^2}{r} $$  

**Step 4: Solve for $v_{\text{min}}$**  
Simplify by dividing both sides by $m$ (valid since $m \neq 0$):  
$$ g = \frac{v_{\text{min}}^2}{r} $$  
Multiply both sides by $r$:  
$$ gr = v_{\text{min}}^2 $$  
Take the positive square root (speed magnitude):  
$$ v_{\text{min}} = \sqrt{gr} $$  
This is the minimum speed required at the top to maintain tension.

## Answer
$$\boxed{\sqrt{g r}}$$

------
## Problem 1
##### Background
When an object moves in a vertical circle, such as a bucket of water being swung overhead, the forces acting on it vary with position due to gravity. At the top of the circle, the water is most prone to spilling if the centripetal force is insufficient to keep it moving in a circular path. This problem explores the minimum speed required at the highest point to prevent spillage by analyzing the balance between gravitational and centripetal forces.

##### Knowledge Points Tested
1. Centripetal force requirement for circular motion.
2. Newton's second law applied to non-uniform circular motion.
3. Force analysis at critical points in vertical circular motion.
4. Equilibrium condition for contact forces.

##### Intradisciplinary Connections
- Connects to energy conservation methods for vertical circles (e.g., using kinetic and potential energy to find speeds at different points).
- Relates to tension and normal force analysis in constrained circular motion.

##### Interdisciplinary Connections
- **Engineering:** Design of roller coasters and centrifuges where minimum speeds prevent detachment.
- **Astronomy:** Orbital mechanics concepts, such as calculating minimum orbital velocities for satellites.

##### Real-World Applications
- Carnival rides like "The Rotor" or "Gravitron" that rely on vertical circular motion principles.
- Washing machine spin cycles where centrifugal force prevents water from leaking at high speeds.
- Aircraft maneuvers during loop-the-loops in aerobatic displays.

##### Problem Statement
A bucket of water is rotated in a vertical circle of radius $r$. The water has mass $m$, and the acceleration due to gravity is $g$. At the top of the circle, the water is on the verge of spilling when the contact force between the bucket and water becomes zero. Derive the minimum speed $v_{\text{min}}$ required at the topmost point to prevent spillage.  

*Express your answer as an analytic expression in terms of $g$ and $r$ only. Do not substitute numerical values.*

## Solution
**Step 1: Identify forces at the top of the circle**  
At the top of the vertical circle, two forces act on the water:  
- Gravitational force: $mg$ downward (toward the center of the circle).  
- Normal force ($N$) from the bucket: downward (since the bucket must push the water toward the center to maintain circular motion).  

The free-body diagram shows both forces directed toward the center, so the net centripetal force is:  
$$ N + mg = \frac{mv^2}{r} $$  
where $v$ is the speed at the top, and $r$ is the radius.

**Step 2: Apply the spillage condition**  
Water spills when it loses contact with the bucket, which occurs when the normal force $N = 0$. Substituting this condition:  
$$ 0 + mg = \frac{mv_{\text{min}}^2}{r} $$  

**Step 3: Solve for $v_{\text{min}}$**  
Simplify the equation:  
$$ mg = \frac{mv_{\text{min}}^2}{r} $$  
Divide both sides by $m$ (since $m \neq 0$):  
$$ g = \frac{v_{\text{min}}^2}{r} $$  
Multiply both sides by $r$:  
$$ gr = v_{\text{min}}^2 $$  
Take the square root:  
$$ v_{\text{min}} = \sqrt{gr} $$  

**Conclusion**  
The minimum speed at the top to prevent spillage is $\sqrt{gr}$. This result is independent of the water's mass because both gravitational and centripetal forces scale linearly with $m$.

## Answer
$$\boxed{\sqrt{gr}}$$

------
## Problem 2
##### Background  
In modern highway engineering, convex bridges are designed with circular arcs to provide smooth transitions for vehicles. These structures rely on principles of circular motion to ensure safety. At the crest of such a bridge, the normal force between the tires and the road must remain positive to prevent loss of traction and control. Autonomous vehicle testing facilities often simulate these conditions to establish speed safety limits.  

##### Knowledge Points Tested  
- Centripetal force in vertical circular motion  
- Newton’s second law for radial dynamics  
- Critical speed analysis for contact loss  
- Free-body diagram construction  

##### Intradisciplinary Connections  
This problem connects to kinematics (tangential velocity), energy conservation (if extended to the full bridge path), and rotational dynamics (centripetal acceleration).  

##### Interdisciplinary Connections  
**Civil Engineering**: Bridge design standards incorporate maximum speed limits based on curvature.  
**Robotics**: Autonomous vehicles use real-time physics models to adjust speed on curved terrain.  
**Meteorology**: Road adhesion varies with weather, but the fundamental speed limit depends on gravity and geometry.  

##### Real-World Applications  
- Setting speed limits on curved highway overpasses (e.g., Interstate highway convex bridges).  
- Roller coaster safety protocols at the top of loops.  
- Drone navigation algorithms when following curved terrain profiles.  

##### Problem Statement  
A test vehicle of mass $m$ moves at speed $v$ over a convex bridge modeled as a circular arc with radius $r$. The gravitational acceleration is $g$. At the crest (highest point), derive the **maximum speed** $v_{\text{max}}$ the vehicle can have without losing contact with the road. Express your answer symbolically in terms of $g$ and $r$.  

**Instructions for final answer format**:  
- Provide a **single analytic expression** for $v_{\text{max}}$ using $g$ and $r$.  
- Use $\sqrt{\cdots}$ for square roots (e.g., $\sqrt{g r}$).  
- Do **not** include units, numerical values, or the vehicle mass $m$ in the final expression.

## Solution
#### Step 1: Identify Forces at the Crest  
At the crest, the vehicle experiences:  
- Weight $mg$ downward (toward Earth's center).  
- Normal force $N$ upward (exerted by the bridge).  
The center of the circular path is **below** the crest, so the centripetal force direction is downward.  

#### Step 2: Apply Newton’s Second Law  
For circular motion, the net radial force provides centripetal acceleration. At the crest:  

$$
mg - N = \frac{mv^2}{r}
$$
  
where $v$ is the speed, and $\frac{mv^2}{r}$ is the required centripetal force.  

#### Step 3: Define Contact-Loss Condition  
Contact is lost when the bridge cannot exert an upward normal force, i.e., $N = 0$. Substitute this into the equation:  

$$
mg - 0 = \frac{mv_{\text{max}}^2}{r}
$$
  

#### Step 4: Solve for Maximum Speed  
Simplify the equation:  

$$
mg = \frac{mv_{\text{max}}^2}{r}
$$
  
Divide both sides by $m$ (mass cancels out):  

$$
g = \frac{v_{\text{max}}^2}{r}
$$
  
Multiply both sides by $r$:  

$$
g r = v_{\text{max}}^2
$$
  
Take the square root to solve for $v_{\text{max}}$:  

$$
v_{\text{max}} = \sqrt{g r}
$$
  

**Key Insight**: The maximum speed depends only on gravity and the bridge’s radius, not the vehicle’s mass. This is why small and large vehicles share the same speed limit on curved bridges.

## Answer
$$\boxed{\sqrt{g r}}$$

------
## Problem 3
##### Background
In vertical circular motion, an object attached to a string experiences varying tension due to gravitational forces and centripetal acceleration. This scenario models real-world systems like amusement park rides (e.g., roller coaster loops) or athletic events (e.g., hammer throw), where understanding tension dynamics is crucial for safety and performance. The minimum speed condition at the top ensures the object maintains circular motion without the string going slack.

##### Knowledge Points Tested
1. **Conservation of mechanical energy**: Relates kinetic and potential energy between two points.
2. **Centripetal force analysis**: Newton's second law applied to circular motion.
3. **Tension-force relationships**: Vector resolution in radial and tangential directions.

##### Intradisciplinary Connections
Connects to rotational dynamics (torque and angular momentum) and harmonic motion, as the tension variation resembles periodic behavior in oscillatory systems.

##### Interdisciplinary Connections
- **Engineering**: Structural integrity analysis in pendulum-based rides or rotating machinery.
- **Sports science**: Optimizing release angles and speeds in hammer throw or shot put.

##### Real-World Applications
- **Theme park safety**: Calculating maximum tension on roller coaster cables during loops to prevent structural failure.
- **Space mission design**: Simulating gravitational forces in centrifuges for astronaut training.

##### Problem Statement
A stone of mass $m$ is tied to an inextensible string of length $l$. The stone is swung in a vertical circle such that its speed at the highest point is $\sqrt{g l}$, where $g$ is the acceleration due to gravity. Derive an expression for the tension $T$ in the string when the stone is at the lowest point. Express $T$ symbolically in terms of $m$ and $g$.

## Solution
**Step 1: Define energy conservation between top and bottom**  
The total mechanical energy is conserved (no non-conservative forces). Set the lowest point as the reference height ($h = 0$).  
- **Top point**: Height = $2l$, speed = $v_{\text{top}} = \sqrt{g l}$  
  Kinetic energy = $\frac{1}{2} m v_{\text{top}}^2 = \frac{1}{2} m (\sqrt{g l})^2 = \frac{1}{2} m g l$  
  Potential energy = $m g (2l) = 2 m g l$  
  Total energy at top: $E_{\text{top}} = \frac{1}{2} m g l + 2 m g l = \frac{5}{2} m g l$  
- **Bottom point**: Height = $0$, speed = $v_{\text{bottom}}$ (unknown)  
  Kinetic energy = $\frac{1}{2} m v_{\text{bottom}}^2$  
  Potential energy = $0$  
  Total energy at bottom: $E_{\text{bottom}} = \frac{1}{2} m v_{\text{bottom}}^2$  

By conservation of energy:  
$$E_{\text{top}} = E_{\text{bottom}}$$  
$$\frac{5}{2} m g l = \frac{1}{2} m v_{\text{bottom}}^2$$  

**Step 2: Solve for $v_{\text{bottom}}$**  
Multiply both sides by 2:  
$$5 m g l = m v_{\text{bottom}}^2$$  
Divide by $m$ (assuming $m \neq 0$):  
$$v_{\text{bottom}}^2 = 5 g l \quad (1)$$  

**Step 3: Apply Newton's second law at the bottom**  
At the lowest point:  
- Forces acting toward the center (upward): Tension $T$  
- Forces acting away from the center (downward): Weight $m g$  
Net centripetal force = $T - m g$  

Centripetal force required = $\frac{m v_{\text{bottom}}^2}{l}$  
Thus:  
$$T - m g = \frac{m v_{\text{bottom}}^2}{l}$$  

Substitute $v_{\text{bottom}}^2$ from equation (1):  
$$T - m g = \frac{m (5 g l)}{l}$$  
Simplify:  
$$T - m g = 5 m g$$  

**Step 4: Solve for tension $T$**  
$$T = 5 m g + m g = 6 m g$$

## Answer
$$\boxed{6mg}$$

------
# work function and threshold frequency

## Problem 0
##### Background
The photoelectric effect is a quantum phenomenon where electrons are emitted from a metal surface when illuminated by light of sufficient frequency. The work function $\phi$ is the minimum energy required to eject an electron, and the threshold frequency $\nu_0$ is the minimum frequency of light needed to initiate this process. These quantities are related by $\phi = h\nu_0$, where $h$ is Planck's constant. In practical applications, work functions are often expressed in electronvolts (eV), a unit defined as the kinetic energy gained by an electron accelerated through a potential difference of 1 volt.

##### Knowledge Points Tested
1. Photoelectric equation: $K_{\text{max}} = h\nu - \phi$
2. Threshold frequency definition: $\phi = h\nu_0$
3. Energy conversion: joules to electronvolts using the elementary charge $e$
4. Algebraic manipulation of equations

##### Intradisciplinary Connections
This problem connects quantum physics (photoelectric effect) with atomic physics (electron binding energy) and electromagnetism (energy units and electronvolts).

##### Interdisciplinary Connections
The concept applies to materials science (properties of metal surfaces) and electrical engineering (design of photodetectors and solar cells).

##### Real-World Applications
Work function measurements are critical in developing photocathodes for night-vision devices, photomultiplier tubes in medical imaging, and photovoltaic cells for solar energy conversion.

##### Problem Statement
In a photoelectric effect experiment, two different metals (Metal A and Metal B) are illuminated by monochromatic light of frequency $\nu$. The stopping potential for Metal A is $V_A$, and for Metal B is $V_B$. The threshold frequency for Metal A is $\nu_{0A}$.  

Derive an expression for the work function $\phi_B$ of Metal B in electronvolts (eV). Express your answer analytically in terms of $V_A$, $V_B$, $\nu_{0A}$, Planck's constant $h$, and the elementary charge $e$.  

**Answer Format Instructions**:  
- Provide only the final analytic expression enclosed in \boxed{}.
- Use standard LaTeX notation:  
  - Fractions: $\frac{a}{b}$  
  - Elementary charge: $e$  
  - Planck's constant: $h$  
- Do **not** substitute numerical values for constants.  
- The expression must be simplified and dimensionless (implied by eV units).

## Solution
**Step 1: Write the photoelectric equation for Metal A**  
The maximum kinetic energy of ejected electrons is related to the stopping potential $V_A$ by:  

$$
K_{\text{max},A} = eV_A
$$
  
By the photoelectric effect equation:  

$$
K_{\text{max},A} = h\nu - \phi_A
$$
  
where $\phi_A$ is the work function of Metal A. Equating both expressions:  

$$
eV_A = h\nu - \phi_A \quad (1)
$$


**Step 2: Express $\phi_A$ in terms of threshold frequency**  
The work function of Metal A is related to its threshold frequency $\nu_{0A}$:  

$$
\phi_A = h\nu_{0A} \quad (2)
$$
  
Substitute (2) into (1):  

$$
eV_A = h\nu - h\nu_{0A} \quad (3)
$$
  
Solving for $\nu$:  

$$
h\nu = eV_A + h\nu_{0A} \quad (4)
$$


**Step 3: Write the photoelectric equation for Metal B**  
The maximum kinetic energy for Metal B is:  

$$
K_{\text{max},B} = eV_B = h\nu - \phi_B \quad (5)
$$
  
where $\phi_B$ is the work function of Metal B.

**Step 4: Substitute $\nu$ into Metal B's equation**  
Substitute expression (4) for $h\nu$ into (5):  

$$
eV_B = (eV_A + h\nu_{0A}) - \phi_B \quad (6)
$$
  
Rearrange to solve for $\phi_B$:  

$$
\phi_B = eV_A + h\nu_{0A} - eV_B \quad (7)
$$


**Step 5: Convert $\phi_B$ to electronvolts (eV)**  
Since $1  \text{eV} = e \times 1  \text{J}$, the work function in eV is obtained by dividing $\phi_B$ (in joules) by $e$:  

$$
\phi_B (\text{in eV}) = \frac{\phi_B}{e} = \frac{eV_A + h\nu_{0A} - eV_B}{e} = V_A - V_B + \frac{h\nu_{0A}}{e} \quad (8)
$$
  
The expression $V_A - V_B + \frac{h\nu_{0A}}{e}$ is dimensionless and represents the work function in eV.

## Answer
$$\boxed{V_A - V_B + \frac{h\nu_{0A}}{e}}$$

------
## Problem 1
#### Background
The photoelectric effect occurs when light incident on a metal surface ejects electrons if the photon energy exceeds the metal's work function ($\phi$), defined as the minimum energy needed to remove an electron. The threshold wavelength ($\lambda_0$) is the maximum wavelength at which electron ejection occurs. This wavelength is critical for designing photoelectric sensors in security systems, where specific light sources must be matched to metal surfaces. For a new alloy used in spacecraft radiation shielding, the work function is $\phi = 2.30 \text{ eV}$.

#### Knowledge Points Tested
- Einstein's photoelectric equation: $E_{\text{photon}} = h\nu = \frac{hc}{\lambda}$.
- Threshold condition: $E_{\text{photon}} = \phi$ at $\lambda_0$.
- Energy unit conversions: electronvolts (eV) to joules (J).
- Wavelength unit conversions: meters (m) to nanometers (nm).

#### Intradisciplinary Connections
- Quantum mechanics: photon energy quantization.
- Atomic physics: work function relates to electron binding energy in metals.
- Electromagnetism: light wavelength and frequency interdependence.

#### Interdisciplinary Connections
- Materials science: alloy work functions impact sensor efficiency.
- Aerospace engineering: radiation shielding in spacecraft.
- Sustainable technology: photoelectric sensors for solar energy harvesting.

#### Real-World Applications
- Security systems: photoelectric sensors in automatic doors or intruder alarms.
- Space technology: radiation detectors in satellites.
- Environmental monitoring: UV sensors for ozone layer measurement.

#### Problem Statement
The work function of a metal alloy is $\phi = 2.30 \text{ eV}$. Derive an expression for the threshold wavelength $\lambda_0$ in terms of $\phi$ (converted to joules), Planck's constant $h$, and the speed of light $c$. Then, using:  
- $h = 6.626 \times 10^{-34} \text{ J·s}$,  
- $c = 3.00 \times 10^{8} \text{ m/s}$,  
- $1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}$,  
compute $\lambda_0$ in nanometers. Round your final answer to three significant figures.  
**Format instructions**: Provide only the numerical value in the boxed answer.

## Solution
**Step 1: Establish the photoelectric threshold condition**  
At threshold, photon energy equals the work function:  
$$ E_{\text{photon}} = \phi $$  
Photon energy is given by $E_{\text{photon}} = \frac{hc}{\lambda}$, so:  
$$ \frac{hc}{\lambda_0} = \phi $$  

**Step 2: Derive the symbolic expression for $\lambda_0$**  
Solve for $\lambda_0$:  
$$ \lambda_0 = \frac{hc}{\phi} $$  
where $\phi$ must be in joules (J) for unit consistency.  

**Step 3: Convert $\phi$ to joules**  
Given $\phi = 2.30 \text{ eV}$ and $1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}$:  
$$ \phi = 2.30 \times (1.602 \times 10^{-19}) = 3.6846 \times 10^{-19} \text{ J} $$  

**Step 4: Compute $hc$**  
Substitute $h$ and $c$:  
$$ hc = (6.626 \times 10^{-34}) \times (3.00 \times 10^{8}) = 1.9878 \times 10^{-25} \text{ J·m} $$  

**Step 5: Calculate $\lambda_0$ in meters**  
$$ \lambda_0 = \frac{1.9878 \times 10^{-25}}{3.6846 \times 10^{-19}} = 5.3940 \times 10^{-7} \text{ m} $$  

**Step 6: Convert meters to nanometers**  
$1 \text{ m} = 10^9 \text{ nm}$, so:  
$$ \lambda_0 = 5.3940 \times 10^{-7} \times 10^9 = 539.40 \text{ nm} $$  

**Step 7: Round to three significant figures**  
$539.40 \to 539$ (since $539.40$ rounds to $539$ with three significant figures).

## Answer
$$\boxed{539}$$

------
## Problem 2
##### Background
The photoelectric effect involves the emission of electrons from a material when exposed to electromagnetic radiation. According to quantum theory, each photon of frequency $\nu$ carries energy $h\nu$, where $h$ is Planck's constant. For electrons to be ejected, the photon energy must exceed the work function $\phi$ of the material—the minimum energy required to liberate an electron. The maximum kinetic energy of emitted electrons is given by $K_{\max} = h\nu - \phi$. This principle underlies technologies like photoelectric sensors and solar cells.  

When the light source is in motion relative to the target material, the observed frequency shifts due to the Doppler effect. For a source approaching a stationary observer at non-relativistic speeds, the observed frequency increases as $\nu = \nu_0 \left(1 + \frac{v}{c}\right)$, where $\nu_0$ is the rest frequency, $v$ is the relative speed, and $c$ is the speed of light. This frequency shift affects the photoelectron energy.

##### Knowledge Points Tested
1. Einstein's photoelectric equation: $K_{\max} = h\nu - \phi$.  
2. Doppler effect for electromagnetic waves (non-relativistic approximation).  
3. Energy conservation in photon-electron interactions.  

##### Intradisciplinary Connections
- Connects quantum mechanics (photoelectric effect) with wave optics (Doppler shift).  
- Reinforces energy quantization and photon-particle duality.  

##### Interdisciplinary Connections
- Aerospace engineering: Motion-induced frequency shifts in satellite communications.  
- Astronomy: Doppler measurements in stellar spectroscopy.  

##### Real-World Applications
- Precision sensors in spacecraft navigation, where relative motion affects laser-based measurements.  
- Dynamic calibration of photodetectors in high-speed industrial automation.  

##### Problem Statement
A spacecraft moves directly toward a stationary metal plate at speed $v$. The spacecraft emits a laser beam with rest frequency $\nu_0$. The metal has work function $\phi$. Derive an expression for the maximum kinetic energy $K_{\max}$ of photoelectrons ejected from the metal. Express $K_{\max}$ symbolically in terms of $h$ (Planck's constant), $c$ (speed of light), $\nu_0$, $\phi$, and $v$.

## Solution
The observed frequency $\nu$ of the laser light at the metal plate is affected by the Doppler shift. Since the spacecraft is moving toward the stationary plate, the frequency increases. For non-relativistic speeds ($v \ll c$), the Doppler formula is:  
$$ \nu = \nu_0 \left(1 + \frac{v}{c}\right) $$  

The maximum kinetic energy of photoelectrons follows from Einstein's photoelectric equation:  
$$ K_{\max} = h\nu - \phi $$  

Substitute the Doppler-shifted frequency $\nu$ into this equation:  
$$ K_{\max} = h \left[ \nu_0 \left(1 + \frac{v}{c}\right) \right] - \phi $$  

Simplify the expression:  
$$ K_{\max} = h\nu_0 \left(1 + \frac{v}{c}\right) - \phi $$  

This is the symbolic expression for the maximum kinetic energy of the photoelectrons.

## Answer
$$\boxed{ h\nu_{0}\left(1 + \frac{v}{c}\right) - \phi }$$

------
## Problem 3
##### Background
In the photoelectric effect, electrons are emitted from a metal surface when light of sufficiently high frequency strikes it. The minimum energy required to eject an electron is known as the work function ($W$) of the metal. In an experiment, the stopping potential $V_s$ is measured for different frequencies of incident light. The stopping potential is defined as the voltage needed to stop the most energetic photoelectrons.

##### Knowledge Points Tested
1. Einstein's photoelectric equation: $K_{\max} = hf - W$, where $K_{\max}$ is the maximum kinetic energy of the ejected electrons, $h$ is Planck's constant, $f$ is the frequency of the incident light, and $W$ is the work function.
2. The relationship between stopping potential and maximum kinetic energy: $K_{\max} = eV_s$, where $e$ is the elementary charge and $V_s$ is the stopping potential.

##### Intradisciplinary Connections
- Quantum physics: The photoelectric effect demonstrates the particle nature of light.
- Electricity: The stopping potential is related to the kinetic energy by the charge of the electron.

##### Interdisciplinary Connections
- Chemistry: The work function is related to the binding energy of electrons in atoms.
- Engineering: Photoelectric devices such as photodiodes and solar cells rely on this effect.

##### Real-World Applications
- Solar panels convert sunlight into electricity by the photoelectric effect.
- Digital cameras use image sensors that rely on the photoelectric effect to capture light.

##### Problem Statement
A researcher conducts a photoelectric effect experiment on an unknown metal. The following measurements are recorded:
- For light of frequency $f_1 = 6.00 \times 10^{14} \text{ Hz}$, the stopping potential is $V_{s1} = 0.500 \text{ V}$.
- For light of frequency $f_2 = 7.00 \times 10^{14} \text{ Hz}$, the stopping potential is $V_{s2} = 1.00 \text{ V}$.

The elementary charge is $e = 1.602 \times 10^{-19} \text{ C}$.

Derive an expression for the work function $W$ in terms of the given symbols: $f_1$, $f_2$, $V_{s1}$, $V_{s2}$, and $e$. Then, compute the numerical value of the minimum photon energy (which equals the work function) in joules. Round your final answer to three significant figures and express it in scientific notation.

Provide only the numerical value for the minimum photon energy in joules, without the unit.

## Solution
We start with Einstein's photoelectric equation and the relationship between the stopping potential and the maximum kinetic energy.

The photoelectric equation is:
$$ K_{\max} = h f - W $$

The maximum kinetic energy is related to the stopping potential by:
$$ K_{\max} = e V_s $$

Combining these, we have:
$$ e V_s = h f - W $$

We write this equation for the two measurements:

For frequency $f_1$ and stopping potential $V_{s1}$:
$$ e V_{s1} = h f_1 - W \quad \text{(1)} $$

For frequency $f_2$ and stopping potential $V_{s2}$:
$$ e V_{s2} = h f_2 - W \quad \text{(2)} $$

We have two equations with two unknowns: $h$ and $W$. We can solve for $W$ by eliminating $h$.

Subtract equation (1) from equation (2):
$$ e V_{s2} - e V_{s1} = (h f_2 - W) - (h f_1 - W) $$
$$ e (V_{s2} - V_{s1}) = h f_2 - W - h f_1 + W $$
$$ e (V_{s2} - V_{s1}) = h (f_2 - f_1) $$

Solve for $h$:
$$ h = \frac{e (V_{s2} - V_{s1})}{f_2 - f_1} $$

Now, substitute this expression for $h$ into equation (1) to solve for $W$:
$$ e V_{s1} = \left( \frac{e (V_{s2} - V_{s1})}{f_2 - f_1} \right) f_1 - W $$

Divide both sides by $e$ (assuming $e \neq 0$):
$$ V_{s1} = \frac{ (V_{s2} - V_{s1}) f_1 }{f_2 - f_1} - \frac{W}{e} $$

Solve for $W$:
$$ \frac{W}{e} = \frac{ (V_{s2} - V_{s1}) f_1 }{f_2 - f_1} - V_{s1} $$
$$ W = e \left( \frac{ (V_{s2} - V_{s1}) f_1 }{f_2 - f_1} - V_{s1} \right) $$

This is the expression for the work function in terms of the given symbols.

Now, we substitute the numerical values:
- $V_{s2} = 1.00 \text{ V}$
- $V_{s1} = 0.500 \text{ V}$
- $f_1 = 6.00 \times 10^{14} \text{ Hz}$
- $f_2 = 7.00 \times 10^{14} \text{ Hz}$
- $e = 1.602 \times 10^{-19} \text{ C}$

First, compute the differences:
$ V_{s2} - V_{s1} = 1.00 - 0.500 = 0.500 \text{ V} $
$ f_2 - f_1 = 7.00 \times 10^{14} - 6.00 \times 10^{14} = 1.00 \times 10^{14} \text{ Hz} $

Now, compute the term inside the parentheses:
$ \frac{ (V_{s2} - V_{s1}) f_1 }{f_2 - f_1} = \frac{ (0.500) \times (6.00 \times 10^{14}) }{1.00 \times 10^{14}} = \frac{3.00 \times 10^{14}}{1.00 \times 10^{14}} = 3.00 $

Then, subtract $V_{s1}$:
$ 3.00 - 0.500 = 2.50 $

Now, multiply by $e$:
$ W = (1.602 \times 10^{-19}) \times 2.50 = 4.005 \times 10^{-19} \text{ J} $

Rounding to three significant figures: $4.01 \times 10^{-19}$.

Therefore, the minimum photon energy required is $4.01 \times 10^{-19}$ joules.

## Answer
$$\boxed{4.01 \times 10^{-19}}$$

------
## Problem 4
##### Background
The photoelectric effect, first explained by Albert Einstein, demonstrates the particle-like nature of light. When light of sufficiently high frequency strikes a metal surface, electrons are ejected. The work function ($\phi$) is the minimum energy required to remove an electron from the metal. This experiment is fundamental to quantum mechanics and underpins technologies like solar cells and photodetectors.

##### Knowledge Points Tested
- The photoelectric effect equation: $K_{\text{max}} = h\nu - \phi$
- Relationship between frequency ($\nu$), wavelength ($\lambda$), and speed of light ($c$): $\nu = \frac{c}{\lambda}$
- Energy conservation and unit conversions (e.g., nanometers to meters, electronvolts to joules)

##### Intradisciplinary Connections
Connects to atomic physics (electron energy levels), wave-particle duality, and the quantization of electromagnetic radiation.

##### Interdisciplinary Connections
- **Chemistry**: Photoemission spectroscopy for material surface analysis.
- **Engineering**: Design of photovoltaic cells and optical sensors.
- **Environmental Science**: Efficiency of solar energy conversion.

##### Real-World Applications
- **Solar Panels**: Convert sunlight to electricity via electron ejection in semiconductor materials.
- **Digital Imaging**: Charge-coupled device (CCD) sensors in cameras use the photoelectric effect to detect light.
- **Night Vision Devices**: Photocathodes eject electrons when exposed to low-intensity infrared radiation.

##### Problem Statement
In a photoelectric effect experiment, light of wavelength $300 \text{ nm}$ is incident on a metal surface, ejecting electrons with a maximum kinetic energy of $1.8 \text{ eV}$. Determine the work function $\phi$ of the metal in eV. Use the following physical constants:  
- Planck's constant $h = 4.135667696 \times 10^{-15} \text{ eV·s}$  
- Speed of light $c = 2.99792458 \times 10^8 \text{ m/s}$  

Derive the expression for $\phi$ from fundamental principles before numerical substitution. Express your final answer as a numerical value rounded to two significant figures. Do not include the unit in the box.

## Solution
The photoelectric effect equation is derived from energy conservation. The maximum kinetic energy ($K_{\text{max}}$) of an ejected electron equals the photon energy minus the work function ($\phi$):  
$$ K_{\text{max}} = h\nu - \phi $$  
The frequency ($\nu$) is related to the wavelength ($\lambda$) and speed of light ($c$) by:  
$$ \nu = \frac{c}{\lambda} $$  
Substitute this into the photoelectric effect equation:  
$$ K_{\text{max}} = \frac{hc}{\lambda} - \phi $$  
Solve for $\phi$:  
$$ \phi = \frac{hc}{\lambda} - K_{\text{max}} $$  
Now substitute the given values:  
- $\lambda = 300 \text{ nm} = 300 \times 10^{-9} \text{ m} = 3.00 \times 10^{-7} \text{ m}$  
- $K_{\text{max}} = 1.8 \text{ eV}$  
- $h = 4.135667696 \times 10^{-15} \text{ eV·s}$  
- $c = 2.99792458 \times 10^8 \text{ m/s}$  

First, compute $hc$:  
$$ hc = (4.135667696 \times 10^{-15} \text{ eV·s}) \times (2.99792458 \times 10^8 \text{ m/s}) = 1.239841984 \times 10^{-6} \text{ eV·m} $$  
Next, compute $\frac{hc}{\lambda}$:  
$$ \frac{hc}{\lambda} = \frac{1.239841984 \times 10^{-6} \text{ eV·m}}{3.00 \times 10^{-7} \text{ m}} = 4.132806613 \text{ eV} $$  
Now solve for $\phi$:  
$$ \phi = 4.132806613 \text{ eV} - 1.8 \text{ eV} = 2.332806613 \text{ eV} $$  
Round to two significant figures: $2.3 \text{ eV}$.

## Answer
$$\boxed{2.3}$$

------
