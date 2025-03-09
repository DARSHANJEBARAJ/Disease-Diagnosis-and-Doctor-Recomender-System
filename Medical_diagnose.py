import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tkinter import *
from tkinter import messagebox

nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
df = pd.read_csv('555.csv')

# Preprocess data
df['Symptoms'] = df['Symptoms'].apply(lambda x: x.lower())
df['Symptoms'] = df['Symptoms'].apply(lambda x: word_tokenize(x))
stop_words = set(stopwords.words('english'))
df['Symptoms'] = df['Symptoms'].apply(lambda x: [word for word in x if word not in stop_words])

# Define chatbot functions
def diagnose_disease(symptoms):
    # Tokenize user input
    tokens = word_tokenize(symptoms)
    tokens = [word for word in tokens if word not in stop_words]
    
    # Find matching diseases
    matches = df[df['Symptoms'].apply(lambda x: any(token in x for token in tokens))]
    # Return top match
    return matches.iloc[0]['Disease']

def get_disease(inputs): 
    row = df[df['Disease'] == inputs]
    return {
        'cause': row['Causes'].values[0],
        'Effect': row['Effects'].values[0],
        'Medicines': row['Medicines'].values[0]
    }

def recommend_doctor(location, specialty):
    # Find matching doctors
    doctor_location = df[df['Doctor Location'] == location]
    doctor_specialist = doctor_location[doctor_location['Specialist'] == specialty]
    
    if doctor_specialist.empty:
        return "No doctors found", "N/A"
    
    # Return the first matching doctor
    return doctor_specialist['Doctor Name'].iloc[0], doctor_specialist['Hospital Name'].iloc[0]


def send_ambulance(phone_number, address):
    # Send ambulance (this is just a placeholder, you would need to integrate with an ambulance service API)
    messagebox.showinfo(f"Ambulance will contact to the number", "An ambulance has been sent to "+ address)

