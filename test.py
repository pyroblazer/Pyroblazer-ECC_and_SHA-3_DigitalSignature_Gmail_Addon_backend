import chardet
#from flask import Flask, jsonify, request
#from flask_cors import CORS, cross_origin
import shamaq, iterator, modes, ecdsa, signature
from ecc import Curve, Point
import ecc
import logging
from urllib.parse import unquote
import re

# n = "5"
# key = ecdsa.generate_private(int(n))
# json_data = {
#     'status' : 200,
#     'private_key' : key
# }
# print(json_data)

message = "980935360bf24012ca6c80f85bbb77ff996ece87768d81ed886af0ce9120a2f9"
private_key = "1"
demo_curve_obj = ecc.demo_curve()
print(demo_curve_obj)
sign_point = signature.sign(message, private_key, demo_curve_obj)
sign = str(sign_point.x) + "-" + str(sign_point.y)
json_data = {
    'status' : 200,
    'signature' : sign
}
print(json_data)


#jsonify(json_data)

# #test = "\u0011\u00c0'\u00d9hp\u000f\u00eb"
# test = "\\u0011\\u00c0%27\\u00d9hp\\u000f\\u00eb"
# test = test.encode().decode('unicode_escape')


# key = "aa"
# cipher = shamaq.Shamaq(key)
# mode = modes.ECB(cipher)

# string = unquote(test)
# print(string)
# #string = string.decode()
# input_bytes = string.encode("latin-1")
# input_iterator = iterator.bytes_block_iterator(input_bytes, mode.block_size_ciphertext)

# decrypted_string = ""
# for data in mode.decrypt(input_iterator):
#     decrypted_string += data.decode("latin-1")
    
# #decrypted_string = decrypted_string.decode()

# json_data = {
#     'status' : 200,
#     'result' : decrypted_string
# }
# print(json_data)
