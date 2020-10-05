f=lambda x:m.atan(x-m.e)

f_linha=lambda x:1/(1+(x**2) - (m.e*2*x) + (m.e**2))

def grafico(a,b,f,raiz,funcao):
    """Essa é a função criada com o objetivo único de esboçar o gráfico da função escolhida no interválo escolhido, ela recebe parâmetros com base na função e interválo escolhidos"""
    listax=myRange(a if f(a)<f(b) else b,a if f(a)>f(b) else b,0.01)
    y = myMap(f, listax)
    fig2=plt.figure(figsize=(10,5))
    bx=fig2.add_subplot(111)
    bx.plot(listax, y)
    bx.grid(True)
    bx.set_xlabel("x", fontsize=14)
    bx.set_ylabel("y", fontsize=14)
    bx.plot(raiz, 0, 'co')
    #Condicionais para definir o título do gráfico da função
    if funcao=="f":
        bx.text(raiz-0.1,0.1,"Raiz",fontsize=14)
        bx.set_title(r'$f(x) = arc tan(x-e)$', fontsize = 14)      
    elif funcao=="g":
        bx.text(raiz-0.04,0.15,"Raiz",fontsize=14)
        bx.set_title(r'$f(x) = tan(x)$', fontsize = 14)  
    else:
        bx.text(raiz-0.04,0.15,"Raiz",fontsize=14)
        bx.set_title(r'$f(x) = x^2-e$', fontsize = 14)
    plt.show()
        

grafico(-5,10,f,m.e,"f")


#Implementação do método da Bisseção
def bissecao(a,b,f,lim=50,tol=10**-15,lA=[],r1=[],i1=0,erro=[]):
    """Essa é a função que implementa o metodo da Bisseção, afim de aproximar a raiz de f(x)"""
    if i1==lim:
        return r1,erro
    elif abs((a-b)/2)<tol:
        return r1+[(b+a)/2],erro+[abs((a-b)/2)]
    else:
        if f(a)*f(b)<0:
            return bissecao((b+a)/2,b,f,lim,tol,lA+[a],r1+[(b+a)/2],i1+1,erro+[abs((a-b)/2)])
        else:
            return bissecao(lA[i1-1],a,f,lim,tol,lA,r1,i1,erro)
            
           
#Implementação do metodo de Newton-Raphson.
def raphson(p,f,dx,lim=50,tol=10**-15,r2=[],i2=0,erro=[]):
    """Essa é a função que implementa o metodo de Newton-Raphson, afim de aproximar a raiz de f(x) usando sua derivada"""
    if i2==lim:
        return r2,erro
    elif abs(((p-(f(p)/dx(p)))-p)/(p-(f(p)/dx(p))))<tol:
        return r2 + [p-(f(p)/dx(p))],erro + [abs(((p-(f(p)/dx(p)))-p)/(p-(f(p)/dx(p))))]
    else:
        return raphson(p-(f(p)/dx(p)),f,dx,lim,tol,r2+[p-(f(p)/dx(p))],i2+1,erro+[abs(((p-(f(p)/dx(p)))-p)/(p-(f(p)/dx(p))))])    
        
        
#Implementação do Metodo da Secante.
def secante(x1,x2,f,lim=50,tol=10**-15,r3=[],i3=0,ind=0,erro=[]):
    """Essa é a função que implementa o metodo da Secante para aproximar a raiz de f(x)"""
    if i3==lim:
        return r3,erro
    elif abs(((x1-(f(x1)*(x1-x2))/(f(x1)-f(x2)))-x1)/(x1-(f(x1)*(x1-x2))/(f(x1)-f(x2))))<tol:
        return r3 + [x1-(f(x1)*(x1-x2))/(f(x1)-f(x2))] , erro + [abs(((x1-(f(x1)*(x1-x2))/(f(x1)-f(x2)))-x1)/(x1-(f(x1)*(x1-x2))/(f(x1)-f(x2))))]
    else:
        return secante(x1-(f(x1)*(x1-x2))/(f(x1)-f(x2)),x1,f,lim,tol,r3+[x1-(f(x1)*(x1-x2))/(f(x1)-f(x2))],i3+1,ind+1,erro+[abs(((x1-(f(x1)*(x1-x2))/(f(x1)-f(x2)))-x1)/(x1-(f(x1)*(x1-x2))/(f(x1)-f(x2))))])
        
        
        
        
