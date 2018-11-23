"""Level 1"""
alpha = list("abcdefghijklmnopqrstuvwxyzab")
#print(alpha.index('f'))
#print(alpha[7])

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmg\
le gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.\
kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
char = list(text)
solution = []
for i in char:
    if i in alpha:
        i = alpha[alpha.index(i)+2]
    solution.append(i)
print(''.join(solution))

table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print(text.translate(table))
