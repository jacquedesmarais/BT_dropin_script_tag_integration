from flask import Flask, render_template, request
import braintree

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    'your_merchant_id',
    'your_public_key',
    'your_private_key'
)

app = Flask(__name__)

@app.route("/")
def index():
    client_authorization = "sandbox_rx8dxxqr_qr7h9y9634y43hy3"
    return render_template('index.html', client_authorization=client_authorization)

@app.route("/checkout", methods=["POST"])
def checkout():
    payment_method_nonce = request.form["payment_method_nonce"]
    result = braintree.Transaction.sale({
        'amount': '10',
        'payment_method_nonce':payment_method_nonce
        })
    return render_template('checkout.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
