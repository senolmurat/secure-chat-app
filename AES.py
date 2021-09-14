
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad



def AES_encrypt(msg, secret_key,iv ,mode):
    if mode == "CBC":
        cypher = AES.new(secret_key, AES.MODE_CBC, iv)
        # pad the private_msg
        # because AES encryption requires the length of the msg to be a multiple of 16
        padded_msg = pad(msg, AES.block_size)
        encrypted_msg = cypher.encrypt(padded_msg)
        return "", iv + encrypted_msg
    elif mode == "CTR":
        cypher = AES.new(secret_key, AES.MODE_CTR)
        encrypted_msg = cypher.encrypt(msg)
        nonce = cypher.nonce
        return nonce, encrypted_msg


def AES_decrypt(encrypted_msg, secret_key, mode,nonce=None):
    if mode == "CBC":
        cypher = AES.new(secret_key, AES.MODE_CBC, encrypted_msg[:AES.block_size])
        decrypted_msg = cypher.decrypt(encrypted_msg[AES.block_size:])
        unpadded_msg = unpad(decrypted_msg, AES.block_size)
        return unpadded_msg
    elif mode == "CTR":
        cypher = AES.new(secret_key, AES.MODE_CTR, nonce=nonce)
        plaintext = cypher.decrypt(encrypted_msg)
        return plaintext