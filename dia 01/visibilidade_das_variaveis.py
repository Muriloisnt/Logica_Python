GLOBAL_VAR = 'valor global'
def exemplo_local():
 
    # variavel local - só existe dentro desta funçao
 
    local_var = 'valor local'
    print('local_var:', local_var)

    # acessar variavel global para leitura funciona sem declarar ´global´

    print('GLOBAL_VAR:', GLOBAL_VAR)

    #Usar um built-in (len)

    print('built-in len(\'abc\'):', len('abc'))

def exemplo_modifica():
    
    # para modificar a variavel global dentro da funçao, declarar `global`

    global GLOBAL_VAR
    GLOBAL_VAR = 'novo valor global'
    print('GLOBAL_VAR modificando para:', GLOBAL_VAR)

print('GLOBAL_VAR(antes):', GLOBAL_VAR)
exemplo_local()
exemplo_modifica()
print('GLOBAL_VAR (depois):', GLOBAL_VAR)