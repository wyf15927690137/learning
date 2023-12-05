import cbor2
import base64

# Create a Python object to encode as CBOR
data = {
    "name": "John Doe",
    "age": 30,
    "is_student": True,
    "scores": [85, 90, 95]
}

data1 = 'oWRkYXRhomR0eXBldGNiZ19saWNlbnNlU3RhdHVzTXNnamF0dHJpYnV0ZXOhbGhvc3RJZEV4cGlyeXghMTItMzEtMjAyM1QyMzo1OTo1OS0wNTowMCAoVVRDLTUp'
# Encode the Python object as CBOR
cbor_data = cbor2.dumps(data)
# Print the CBOR-encoded data
print("CBOR data:", cbor_data, "\n")
# Decode the CBOR data back to a Python object
decoded_data = cbor2.loads(cbor_data)
# Print the decoded Python object
print("Decoded data:", decoded_data, "\n")

destr = base64.b64decode(data1)

cbstr = cbor2.loads(destr)
print(cbstr)