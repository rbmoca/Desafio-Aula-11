import pandas as pd
#import numpy  as np

# valor = [1000., 5000., 50., 60., 40., 60., 60., 50., 60.0]
# regioes    = ['Sudeste', 'Norte', 'Sul']
# produtos   = ['Smartphone', 'Camisa', 'Arroz']

data = pd.DataFrame({
    'vendas':[1000, 2000, 3000, 50000, 9000, 7000, 8000],
    'vendedor':['CARLOS', 'FERNANDO', 'MARIA', 'MARTA', 'ELOYSA', 'CARMEM','PABLO']
})

data.to_csv('dados.csv', index=True)
print('Ação Realizada')
