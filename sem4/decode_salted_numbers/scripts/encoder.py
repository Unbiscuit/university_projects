import hashlib

def encode(hash_type):
    with open('outputs/numbers', 'r') as numbers_file:
        with open('outputs/salt', 'r') as salt_file:
            with open(f'outputs/{hash_type}_hashes', 'w') as encoder:
                salt = salt_file.readline().replace('\n', '')
                for number in numbers_file:
                    string = (str(int(number.replace('\n', '')) + int(salt))).encode()
                    if hash_type == 'sha512':
                        hash = hashlib.sha512(string).hexdigest()
                    if hash_type == 'sha256':
                        hash = hashlib.sha256(string).hexdigest()
                    if hash_type == 'sha1':
                        hash = hashlib.sha1(string).hexdigest()
                    if hash_type == 'md5':
                        hash = hashlib.md5(string).hexdigest()
                    encoder.write(hash)
                    encoder.write('\n')

if __name__ == "__main__":
    hash_type = 'sha512'
    encode(hash_type)