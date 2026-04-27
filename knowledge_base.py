# knowledge_base.py

knowledge_base = {
    "Common Cold": {
        "symptoms": ["cough", "sore throat", "runny nose", "fever"],
        "advice": "A self-limiting viral upper respiratory infection that typically resolves within a week with supportive care.",
        "treatment": (
            "✔ Supportive Care Plan:\n"
            "- Maintain adequate oral hydration (warm fluids preferred)\n"
            "- Steam inhalation 2–3 times daily to reduce nasal congestion\n"
            "- Saline nasal spray for relief from blocked nose\n"
            "- Ensure proper rest and avoid exposure to cold air\n"
            "- Maintain light nutrition (soups, warm meals)\n\n"
            "⚠ Monitor and seek care if:\n"
            "- Fever persists beyond 3–4 days\n"
            "- Symptoms worsen instead of improving\n"
            "- Breathing discomfort develops"
        )
    },

    "Flu": {
        "symptoms": ["fever", "body pain", "fatigue", "headache", "cough"],
        "advice": "Influenza is a systemic viral infection that may cause significant weakness and fever for several days.",
        "treatment": (
            "✔ Clinical Management:\n"
            "- Strict rest until fever subsides completely\n"
            "- Increase fluid intake (water, ORS, soups)\n"
            "- Monitor temperature regularly\n"
            "- Maintain light, nutritious diet even with reduced appetite\n"
            "- Avoid physical exertion during recovery phase\n\n"
            "⚠ Seek medical attention if:\n"
            "- High fever persists beyond 72 hours\n"
            "- Severe weakness or dehydration signs appear\n"
            "- Chest pain or breathing difficulty develops"
        )
    },

    "COVID-19": {
        "symptoms": ["fever", "cough", "breathing issue", "fatigue"],
        "advice": "Respiratory infection with variable severity; monitoring oxygen levels and symptom progression is essential.",
        "treatment": (
            "✔ Home Isolation Protocol:\n"
            "- Isolate from others to prevent transmission\n"
            "- Monitor oxygen saturation regularly if device available\n"
            "- Maintain upright or semi-upright sleeping position\n"
            "- Stay hydrated and consume light meals\n"
            "- Perform gentle breathing exercises if comfortable\n\n"
            "⚠ Emergency indicators:\n"
            "- Oxygen saturation dropping below normal range\n"
            "- Persistent chest tightness or pressure\n"
            "- Severe breathlessness at rest\n"
            "- Confusion or inability to stay awake"
        )
    },

    "Migraine": {
        "symptoms": ["headache", "nausea", "sensitivity to light"],
        "advice": "Neurological condition often triggered by stress, sleep disturbance, dehydration, or sensory overload.",
        "treatment": (
            "✔ Acute Episode Management:\n"
            "- Rest in a quiet, dark, low-stimulation environment\n"
            "- Avoid screen exposure and bright light\n"
            "- Maintain hydration\n"
            "- Apply cold compress to head if needed\n"
            "- Maintain regular sleep schedule\n\n"
            "⚠ Consult a specialist if:\n"
            "- Headaches become frequent or severe\n"
            "- Pain does not respond to rest or triggers persist\n"
            "- Neurological symptoms like vision disturbance appear"
        )
    },

    "Allergy": {
        "symptoms": ["sneezing", "runny nose", "itchy eyes", "cough"],
        "advice": "Immune response triggered by allergens such as dust, pollen, or environmental factors.",
        "treatment": (
            "✔ Allergy Management:\n"
            "- Identify and avoid triggering allergens\n"
            "- Maintain clean indoor environment (dust-free spaces)\n"
            "- Use protective masks in high-dust areas\n"
            "- Wash face and hands after exposure\n\n"
            "⚠ Seek care if:\n"
            "- Symptoms become persistent or severe\n"
            "- Breathing difficulty or wheezing develops"
        )
    },

    "Food Poisoning": {
        "symptoms": ["nausea", "vomiting", "stomach pain", "diarrhea", "fever"],
        "advice": "Caused by ingestion of contaminated food or water leading to gastrointestinal irritation.",
        "treatment": (
            "✔ Gastrointestinal Recovery Plan:\n"
            "- Maintain hydration using ORS or electrolyte fluids\n"
            "- Avoid solid or heavy meals initially\n"
            "- Gradually reintroduce bland diet (rice, bananas, toast)\n"
            "- Rest adequately to support recovery\n\n"
            "⚠ Immediate care needed if:\n"
            "- Severe dehydration symptoms appear\n"
            "- Persistent vomiting or diarrhea occurs\n"
            "- Blood is present in stool or vomit"
        )
    },

    "Dengue (Suspected)": {
        "symptoms": ["fever", "body pain", "headache", "fatigue", "rash"],
        "advice": "Vector-borne viral infection requiring careful monitoring of platelet levels and hydration status.",
        "treatment": (
            "✔ Clinical Monitoring Plan:\n"
            "- Strict rest and continuous hydration\n"
            "- Avoid self-medication without medical supervision\n"
            "- Monitor temperature and hydration levels regularly\n"
            "- Maintain mosquito protection measures\n\n"
            "⚠ Urgent warning signs:\n"
            "- Bleeding gums or unusual bruising\n"
            "- Sudden drop in energy levels\n"
            "- Severe abdominal pain\n"
            "- Persistent vomiting"
        )
    },

    "Malaria (Suspected)": {
        "symptoms": ["fever", "chills", "sweating", "headache", "fatigue"],
        "advice": "Parasitic infection transmitted by mosquitoes, often showing periodic fever cycles.",
        "treatment": (
            "✔ Medical Care Guidance:\n"
            "- Immediate diagnostic testing required\n"
            "- Maintain hydration and rest\n"
            "- Avoid delay in medical consultation\n"
            "- Use mosquito protection measures\n\n"
            "⚠ Critical indicators:\n"
            "- High recurrent fever cycles\n"
            "- Severe weakness or confusion\n"
            "- Signs of anemia or dehydration"
        )
    },

    "Acid Reflux": {
        "symptoms": ["chest pain", "heartburn", "nausea", "stomach discomfort"],
        "advice": "Digestive condition caused by stomach acid flowing back into the esophagus.",
        "treatment": (
            "✔ Lifestyle Management:\n"
            "- Eat smaller, frequent meals instead of large portions\n"
            "- Avoid spicy, oily, and acidic foods\n"
            "- Do not lie down immediately after eating\n"
            "- Maintain healthy body posture during and after meals\n\n"
            "⚠ Consult doctor if:\n"
            "- Symptoms become chronic or severe\n"
            "- Chest pain becomes persistent"
        )
    },

    "Anxiety": {
        "symptoms": ["rapid heartbeat", "breathing issue", "sweating", "restlessness"],
        "advice": "Psychological condition often triggered by stress, emotional strain, or environmental pressure.",
        "treatment": (
            "✔ Stress Management Plan:\n"
            "- Practice controlled breathing techniques\n"
            "- Maintain regular sleep schedule\n"
            "- Reduce exposure to stress triggers\n"
            "- Engage in light physical activity or meditation\n\n"
            "⚠ Seek professional help if:\n"
            "- Symptoms interfere with daily functioning\n"
            "- Panic episodes become frequent"
        )
    },

    "Dehydration": {
        "symptoms": ["fatigue", "dizziness", "dry mouth", "headache"],
        "advice": "Condition caused by excessive fluid loss or inadequate intake.",
        "treatment": (
            "✔ Rehydration Protocol:\n"
            "- Increase water intake gradually but consistently\n"
            "- Use electrolyte solutions if needed\n"
            "- Avoid excessive caffeine or sugary drinks\n"
            "- Rest in a cool environment\n\n"
            "⚠ Medical attention required if:\n"
            "- Severe dizziness or fainting occurs\n"
            "- Inability to retain fluids"
        )
    }
}

symptoms_list = [
    "fever", "cough", "sore throat", "runny nose",
    "fatigue", "headache", "body pain",
    "breathing issue", "nausea", "sensitivity to light"
]