def myRange(inicio,fim,step=0.001,listax=[]):
    """Essa função é uma das auxiliares usadas para o esboço do gráfico"""
    if round(inicio,1)>fim:
        return listax
    else:
        return myRange(inicio+step,fim,step,listax+[round(inicio,1)])
    
    

def myMap(f, listax, V = []):
    """Essa função é uma das auxiliares usadas para o esboço do gráfico"""
    if len(listax)==0:
        return V
    else: 
        a=f(listax[0])
        return myMap(f,listax[1:],V+[a])

    
def grafico(a,b,f,raiz,funcao):
    """Essa é a função criada com o objetivo único de esboçar o gráfico da 
    função escolhida no interválo escolhido, ela recebe parâmetros com base na função e interválo escolhidos"""
    listax=myRange(a if f(a)<f(b) else b,a if f(a)>f(b) else b)
    y = myMap(f, listax)
    fig2=plt.figure(figsize=(10,5))
    bx=fig2.add_subplot(111)
    bx.plot(listax, y)
    bx.grid(True)
    bx.set_xlabel("x", fontsize=14)
    bx.set_ylabel("y", fontsize=14)
    bx.plot(raiz, 0, 'co')
    #Condicionais para definir o título do gráfico da função
    if funcao=="f":
        bx.text(raiz-0.1,0.1,"Raiz",fontsize=14)
        bx.set_title(r'$f(x) = arc tan(x-e)$', fontsize = 14)      
    elif funcao=="g":
        bx.text(raiz-0.04,0.15,"Raiz",fontsize=14)
        bx.set_title(r'$f(x) = tan(x)$', fontsize = 14)  
    else:
        bx.text(raiz-0.04,0.15,"Raiz",fontsize=14)
        bx.set_title(r'$f(x) = x^2-e$', fontsize = 14)
    plt.show()
        

        
def comparacao(a,b,f,derivada,lim):
    """Essa função esboça o gráfico comparando o desempenho de cada metódo utilizado"""
    raiz1,erros1 = bissecao(a if f(a)>f(b) else b,b if f(b)<f(a) else a,f,lim)
    raiz2,erros2 = raphson(a if f(a)>f(b) else b,f,derivada,lim)
    raiz3,erros3 = secante(a if f(a)>f(b) else b,b if f(b)<f(a) else a,f,lim)
    x1=myRange(1,len(raiz1),1)
    x2=myRange(1,len(raiz2),1)
    x3=myRange(1,len(raiz3),1)
    
    ###############################################################################################
    #Gráfico 1
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(111)
    ax.plot(x1, raiz1, label='Método da Bisseção',       lw=2, markersize=8, color='#9467BD', marker='D', markeredgecolor='#9467BD', markerfacecolor='#C9B3DE')
    ax.plot(x2, raiz2, label='Método de Newton-Raphson', lw=2, markersize=8, color='#1F77B4', marker='o', markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
    ax.plot(x3, raiz3, label='Método da Secante',        lw=2, markersize=8, color='#D62728', marker='s', markeredgecolor='#D62728', markerfacecolor='#EA9393')
    ax.grid(True)
    ax.set_ylabel("f(x)", fontsize = 14)
    ax.set_title("Aproximação da raiz da função por cada método", fontsize = 14)
    ax.set_xlabel("Interações",fontsize=14)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, bbox_to_anchor=(1, 1), loc=1, borderaxespad=0)
    plt.show()
    
    ###############################################################################################
    #Gráfico 2
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(111)
    ax.plot(x1, erros1, label='Método da Bisseção',       lw=2, markersize=11, color='#00b300', marker='p', markeredgecolor='#00b300', markerfacecolor='#80ff80')
    ax.plot(x2, erros2, label='Método de Newton-Raphson', lw=2, markersize=11, color='#cc7a00', marker='H', markeredgecolor='#cc7a00', markerfacecolor='#ffb84d')
    ax.plot(x3, erros3, label='Método da Secante',        lw=2, markersize=11, color='#000099', marker='d', markeredgecolor='#000099', markerfacecolor='#4d4dff')
    ax.grid(True)
    ax.set_ylabel("Erro", fontsize = 14)
    ax.set_title("Variação do erro em cada método", fontsize = 14)
    ax.set_xlabel("Interações",fontsize=14)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, bbox_to_anchor=(1, 1), loc=1, borderaxespad=0)
    plt.show()
    
    ###############################################################################################
    #Gráfico 3
    fig3, cx = plt.subplots(figsize=(10, 5))
    eixox=[1,2,3]
    eixoy=[len(raiz1),len(raiz2),len(raiz3)]

    
    cx.bar(eixox, eixoy, color='#1F77B4')

    cx.set_xlabel('Métodos', fontsize = 14)
    cx.set_ylabel('Interações', fontsize = 14)
    cx.set_title('Interações necessarias em cada método', fontsize = 14)
    cx.set_axisbelow(True) 
    cx.yaxis.grid(True)
    cx.set_xticks(eixox)
    cx.set_xticklabels(('Método da Bisseção', 'Método de Newton', 'Método da Secante'))
    plt.ylim(0, lim+2)
    plt.show()


