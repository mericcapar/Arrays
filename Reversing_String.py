#Bir stringi tersine ceviren bir fonksiyon yaz.
#"Merhaba" verildigi zaman "abahreM" olmali.

#Akla ilk gelen cozum genel olarak budur. Bize verilen ifadenin elemanlarini bir listede toplayip yeni olusturdugumuz array de saklayarak bu soruyu cozebiliriz.
def simple_reverse(string):
    new_string = []
    for i in range(len(string)-1 , -1 , -1):
        new_string.append(string[i])

    return ''.join(new_string)

string = "Merhaba benim adim Meric."
print(simple_reverse(string))
#String i sadece bir kere ters cevirdigimiz ve range fonksiyonunda loop a aldigimiz icin time complexity O(n) olur.


#Bir diger yapacagimiz sey ise string in her iki ucundan eleman alip yerlerini degistirmek olabilir.


def swap(string, a, b):  # Bu fonksiyon, bir dizinin içindeki iki karakteri değiştiren bir işlevdir.
    string = list(string)  # Verilen string'i bir karakter dizisinden liste tipine çeviriyoruz.
    temp = string[a]  # Geçici bir değişken kullanarak a ve b indekslerindeki karakterleri takas ediyoruz.
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)  # Değiştirilmiş listeyi tekrar birleştirerek yeni bir string olarak döndürüyoruz.

def smarter_reverse(string):
    for i in range(len(string)//2):  # Dizinin yarısına kadar olan indeksler üzerinde dönüyoruz.
        string = swap(string, i, len(string)-i-1)  # Her iterasyonda i ve len(string)-i-1 indekslerindeki karakterleri takas ediyoruz.
    return string

print(smarter_reverse(string))


#Bu da O(n) zaman karmasikligina sahiptir fakat ilk yazdigimiza gore daha basitlestirilmis halidir.

#Built-in fonksiyonlar kullanarak da buislemi yapabilirdik.


string1 = 'abcde'
string2 = reversed(string1)
print(''.join(string2))

list1 = list(string1)
list1.reverse()
print(''.join(list1))

#Bunlarda da time complexity O(n) olurdu.