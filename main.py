from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        activity = request.form['activity']

        if activity == 'low':
            maintenance_calorie = 1.2 * (10 * weight + 6.25 * height - 5 * 25 + 5)
        elif activity == 'medium':
            maintenance_calorie = 1.55 * (10 * weight + 6.25 * height - 5 * 25 + 5)
        elif activity == 'high':
            maintenance_calorie = 1.9 * (10 * weight + 6.25 * height - 5 * 25 + 5)
        
        return render_template('result.html', maintenance_calorie=maintenance_calorie)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
