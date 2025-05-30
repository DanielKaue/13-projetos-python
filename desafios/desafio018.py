import math
an=float(input('Qual ângulo você deseja? '))
co=math.cos((math.radians(an)))
se=math.sin((math.radians(an)))
tan=math.tan((math.radians(an)))
print('O Seno é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}.'.format(se, co, tan))