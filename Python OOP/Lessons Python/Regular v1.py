import re

s = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.match("AC",s) #ищет символ в начале строки
result = re.search("DC",s) # ищет 1 заданный символ в строке
result = re.findall("DC",s) # ищет все символы в строке
result = re.split("/",s,maxsplit=3) # разбивает символы по слешу и формирует список
result = re.sub("A", "D",s) # меняет А на D в строке
result = re.fullmatch("AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC",s) # сравнение строк
print(result)

t = "87+453543 --- kjgdfghdfldfph8667636^7  HGFDKJNOIHJijijoij"
result = re.search(r"\d\d\d",t) # выводит 3 цифры
result = re.search(r"\D",t)# выводит не цифры
result = re.search(r"\s",t)
result = re.search(r"\S",t)
result = re.search(r"\w",t)
result = re.search(r"\W",t)
result = re.search(r"\bHGF",t) # конец слова
result = re.search(r"\BHGF",t) # середина слова
result = re.search(r"\d*",t)
result = re.search(r"\d+",t)
result = re.search(r"[gjkjd]",t)
result = re.search(r"[^4-6]",t)
result = re.search(r"H|f",t)
result = re.search(r"\d{3}",t)
result = re.search(r"\d{1,3}",t)
result = re.search(r"\d{4,}",t)
result = re.search(r"\d{,4}",t)
m = "Привет! Как дела? А у меня нормально."
result = re.findall(r"[бвгдзклмнпрстфхчшщБВГДЗКЛМНПРСТФХЧШЩ]\w+", m)
print(result)