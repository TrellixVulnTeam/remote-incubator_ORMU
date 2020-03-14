import razorpay
import os

razorpay_key = os.environ.get('RAZOR_KEY')
r_secret_key = os.environ.get('RAZOR_SECRET_KEY')

# client = razorpay.Client(auth=(razorpay_key, r_secret_key))
client = razorpay.Client(auth=(razorpay_key, r_secret_key))

#App detail, setting up app details before making any request to Razorpay using the following:
client.set_app_details({"title" : "Flask", "version" : "1.1.1"})