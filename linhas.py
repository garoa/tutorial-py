
with open('euro.py') as fp:

    for lin in fp:
        lin = lin.strip()
        if not lin or lin.startswith(x):
            continue
        print '>>>', lin

