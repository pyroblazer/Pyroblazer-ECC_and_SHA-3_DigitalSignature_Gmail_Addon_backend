import chardet
#from flask import Flask, jsonify, request
#from flask_cors import CORS, cross_origin
import shamaq, iterator, modes, ecdsa, signature
from ecc import Curve, Point
import logging
from urllib.parse import unquote

#test = "\u0011\u00c0'\u00d9hp\u000f\u00eb"
test = "\u0011\u00c0%27\u00d9hp\u000f\u00eb"

key = "aa"
cipher = shamaq.Shamaq(key)
mode = modes.ECB(cipher)

string = unquote(test)
#string = string.decode()
input_bytes = string.encode("latin-1")
input_iterator = iterator.bytes_block_iterator(input_bytes, mode.block_size_ciphertext)

decrypted_string = ""
for data in mode.decrypt(input_iterator):
    decrypted_string += data.decode("latin-1")
    
#decrypted_string = decrypted_string.decode()

json_data = {
    'status' : 200,
    'result' : decrypted_string
}
print(json_data)

