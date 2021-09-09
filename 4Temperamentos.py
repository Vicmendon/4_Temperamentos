import streamlit as st


def importLista(file):

    arquivo = open(file, 'r', encoding='UTF-8')
    lista = arquivo.readlines()  # readlinesssssss
    arquivo.close()
    # print(cpfs)

    questoes = []

    for x in lista:
        x = x.replace('\n', '')
        questoes.append(x)

    return questoes


def resposta(respostas):

    fleumatico = importLista('Fleumatico.txt')
    acertos_fleumatico = 0
    fleumatico = fleumatico[0].split(' ')

    colerico = importLista('Colerico.txt')
    acertos_colerico = 0
    colerico = colerico[0].split(' ')

    sanguineo = importLista('Sanguineo.txt')
    acertos_sanguineo = 0
    sanguineo = sanguineo[0].split(' ')

    melancolico = importLista('Melancolico.txt')
    acertos_melancolico = 0
    melancolico = melancolico[0].split(' ')

    for x in respostas:
        if x in fleumatico:
            acertos_fleumatico += 1
        if x in colerico:
            acertos_colerico += 1
        if x in sanguineo:
            acertos_sanguineo += 1
        if x in melancolico:
            acertos_melancolico += 1

    return acertos_fleumatico, acertos_colerico, acertos_sanguineo, acertos_melancolico


lista_questoes = importLista('questões.txt')

questoes = []

num_questao = 1

for x in lista_questoes:
    questao = {'num_questao': str(num_questao),
               'questao': x}
    num_questao += 1
    questoes.append(questao)


st.markdown("<h1 style='text-align: center; color: red;'>Teste de Temperamento 2.0</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'></h1>", unsafe_allow_html=True)


for pergunta in questoes:
    with st.container():
        st.checkbox(label=f'{pergunta["questao"]}', key=pergunta["num_questao"])


# st.checkbox(label=f'Teste de pergunta', key='pergunta1')
if st.button('Próximo', key='btn_calcular'):
    respostas = []
    for x in questoes:
        variable = st.session_state[x['num_questao']]
        if variable:
            respostas.append(x['num_questao'])

    acertos_fleumatico, acertos_colerico, acertos_sanguineo, acertos_melancolico = resposta(respostas)

    st.text(f'COLÉRICO: {acertos_colerico}')
    st.text(f'FLEUMÁTICO: {acertos_fleumatico}')
    st.text(f'SANGUÍNEO: {acertos_sanguineo}')
    st.text(f'MELANCÓLICO: {acertos_melancolico}')

    if acertos_colerico > acertos_fleumatico and acertos_colerico > acertos_sanguineo and acertos_colerico > acertos_melancolico:
        st.success('COLÉRICO!!!')
    elif acertos_fleumatico > acertos_colerico and acertos_fleumatico > acertos_sanguineo and acertos_fleumatico > acertos_melancolico:
        st.success('COLÉRICO!!!')
    elif acertos_colerico > acertos_fleumatico and acertos_colerico > acertos_sanguineo and acertos_colerico > acertos_melancolico:
        st.success('COLÉRICO!!!')
    elif acertos_colerico > acertos_fleumatico and acertos_colerico > acertos_sanguineo and acertos_colerico > acertos_melancolico:
        st.success('COLÉRICO!!!')
