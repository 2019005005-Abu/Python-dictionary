# Nested List
list1=[1,2,34,[34,67,45],[10,200,56]];
lis2=['a','b',['c','d'],['e','f','g'],'8',100];
for i in range(len(list1)):
    print(list1[i]);
print(list1[3]);
print(list1[4]);

##Aliasinging List
a='python'
b=a;
b='python'
print(a);
print(b);
print(a is b);
lis2.append(100);
lis2.pop()
print(lis2);
print(lis2[:]);
# Dictionary
Dic={
'Name':'Rifat',
 'Age':5,
 'class':'Geade1',
 'Height':'3feet',
 'width':'2okg'
}
print(Dic);

dic1={
 'a1':'Vegetable & Fruits',
 'a2':'Frozen Foods',
 'a3':'Canned Food',
 'a4':'Baked Gods'
}
print(dic1);

dic3=dict([('Name','Rifat'),
           ('Profession','Software Enginner'),
           ('age',25)]);
print(dic3);

print(dic3['Name']);
print(dic3['age']);
print(dic3['Profession']);
dic3['Profession']='Software Enginner && Full stack developer';
print(dic3);

dic4={'country':['India','china','Indonesia']};
print(dic4['country'][0]);
print(dic4['country'][1]);
print(dic4['country'][2]);

dic5={'Type':{'Immutable':'string','Mutable':'List'}}
print(dic5);
print(dic5['Type']);

##Dictionary Methods
Dicc1={'name':"Rifat",'country':"Bangladesh"};
Dicc12={'capital':'Dhaka','Independent':'1971'}
print(Dicc1['name']);
print(Dicc1.clear);
print(dic4.get('country',-1));
print(dic4.get('r',-1));
print(Dicc1.items());
print(Dicc1.keys());
print(Dicc1.values());
print(Dicc1.pop('country'));
print(Dicc1.popitem());
print(Dicc1.update(dic5))
print(Dicc12['Independent']);
print(len(Dicc12));
print('name' in dic4);
print('capital' not in Dicc12);
print(dic4.keys());
print(dic5.values());

for i in dic1.keys():print(i);
for i in dic1.values():print(i);
for i in dic1.items():print(i);








