from flask import Flask, render_template, request
import rsa
import AES
import os
from Crypto.Random import get_random_bytes


class Client:
    def __init__(self):
        self.__client_private_key, self.client_public_key = generate_keys()

    def verify_certificate(self ,certificate):

        try:
            username = rsa.decrypt(certificate, self.__client_private_key)
            return True
        except Exception as certificate_not_verified:
            print("Certificate did not verified by the user")
            return False

    def post_image(self , client_private_key, server_public_key):

        f = open("wallhaven-760704.jpg", "rb")
        img = f.read()
        f.close()

        """Generate AES KEY"""
        AES_key_length = 32  # 256 bits
        AES_key = os.urandom(AES_key_length)

        """AES encryption of image"""
        img = bytearray(img)
        iv = get_random_bytes(AES.AES.block_size)
        encrypted_image_b = AES.AES_encrypt(img, AES_key, iv, "CBC")

        """Generating Digital Signature"""
        digest_m = rsa.compute_hash(img, 'SHA-256')
        digital_signature = rsa.sign_hash(digest_m, client_private_key, 'SHA-256')

        encrypted_aes_key = rsa.encrypt(AES_key, server_public_key);

        """send POST_IMAGE message , image_name, encrypted image, digital signature, encrypted
        AES key and Initialization Vector (IV) to the server."""

    # Connect to Server ?


def generate_keys():
    (public_key, private_key) = rsa.newkeys(1024)
    return private_key, public_key







