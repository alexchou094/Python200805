d = { 'phone' : '0912345678',
      'height' : '170',
      'weight' : '60'
}
print(d)   
d[ 'a' ] = '2020'
print(d)
bday = d.pop( 'a' )
d2 = { 'phone' : '0987654321',
       'height' : '175',
       'weight' : '65',
}
d.update(d2)
print(d)

