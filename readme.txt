Waste Segregation Model
This project is a machine learning model designed to classify waste into 12 different categories, helping to automate the process of waste segregation. The model is trained on a dataset of waste images and can be used to predict the category of new images.
Table of Contents
* Project Overview
* Dataset
* File Descriptions
* Getting Started
   * Prerequisites
   * Installation
* Usage
   * Verifying the Dataset
   * Training the Model
   * Running the Web Application
* Contributing
* License
Project Overview
The primary goal of this project is to build and deploy a deep learning model that can accurately classify images of waste into 12 predefined categories. This can be a crucial component in building automated sorting systems for waste management facilities.
Dataset
The model is trained on a custom dataset of waste images, sorted into 12 categories.
* dataset/train/: This directory should contain the training images, organized into 12 subdirectories where each subdirectory name corresponds to a waste category. For example:
   * dataset/train/cardboard/
   * dataset/train/glass/
   * dataset/train/metal/
   * dataset/train/paper/
   * dataset/train/plastic/
   * dataset/train/trash/
   * (and 6 other categories)
File Descriptions
Here's a breakdown of the important files in this project:
* train_model.py: This script contains the code to build, train, and save the waste segregation model. It reads the images from the dataset/train directory, trains a neural network, and saves the trained model to a file (e.g., waste_model.h5).
* app.py: A simple web application (likely built with a framework like Flask or Streamlit) that loads the pre-trained model and provides a user interface to upload an image. The application then displays the predicted waste category for the uploaded image.
* verify_image.py: A utility script to check the dataset/train directory and ensure that it contains only valid image files. This is useful for cleaning the dataset before training.
Getting Started
Follow these instructions to get the project up and running on your local machine.
Prerequisites
You need to have Python installed on your system. It is also recommended to use a virtual environment. You will need the following libraries:
* TensorFlow ==2.10.0
* Pillow (PIL)
* NumPy
* Flask (or any other web framework used in app.py)
* scipy
Installation
1. Clone the repository:
git clone [https://github.com/ViNiT-BeNiWaL/waste-segregation.git]

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
pip install -r requirements.txt

Usage
Verifying the Dataset
Before training, it's a good practice to verify that all files in the dataset/train directory are valid images. Run the verify_image.py script to check the dataset.
python verify_image.py

This script will scan the directory and report any non-image files that might cause errors during training.
Training the Model
To train the model from scratch using the images in the dataset/train directory, run the train_model.py script:
python train_model.py

This script will process the images, train the model, and save the final model weights to a file.
Running the Web Application
Once the model is trained and saved, you can start the web application to interact with it through a browser.
python app.py

Open your web browser and navigate to the address provided (e.g., http://127.0.0.1:5000). You should see an interface where you can upload an image and get a prediction.
Contributing
Contributions are welcome! If you have suggestions for improvements, please open an issue or submit a pull request.
   1. Fork the Project
   2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
   3. Commit your Changes (git commit -m 'Add some AmazingFeature')
   4. Push to the Branch (git push origin feature/AmazingFeature)
   5. Open a Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.