from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for appointments (for simplicity)
appointments = []

@app.route('/')
def index():
    return render_template('index.html', appointments=appointments)

@app.route('/book', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        
        # Store the appointment
        appointment = {
            'name': name,
            'date': date,
            'time': time
        }
        appointments.append(appointment)
        
        return redirect(url_for('index'))
    
    return render_template('book.html')

if __name__ == '__main__':
    app.run(debug=True)
