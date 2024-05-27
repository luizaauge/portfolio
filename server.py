'''Module providing the server'''
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    '''Function to create home page based on index.html'''
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    '''Function to create other pages to the website'''
    return render_template(page_name)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    '''Function to submit the message form'''
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            comment = request.form['comment']
            fieldnames = ['name', 'email', 'comment']
            with open('database.csv', 'a') as inFile:
                writer = csv.DictWriter(inFile, fieldnames=fieldnames)
                writer.writerow({'name': name, 'email': email, 'comment': comment})
            return redirect('thankyou.html')
        except:
            return 'Message not sent'

if __name__ == "__main__":
    app.run(debug=True)
