from flask import Flask, jsonify
import random

app = Flask(__name__)

# Versão da API
VERSAO_API = "1.0.0"

# Lista de perguntas
perguntas = [
    {
        'pergunta': "O que é uma lista em Python?",
        'resposta': "Uma coleção ordenada e mutável de itens.",
        'alternativas': [
            "Uma coleção ordenada e imutável de itens.",
            "Uma coleção desordenada de itens.",
            "Uma coleção ordenada e mutável de itens.",
            "Uma coleção de dados complexos apenas."
        ]
    },
    {
        'pergunta': "Como acessar o primeiro elemento de uma lista chamada 'lista'?",
        'resposta': "lista[0]",
        'alternativas': [
            "lista[1]",
            "lista[0]",
            "lista[-1]",
            "lista.first()"
        ]
    },
    {
        'pergunta': "Qual método adiciona um elemento ao final de uma lista?",
        'resposta': "append()",
        'alternativas': [
            "add()",
            "append()",
            "insert()",
            "extend()"
        ]
    },
    {
        'pergunta': "Qual método remove o primeiro item com um valor específico de uma lista?",
        'resposta': "remove()",
        'alternativas': [
            "pop()",
            "remove()",
            "delete()",
            "clear()"
        ]
    },
    {
        'pergunta': "Como obter a quantidade de elementos de uma lista?",
        'resposta': "len()",
        'alternativas': [
            "size()",
            "length()",
            "len()",
            "count()"
        ]
    },
    {
        'pergunta': "O que o comando 'lista.pop()' faz?",
        'resposta': "Remove e retorna o último elemento da lista.",
        'alternativas': [
            "Remove o primeiro elemento da lista.",
            "Remove e retorna o último elemento da lista.",
            "Adiciona um elemento ao final da lista.",
            "Ordena a lista em ordem crescente."
        ]
    },
    {
        'pergunta': "Qual desses métodos retorna a quantidade de vezes que um elemento aparece na lista?",
        'resposta': "count()",
        'alternativas': [
            "count()",
            "len()",
            "index()",
            "insert()"
        ]
    },
    {
        'pergunta': "Como você ordenaria uma lista chamada 'lista' em ordem crescente?",
        'resposta': "lista.sort()",
        'alternativas': [
            "lista.sort()",
            "sorted(lista)",
            "lista.order()",
            "sort(lista)"
        ]
    },
    {
        'pergunta': "O que acontece se você tentar acessar um índice que não existe em uma lista?",
        'resposta': "Gera um erro IndexError",
        'alternativas': [
            "Nada acontece.",
            "O índice é automaticamente ajustado.",
            "Gera um erro IndexError",
            "A lista é estendida automaticamente."
        ]
    },
    {
        'pergunta': "Como podemos criar uma lista com os quadrados de 1 a 5 usando list comprehension?",
        'resposta': "[x**2 for x in range(1, 6)]",
        'alternativas': [
            "[x**2 for x in range(1, 5)]",
            "[x**2 for x in range(5)]",
            "[x**2 for x in range(1, 6)]",
            "range(1, 6)**2"
        ]
    }
]

# Endpoint para retornar a versão da API
@app.route('/version', methods=['GET'])
def get_version():
    return jsonify({'version': VERSAO_API})

# Endpoint para retornar uma pergunta aleatória
@app.route('/pergunta', methods=['GET'])
def get_pergunta():
    pergunta_aleatoria = random.choice(perguntas)
    return jsonify(pergunta_aleatoria)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
