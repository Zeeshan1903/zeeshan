def capitalizing(s):
    a = chr(ord(s[0])+ord('A')-ord('a'))
    
    for i in range(len(s)):
        if( i != 0):
            a+=s[i]
    return a

print(capitalizing('stringF'))
import time
st = time.time()
##Find operator Code for finding the substring from the string 
def makeString(s,start,len):
    a = ''
    for i in range(len):
        a+=s[start+i]
    return a
print(makeString('string',2,3))

def finding(s,find):
    checkString = ''
    for i in range(len(s)):
        try:
            checkString = makeString(s,i,len(find))
            if(checkString == find):
                return i
                
        except:
            return -1
print(finding('absdfsdsdfsdfsdfjkljljkljkljkljlkjkljjnknknknnkernknkdnkngkngngkngnelnnnlnnknnvgvrfvnninvninisdfasdfsdfsadfsdfasdfasdfsdafsadba','ba'))
et = time.time()
print(et-st)