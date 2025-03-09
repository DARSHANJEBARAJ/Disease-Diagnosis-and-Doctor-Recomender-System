**Disease-Diagnosis-and-Doctor-Recomender-System - README**




Overview
The Healthcare Chatbot is a Python-based application that helps users diagnose diseases based on their symptoms. It leverages a dataset containing disease information, including symptoms, causes, effects, medicines, and recommended doctors. The chatbot guides the user through a series of questions, analyzes the symptoms provided, and suggests potential diseases, their details, and even a recommended doctor.

The chatbot is built with a graphical user interface (GUI) using the Tkinter library, and the processing is handled with pandas for data manipulation, and nltk for natural language processing (NLP).

Features
Symptom-based Diagnosis: The chatbot can diagnose diseases based on symptoms entered by the user.
Disease Details: Once a disease is identified, detailed information about the disease is provided, including:
Causes
Effects
Medicines
Doctor Recommendation: Based on the diagnosed disease, the chatbot recommends a doctor with relevant expertise.
Emergency Contact: The user can provide their contact information, which will be sent to an ambulance service.
Natural Language Processing: The chatbot uses tokenization and stopword removal for processing user input and matching symptoms with diseases in the dataset.
Requirements
To run the application, you will need the following libraries:

Tkinter (for the GUI)
Pandas (for data manipulation)
NLTK (for natural language processing tasks)
You can install the necessary Python packages by running:

bash
Copy
pip install pandas nltk
Note: Tkinter is generally bundled with Python, but it may need to be installed separately depending on your environment.

How to Use
Launch the Application:

Run the chatbot.py script. This will open a window with the chatbot interface.
Symptom-based Diagnosis:

The chatbot first asks if you are feeling well today.
If you are not feeling well, you will be prompted to enter your symptoms.
Disease Diagnosis:

After entering symptoms, the chatbot will suggest possible diseases based on the symptoms you provided.
Receive Disease Details:

For each potential disease, the chatbot will show you detailed information, including:
Causes of the disease
Effects of the disease
Recommended medicines
Doctor Recommendation:

The chatbot will recommend a doctor, including:
The doctor's name
The doctor's location
The doctor's specialty
Emergency Contact Information:

After diagnosing the disease, you can provide your phone number and address for ambulance services. This information will be sent to the service.
Feel Well Today:

If you feel well, you can simply exit the chatbot by clicking the "Yes" option when prompted.
Dataset
The chatbot uses a dataset stored in a CSV file (555.csv). The dataset must have the following columns:

Disease: The name of the disease.
Symptoms: A list of symptoms related to the disease.
Causes: The causes of the disease.
Effects: The effects of the disease.
Medicines: The medicines prescribed for the disease.
Doctor Name: The name of a recommended doctor for the disease.
Doctor Location: The location of the recommended doctor.
Specialist: The specialty of the recommended doctor.
Example CSV Format
Disease	Symptoms	Causes	Effects	Medicines	Doctor Name	Doctor Location	Specialist
Flu	fever, cough, fatigue	virus	chills	paracetamol	Dr. Smith	NY, USA	General
Diabetes	increased thirst, fatigue	high sugar	blurred vision	insulin	Dr. Johnson	LA, USA	Endocrinologist
Migraine	headache, nausea	unknown	vomiting	ibuprofen	Dr. Doe	London, UK	Neurologist
How the Application Works
Symptom Processing:

The user's input is processed using the nltk library for tokenization, where the symptoms are converted into individual tokens.
Stopwords (commonly used words like "the", "is", "and") are removed to focus on the key symptoms.
Disease Matching:

The chatbot checks if any diseases in the dataset match the symptoms entered by the user.
If no exact match is found, it looks for diseases with the most matching symptoms.
Disease Details:

After determining a potential disease, detailed information about the disease is displayed, including causes, effects, and recommended medicines.
Doctor Recommendation:

The chatbot suggests a doctor based on the diagnosed disease, providing the doctor's name, location, and specialty.
Emergency Contact:

The user is prompted to provide their phone number and address. This information is then sent to an ambulance service, and a confirmation message is displayed.
Known Issues
The chatbot depends on the 555.csv dataset. If the dataset is missing or improperly formatted, the chatbot may not work correctly.
The symptom matching may not be perfect due to the simple token matching approach. Future improvements could involve more advanced NLP techniques like fuzzy matching or machine learning-based approaches.
Future Enhancements
Improve Symptom Matching: Implement more advanced matching techniques, such as fuzzy matching or machine learning algorithms for better diagnosis accuracy.
Support Multiple Languages: Extend the chatbot to support different languages.
Add More Diseases: Extend the dataset with more diseases and symptoms to improve diagnosis accuracy.
Emergency Response Integration: Integrate real-time emergency services or make direct API calls to healthcare services for a more robust response.
