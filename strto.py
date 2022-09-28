a="['baklashka','tupoy','qo`y','lampa']"
def get_array(array):
    array=array[1:len(array)-1]
    s=array.split(',')
    return s
def get_str(string):
    s='['
    a=-1
    for i in string:
        a=a+1
        if a==0:
            s=s+i
        elif (a>0) and (len(string)>a):
            s=s+','+i
        elif a-1==len(string):
            s=s+','+i
    s=s+']'
    return s
