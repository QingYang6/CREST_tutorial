# CREST tutorial

Instructor: Qing Yang, qing.2.yang@uconn.edu

Tutorial for CREST version 3.0, focusing on hydrologic modeling operation, including the following lessons:

## Lesson 1: Introduction to CREST

[`Introduction`](./CREST_Introduction.pdf)

CREST flood warning on NCM:

[`CREST flood warning`](http://weathermodels.ncm.gov.sa/ffg.php?model=CREST&variable=quantile)

## Lesson 2: Files preparation

To prepare the necessary files for CREST, follow the steps outlined in the notebook.

[`Files_prepare.ipynb`](./Files_prepare.ipynb)

## Lesson 3: Set up new project

Upload the input files to WeMET, and set up a new project.

Control files for the CREST project:

[`.prject file`](./control_file_template/project_file.md)

[`forcing control file`](./control_file_template/forcing_control_file.md)

[`parameters file`](./control_file_template/parameters_file.md)

[`InitialConditions file`](./control_file_template/InitialConditions_file.md)

[`calibrations file`](./control_file_template/calibrations_file.md)

## Lesson 4: Run CREST and calibration

After conducting the routing step, we can move forward to calibration.

Submit the [`demo_cali.sh`](./demo_project/demo_cali.sh) through server terminal.

Result visualize and parameter sensitivity analysis:

[`Hydrograph_visualizer.ipynb`](./Hydrograph_visualizer.ipynb)

## Lesson 5: Visualize through Web

Template of building a website for CREST output:

[`CREST_Web_cookbook`](./Flood_quantile_web.ipynb)

[CREST_Web_Test](./demo_project/test_crest_out.html)

### CREST manual
[`CREST v3`](./manual/CREST_User_Manual_v3.pdf)
[`CREST v2.1.3`](./manual/CREST_User_Manual_v2_1_3.pdf)
