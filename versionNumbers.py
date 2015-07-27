__author__ = 'cenk'


def compareVersion(version1, version2):
    v1 = version1.split(".")
    v2 = version2.split(".")

    longest = max(len(v1),len(v2))

    if len(v1) < longest:
       i = 0
       le = len(v1)
       while i < longest - le:
            v1.append('0')
            i += 1

    elif len(v2) < longest:
        i = 0
        le = len(v2)
        while i < longest - le:
            v2.append('0')
            i += 1

    i = 0
    while i < longest:
        if int(v1[i]) < int(v2[i]):
            return -1
        elif int(v1[i]) > int(v2[i]):
            return 1
        i += 1

    return 0

print compareVersion("13.37.4","13.37.4.0.0.0.0.0")