import json

rec_key = ''
rec_body = {}
rec_num = 0
key_array = []
temp = {}
keys = []
flag = False


f_read = open("sample_products.TXT", "r")
f_write = open("output.json", "w")


for line in f_read:
    line = line.strip()                    ##removing leading and trailing space characters

    if len(line.split()) == 0:
        continue

    if line == "REC$$":
        f_write.write('\n')
        f_write.write(str({rec_key:rec_body})+'\n')
        rec_key = ''
        rec_body = {}
        keys = []
    else:
        key, value = line.split("=")      ##splitting the line with = as pivot to give key and value
        if key == "refNum":
            rec_key = value
        if key.find('_') == -1:
            flag = False                  ##False if nested key is not found
        else:
            key_array = key.split('_')
            key = key_array[0]
            flag = True
        if value == '':                   ##Assign NULL value if empty
            value = 'NULL'
        if (flag and (key not in keys)):
            temp[key_array[1]] = value
            rec_body[key] = temp
            temp = {}
            flag = False
        elif flag:
            rec_body[key][key_array[1]] = value
            flag = False
        elif not flag:
            rec_body[key] = value
        keys.append(key)
        
f_write.close()
f_read.close()


