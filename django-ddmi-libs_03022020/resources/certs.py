import certifi

cafile = certifi.where()
with open('/opt/SHA256CAbundle.pem', 'rb') as infile:
    customca = infile.read()
with open(cafile, 'ab') as outfile:
    outfile.write(customca)