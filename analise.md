# Resposta do Modelo:

(venv) PS C:\Users\natan\Documents\Universidade\devIA\atividade 3\dev-IA-Atividade3> python .\agent.py

You are a coding assistant whose goal it is to help us solve coding tasks.
You can perform actions by emitting a single command line in exactly this format, and nothing else on that line:

tool: NAME({"arg": "value"})

Do not use JSON function-calling, a <tool_call> tag, or any other structured tool-call format your training may default to.
The ONLY format the system running you understands is the plain text line above.

Available commands:

TOOL
===
    Name: read_file
    Description: 
Gets the full content of a file provided by the user.
:param filename: The name of the file to read.
:return: The full content of the file.

    Signature: (filename: str) -> Dict[str, Any]
    
===============
TOOL
===
    Name: list_files
    Description: 
Lists the files in a directory provided by the user.
:param path: The path to a directory to list files from.
:return: A list of files in the directory.

    Signature: (path: str) -> Dict[str, Any]
    
===============
TOOL
===
    Name: edit_file
    Description: 
Replaces first occurrence of old_str with new_str in file. If old_str is empty,
create/overwrite file with new_str.
:param path: The path to the file to edit.
:param old_str: The string to replace.
:param new_str: The string to replace with.
:return: A dictionary with the path to the file and the action taken.

    Signature: (path: str, old_str: str, new_str: str) -> Dict[str, Any]
    
===============


Example of a correct response when you want to read a file named 'notes.txt':
tool: read_file({"filename": "notes.txt"})

Use compact single-line JSON with double quotes. After receiving a tool_result(...) message, continue the task using the same format when another action is needed.
If no action is needed, respond in plain prose.

You::encontre e conserte o bug baseado no teste que está falhando em test_inventory.py
Thought: I'll help you find and fix the bug. Let me start by exploring the project structure.
Action: list_files {'path': '.'}
'}, {'filename': 'venv', 'type': 'dir'}]}
Action: read_file {'filename': 'test_inventory.py'}
C:\Users\natan\Documents\Universidade\devIA\atividade 3\dev-IA-Atividade3\test_inventory.py
Observation: {'file_path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\test_inventory.py', 'content': 'from inventory import apply_discount\n\n\ndef test_apply_discount():\n    assert apply_discount(200, 10) == 180\n'}
Action: read_file {'filename': 'inventory.py'}
C:\Users\natan\Documents\Universidade\devIA\atividade 3\dev-IA-Atividade3\inventory.py
Observation: {'file_path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\inventory.py', 'content': 'def apply_discount(price, percent):\n    """Aplica um desconto percentual ao preÃ§o."""\n    return price - percent\n'}
Assistant:: 
You::encontre e conserte o bug baseado no teste que está falhando em test_inventory.py
Thought: O bug está na função `apply_discount` em `inventory.py`. Ela apenas subtrai `percent` (número) diretamente do preço, em vez de calcular o valor real do desconto baseado na porcentagem.

Correndo o cálculo:
Action: edit_file {'path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\inventory.py', 'old_str': 'def apply_discount(price, percent):\n    """Aplica um desconto percentual ao preço."""\n    return price - percent', 'new_str': 'def apply_discount(price, percent):\n    """Aplica um desconto percentual ao preço."""\n    discount = price * (percent / 100)\n    return price - discount'}
Observation: {'path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\inventory.py', 'action': 'edited'}
Thought: Bug corrigido! ✅

**Problema:** Em `inventory.py`, a função `apply_discount` estava fazendo `price - percent` (subtraindo o percentual diretamente do preço) em vez de calcular o desconto corretamente.

Para o teste `apply_discount(200, 10) == 180`, o valor esperado é de um desconto de **10%** sobre 200, ou seja, 200 - (200 × 10/100) = 200 - 20 = **180**.

**Correção:**
```pythonObservation: {'path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3', 'files': [{'filename': '.env', 'type': 'file'}, {'filename': '.git', 'type': 'dir'}, {'filename': 'agent.py', 'type': 'file'}, {'filename': 'inventory.py', 'type': 'file'}, {'filename': 'README.md', 'type': 'file'}, {'filename': 'requirements.txt', 'type': 'file'}, {'filename': 'test_inventory.py', 'type': 'file
def apply_discount(price, percent):
    """Aplica um desconto percentual ao preço."""
    return price - (price * percent / 100)
```

Agora a função calcula o valor percentual do desconto sobre o preço e o subtrai, fazendo com que o teste passe.
Assistant:: Bug corrigido! ✅

**Problema:** Em `inventory.py`, a função `apply_discount` estava fazendo `price - percent` (subtraindo o percentual diretamente do preço) em vez de calcular o desconto corretamente.

Para o teste `apply_discount(200, 10) == 180`, o valor esperado é de um desconto de **10%** sobre 200, ou seja, 200 - (200 × 10/100) = 200 - 20 = **180**.

**Correção:**
```python
def apply_discount(price, percent):
    """Aplica um desconto percentual ao preço."""
    return price - (price * percent / 100)
```

Agora a função calcula o valor percentual do desconto sobre o preço e o subtrai, fazendo com que o teste passe.
You::

