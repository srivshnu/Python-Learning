import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Prevent browser caching of static files during development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    technologies = ['HTML', 'CSS', 'Flask', 'Python']
    page_title = '30 Days Of Python Programming'
    return render_template('home.html', techs=technologies, name=page_title, title='Home')

@app.route('/about')
def about():
    page_title = '30 Days Of Python Programming'
    return render_template('about.html', name=page_title, title='About Us')

@app.route('/post', methods=['GET', 'POST'])
def post():
    analyzer_title = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=analyzer_title, title=analyzer_title)
    
    if request.method == 'POST':
        raw_text = request.form.get('content', '')
        
        # Simple text metrics logic
        word_count = len(raw_text.split())
        char_count = len(raw_text)
        
        # Pass metrics forward or store for processing
        return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html', title='Analysis Results')

if __name__ == '__main__':
    # Binds to PORT environment variable for production deployment platforms
    server_port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=server_port)