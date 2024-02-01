from app import application

from flask import Flask, render_template, redirect, url_for, flash
from app.forms import SignUpForm
import boto3

# dynamodb
db = boto3.resource('dynamodb', region_name='us-west-2')
table = db.Table('signuptable')

# AWS SNS
notification = boto3.client('sns', region_name='us-west-2')
topic_arn = "arn:aws:sns:us-west-2:936668792450:eb-flask-sns"


@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        table.put_item(
            Item={
                'name': form.name.data,
                'email': form.email.data,
                'mobile': form.mobile.data,
                'country': form.country.data,
                'newsletter': form.newsletter.data
            }
        )
        msg = 'Congratulations !!! {} is now a premium member !'.format(form.name.data)
        flash(msg)

        # sending email to owner using sns
        email_message = f"\nname: {form.name.data}" \
                        f"\nemail: {form.email.data}" \
                        f"\nmobile: {form.mobile.data}" \
                        f"\ncountry: {form.country.data}"

        notification.publish(Message=email_message, TopicArn=topic_arn, Subject="A new signup form submitted")
        return redirect(url_for('home_page'))

    return render_template('signup.html', form=form)
