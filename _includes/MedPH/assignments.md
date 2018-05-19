<div markdown="1">

### Major Assignments

There will be two major assignments for this course, a group poster presentation (given during the MMED Clinic) and a final written project (due June 14).

### Academic Integrity and Plagiarism

All sources for information, figures, and wording must be properly cited. Before submitting any assignments for this class, please **review the following**:

- [Stellenbosch guidelines on academic integrity](https://www.sun.ac.za/english/research-innovation/Research-Development/Documents/Policies%20and%20Guidelines/ENGLISH/SU%20Plagiarism%20Policy_2016.pdf)
- Examples of plagiarism versus acceptable paraphrasing and summarizing
  1.  [1st](http://www.lib.usm.edu/legacy/plag/paraphrasing.php)
  2.  [2nd](https://integrity.mit.edu/handbook/academic-writing/avoiding-plagiarism-paraphrasing)
  3. [3rd](http://writing.wisc.edu/Handbook/QPA_paraphrase.html)

### Group poster project

Examples from previous years

- [2014 Example]({{page.repo}}/blob/master/projectData/KathleenKagisoPoster.pdf?raw=true)
- [2015 Example]({{page.repo}}/blob/master/projectData/WhoopingCoughOntario2.pdf?raw=true)

[Example EVD plotting code]({{page.repo}}/blob/master/projectData/examplePlottingCode.R?raw=true)n

[Example ODE weekly incidence code ](https://raw.githubusercontent.com/ICI3D/RTutorials/master/seir_cumInc.R)

#### Data Sets

- Poster projects will be completed in groups, TBD:
    1. **London<sup>1</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/figsLondon.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/dataLondon.Rdata?raw=true))
    2. **Zaire 1976 Ebola Epidemic<sup>2</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/figsZaireEbola.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/dataZaireEbola.Rdata?raw=true))
    3. **Liberia 2014-2016 Ebola Epidemic<sup>3</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/LiberiaEVD.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/WAevddat.Rdata?raw=true))
    4. **Sierra Leone 2014-2016 Ebola Epidemic<sup>3</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/SLEVD.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/WAevddat.Rdata?raw=true))
    5. **Guinea 2014-2016 Ebola Epidemic<sup>3</sup>:** ([download figures]({{page.repo}}/blob/master/projectData/GuineaEVD.pdf?raw=true), [download data]({{page.repo}}/blob/master/projectData/WAevddat.Rdata?raw=true))

<sup>1</sup> Data made available courtesy of **Prof. David Earn, Dept. of Mathematics, McMaster University**. The data files are available online from the International Infectious Disease Data Archive (IIDDA, <http://iidda.mcmaster.ca>) and were first published in either *D. J. D. Earn; P. Rohani; B. M. Bolker; B. T. Grenfell (2000) A simple model for complex dynamical transitions in epidemics Science 287(5453): 667-670.* or *C. T. Bauch and D. J. D. Earn (2003) Transients and Attractors in Epidemics. Proceedings of the Royal Society of London Series B 270:1573-1578.* **Note that use of these data is only permitted for the purposes of this course, and any outside use must receive prior approval from Prof. Earn.**

<sup>2</sup> Data from [Camacho a., Kucharski a. J, Funk S, Breman J, Piot P, Edmunds WJ. Potential for large outbreaks of Ebola virus disease. Epidemics 2014](http://linkinghub.elsevier.com/retrieve/pii/S1755436514000528) supplementary material and cleaned by Becky.

<sup>3</sup> Data from the [Humanitarian Data Exchange](https://data.humdata.org/dataset/rowca-ebola-cases) and cleaned by Steve.

#### Instructions

- **Step I:** Download the figures summarizing the data that your group will be working with. Each group member should pick one figure to focus on for this step. For the chosen figure, describe (in writing) what you see in the data. Do you notice any patterns? Over what timescale do these patterns occur. Then compare notes with your group members - do the data in their figure show similar or different patterns? As a group, think about what may be causing the patterns you see and the similarities and differences between data sets.
- **Step II:** As a group, learn about the natural history of the pathogens for which your group has data, documenting where you find each piece of information. Does this give you a better idea for where the pattern/s come from? Also learn about prevention and control options, and the history of their implementation, again documenting where you find each piece of information - does this give you a better idea for where the pattern/s come from? Does this help your understand the different patterns observed for different pathogens in your time period/location?
    - NOTE: You may find the references tab useful for this step. You may also want to search the scientific literature or access additional references cited on the pages below. If you are looking for a paper but don't have access, let Steve or Becky know and they may be able to access it for you. If so, they'll post it in the [readings folder of the course repository]({{page.repo}}/blob/master/readings).
- **Step III:** As a group, develop a research question based on a pattern observed in one or more of the time series datasets.
- **Step IV:** Figure out how to use a mechanistic infectious disease transmission model (ie, an SIR or SEIR type model) to address your research question. Remember that the type of model you use will depend on your research question, and you should try to use the simplest model possible that allows you to address your question. For example, if you are interested in what drives the period of observed cycles (and changes in the period over time), you will likely need to use a model that includes seasonal dynamics); however, if you're interested in comparing the relative incidence of different diseases in the same population at the same point of time, you may be able to use a non-seasonal model.
- **Step V:** Develop and implement a research plan to address your research question through a combination of data analysis and model development.
- **Step VI:** Use the [poster template]({{page.repo}}/blob/master/assignments/PosterTemplate.pptx) to design a poster on your project. Be sure to include background information, your research question, a description of your approach, your results, your conclusions, and next steps/further questions.

### Final written project

- [Project instructions](./Project_guidelines_2017.pdf) "Guidelines for the final project")
- Your final project can be based on your poster project or your MMED group project. You will have lot of free time during the last week of MMED to write this.
- A list of suggested topics for MMED group projects is available at [on this page]({{ site.url }}/projects).

- [Example written project]({{page.repo}}/blob/master/assignments/LourensTrachoma2013.pdf?raw=true)

### For Tuesday

- Read the measles paper in detail
- Skim the rabies paper
- Finish Tutorial 1

### For Wednesday

- Complete Tutorial 2
    - **Submit answers to Tutorial 2, Questions 3 and 4 by email to Zinhle at zinhle@aims.ac.za**
- Read Hampson et al. 2009 ([Rabies]({{page.repo}}/blob/master/readings/Hampson2009.pdf?raw=true)) – due Wed AM
- Steps I and II for poster projects – due Wed PM

### For Thursday

- Complete Tutorial lab 3
    - **Submit answer to Tutorial 3, Question 3 by email to Zinhle** – due Sunday PM
- Steps III and IV for poster project development – due Thurs AM
- Begin poster planning

### For Friday

- Complete Tutorial lab III
    - **Submit answer to Tutorial 3, Question 3 by email to Zinhle** – due Sunday PM
- Continue project development
- Prepare poster presentation – first draft due Fri AM

### For Saturday

- Finish poster revision based on feedback and additional practice presentations (as needed)
- (Saturday is a free day for those whose poster and presentation are finalized by the end of the day on Friday)

Readings
========

- [Panum's Investigation of the 1846 Measles Outbreak on the Faroe Islands](./panum.html)
- [Hampson *et al*. 2009]({{page.repo}}/blob/master/readings/Hampson2009.pdf?raw=true)

</div>
