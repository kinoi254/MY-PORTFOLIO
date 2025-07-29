import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('All fields are required.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Send email if mail is configured
        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
            msg = Message(
                subject=f"Portfolio Contact: {subject}",
                recipients=[app.config['MAIL_DEFAULT_SENDER'] or app.config['MAIL_USERNAME']],
                body=f"""
New contact form submission:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
                """,
                reply_to=email
            )
            mail.send(msg)
            flash('Thank you for your message! I will get back to you soon.', 'success')
        else:
            # Log the message if email is not configured
            app.logger.info(f"Contact form submission from {name} ({email}): {subject} - {message}")
            flash('Thank you for your message! (Note: Email configuration needed for delivery)', 'info')
        
    except Exception as e:
        app.logger.error(f"Error sending contact form: {str(e)}")
        flash('Sorry, there was an error sending your message. Please try again.', 'error')
    
    return redirect(url_for('index') + '#contact')

@app.route('/download-cv')
def download_cv():
    """Download CV file"""
    try:
        return send_from_directory('static/files', 'cv.pdf', as_attachment=True)
    except FileNotFoundError:
        flash('CV file not found. Please contact me directly.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
