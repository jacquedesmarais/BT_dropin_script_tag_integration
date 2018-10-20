# Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. This means flask provides you with tools, libraries and technologies that allow you to build a web application.

from flask import Flask, render_template, request
# In this line you are first making available the code you need to build web apps with flask. flask is the framework here, while Flask is a Python class datatype. In other words, Flask  is the prototype used to create instances of web application or web applications if you want to put it simple.

# To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. When you include this Flask will look for templates in the templates folder - in our case, the HTML files.

# Request is going to tell us to access one of our HTML forms and get something to use later


import braintree
# This is importing the Braintree package

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='qr7h9y9634y43hy3',
    public_key='8wtdvybw5yht6crc',
    private_key='your_private_key'
  )
)
# Here is where we configure the environment and API credentials - this tells Braintree what account to send the transaction to. Think of this like the Braintree username and password so the Braintree servers know where to go with this information (in our case a transaction).

app = Flask(__name__)
# Once we import Flask, we need to create an instance of the Flask class for our web app. That’s what this line does. __name__ is a special variable that gets as value the string "__main__" when you’re executing the script.

@app.route("/")
def index():
    client_authorization = "sandbox_rx8dxxqr_qr7h9y9634y43hy3"
    return render_template('index.html', client_authorization=client_authorization)
# Here we are defining a function that authorizes our client. That function is mapped to the home  ‘/’ URL. That means when the user navigates to localhost:5000/, the home function will run and in our case, it will return the Drop-in UI. This entire function says, go find the index.html page, render the template on that page, and use this tokenization key.


@app.route("/checkout", methods=["POST"])
# This says, after you send this stuff to Braintree, add /checkout to the URL. The URL would now become http://127.0.0.1:5000/checkout in our case.
def checkout():
    payment_method_nonce = request.form["payment_method_nonce"]
    result = gateway.transaction.sale({
        'amount': '10',
        'payment_method_nonce':payment_method_nonce
        })
    return render_template('checkout.html', result=result)
    # This is our checkout function. The first thing we do is get the payment method nonce from the server, in our case, this is imbeded as a hidden value in the form. Then, we make a transaction sale call to Braintree including an amount and a payment method nonce (credit card number and expiration). At the end of this function, we are saying, render the checkout.html page

if __name__ == "__main__":
    app.run(debug=True)
# Python assigns the name "__main__" to the script when the script is executed. If the script is imported from another script, the script keeps it given name (e.g. app.py). In our case we are executing the script. Therefore, __name__ will be equal to "__main__". That means the if conditional statement is satisfied and the app.run() method will be executed. This technique allows the programmer (us) to have control over script’s behavior.

# Notice also that we are setting the debug parameter to true. That will print out possible Python errors on the web page helping us trace the errors. However, in a production environment, you would want to set it to False as to avoid any security issues.
