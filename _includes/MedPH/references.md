<div markdown="1">

You can visit these pages to find general information on many diseases and specific information about recent outbreaks:

- [US Centers for Disease Control and Prevention](http://www.cdc.gov/DiseasesConditions)
- [ProMED mail](http://www.promedmail.org) - a list serve about disease outbreaks
- [WHO disease outbreak site](http://www.who.int/csr/don/en/index.html)
- [Research and Policy for Infectious Disease Dynamics (RAPIDD program)](http://scholar.google.com/citations?hl=en&user=ngDeGF8AAAAJ) - publications on the dynamics of infectious diseases, with a emphasis on data-driven modeling methods
- [Project Tycho](http://www.tycho.pitt.edu/) - long-term data sets on many infectious diseases in the US

### For groups working on Measles

Measles data to be used in the projects are made available courtesy of **Professor David Earn, Department of Mathematics, McMaster University**. The data files are available online from the International Infectious Disease Data Archive (IIDDA, <http://iidda.mcmaster.ca>). **Note that use of these data is only permitted for the purposes of this course, and any outside use must receive prior approval from Prof. Earn.** These data were originally analyzed in the following two publications:

- [D. J. D. Earn; P. Rohani; B. M. Bolker; B. T. Grenfell (2000) A simple model for complex dynamical transitions in epidemics Science 287(5453): 667-670.]({{page.repo}}/blob/master/references/Earn2000.pdf?raw=true)
- [C. T. Bauch and D. J. D. Earn (2003) Transients and Attractors in Epidemics. Proceedings of the Royal Society of London Series B 270:1573-1578.]({{page.repo}}/blob/master/references/Bauch2003.pdf?raw=true)

### For groups working on London data

- All available data from London ([download]({{page.repo}}/blob/master/projectData/dataLondon_all.Rdata?raw=true))

### For groups working on US data

This paper gives a nice explanation of the relationship between infectious disease population parameters and the periodicity of the expected limit cycle:

- [Dushoff, J, Plotkin, JB, Levin, SA, & Earn, DJD (2004). Dynamical resonance can account for seasonality of influenza epidemics. _Proceedings of the National Academy of Sciences of the United States of America_, 101(48), 16915–6. <doi:10.1073/pnas.0407293101>]({{page.repo}}/blob/master/references/Dushoff2004.pdf?raw=true)

- All available data from the US ([download]({{page.repo}}/blob/master/projectData/dataUS_all.Rdata?raw=true))

### For groups working on Ebola

- WHO Ebola Response Team. [Ebola Virus Disease in West Africa - The First 9 Months of the Epidemic and Forward Projections]({{page.repo}}/blob/master/references/EbolaFirst9Months.pdf?raw=true). N Engl J Med 2014.
- Chowell G, Hengartner NW, Castillo-Chavez C, Fenimore PW, Hyman JM. [The basic reproductive number of Ebola and the effects of public health measures: The cases of Congo and Uganda]({{page.repo}}/blob/master/references/ChowellEbola2004.pdf?raw=true). J Theor Biol 2004; 229: 119–26.
- Bellan SE, Pulliam JRC, Dushoff J, Meyers LA. [Ebola control: effect of asymptomatic infection and acquired immunity]({{page.repo}}/blob/master/references/BellanAsymptomaticEbola2014.pdf?raw=true). Lancet 2014. (accompanying [SEIR model code](http://ebola.ici3d.org/Lancet/ebolaSEIR.R))
- [Kucharski et al. (2015). Measuring the impact of Ebola control measures in Sierra Leone. PNAS.]({{page.repo}}/blob/master/references/KucharskiPNAS2015.pdf)

### Data Sets

#### Ebola in West Africa

- **Liberia 2014-2016 Ebola Epidemic<sup>1</sup>** ([download figures]({{page.repo}}/blob/master/projectData/LiberiaEVD.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/WAevddat.Rdata?raw=true))
- **Sierra Leone 2014-2016 Ebola Epidemic<sup>1</sup>** ([download figures]({{page.repo}}/blob/master/projectData/SLEVD.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/WAevddat.Rdata?raw=true))
- **Guinea 2014-2016 Ebola Epidemic<sup>1</sup>** ([download figures]({{page.repo}}/blob/master/projectData/GuineaEVD.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/WAevddat.Rdata?raw=true))

<sup>1</sup> Data from the [Humanitarian Data Exchange](https://data.humdata.org/dataset/rowca-ebola-cases) and cleaned by Steve Bellan.

#### Other data sets

- **London<sup>1</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/figsLondon.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/dataLondon.Rdata?raw=true))
- **Zaire 1976 Ebola Epidemic<sup>2</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/figsZaireEbola.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/dataZaireEbola.Rdata?raw=true))
- **Nigeria Lassa Fever Epidemic<sup>3</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/figsNigeriaLF.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/dataNigeriaLF.Rdata?raw=true))
- **Democratic Republic of Congo Ebola Epidemic<sup>4</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/figsDRC_Ebola.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/dataDRC_Ebola.Rdata?raw=true))

<sup>1</sup> Data made available courtesy of **Prof. David Earn, Dept. of Mathematics, McMaster University**. The data files are available online from the International Infectious Disease Data Archive (IIDDA, <http://iidda.mcmaster.ca>) and were first published in either *D. J. D. Earn; P. Rohani; B. M. Bolker; B. T. Grenfell (2000) A simple model for complex dynamical transitions in epidemics Science 287(5453): 667-670.* or *C. T. Bauch and D. J. D. Earn (2003) Transients and Attractors in Epidemics. Proceedings of the Royal Society of London Series B 270:1573-1578.* **Note that use of these data is only permitted for the purposes of this course, and any outside use must receive prior approval from Prof. Earn.**

<sup>2</sup> Data from [Camacho a., Kucharski a. J, Funk S, Breman J, Piot P, Edmunds WJ. Potential for large outbreaks of Ebola virus disease. Epidemics 2014](http://linkinghub.elsevier.com/retrieve/pii/S1755436514000528) supplementary material and cleaned by Becky.

<sup>3</sup> Data made available courtesy of **Dr. Caitlin Rivers, Johns Hopkins Center for Health Security** (https://github.com/cmrivers/ebola_drc) GitHub repository and cleaned by Becky. The original data files are available online from the WHO Disease Outbreak Network ( <http://www.who.int/csr/don/en/>), WHO situation reports (<http://www.who.int/ebola/situation-reports/drc-2018/en/>), and the DRC Ministry of Health mailing list.

<sup>4</sup> Data made available courtesy of **Dr. Simon Frost, Dept of Veterinary Medicine, University of Cambridge** (https://github.com/sdwfrost/nigeria-lassa-data) GitHub repository and cleaned by Becky.

### Code that groups might find useful

- [Example ODE weekly incidence code ](https://raw.githubusercontent.com/ICI3D/RTutorials/master/seir_cumInc.R)

### Poster examples from previous years

- [2014 Example]({{page.repo}}/blob/master/projectData/KathleenKagisoPoster.pdf?raw=true)
- [2015 Example]({{page.repo}}/blob/master/projectData/WhoopingCoughOntario2.pdf?raw=true)

</div>
