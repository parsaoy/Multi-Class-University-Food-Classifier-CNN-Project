## Multi-Class University Food Classification using transfer learning (MobileNetV2) with CNN

### Quick Overview
In this project, I used the MobileNetV2 architecture to classify images of our University’s daily dishes using CNN.

I had a dataset comprising of only 190 food images and I needed to train a model to classify them into 9 different categories of food. Due to the small size of my dataset, I had to use a lot of data augmentation techniques to generate more training samples and make the dataset richer.

Due to the high imbalance of data, I balanced the weights based on the number of data points in each class.

### Implementation

I first loaded the pre-trained MobileNetV2 model and checked the input shape size, which was 224x224. Then, I loaded all layers except for the top FC layers. After that, I froze all the layers and added my own top layers, which were as follows:
>* AveragePooling 
>* FC: 256, relue, L2 regularizer
>* Dropute: 0.6
>* FC: 32, relu
>* FC: 9, softmax

After instantiating an image data generator, I included various data augmentation features:
>* zooming
>* shearing
>* vertical & horizontal Flipping
>* brightness changing
>* color channels shifting
>* rotating

I trained a model using various training and development data generators with different parameters, and ran them through my model for multiple epochs. Due to the large number of augmented images in the training process, it was difficult to fit the model, resulting in high accuracy on the validation set. As a result, I frequently obtained higher accuracy on the validation set than on the training set.

*In the end, I achieved somehow excellent results with my augmented training generator images. The accuracy was around 92%, and the accuracy on the validation dataset was roughly 100%.*


----
### Final Results on Train Image Generator with Data Augmentation:


<img src="https://github.com/parsaoy/Multi-Class-University-Food-Classifier-CNN-Project/blob/master/README%20images/Final%20Results.jpeg?raw=true" alt="Sample Image" width="710" height="430">


### Model Evaluation on Train Image Generator with Data Augmentation


<img src="https://github.com/parsaoy/Multi-Class-University-Food-Classifier-CNN-Project/blob/master/README%20images/Evaluation.jpeg?raw=true" alt="Sample Image" width="300" height="400">