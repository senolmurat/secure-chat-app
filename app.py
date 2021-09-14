from flask import Flask, render_template, request
import rsa
import client

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def handle_client():

    new_client = client.Client()

    if request.method == 'POST':

        username = request.form["name"]
        client_public_key = new_client.client_public_key
        signed_certificate = create_certificate(username, client_public_key)
        real_signed_certificate = rsa.sign(signed_certificate, server_private_key,'SHA-256')
        if new_client.verify_certificate(signed_certificate):
            print("ok")

    return render_template("index.html")


def create_certificate(message, enc):
    encoded_m = message.encode()
    certificate = rsa.encrypt(encoded_m, enc)
    return certificate


def generate_keys():
    (public_key, private_key) = rsa.newkeys(1024)
    return private_key, public_key


if __name__ == '__main__':
    app.run()

server_private_key, server_public_key = generate_keys()
