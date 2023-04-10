#Proyectos-AI

Psychological Help Diagnosis
This project provides a simple GUI to diagnose psychological symptoms and provide potential help or treatment options based on the diagnosis. The project uses a neural network model that has been trained on psychological symptom data to provide the diagnosis.

Installation
To run this project, you will need Python 3 installed on your system along with the following libraries:

shelve
tensorflow
tkinter
scikit-learn
Usage
To use the project, run the main() function in the code. This will open a GUI window where you can select your language and the symptoms you are experiencing along with their intensity. Once you click on the "Diagnóstico" button, the program will display the diagnosis and potential treatment options.

Model
The neural network model used in this project has been trained on a dataset of psychological symptom data. The model consists of two dense layers with 50 and 1 neurons respectively, and uses the mean squared error loss function with the Adam optimizer.

Data
The data used to train the model is stored in a shelve database file named "psychological_help_database". If no data is found in the database, the program will start from scratch.

Disclaimer
Please note that this project is not a substitute for professional medical advice or treatment. If you are experiencing severe psychological symptoms, please seek help from a licensed mental health professional.
