import math
an = float(input(' coloque a seguir o angulo de seu triangulo: '))
sen = math.sin (math.radians(an))
cos = math.cos (math.radians(an))
tg = math.tan(math.radians(an))
print(' a partir do angulo enviado, o seu trabgulo possui o sen {:.2f} cos {:.2f} e tan {:.2f}'.format(sen, cos, tg))