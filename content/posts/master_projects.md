---
title: "Master thesis projects"
date: 2024-06-16T08:30:00
description: Master thesis projects
menu:
  sidebar:
    name: Master thesis projects
    identifier: master
    weight: 10
tags: []
categories: []
---

In this page you can find a list of Master thesis project avaialble.
Please contact me if you are interested in working on one of these topic or if you have other ideas you 
want to pursue together.

### 1. Multiterminal Josephson Effects with Floquet Scattering Matrices

Josephson junctions are fundamental components in the realm of superconducting quantum electronics and quantum computing, primarily due to the DC Josephson effect, which produces the nonlinear inductance necessary for qubit operation.

The AC Josephson effect, a dynamic counterpart of the DC effect, occurs when a finite voltage applied to a junction induces an alternating current (AC). The mechanisms underlying the AC Josephson effect are less straightforward compared to those of the DC Josephson effect, resulting in a theory that is not easily generalizable.

This project aims to reformulate the theory of the Josephson effects by utilizing Floquet scattering matrices. This novel approach is expected to yield a simpler, more generalizable framework. Initially, we will develop a foundational model using these matrices to understand the simple case of a normal junction. Subsequently, the model will be applied to analyze junctions constructed from unconventional materials, multiterminal junctions, and finally general superconducting circuits.

The successful execution of this project could lead to significant advancements in the understanding and application of Josephson junctions in quantum technologies. The expected duration is one academic year and is aimed at writing a paper. The project may include a strong numerical part depending on the direction we choose to follow.

**What you can expect from this project:**

- An extensive introduction to superconductor nanoelectronics.
- Learn the language of Floquet scattering matrices for the description of quantum transport.
- Understand how to develop a new method for a known problem, and how to apply a known method to a new unknown problem.

**References:**

1. *Scattering Matrix Approach to Non-Stationary Quantum Transport*, Michael V Moskalets
2. Pankratova, Natalia, et al. "Multiterminal josephson effect." *Physical Review X* 10 031051 (2020)

### 2. Vortices in Altermagnetic Superconductors

Altermagnets are a newly discovered form of magnetic order, similar to antiferromagnets, that do not preserve Kramers degeneracy and show staggered magnetism both in real-space and in momentum-space. After being proposed theoretically, signatures of altermagnetism have been observed in some oxides.

Because of this peculiar spin-split band structure, altermagnetism holds the promise of new intriguing phenomena when put in contact with superconductors. Can we create synthetic unconventional superconducting pairing by combining these two materials? Can we use altermagnetism as a new tool in synthetic topological quantum matter?

In this project, you will try to answer these questions. In particular, we will focus on magnetic vortices in altermagnetic superconductors. The project will be mainly numerical; we will develop a Bogoliubov-De Gennes (BdG) model and study tight-binding simulations.

**What you can expect from this project:**

- Develop a thorough understanding of the Bogoliubov-de Gennes (BdG) methods, exact diagonalization techniques, and the Kernel Polynomial Method.
- Study Abrikosov vortex physics in the context of altermagnetic superconductors
- Learn how to write efficient numerical software, and the basics of scientific software engineering.
- Get hands-on experience with High Performance Computing (HPC).
- This project is part of an international collaboration on altermagnetic superconductors.

**References:**

1. Mazin, *Altermagnetism—A New Punch Line of Fundamental Magnetism* [https://doi.org/10.1103/PhysRevX.12.040002](https://journals.aps.org/prx/edannounce/10.1103/PhysRevX.12.040002)
2. Ouassou et al, *dc Josephson Effect in Altermagnets*, Phys. Rev. Lett. **131**, 076003 [https://arxiv.org/abs/2301.03603](https://arxiv.org/abs/2301.03603)


### 3. Numerical solution of the Usadel equations for diffusive superconductors.

The Usadel equations are a powerful model for describing diffusive superconductors. These equations are particularly efficient for modeling inhomogeneous systems out of equilibrium, including effects of magnetism and spin-orbit coupling, while remaining computationally affordable. This makes them an ideal framework for studying mesoscopic superconducting devices.

In a previous project, I developed pyUsadel, a Python package designed to solve 2D problems in equilibrium settings. For future work, we aim to rewrite the package within a finite-element framework. This will allow us to handle more complex geometries and extend the tool's capabilities to support multicomponent superconductors and non-equilibrium setups. An improved tool could significantly benefit the development of superconducting quantum devices.

This project not only aims to advance the computational tools available for studying superconducting systems but also provides a comprehensive learning experience in computational physics, software engineering, and high-performance computing.

**What you can expect from this project:**

- Develop a deep understanding of the Usadel equations and their significance in the study of superconductors.
- Learn and apply Finite Element Modeling techniques to solve complex differential equations.
- Gain experience in scientific computing and software development, focusing on efficiency and extensibility.
- Enhance your programming skills, particularly in Python, and learn how to develop and maintain scientific software packages.
- Experience the workflow of HPC environments, including job scheduling, parallel computing, and performance optimization.

**References:**

1. Maiani, *pyUsadel* [Github Repo](https://github.com/maiani/pyusadel)
2. Maiani et al, *Percolative supercurrent in superconductor-ferromagnetic insulator bilayers*, arXiv:2404.17320 [https://arxiv.org/abs/2404.17320](https://arxiv.org/abs/2404.17320)
