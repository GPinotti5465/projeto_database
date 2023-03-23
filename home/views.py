from django.shortcuts import render, redirect
import globalarch.package.functions as func
import psycopg2 as pgre



# INDEX---------------------------


def index(request):

    if request.method == 'POST':
        # PEGANDO VARIÁVEIS DO HTML
        name = request.POST['name']
        cpfcnpj = request.POST['cpfcnpj']
        cep = request.POST['cep']
        inativo = request.POST['valuecontrato']

        request.POST=None
        request._load_post_and_files()

        cepinvalido=False;cpfcnpjinvalido=False
        # VERIFICAÇÃO
        if func.cepsearch(cep) == 'false':
            cepinvalido=True
        cep = func.filtnum(cep)

        if func.modulo11cnpj(cpfcnpj) == 'VÁLIDO':
            cpfcnpj = func.filtnum(cpfcnpj)
        elif func.modulo11cpf(cpfcnpj) == 'VÁLIDO':
            cpfcnpj = func.filtnum(cpfcnpj)
        else:
            cpfcnpjinvalido=True


        if cepinvalido and cpfcnpjinvalido:
            return render(request, 'homewithhud.html', {'cpfcnpjinvalido': True, 'cepinvalido': True})
        elif cepinvalido:
            return render(request, 'homewithhud.html', {'cepinvalido': True})
        elif cpfcnpjinvalido:
            return render(request, 'homewithhud.html', {'cpfcnpjinvalido': True})




        # establish a connection to the PostgreSQL database
        conn = pgre.connect(
            host="127.0.0.1",
            database="cienciae_db001",
            user="cienciaemp",
            password="ciencia#2023"
        )

        # create a cursor object to execute SQL queries
        cursor = conn.cursor()


        query = f"INSERT INTO logs (nome, cep, cpfcnpj, status) VALUES ('{name}', '{cep}', '{cpfcnpj}', '{inativo}')"
        cursor.execute(query)

        # commit the transaction
        conn.commit()

        # close the cursor and connection
        cursor.close()
        conn.close()



        #  LIMPAR LOG DO BROWSER

    return render(request, 'homewithhud.html')