# Respostas da Atividade:

1. Loop: uma iteração completa e o que faz o laço continuar ou parar ali.

## Exemplo de iteração completa: 

You::encontre e conserte o bug baseado no teste que está falhando em test_inventory.py
Thought: I'll help you find and fix the bug. Let me start by exploring the project structure.
Action: list_files {'path': '.'}
Observation: {'path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3', 'files': [{'filename': '.env', 'type': 'file'}, {'filename': '.git', 'type': 'dir'}, {'filename': 'agent.py', 'type': 'file'}, {'filename': 'inventory.py', 'type': 'file'}, {'filename': 'README.md', 'type': 'file'}, {'filename': 'requirements.txt', 'type': 'file'}, {'filename': 'test_inventory.py', 'type': 'file'}, {'filename': 'venv', 'type': 'dir'}]}
Action: read_file {'filename': 'test_inventory.py'}
C:\Users\natan\Documents\Universidade\devIA\atividade 3\dev-IA-Atividade3\test_inventory.py
Observation: {'file_path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\test_inventory.py', 'content': 'from inventory import apply_discount\n\n\ndef test_apply_discount():\n    assert apply_discount(200, 10) == 180\n'}
Action: read_file {'filename': 'inventory.py'}
C:\Users\natan\Documents\Universidade\devIA\atividade 3\dev-IA-Atividade3\inventory.py
Observation: {'file_path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\inventory.py', 'content': 'def apply_discount(price, percent):\n    """Aplica um desconto percentual ao preÃ§o."""\n    return price - percent\n'}
Assistant:: 

## O que faz o loop parar ou continuar:
A invocação de tools faz o loop parar ou continuar, assim que ele para de chamar tools, voltamos para a iteração onde o usuário manda uma mensagem, mas não temos um teste 


2. Contexto: onde o resultado de uma tool volta para a conversa e passa a fazer parte do que o LLM vê na chamada seguinte.
## Exemplo 
Observation: {'file_path': 'C:\\Users\\natan\\Documents\\Universidade\\devIA\\atividade 3\\dev-IA-Atividade3\\inventory.py', 'content': 'def apply_discount(price, percent):\n    """Aplica um desconto percentual ao preÃ§o."""\n    return price - percent\n'}
Nessa parte, o resultado da tool anterior foi adicionada ao modelo, isso pode ser visto no próximo pensamento do modelo:
Thought: O bug está na função `apply_discount` em `inventory.py`. Ela apenas subtrai `percent` (número) diretamente do preço, em vez de calcular o valor real do desconto baseado na porcentagem.



E também ocorre nesta parte do código:
conversation.append({
                    "role": "user",
                    "content": f"tool_result({json.dumps(resp)})"
                })


3. Tools / ACI: uma chamada de tool e o formato usado (parsing de texto sobre `tool: nome({...})`), comparado com JSON estruturado e tool calling nativo.
## Exemplo de chamada de tool:
O modelo de linguagem retorna esse tool calling:
tool: list_files({"path": "."}). 
O script agent.py por sua vez intercepta essa linha específica na resposta do LLM, exibe o log no terminal como Action: list_files {'path': '.'} e executa a função Python correspondente no sistema operacional, retornando a lista de arquivos no formato de dicionário Observation: {'path': '...', 'files': [...]}.
Em comparação ao Tool Calling nativo (que define ferramentas via JSON Schema no parâmetro tools da API e retorna um objeto estruturado com validação automática), o parsing por texto insere as instruções diretamente no System Prompt e extrai o comando do corpo da resposta do modelo. Enquanto o parsing por texto é agnóstico e funciona em qualquer LLM (embora exija um parser próprio e seja mais sujeito a erros de sintaxe), o formato nativo oferece maior determinismo e segurança, porém depende de suporte específico do modelo e da API.



4. Thought: um trecho de raciocínio do modelo que não gera chamada de tool. Segundo a aula, esse é o passo que normalmente fica escondido dentro das ferramentas prontas.
Thought: O bug está na função `apply_discount` em `inventory.py`. Ela apenas subtrai `percent` (número) diretamente do preço, em vez de calcular o valor real do desconto baseado na porcentagem.

Correndo o cálculo:



5. Guardrail: é o item mais importante. O agente não tem nenhum: ele não roda o teste nem verifica se o problema foi resolvido antes de parar. Explique, com base na sua execução, o que isso significou na prática. Ele pode ter parado achando que terminou sem ter terminado?
Na prática, ele não tem nenhum parâmetro ou teste para se basear para gerar parada, ele fica rodando até o usuário interromper a execução com ctrl+c, ou até o modelo não chamar mais ferramentas, no caso, interrompi com ctrl+c quando a tarefa foi concluída, mas não é o melhor meio, pois como dito anteriormente, o ideal era existir um teste para o modelo parar a execução sozinho e com execução de testes, sem isso ele pode parar a execução sem ter feito realmente o trabalho.


6. Falhas de parsing: o que o parser errou ou deixou passar. Se não houve falha, diga isso.
Não ocorreu nenhuma falha de parsing. 