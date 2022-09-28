from geopy.distance import geodesic as GD
#40.728988, 72.760369
def get_metres(seond):
    qurgantepa1=(   40.728059, 72.762855)
    #q2=(40.754341, 72.754986)
    return  int(GD(qurgantepa1,second).m)