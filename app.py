"""Flask App Project."""

from flask import Flask, jsonify, request
# from flask_cors import CORS, cross_origin
import shamaq, iterator, modes, ecdsa, signature
from ecc import demo_curve, Curve, Point
# import logging

# logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-type'


# @cross_origin()
@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)

# @cross_origin()
@app.route('/encrypt', methods=['GET'])
def encrypt():
    key = request.args.get('key')
    cipher = shamaq.Shamaq(key)
    mode = modes.ECB(cipher)
    
    string = request.args.get('string')
    input_bytes = string.encode("latin-1")
    input_iterator = iterator.bytes_block_iterator(input_bytes, mode.block_size_plaintext)

    encrypted_string = ""
    for data in mode.encrypt(input_iterator):
        encrypted_string += data.decode("latin-1")
    
    json_data = {
        'status' : 200,
        'result' : encrypted_string
    }
    return jsonify(json_data)

# @cross_origin()
@app.route('/decrypt', methods=['GET'])
def decrypt():
    key = request.args.get('key')
    cipher = shamaq.Shamaq(key)
    mode = modes.ECB(cipher)

    string = request.args.get('string')
    input_bytes = string.encode("latin-1")
    input_iterator = iterator.bytes_block_iterator(input_bytes, mode.block_size_ciphertext)

    decrypted_string = ""
    for data in mode.decrypt(input_iterator):
        decrypted_string += data.decode("latin-1")
    
    json_data = {
        'status' : 200,
        'result' : decrypted_string
    }
    return jsonify(json_data)

# @cross_origin()
@app.route('/generate/private', methods=['GET'])
def generate_private():
    n = request.args.get('n')
    key = ecdsa.generate_private(n)
    json_data = {
        'status' : 200,
        'private_key' : key
    }
    return jsonify(json_data)

# @cross_origin()
@app.route('/generate/public', methods=['GET'])
def generate_public():
    private_key = request.args.get('prikey')
    key_point = ecdsa.generate_public(private_key)
    key = str(key_point.x) + "-" + str(key_point.y)
    json_data = {
        'status' : 200,
        'private_key' : key
    }
    return jsonify(json_data)

# @cross_origin()
@app.route('/sign', methods=['POST'])
def generate_public():
    message = request.args.get('message')
    private_key = request.args.get('prikey')
    sign_point = signature.sign(message, private_key, demo_curve)
    sign = str(sign_point.x) + "-" + str(sign_point.y)
    json_data = {
        'status' : 200,
        'signature' : sign
    }
    return jsonify(json_data)

# @cross_origin()
@app.route('/sign', methods=['POST'])
def generate_public():
    message = request.args.get('message')
    sign = request.args.get('signature')
    public_key = request.args.get('pubkey')
    result = signature.verify(message, sign, public_key, demo_curve)
    json_data = {
        'status' : 200,
        'valid' : result
    }
    return jsonify(json_data)

if __name__ == '__main__':
    app.run()
