from flask import Flask, render_template, request
import braintree

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    'qr7h9y9634y43hy3',
    '8wtdvybw5yht6crc',
    'c3bf46039e4b5589f65a5b1235c07857'
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
