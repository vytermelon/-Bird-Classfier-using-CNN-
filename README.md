# -Bird-Classfier-using-CNN-
Using Convolutional neural networks ,ten species of birds are classified.


Step1: Download the dataset
https://www.kaggle.com/gpiosenka/100-bird-species
You can use this labelled 2 Gb dataset or your own, although this has 100+ species we will only need ten.

Step2: Data Augmentation

After downloading, you will notice that each species only contains around 150 pictures. This number is insufficient for your CNN model to train on.
The "IMGAUGMENT.ipynb" file can be used to replicate each and every picture with some changes such as rotation/ padding/crop/cutout.
From 150 images per species, you will now have around 150 x 13 =1950 images. It is advised to have at least 1k images per species.
It is also better to have 7-10 images in your Validation dataset rather than just 5.

Step3: Load Dataset
Use "birddata.py" to convert images to arrays(64,64,3) x_train,y_train,x_test, y_test and load them into "BIRDS.ipynb".

Step: Train and Test your model.
"BIRDS.ipynb"
