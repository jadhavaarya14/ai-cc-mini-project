from flask import Flask, request, render_template_string
from ai_engine import predict_disease
from knowledge_base import symptoms_list

app = Flask(__name__)

HTML = """
<h1>AI Medical Expert System</h1>
<form method="POST">
{% for s in symptoms %}
<input type="checkbox" name="symptoms" value="{{s}}"> {{s}}<br>
{% endfor %}
<button type="submit">Diagnose</button>
</form>

{% if result %}
<h2>Most Likely: {{result[0].disease}}</h2>
{% for r in result[:3] %}
<p>{{r.disease}} → {{r.score}}%</p>
{% endfor %}
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        selected = request.form.getlist("symptoms")
        if selected:
            result = predict_disease(selected)
    return render_template_string(HTML, symptoms=symptoms_list, result=result)

app.run()