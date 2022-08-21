from core.erp.models import *
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(1,6000):
    name = ''.join(random.choices(letters,k=5))
    while Category.objects.filter(name=name).exists():
        name = ''.join(random.choices(letters,k=5))
    Category(name=name).save()
    print('Guardado registro {}'.format(i))