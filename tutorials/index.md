---
layout: page
title: Tutorials
tab: Tutorials
longtitle: ICI3D Tutorials
summary: R tutorials and labs from the MMED and DAIDD clinics.
parent: Resources
alerttype: warning
alertmsg: Instructional materials are available under a <a href="http://creativecommons.org/licenses/by/4.0/"> CC-BY International License</a> unless otherwise stated.
---

## Tutorials

- Tutorial 0: [Introduction to R Studio](https://raw.githubusercontent.com/ICI3D/RTutorials/master/introRstudio.R) - provides an introduction to the user interface
- Tutorial 1: [Introduction to R and its quirks](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_RTutorial_1.R)
- Tutorial 2: [More on Vectors, Data Frames, and Functions](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_RTutorial_2.R)
- Tutorial 3: [Probability Distributions and Control Structures](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_RTutorial_3.R)
- Tutorial 4: [Visualizing Infectious Disease Data in R](www.ici3d.org/MMED/visualizeData)
- Tutorial 5: [Data cleaning and management in R](www.ici3d.org/MMED/dataCleaning)

## ICI3D R package

- This package contains interactive tutorials used at the MMED and DAIDD Clinics; to install, run the following lines of code from the R or Rstudio command line:

<div class="row">
<div class="col-lg-1">
</div>
<div class="col-lg-10">
{% highlight r %}

install.packages('remotes') # if not already installed
remotes::install_github('ICI3D/ici3d-pkg') # BEFORE RUNNING THIS MAKE SURE YOUR R VERSION IS 3.5 OR HIGHER

{% endhighlight %}
</div>
<div class="col-lg-1">
</div>
</div>

## Labs

- Lab 1: [ODE models in R](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab1_ODEmodels.R)
- Lab 2: [Consequences of heterogeneity](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab2_Heterogeneity.R)
    - [Download data file](https://raw.githubusercontent.com/ICI3D/RTutorials/master/HetSIR_functions.Rdata)
    - Note that a newer version of this tutorial is also available through the ICI3D R package. To get started, run the following command at the R Studio command line (after installing the ICI3D package):

<div class="row">
<div class="col-lg-1">
</div>
<div class="col-lg-10">
{% highlight r %}

ICI3D::heterogeneityTutorial()

{% endhighlight %}
</div>
<div class="col-lg-1">
</div>
</div>

- Lab 3: [Study Design in Epidemiology lab](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab3_EpiStudyDesign.R)
- Lab 4: [Study Design for Clinical Trials](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab4_RCT.R)
    - [Download data file](https://github.com/ICI3D/datasets/blob/master/clinicalTrials/MuTxT.Rdata?raw=true)
- Lab 5: [Introduction to Likelihood](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab5_introLikelihood.R)
- Lab 6: [MLE fitting of a dynamic model](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab6_MLE_SIV_HIV.R)
- Lab 7: [MCMC fitting of a binomial distribution](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab7_MCMC-Binomial.R)
- Lab 8: [MCMC fitting of a dynamic model](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Lab8_MCMC-SI_HIV.R)
    - **Note:** Download [this file](https://raw.githubusercontent.com/ICI3D/RTutorials/master/MCMC_SI_runs.Rdata) to avoid having to wait for long MCMC chains to be sampled.

## Exercises and Examples

- Exercise 1: [Basic stochastic simulation models](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_spillover_introductions.R) - Stochastic spillover
- Exercise 2: [Basic stochastic simulation models](https://raw.githubusercontent.com/ICI3D/RTutorials/master/SimpleStochastic/SimpleStochastic.R) - Demographic stochasticity
- [Stochastic SIR Example - Gillespie Algorithm](./gillespie)
- [Stochastic SIR Example - Chain Binomial](https://raw.githubusercontent.com/ICI3D/RTutorials/master/ICI3D_Example_chainBinom.R)