# Define chatbot interface
def chatbot():
    window = Tk()
    window.title("Healthcare Chatbot")
    window.configure(bg='#f0f0f0')

    label = Label(window, text="Welcome! I'm here to help you.", font=("Helvetica", 12, "bold"), bg='#f0f0f0', fg='#333333')
    label.pack(pady=7)

    label2 = Label(window, text="Are you feeling well?", font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
    label2.pack(pady=7)

    feeling_well_var = StringVar()
    feeling_well_var.set("no")

    feeling_well_yes = Radiobutton(window, text="Yes", variable=feeling_well_var, value="yes", bg='#f0f0f0', fg='#333333', font=("Helvetica", 10))
    feeling_well_yes.pack()

    feeling_well_no = Radiobutton(window, text="No", variable=feeling_well_var, value="no", bg='#f0f0f0', fg='#333333', font=("Helvetica", 10))
    feeling_well_no.pack()
    
    label9 = Label(window, text="WHETHER THE PATIENT IS SERIOUS", font=("Helvetica", 12, "bold"), bg='#f0f0f0', fg='#333333')
    label9.pack(pady=10)
    
    serious_var = StringVar()
    serious_var.set("no")
    
    serious_yes = Radiobutton(window, text="Yes", variable=serious_var, value="yes", bg='#f0f0f0', fg='#333333', font=("Helvetica", 12))
    serious_yes.pack(pady=5)

    serious_no = Radiobutton(window, text="No", variable=serious_var, value="no", bg='#f0f0f0', fg='#333333', font=("Helvetica", 12))
    serious_no.pack(pady=5)
    
    def submit_feeling_well():
        if feeling_well_var.get() == "yes":
            messagebox.showinfo("Goodbye", "Thank you! Take care.")
            window.destroy()
        else:
            label3 = Label(window, text="What are your symptoms?", font=("Helvetica", 12), bg='#f0f0f0', fg='#333333')
            label3.pack(pady=10)

            symptoms_entry = Text(window, height=1, width=40, font=("Helvetica", 10), bg='#ffffff', fg='#000000', bd=2)
            symptoms_entry.pack(pady=10)

            def submit_symptoms():
                symptoms = symptoms_entry.get("1.0", END)
                symptoms=symptoms.strip()
                disease = diagnose_disease(symptoms)
                info = get_disease(disease)

                label4 = Label(window, text="You may have " + disease, font=("Helvetica", 10, "bold"), bg='#f0f0f0', fg='#cc0000')
                label4.pack(pady=10)

                label5 = Label(window, text="Cause: " + info['cause'], font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
                label5.pack(pady=5)

                label6 = Label(window, text="Effects: " + info['Effect'], font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
                label6.pack(pady=5)

                label7 = Label(window, text="Medicines: " + info['Medicines'], font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
                label7.pack(pady=5)

                location_label = Label(window, text="Please enter your location:", font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
                location_label.pack(pady=10)

                location_entry = Entry(window, font=("Helvetica", 10), bg='#ffffff', fg='#000000', bd=2)
                location_entry.pack(pady=5)

                specialty_label = Label(window, text="Please enter a specialty:", font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
                specialty_label.pack(pady=10)

                specialty_entry = Entry(window, font=("Helvetica", 10), bg='#ffffff', fg='#000000', bd=2)
                specialty_entry.pack(pady=5)

                def submit_location_specialty():
                    location = location_entry.get()
                    location=location.strip()
                    specialty = specialty_entry.get()
                    specialty= specialty.strip()
                    doctor_name, hospital_name = recommend_doctor(location, specialty)

                    label8 = Label(window, text="We recommend Dr. " + doctor_name + " at " + hospital_name, font=("Helvetica", 12, "bold"), bg='#f0f0f0', fg='#333333')
                    label8.pack(pady=10)
                    def submit_serious():
                        if serious_var.get() == "yes":
                            phone_number_label = Label(window, text="Kindly enter your phone number:", font=("Helvetica", 8), bg='#f0f0f0', fg='#333333')
                            phone_number_label.pack(pady=5)

                            phone_number_entry = Entry(window, font=("Helvetica", 12), bg='#ffffff', fg='#000000', bd=2)
                            phone_number_entry.pack(pady=5)

                            address_label = Label(window, text="Kindly enter your address:", font=("Helvetica", 10), bg='#f0f0f0', fg='#333333')
                            address_label.pack(pady=5)

                            address_entry = Entry(window, font=("Helvetica", 12), bg='#ffffff', fg='#000000', bd=2)
                            address_entry.pack(pady=5)

                            def submit_phone_number_address():
                                phone_number = phone_number_entry.get()
                                address = address_entry.get()
                                send_ambulance(phone_number, address)   
                            submit_phone_number_address_button = Button(window, text="SUMBIT", command=submit_phone_number_address, font=("Helvetica", 8), bg='#4CAF50', fg='#ffffff', bd=2)
                            submit_phone_number_address_button.pack(pady=5)
                        else:
                            messagebox.showinfo("Good","Thanks for choosing us")
                            window.destroy()
                    submit_serious_button = Button(window, text="SUMBIT", command=submit_serious, font=("Helvetica", 12), bg='#4CAF50', fg='#ffffff', bd=2)
                    submit_serious_button.pack(pady=5)

                submit_location_specialty_button = Button(window, text="SUMBIT", command=submit_location_specialty, font=("Helvetica", 12), bg='#4CAF50', fg='#ffffff', bd=2)
                submit_location_specialty_button.pack(pady=5)

            submit_symptoms_button = Button(window, text="SUMBIT", command=submit_symptoms, font=("Helvetica", 12), bg='#4CAF50', fg='#ffffff', bd=2)
            submit_symptoms_button.pack(pady=5)

    submit_feeling_well_button = Button(window, text="SUMBIT", command=submit_feeling_well, font=("Helvetica", 12), bg='#4CAF50', fg='#ffffff', bd=2)
    submit_feeling_well_button.pack(pady=5)
    window.mainloop()
chatbot()
