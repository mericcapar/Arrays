class MyArray():
    def __init__(self):
        # Dizinin başlangıç uzunluğunu 0 olarak belirledik.
        self.length = 0
        # Dizideki elemanları burada tutacağız. Boş bir dictionary kullandık aslında.
        self.data = {}

    def __str__(self):
        # Dizi sınıfının uzunluk ve data bilgilerini string olarak döndürecek.
        return str(self.__dict__)

    def get(self, index):
        # Belirtilen index'teki elemanı getirir.
        return self.data[index]

    def push(self, item):
        # Dizinin sonuna eleman ekler.
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        # Son elemanı bulur.
        last_item = self.data[self.length - 1]
        # Son elemanı siler.
        del self.data[self.length - 1]
        # Uzunluğu bir azaltır.
        self.length -= 1
        # Çıkarılan elemanı gösterir.
        return last_item

    def insert(self, index, item):
        # Uzunluğu bir arttırır.
        self.length += 1
        # Dizideki her elemanı istenen kadar sağa kaydırır.
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        # İstenen yere O(n) zamanda elemanı ekler.
        self.data[index] = item

    def delete(self, index):
        # İstenen eleman için elemanları sola kaydırır.
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        # Dizide kalan son elemanı siler.
        del self.data[self.length - 1]
        # Uzunluğu bir azaltır.
        self.length -= 1

# Örnek kullanım
arr = MyArray()
arr.push(6)
print(arr)  # {'length': 1, 'data': {0: 6}}

arr.push(2)
print(arr)  # {'length': 2, 'data': {0: 6, 1: 2}}

arr.push(9)
print(arr)  # {'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()
print(arr)  # {'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)
print(arr)  # {'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 12, 4: 67}}

arr.insert(3, 10)
print(arr)  # {'length': 6, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 12, 5: 67}}

arr.delete(4)
print(arr)  # {'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 67}}

print(arr.get(1))  # 2
