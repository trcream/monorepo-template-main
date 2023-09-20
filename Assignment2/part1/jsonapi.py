import json 

# Subclass of json.JSONEncoder
class BeautifulEncoder(json.JSONEncoder):
    # We are override default from json.JSONEncoder
    # This allows us to do custom encoding 
    def default(self, obj):
        # First we need to get the type of the object
        name = type(obj).__name__
        print(f"The type of the object is {name}")
        # .__name__ is the name of the class
        try:
            # Try to find a custom encoder for the object type
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            # If there is no custom encoder use the default from the parent class
            print("Super is getting called")
            super().default(obj)
        else:
            # Use the custom encoder if we have one
            encoded = encoder(obj)
            # Tag the encoded object with the special key 
            encoded["__extended_json_type__"] = name
            print("The encoded object is: ", encoded)   
            return encoded

    # Encode complex objects
    def encode_complex(self, obj):
        print("Running encode_complex")
        return {"real" : obj.real, "imag" : obj.imag}
    
    def encode_range(self,obj):
        print("Running encode_range")
        return {"start" : obj.start, "stop" : obj.stop, "step" : obj.step }
    
    def dumps(self, obj, **kwargs):
        print("Running custom dumps")
        return json.dumps(obj, cls=BeautifulEncoder, **kwargs)
        


class BeautifulDecoder(json.JSONDecoder):
    # Extend the default decoder to handle complex and range objects
    def __init__(self, **kwargs):
        # Set object hook to our custom object hook
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)
    
    def object_hook(self,obj):

        try:
            # Getting the type of the object
            name = obj.get("__extended_json_type__")
            # Getting our custom decoder
            decoder = getattr(self,f"decode_{name}")
        except(KeyError, AttributeError):
            # No custom decoder so use default
            return obj 
        else:
            # Use custom decoder
            return decoder(obj)
        
    def decode_complex(self,obj):
        print("Running decode_complex")
        return complex(obj["real"], obj["imag"])
    
    def decode_range(self,obj):
        print("Running decode_complex")
        return range(obj["start"], obj["stop"], obj["step"])
    
    def loads(self,obj, **kwargs):
        print("Running custom loads")
        return json.loads(obj, cls=BeautifulDecoder)

