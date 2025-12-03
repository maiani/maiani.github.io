---
title: "Master thesis projects"
date: 2025-12-03T08:30:00
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

### 1. Probing the quantum energy landscape of a superconducting qubit
Superconducting qubits rely on Josephson junctions—tiny nonlinear elements whose properties ultimately shape how well a qubit behaves. In theory these junctions create a simple cosine-shaped potential. In practice, real devices often carry small imperfections, such as higher harmonics in the potential, that subtly change the qubit’s energy levels and dynamics.

Once the junction sits inside a transmon circuit, these imperfections can no longer be studied with standard DC techniques. Instead, they must be inferred indirectly, through microwave spectroscopy and time-domain measurements. This project explores how well a transmon can reveal such hidden features in its own potential.

You will model how a small second-harmonic contribution affects the qubit's energy landscape and determine how easily it can be detected through different measurement protocols. Tools from quantum metrology, especially the quantum Fisher information, provide a way to quantify how distinguishable two slightly different potentials are. By comparing this ideal sensitivity with what realistic measurements can extract, the project highlights which experiments are most effective at uncovering microscopic imperfections.

**What you can expect from this project**
- Learn how the Josephson potential shapes the behaviour of a transmon qubit.
- Model how small deviations from the ideal potential influence spectra and time evolution.
- Use quantum-estimation tools to assess how much information different measurements can reveal.
- Simulate realistic protocols such as Ramsey and Rabi experiments to evaluate their sensitivity.
- Develop skills in numerical modelling, circuit quantum electrodynamics, and data analysis.

**References:**
- A. Blais et al., Circuit Quantum Electrodynamics, Rev. Mod. Phys. 93, 025005 (2021)
  
### 2. Exploring quantum point contacts with neural networks

Quantum point contacts (QPCs) are a central platform for studying how confinement and interactions shape electronic transport. Their quantized conductance is well understood in non-interacting models, yet interaction-driven phenomena—such as the 0.7 anomaly and the formation of quasi-localized states—remain challenging to capture with conventional techniques.

This project uses neural-network variational Monte Carlo (NNVMC) to investigate QPCs from a many-body perspective. Neural-network wave functions offer a flexible way to approximate correlated states in low-dimensional geometries, making them well suited for studying interacting electrons in constrictions. By combining NNVMC with transport diagnostics such as flux-twist energetics and the Drude weight, we will explore how interactions modify the ground state and how these modifications relate to transport behavior.

The project blends theory and computation: you will learn the essential physics of QPCs, implement and train neural-network wave functions, and extract observables relevant to transport. This provides a strong introduction to machine-learning-assisted quantum simulations and their use in mesoscopic physics.

**What you can expect from this project:**

- Understand QPC physics in both non-interacting and interacting regimes.
- Learn the core ideas of variational Monte Carlo and neural-network quantum states.
- Implement and train neural-network ansätze for confined geometries.
- Compute quantities such as the Drude weight to probe transport properties.
- Gain experience in numerical optimization, Monte Carlo sampling, and GPU-based computation.

**References:**
- A. Avodoshkin, M. Geier, and L. Fu, An integrated neural wavefunction solver for spinful Fermi systems, [https://arxiv.org/abs/2510.18621](https://arxiv.org/abs/2510.18621)

### 3. Simulation of Diffusive Superconductors

The Usadel equations are a powerful model for describing diffusive superconductors. These equations are particularly efficient for modeling inhomogeneous systems out of equilibrium, including effects of magnetism and spin-orbit coupling, while remaining computationally affordable. This makes them an ideal framework for studying mesoscopic superconducting devices.

In a previous project, I developed pyUsadel, a Python package designed to solve 2D problems in equilibrium settings. For future work, we aim to rewrite the package within a finite-element framework. This will allow us to handle more complex geometries and extend the tool's capabilities to support multicomponent superconductors and non-equilibrium setups. An improved tool could significantly benefit the development of superconducting quantum devices. We will then use this tool to simulate how percolative superconductivity arise in superconductor-ferromagnet heterostructures. 

This project not only aims to advance the computational tools available for studying superconducting systems but also provides a comprehensive learning experience in computational physics, software engineering, and high-performance computing. 

**What you can expect from this project:**

- Develop a deep understanding of the Usadel equations and their significance in the study of superconductors.
- Learn and apply Finite Element Modeling techniques to solve complex differential equations.
- Gain experience in scientific computing and software development, focusing on efficiency and extensibility.
- Enhance your programming skills, particularly in Python, and learn how to develop and maintain scientific software packages.
- Experience the workflow of HPC environments, including job scheduling, parallel computing, and performance optimization.

**References:**

1. Maiani, *pyUsadel* [Github Repo](https://github.com/maiani/pyusadel)
2. Maiani et al, *Percolative supercurrent in superconductor-ferromagnetic insulator bilayers*, [https://arxiv.org/abs/2404.17320](https://arxiv.org/abs/2404.17320)
