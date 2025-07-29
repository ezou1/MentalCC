from neurosity import NeurositySDK

neurosity = None

def setup(device_id, email, password):
    global neurosity
    neurosity = NeurositySDK({"device_id": device_id})
    neurosity.login({
        "email": email,
        "password": password
    })

def register_kinesis(label, callback):
    return neurosity.kinesis(label, callback)