def imprime(l1,l2,i=0):
    """Essa função imprime as tabelas com os erros e raízes por interação de cada método"""
    if i==0:
        print(" ____________________________________________")
        print("|  i |       Raiz        |        Erro       |")
        return imprime(l1,l2,i+1)
    elif len(l1)==i-1:
        print("|____________________________________________|")
    else:
        print("| {:02.0f} | {:.15f} | {:.15f} |".format(i,l1[i-1],l2[i-1]))
        return imprime(l1,l2,i+1)
        
        
        
        
 def main():
    """A main executa todas as outras funções ,lista o desempenho de cada uma, e plota o gráfico da função escolhida no interválo escolhido"""
    funcao=input("Função escolhida: ")
    b=float(input("Primeiro ponto do interválo: "))
    a=float(input("Segundo ponto do interválo: "))
    print("Interválo: [{},{}]".format(min(b,a),max(b,a)))
    lim=int(input("Máximo de interações: "))
    if funcao=="f":
        t1,t2=bissecao(a if f(a)>f(b) else b, b if f(b)<f(a) else a,f,lim)
        u1,u2=raphson(a if f(a)>f(b) else b,f,f_linha,lim)
        v1,v2=secante(a if f(a)>f(b) else b, b if f(b)<f(a) else a,f,lim)
        grafico(a,b,f,m.e,funcao)
        comparacao(a,b,f,f_linha,lim)
    elif funcao=="g":
        t1,t2=bissecao(a if f(a)>f(b) else b, b if f(b)<f(a) else a,g,lim)
        u1,u2=raphson(a if f(a)>f(b) else b,g,g_linha,lim)
        v1,v2=secante(a if f(a)>f(b) else b, b if f(b)<f(a) else a,g,lim)
        grafico(a,b,g,m.pi,funcao)
        comparacao(a,b,g,g_linha,lim)
    else:
        t1,t2=bissecao(a if f(a)>f(b) else b, b if f(b)<f(a) else a,h,lim)
        u1,u2=raphson(a if f(a)>f(b) else b,h,h_linha,lim)
        v1,v2=secante(a if f(a)>f(b) else b, b if f(b)<f(a) else a,h,lim)
        grafico(a,b,h,m.sqrt(m.e),funcao)
        comparacao(a,b,h,h_linha,lim)
    print("\n        Metodo da Bisseção a={} b={}       ".format(a,b))
    imprime(t1,t2)
    print()
    print("\n        Metodo de Newton-Raphson x1={}       ".format(max(a,b)))
    imprime(u1,u2)
    print()
    print("\n        Metodo da Secante x1={} x2={}       ".format(a,b))
    imprime(v1,v2)
      
