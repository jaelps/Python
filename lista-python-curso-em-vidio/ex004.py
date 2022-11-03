algo = input('Digite algo:  ')
print('este item é do tipo', type(algo))
print('item identificado é numero ?', algo.isnumeric())
print('item identificado é letra ?', algo.isalpha())
print('item identificado é decimal ?', algo.isdecimal())
print('item identificado é menuscolo ?', algo.islower())
print('item identificado contem apenas espaço ?', algo.isspace())

