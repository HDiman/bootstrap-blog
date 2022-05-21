from flask import Flask, render_template, request
import requests
import smtplib

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    sender = 'split777hisense@gmail.com'
    sender_password = 'Split777hisense159'
    receiver = 'dsannikov@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, sender_password)
    server.sendmail(sender, sender, f"Subject: Contacts\n{email_message}")
    print('Mail sent')


app = Flask(__name__)

def get_all_posts():
    blog_url = "https://api.npoint.io/8169b5687e2da25a607c"
    response = requests.get(blog_url)
    return response.json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=get_all_posts(), posts_num=len(get_all_posts()))

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data['user_name'], data['user_email'], data['user_phone'], data['user_text'])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

@app.route("/post/<num>")
def get_blog(num):
    return render_template("post.html", all_posts=get_all_posts(), num=int(num))


if __name__ == '__main__':
    app.run(debug=True)
