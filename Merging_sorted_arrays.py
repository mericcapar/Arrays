#Sirali bir sekilde verilmis iki farkli listeyi tek bir listede siralanmis bir sekilde birlestirebilir misin?

#Ornek olarak array1 = [1,3,5,7] ve array2 = [2,4,6,8]
#Bunlari birlestirip siraladigin zaman [1,2,3,4,5,6,7,8] elde etmen gerekli.


def merge(array1 , array2):
    new_array = []
    i ,j = 0 , 0

    while i<len(array1) and j<len(array2):
        if array1[i] > array2[j]:
            new_array.append(array2[j])
            j+=1
        else:
            new_array.append(array1[i])
            i+=1

    new_array.extend(array1[i:])
    new_array.extend(array2[j:])

    return new_array

array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]

sonuc = merge(array1,array2)
print(sonuc)

#Ile cozum saglayabiliriz.

