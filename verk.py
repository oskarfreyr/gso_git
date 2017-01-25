#Óskar Freyr
#25.01.17

skra = input("sláðu inn nafn á skrá")
nafnskra = skra + ".txt"
SkrainMin = open(nafnskra, 'w+')

SkrainMin.write("Fyrsta Línan Í skránni"'\n')
SkrainMin.close()

lina1 = input("Skráðu inn línu eitt")
lina2 = input("Skráðu inn línu tvö")
lina3 = input("Skráðu inn línu þrjú")
SkrainMin = open(nafnskra, 'a')
SkrainMin.write(lina1 + '\n')
SkrainMin.write(lina2 + '\n')
SkrainMin.write(lina3 + '\n')
SkrainMin.close()
SkrainMin = open(nafnskra, 'r')
print("")
print(SkrainMin.read())
