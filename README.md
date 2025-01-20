# NN Image Classifier
*Neural Network Image Classifier*

A short project to get familiar with the MobileNet neural network model.
I tweaked and trained the model to classify images into 10 types of fruit.

<img src="https://firebasestorage.googleapis.com/v0/b/creatoratnight-babdb.appspot.com/o/images%2F68747470733a2f2f63726561746f7261746e696768742e636f6d2f6769746875622f6e6e30322e706e67.png?alt=media&token=3b85bbe0-3802-45b8-b566-cd3a729d5990">

I collected and prepared my own training data to make sure that I understand what the training data should look like.
After training for only 30 epochs with a training batch of 2000 images and validation batch of 500 images, I got a loss value of 0.0039 and an accuracy of 0.9985, which resultated in a 100% success rate when testing on a batch of 200 images.

<img src="https://firebasestorage.googleapis.com/v0/b/creatoratnight-babdb.appspot.com/o/images%2F68747470733a2f2f63726561746f7261746e696768742e636f6d2f6769746875622f6e6e30312e706e67.png?alt=media&token=4447a2b2-82b0-4fb4-ac41-693616ff1a41">

I saved the model and training data into a H5 file to use in this program.
You can put any images of the 10 types of fruit in the input/images folder.
When running the program it will classify all the images and print it to the terminal.

<img src="https://firebasestorage.googleapis.com/v0/b/creatoratnight-babdb.appspot.com/o/images%2F68747470733a2f2f63726561746f7261746e696768742e636f6d2f6769746875622f6e6e30332e706e67.png?alt=media&token=e7cd4bf2-22d3-46fb-a148-9b0a3d0e9a10">
