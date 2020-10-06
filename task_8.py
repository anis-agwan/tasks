# Task 8

# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".
import zlib

def comp(s):
    t = zlib.compress(s.encode())
    return t

def decomp(t):
    s = zlib.decompress(t)
    return s

if __name__ == "__main__":        
    string = input('Enter string: ')
    comp_str = comp(string)
    decomp_str = decomp(comp_str)

    print (comp_str)
    print (decomp_str)