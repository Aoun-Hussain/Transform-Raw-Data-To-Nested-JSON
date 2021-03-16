import json
​import logging

data = {}
record_key = ''
record_body = {}
record_number = 0
​
f_write = open("output.json", "w")
f_read = open("sample_products.TXT", "r")
​
for x in f_read:
  # Remove leading and trailing spaces  
  x = x.strip()
​
  if len(x.split()) == 0:
    print("Skiipinh empty line")
    continue
  print("Processing new line in a file")
  print(f">>{x}<<")
  if x == "REC$$":
    #old record completed
    record_number += 1
    print(f"adding a new product record {record_number}")
    print(f"Record_ID>>{record_key} | Record_Body>>")
    print(record_body)
    f_write.write('{"index":{"_index":"sample","_type":"sample","_id":"'+record_key+'"}}\n')
    f_write.write(json.dumps(record_body) + "\n")
    print("Refreshing old values")
    record_key = ''
    record_body = {}
  else:
    key,value = x.split("=", 1)
    if key == "refNum":
      record_key = value
    record_body[key] = value
    
f_write.close()
f_read.close()
