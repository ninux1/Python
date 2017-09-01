"""
In python when you open the file in "with" block the file automatically closes on exit of with block
However if the file is opened without the "with" block it stays open till you close the file pointer explicitly.

"""

python JSON encoder and decoder

1) json.load(valid json opened file pointer) loads/decodes a json file directly into a python dictionary data structure
2) json.dump(python dict, file open for writing) directly encodes python dictionary into a json file

3) json.loads(opened json file) reads/decodes string formatted json object to python dictionary
4) json.dumps(python dictionary)  encodes python data structure to json string format.