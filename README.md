# Buscador de Frases em Arquivos PDF

Este é um script em Python que busca por frases específicas em arquivos PDF dentro de uma pasta selecionada pelo usuário. Ele utiliza técnicas de extração de texto direta e OCR (Reconhecimento Óptico de Caracteres) para buscar as frases definidas em cada arquivo PDF. Não importando ser um arquivo digital ou um digitalização de scanner ou ainda uma foto. A interface é básica porque a idéia é demonstrar a capacide de ajsute do OCR.

![Inicialização](https://lh3.googleusercontent.com/d/1tuTIfuN2t1EHsgQyBoVfIN3y_zBSFWOo)
![Busca do local via explorer](https://lh3.googleusercontent.com/d/12vjL6h9rutDJNAGDY8pEifHnIc5yjb6I)
![Retorno das buscas](https://lh3.googleusercontent.com/d/1tRHvVpFy4pqOUxDUBptrrQ-gT9N3DRvq)


## Funcionalidades

- **Busca por Frases**: O script busca por frases pré-definidas em arquivos PDF.
- **Extração de Texto**: Utiliza a biblioteca PyMuPDF para extrair texto de PDFs textuais.
- **OCR para PDFs Digitalizados**: Utiliza a biblioteca Pytesseract para realizar OCR em PDFs digitalizados e extrair texto.
- **Apresentação de Resultados**: Exibe os arquivos PDF onde as frases foram encontradas.
- **Interface Gráfica para Seleção de Pasta**: Abre uma janela para o usuário escolher a pasta contendo os arquivos PDF.

## Tecnologias Utilizadas

- Python 3
- PyMuPDF para manipulação de PDFs
- pytesseract para OCR
- pdf2image para conversão de PDFs em imagens
- OpenCV (cv2) para pré-processamento de imagens
- tkinter para interface gráfica de seleção de pasta
- shutil para operações de sistema de arquivos

## Como Usar

1. **Clone o Repositório**: Clone este repositório para o seu ambiente local.
2. **Instale as Dependências**: Instale as bibliotecas Python necessárias usando pip.
3. **Execute o Script**: Execute o script Python `buscador.py` e siga as instruções no terminal para selecionar a pasta com os arquivos PDF e iniciar a busca.

4. **Resultados**: Ao final da busca, os arquivos PDF onde as frases foram encontradas serão exibidos. Você pode optar por buscar novamente ou fechar o programa.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, novas funcionalidades ou corrigir problemas através de issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

# Executando o Buscador de Frases em Arquivos PDF

Para utilizar o buscador de frases em arquivos PDF, siga os passos abaixo e crie um executalvel windows:

# Criando um Executável Windows com PyInstaller

Para criar um executável Windows a partir do seu código Python, você pode utilizar a biblioteca PyInstaller, que é uma ferramenta eficiente para empacotar aplicativos Python em executáveis independentes. Vamos guiá-lo através dos passos para criar um executável a partir do seu código.

## Passo 1: Preparação

Certifique-se de que você tem o PyInstaller instalado. Você pode instalá-lo via pip se ainda não o fez:

```bash
pip install pyinstaller

## Passo 2: Criando o Executável
Abra o Terminal:

Navegue até o diretório onde está localizado o seu script Python. Se você estiver usando o Windows, abra o Prompt de Comando ou o PowerShell.
Execute o PyInstaller:

Use o seguinte comando para criar o executável:

pyinstaller --onefile --windowed seu_script.py

Substitua seu_script.py pelo nome do seu arquivo Python principal que contém o código que você deseja transformar em executável.

--onefile: Cria um único arquivo executável.
--windowed: Executa o programa sem abrir uma janela de console.
Aguarde o Processo de Build:

O PyInstaller irá analisar seu script, resolver as dependências automaticamente e criar o executável na pasta dist dentro do diretório atual.

## Passo 3: Distribuição
Depois que o PyInstaller terminar de processar seu script, você encontrará o arquivo executável na pasta dist. Este arquivo executável pode ser distribuído e executado em outras máquinas Windows sem a necessidade de ter o Python instalado, pois inclui tudo o que é necessário para a execução do programa.

Notas Adicionais
Dependências Externas: Se o seu código depende de bibliotecas que não são puramente Python (como OpenCV, PyMuPDF, etc.), você pode precisar ajustar o processo para garantir que essas dependências sejam incluídas corretamente no executável. Às vezes, isso pode exigir configurações adicionais no arquivo de especificação do PyInstaller (seu_script.spec).

Teste do Executável: Antes de distribuir o executável, é uma boa prática testá-lo em diferentes máquinas para garantir que tudo funcione como esperado.

Atualizações e Manutenção: Lembre-se de que cada vez que você fizer alterações significativas no seu código, precisará reconstruir o executável usando o PyInstaller para garantir que as mudanças sejam refletidas na versão distribuída.

Seguindo esses passos, você deve conseguir criar um executável Windows a partir do seu código Python com sucesso.

