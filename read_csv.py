import csv
# from pprint import pprint
#dicts https://realpython.com/python-dicts/#:~:text=Built%2Din%20Dictionary%20Methods,-As%20with%20strings%20and%20lists

ff = [1]
# Formats
def ltime(x): return f'{x}'  # 11 chars



def fbp(bp):       # returns string aaa/aaa
    try   : return f'{bp[0]:3}/{bp[1]:<3}'
    except: return 7*' '
def get_bp(i,j):   # returns string aaa/aaa
    #print(i,j)
    return sysdia(lines[i][j])
def sysdia(sdp):   # returns [alpha,alpha]
    if sdp in ['','out']: return 0
    z=sdp.split('-')[0].split('/')
    return [int(z[0]),int(z[1])]
    #return z
def get_weight(i): # returns 5 alpha
    if lines[i][1] == '': return '     '
    #print(f'{lines[i][1]:5}')
    return f'{lines[i][1]:5}'
def bp_avg(j):
    n = 0 # sample size
    s = 0 # sys total
    d = 0 # dia total
    for i in range (nlines-1):
        v = bp.get((i,j),0)
        if v:
            s = s + v[0]
            d = d + v[1]
            n = n + 1
    return [round(s/n),round(d/n)]



# Begin Execution

if __name__ == '__main__':

    # lines[_] is list of alpha strings
    with open(r"C:\Users\ronwi\Downloads\__Daily Numbers - data.csv", newline='') as sheet:
        reader = csv.reader(sheet)
        lines = [line for line in reader]
    nlines = len(lines)

    # show lines for debug
    for line in lines:
        print(line)
    print()

    for i in range(1,nlines):
        oput = lines[i][0] + ' ' + get_weight(i) + ' '
        for j in range (1,5+1):
            s = lines[i][j+1] #.split('-')[0].split('/')
            oput = oput + s + ' '
 #        # line = [get_bp(i,j) for j in [1,2,3,4,5]]
 #       # print(i,line)
        print(oput)

    # build bp dict
    bp = {}
    for i in range (nlines-1):
        for j in [1,2,3,4,5]:
            #bp[i+1,j] = get_bp(i+1,j+1)
            x = get_bp(i+1,j+1)
            if x: bp[i+1,j] = x
    pass # for debug log


    print()

    for j in [1,2,3,4,5]:
        print(f'bp avg {j} = {bp_avg(j)}')
 