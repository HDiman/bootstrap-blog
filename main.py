from flask import Flask, render_template, request
import requests

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

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route('/contact', methods=['POST'])
def receive_data():
    get_name = request.form['user_name']
    get_email = request.form['user_email']
    get_phone = request.form['user_phone']
    get_text = request.form['user_text']

    # return render_template('contact.html')
    return f"<h1>Successfully sent your message</h1>"
    #        f"1. {get_name} \n" \
    #        f"2. {get_email} \n" \
    #        f"3. {get_phone} \n" \
    #        f"4. {get_text}\n"


@app.route("/post/<num>")
def get_blog(num):
    return render_template("post.html", all_posts=get_all_posts(), num=int(num))




if __name__ == '__main__':
    app.run(debug=True)
