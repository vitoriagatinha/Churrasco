import webbrowser

class Churrasco:
    def __init__(self, nome):
        self.nome = nome
        self.lista_desejos = []
        self.lista_convidados = []
        self.consumo = {}
        self.imagem_churrasco = "https://static.wixstatic.com/media/13aa37_cac8963824c548e5aaf720e4f5a93908~mv2_d_5616_3744_s_4_2.jpg/v1/fill/w_2500,h_1666,al_c/13aa37_cac8963824c548e5aaf720e4f5a93908~mv2_d_5616_3744_s_4_2.jpg"  

    def adicionar_item(self):
        while len(self.lista_desejos) < 20:
            item = input("Insira um item para o churrasco ou 'sair' para terminar: ")
            if item.lower() == 'sair':
                break
            else:
                self.lista_desejos.append(item)

    def adicionar_convidado(self):
        while len(self.lista_convidados) < 30:
            convidado = input("Insira um convidado para o churrasco ou 'sair' para terminar: ")
            if convidado.lower() == 'sair':
                break
            else:
                self.lista_convidados.append(convidado)

    def calcular_consumo(self):
        for item in self.lista_desejos:
            self.consumo[item] = len(self.lista_convidados) * 1

    def gerar_html(self):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Churrasco {self.nome}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f8f9fa;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 80%;
                    margin: 0 auto;
                }}
                h1, h2 {{
                    color: #333;
                    text-align: center;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    margin-bottom: 10px;
                    background-color: #fff;
                    border: 1px solid #ddd;
                    padding: 10px;
                    border-radius: 5px;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>CHURRASCO {self.nome}</h1>
                <img src="{self.imagem_churrasco}" alt="Imagem de churrasco">
                <h2>Lista de Desejos</h2>
                <ul>
        """
        for item in self.lista_desejos:
            html += f"<li>{item}</li>"
        html += "</ul><h2>Lista de Convidados</h2><ul>"
        for convidado in self.lista_convidados:
            html += f"<li>{convidado}</li>"
        html += "</ul><h2>Consumo</h2><ul>"
        for item, quantidade in self.consumo.items():
            html += f"<li>{item}: {quantidade}</li>"
        html += "</ul></div></body></html>"
        return html

churrasco = Churrasco("VITORIA GISLAINE")
churrasco.adicionar_item()
churrasco.adicionar_convidado()
churrasco.calcular_consumo()
html = churrasco.gerar_html()

with open('churrasco.html', 'w', encoding='utf-8') as f:
    f.write(html)

webbrowser.open('churrasco.html')
