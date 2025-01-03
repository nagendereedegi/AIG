'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode('utf-8'))
        return True
    except Exception as e:
        return False

def main():
    print("[+] Beginning brute force attack")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                password = line.strip()  # Remove any leading/trailing whitespace
                print(f"[-] Trying password: {password}")
                if attempt_extract(zf, password):
                    print(f"[+] Success! Password found: {password}")
                    return
    print("[-] Password not found in list")

if __name__ == "__main__":
    main()