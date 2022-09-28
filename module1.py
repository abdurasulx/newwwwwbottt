'''import db
import var
c=var.product[10]
djb=db.Database('products.db')
for i in range(1,9):
    djb.set_lavsh(12250,c+str(i))
    #djb.add(c+str(i))

product=db.mahsulotlar('products.db')
a=product.get_price(1,var.products[4])
print(a)
product=db.mahsulotlar('products.db')
a=product.get_name(1,'Pitsalar')
print(a)'''
from geopy.distance import geodesic as GD
#40.728988, 72.760369
qurgantepa1=(   40.728059, 72.762855)
q2=(40.754341, 72.754986)
print(GD(qurgantepa1,q2).m)