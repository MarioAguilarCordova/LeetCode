eng = [73,9,30,44,130,28,16,35,74,2,3,35,25,78,74,27,3,77,63,93,27,13,16,5,19,1]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def clean(txt):
    return "".join([a.upper() for a in txt if a.isalpha()])
def encrypt_vig(ptxt, ky):
    cptxt = clean(ptxt)
    return "".join([alpha[(alpha.index(cptxt[i]) + alpha.index(ky[i%len(ky)]))%26] for i in range(len(cptxt))])
def decrypt_vig(ptxt, ky):
    cptxt = clean(ptxt)
    return "".join([alpha[(alpha.index(cptxt[i]) - alpha.index(ky[i%len(ky)]))%26] for i in range(len(cptxt))])
def score_text(txt):
    counts = [txt.count(a) for a in alpha]
    return sum(counts[i]*eng[i] for i in range(26))
def best_caesar_shift(ct):
    scores = [score_text(decrypt_vig(ct, a)) for a in alpha]
    return alpha[scores.index(max(scores))]
def best_vig_keyword(ct, length):
    return "".join([best_caesar_shift("".join([ct[i] for i in range(len(ct)) if i%length==p])) for p in range(length)])


def main():

    cipher_text = "EAQXA IOIEA FHXLF IMVBE WXHGE HFLEE HWWJR KPPWF WDBZB ZXYQB PMVGE WBKVK\\\nHJIBY MXHVW AAKGH VGBJI LBSQH BPMFE QBPIJ BEQTB NSBVV XRMFP MWAWN DHSGH\\\nBXSDM VMWVA TRGBJ BWKRD MEWFT PRKCI FBDDM EWFLV XLDQF ZXRZA BLXRW LPWLA\\\nIKHIM DXWVM DMSZI QVUMK MMPTP MVMLD MQXLH QLEHQ GGTHH LTWVS XEZJW PMWAK\\\nCLLLH EPMJP LHGSQ FMIUA EBKML DMSQD EPLDA TQUIE RZMUT JWXNE ZBGKA ATAVS\\"

    print(cipher_text, "\n")

    ct = clean(cipher_text)

    letter = best_caesar_shift(ct)

    print(letter, "\n")

    key = best_vig_keyword(ct,7)

    print(key, "\n")

    answer = decrypt_vig(cipher_text,key)

    print(answer, "\n")

main()