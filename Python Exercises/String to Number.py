import string

def alphabet_position(text):
    final= []
    alph=[string.ascii_letters]
    val= 1
    for i in alph:
        i = val
        val= val + 1
        if i == "A":
            val = 1
            i = val
            val = val + 1
    for i in text:
         final.append(*i)
    print(str(final)) 

alphabet_position("ABCd")