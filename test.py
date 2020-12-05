import chardet
#from flask import Flask, jsonify, request
#from flask_cors import CORS, cross_origin
import shamaq, iterator, modes, ecdsa, signature
from ecc import Curve, Point
import ecc
import logging
from urllib.parse import unquote
import re
from util import is_prime

#generate private key
n = "5"
pri_key = ecdsa.generate_private(int(n))
json_data = {
    'status' : 200,
    'private_key' : pri_key
}
print(json_data)

#generate public key
print(type(pri_key))
key_point = ecdsa.generate_public(pri_key)
pub_key = str(key_point.x) + "-" + str(key_point.y)
json_data = {
    'status' : 200,
    'public_key' : pub_key
}
print(json_data)

#sign
print("sign")
message = "980935360bf24012ca6c80f85bbb77ff996ece87768d81ed886af0ce9120a2f9"
private_key = pri_key
demo_curve_obj = ecc.demo_curve()
print(demo_curve_obj)
sign_point = signature.sign(message, private_key, demo_curve_obj)
sign = str(sign_point.x) + "-" + str(sign_point.y)
json_data = {
    'status' : 200,
    'signature' : sign
}
print(json_data)

#verify
print("verify")
message_verify = "980935360bf24012ca6c80f85bbb77ff996ece87768d81ed886af0ce9120a2f9"
public_key = pub_key
demo_curve_obj = ecc.demo_curve()
result = signature.verify(message_verify, sign, public_key, demo_curve_obj, pri_key)
json_data = {
    'status' : 200,
    'valid' : result
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
