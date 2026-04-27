# ai_engine.py

from knowledge_base import knowledge_base

def predict_disease(selected_symptoms):
    results = []

    for disease, data in knowledge_base.items():
        match = set(selected_symptoms) & set(data["symptoms"])

        score = (len(match) / len(data["symptoms"])) * 100

        if len(match) >= 3:
            score += 10  # boost AI confidence

        results.append({
            "disease": disease,
            "score": round(score, 2),
            "advice": data["advice"],
            "treatment": data["treatment"]
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results