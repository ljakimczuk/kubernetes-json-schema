#!/usr/bin/python3.6

import os
import json
import sys
import string

def checkForFormat(schema,parent):
  if type(schema) is dict and schema:
    for key in list(schema):
      if key == "description" and type(schema[key]) is not dict:
        if schema[key].find("DNS_LABEL") > -1:
          if "format" not in schema:
            schema["format"] = "hostname"
      checkForFormat(schema[key],schema)
  elif type(schema) is list and schema:
    for entity in schema:
      checkForFormat(entity,schema)

def main():
  for filename in os.listdir("."):
    if filename.endswith(".json"):
      with open(filename, "r") as f:
        print("Checking",filename)
        schema = json.load(f)
        checkForFormat(schema,None)
        
      os.remove(filename)
      with open(filename, "w") as f:
        json.dump(schema,f,indent=2)
        f.write("\n")

if __name__ == "__main__":
  main()
