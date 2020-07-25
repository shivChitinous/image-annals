README

Module 9 has two components - 1. constructing a training dataset of objects which have been manually identified as bacteria
or non-bacteria and training an SVM classifier on this 2. testing this classifier on a testing dataset.

1. TRAINING
To do this, the module_9_training.ipynb notebook contains a gui for pointing and selecting objects. 
The bacterial_colonies folder contains three .csv files - bacterial_colony_1.csv, bacterial_colony_3.csv
and bacterial_colony_5.csv that contain the index of the labelled object, their eccentricity and area as well as their classification. This was done using the point-and-select gui. The bacterial_

It also contains one .csv file that has NOT been manually classified - bacterial_colony_7.csv.

An SVM classifier was constructed using MATLAB's Classification Learner toolbox (SVM model type - optimizable). This is stored in the train-test.mat file (accuracy on training set - 95%) in the bacterial_colonies folder. 

The training data for this classifier consisted of bacterial_colony_1.csv and bacterial_colony_5.csv (look at SVM.mlx live script for details).

2. TESTING
To test the classifier, it was run on two csv files - bacterial_colony_3.csv as well as bacterial_colony_7.csv. In the first case, we can actually compare the performance of the SVM classifier with manual classification (as shown in module_9_testing.ipynb). In the second case, we can only observe by eye and feel good/bad about our classifier. 

Note:
The gui can be used to manually classify other plates.
The bacterial_colony folder also contains a zipped folder 'labelled_colonies.zip'. Extract labelled images from this in the form of .csv files (ex: labelled_colony_1.csv can be imported as an image as in module_9_testing.ipynb).
Plates folder contains seven images of bacterial culture plates.
