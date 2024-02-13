# Blood Pressure Fields
# int1/int2-int3 --> [systole,diastole,pulse]
#
def sysdia(sdp):
    z=sdp.split('-')[0].split('/')
    return z
def mmddhhmm(dt):
    d = dt[2:4] + '/' + dt[4:6]
    t = dt[7:9] + ':' + dt[9:11]
    #print([d,t])
    return([d,t])
def gbp(bp):
    try   : return f'{bp[0]:3}/{bp[1]:<3}'
    except: return 7*' '
def get_bp(i,j):
    return fbp(lines[i][j])

def fbp(x): # x = '' or sss/ddd -> 7 chars
    if x == '': return 7*' '
    y = ['***','**']
    try   : y = x.split('-')[0].split('/') # y = [s,d]
    except: return 7*'*'
    finally: return f'{y[0]}/{y[1]:3}'

print(1,fbp(''))
print(2,fbp('130/23'))
#print(3,fbp('c'))