
#Arrayler data structures konusunda oldukca fazla kullanilir.
#Static ve Dynamic olmak uzere iki cesit array vardir.
#Static arraylerde kullandiklari ve belirlenen alan kisitli olurken dynamic arraylerde boyle bir durum yoktur.
#Python da sadece dynamic arrayler vardir.

#Look-up/Accses - O(1)
#Push/Pop - O(1) *
#Insert - O(n)
#Delete - O(n)

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


#Look-up/Access
#Herhangi bir array elemanina index i ile birlikte erisebiliriz.
first_index = array[0] #O(1)
last_index =array[-1] #O(1)

#Push ve pop dedigimiz komutlar da oldukca benzerdir.
#Python dynamic bir dil oldugu icin genelde push yerine append kullanilir.

array.insert(0,15) #Insert komutunda index  belirtiriz. O(n)

array.append(167) #Append komutunda herhangi bir index belirtilemez ve listenin direkt olarak sonuna ekledigimiz icin time complexity O(1) olur.


#Silme Islemleri

#Insert in tersi olarak bu sefer istedigimiz yerden bir eleman siler. Elemanlar silindikten sonra bir kayma olacagi icin bir dongu olur bu yuzden
#Time complexity O(n) olur.

array.remove(2) #Burada da bir kayma olacagi icin Time complexity O(n) olur.
array.pop(0) #Eger ki bos yerine bir deger verirsek time complexity O(n) olur. Bunun sebebi array deki tum elemanlarin bir kaymasi gerektigindendir.
array.pop() #Bu sekilde olursa time complexity O(1) olur. Herhangi bir kayma soz konusu degil. Sadece son eleman cikarildi ve arraylerde herhangi bir kayma olmadi.
array.pop()


print(array)

