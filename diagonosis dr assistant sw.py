disease_dict = {
    "Flu": ["fever", "cough", "sore throat", "runny nose", "fatigue"],
    "Malaria": ["fever", "chills", "sweating", "headache", "nausea"],
    "COVID-19": ["fever", "cough", "loss of taste", "shortness of breath", "fatigue"],
    "Migraine": ["headache", "nausea", "sensitivity to light", "vomiting", "blurred vision"],
    "Typhoid": ["fever", "abdominal pain", "loss of appetite", "weakness", "diarrhea"],
    "Pneumonia": ["fever", "cough", "chest pain", "difficulty breathing", "fatigue"],
    "Dengue Fever": ["fever", "severe headache", "joint pain", "rash", "nausea"],
    "Tuberculosis": ["cough", "night sweats", "weight loss", "chest pain", "fatigue"],
    "Asthma": ["shortness of breath", "wheezing", "cough", "chest tightness"],
    "Food Poisoning": ["vomiting", "diarrhea", "abdominal pain", "nausea", "fever"]
}


def diagnose(symptoms):
    possible_diseases = {}

    for disease, disease_symptoms in disease_dict.items():
        match_count = len(set(symptoms) & set(disease_symptoms))
        
        if match_count >= 2:  
            possible_diseases[disease] = match_count

    if possible_diseases:
        print("\nPossible diseases based on your symptoms:")
        sorted_diseases = sorted(possible_diseases.items(), key=lambda x: x[1], reverse=True)
        for disease, matches in sorted_diseases:
            print(f"- {disease} ({matches} matching symptoms)")
    else:
        print("\nNo disease found. Please consult a doctor.")

# Get symptoms from the user
user_symptoms = input("Enter your symptoms separated by commas: ").lower().split(", ")
diagnose(user_symptoms)
