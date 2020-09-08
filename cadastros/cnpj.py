def validar_cnpj(cnpj):
       if (not cnpj):
           return True
       if (len(cnpj) < 14):
           return False
       s = ''
       for n in cnpj:
           if n in('1234567890'):
              s = s+n
       cnpj = s       
       k = 0
       novo = []
       while k < 12:
           novo.append(int(cnpj[k]))
           k = k+1
         
       prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

       while len(novo) < 14:
           r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
           if r > 1:
               f = 11 - r
           else:
               f = 0
           novo.append(f)
           prod.insert(0, 6)

       calculado = ''
       for k in novo:
           calculado = calculado + str(k) 

       if calculado == cnpj:
          return True
       else:
          return False

#--------------------------------------------------------------------------------------

def validar_cpf(cpf):
       if (not cpf) or (len(cpf) < 11):
           return False
       k = 0
       novo = []
       while k < 9:
           novo.append(int(cpf[k]))
           k = k+1
         
       prod = [10, 9, 8, 7, 6, 5, 4, 3, 2]

       while len(novo) < 11:
           r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
           if r > 1:
               f = 11 - r
           else:
               f = 0
           novo.append(f)
           prod.insert(0, 11)

       calculado = ''
       for k in novo:
           calculado = calculado + str(k) 

      # Se o número gerado coincidir com o número original, é válido
       if calculado == cpf:
          return True
       else:
          return False

#--------------------------------------------------------------------------------------

