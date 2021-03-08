from flask import render_template, request, Blueprint,redirect,flash
from flaskblog.models import Post
import smtplib
import os
from flaskblog.main.forms import SubscriptionForm

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title = 'About')

@main.route("/subscribe", methods =['POST','GET'])
def subscription():
    form = SubscriptionForm()
    email = form.email.data
    message = "You have been subscribed to our monthly newsletter"
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()
    server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
    server.sendmail(os.environ.get('EMAIL_USER'), email, message)
    flash('You have been subscribed to our monthly newsletter!!','success')
    return render_template('subscription.html', title = 'Subscription',form=form)



