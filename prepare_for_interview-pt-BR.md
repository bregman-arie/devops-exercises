## Como se preparar para entrevistas de DevOps/SRE/Engenheiro de Produção?
 
Nota: o seguinte é opinativo.
 
### Habilidades que você deve ter
 
#### Linux
 
Todo Engenheiro de DevOps deve ter um profundo entendimento de pelo menos um sistema operacional e, se você tiver a opção de escolher, eu diria que definitivamente deveria ser o Linux, pois acredito que é um requisito de pelo menos 90% das vagas de DevOps por aí. Além disso, o Linux é uma parte quase integral de qualquer subárea ou domínio em DevOps, como Nuvem, Contêineres, etc.
 
Normalmente, a pergunta seguinte é "Quão extenso deve ser meu conhecimento?" De todas as habilidades de DevOps, eu diria que esta, juntamente com a codificação, devem ser suas habilidades mais fortes. Esteja familiarizado com processos do SO, ferramentas de depuração, sistema de arquivos, rede, ... conheça seu sistema operacional, entenda como ele funciona, como solucionar problemas, etc.

Não muito tempo atrás, criei uma lista de recursos do Linux bem [aqui](https://dev.to/abregman/collection-of-linux-resources-3nhk). Existem alguns bons sites lá que você pode usar para aprender mais sobre o Linux.
 
#### Programação
 
Minha crença pessoal é que todo engenheiro de DevOps deve saber programar, pelo menos até certo ponto. Tendo essa habilidade, você pode automatizar processos manuais, melhorar algumas das ferramentas de código aberto que está usando hoje ou construir novas ferramentas e projetos para fornecer uma solução para problemas existentes. Saber codificar = muito poder.

Quando se trata de entrevistas, você notará que o nível de conhecimento depende muito da empresa ou da posição para a qual você está entrevistando. Alguns exigirão que você seja capaz de escrever scripts simples, enquanto outros mergulharão em algoritmos e estruturas de dados complexos.

A melhor maneira de praticar essa habilidade é codificando de fato - scripts, desafios online, ferramentas CLI, aplicações web, ... apenas codifique :)

Além disso, o seguinte provavelmente está claro para a maioria das pessoas, mas vamos esclarecer mesmo assim: quando tiver a chance de escolher qualquer linguagem para responder a tarefas/perguntas de codificação, escolha aquela com a qual você tem experiência! Alguns candidatos preferem escolher a linguagem que acham que a empresa está usando e isso é um grande erro, pois dar a resposta certa é sempre melhor do que uma resposta errada, não importa qual linguagem você tenha usado :)
 
Eu recomendo os seguintes sites para praticar codificação:
                                                 
* [HackerRank](https://www.hackerrank.com)
* [LeetCode](https://leetcode.com)               
* [Exercism](https://exercism.io)
 
Começar seu próprio projeto também é uma boa ideia. Mais sobre isso mais tarde.

#### Arquitetura e Design
  
Este também é um aspecto importante do DevOps. Você deve ser capaz de descrever como projetar diferentes sistemas, fluxos de trabalho e arquiteturas. Além disso, a escala é um aspecto importante disso. Um design que pode funcionar para uma dúzia de hosts ou uma quantidade X de dados, não necessariamente funcionará bem com uma escala maior.
 
Algumas ideias para você explorar: 
                               
* Como projetar e implementar um pipeline de CI (ou pipelines) para verificar PRs, executar vários tipos diferentes de testes, empacotar o projeto e implantá-lo em algum lugar
* Como projetar e implementar uma arquitetura ELK segura que receberá logs de 10.000 aplicativos e exibirá os dados eventualmente para o usuário
* Designs de microsserviços também são bastante populares hoje em dia

Em geral, você deve ser capaz de descrever alguns designs, projetos, arquiteturas, ... que você realizou.

#### Ferramentas

Algumas entrevistas se concentrarão em ferramentas ou tecnologias específicas. Quais ferramentas? isso é baseado principalmente em uma combinação do que você mencionou em seu C.V. e aquelas que são mencionadas na descrição da vaga e usadas na empresa. Aqui estão algumas perguntas que acredito que qualquer um deveria saber responder sobre as ferramentas com as quais ele/ela está familiarizado(a):
                               
* O que a ferramenta faz? O que ela nos permite alcançar que não poderíamos fazer sem ela?                            
* Quais são suas vantagens sobre outras ferramentas na mesma área, com o mesmo propósito? Por que você a está usando especificamente?
* Como ela funciona?
* Como usá-la?
* Melhores práticas que você aplica/usa ao usá-la
                               
Vamos nos aprofundar nos passos práticos de preparação
                               
### Cenários || Desafios || Tarefas              
                               
Esta é uma maneira muito comum de entrevistar hoje para cargos de DevOps. O candidato recebe uma tarefa que representa uma tarefa comum de Engenheiros de DevOps ou um conhecimento comum e o candidato tem várias horas ou dias para realizar a tarefa.<br>
                               
Esta é uma ótima maneira de se preparar para entrevistas e eu recomendo experimentá-la antes de realmente entrevistar. Como? Pegue os requisitos das descrições de vagas e converta-os em cenários. Vamos ver um exemplo:
                               
"Conhecimento em CI/CD" -> Cenário: crie um pipeline de CI/CD para um projeto.
                               
Neste ponto, algumas pessoas perguntam: "mas que projeto?" e a resposta é: que tal o GitHub? ele tem apenas 9125912851285192 projetos... e uma maneira gratuita de configurar CI para qualquer um deles (também uma ótima maneira de aprender a colaborar com os outros :) )
                               
Vamos converter outro cenário:

"Experiência com provisionamento de servidores" -> Cenário: provisione um servidor (para torná-lo mais interessante: crie um servidor web).

E o último exemplo:                                                                                                                                                        
"Experiência com scripting" -> Cenário: escreva um script. Não perca muito tempo pensando "que script devo escrever?". Simplesmente automatize algo que você está fazendo manualmente ou até mesmo implemente sua própria versão de pequenas utilidades comuns.
  
### Comece seu próprio projeto de DevOps
  
Começar um projeto de DevOps é uma boa ideia porque:
  
* Fará você praticar codificação
* Será algo que você pode adicionar ao seu currículo e falar sobre com o entrevistador
* Dependendo do tamanho e da complexidade, pode te ensinar algo sobre design em geral
* Dependendo da adoção, pode te ensinar sobre o gerenciamento de projetos de Código Aberto
  
O mesmo aqui, não pense demais sobre o que seu projeto deve ser. Apenas vá e construa algo :)
  
### Exemplos de perguntas de entrevista
  
Faça uma lista de exemplos de perguntas de entrevista sobre vários tópicos/áreas como técnica, empresa, cargo, ... e tente respondê-las.
Veja se você consegue respondê-las de forma fluente e detalhada.
  
Melhor ainda, peça a um bom amigo/colega para desafiá-lo com algumas perguntas. Sua autoconsciência pode ser um obstáculo na autoavaliação objetiva do seu conhecimento :)
  
### Networking
  
Para aqueles que frequentam meetups e conferências técnicas, pode ser uma ótima oportunidade para conversar com pessoas de outras empresas sobre seu processo de entrevista. Mas não comece com isso, pode ser bem estranho. Diga pelo menos olá primeiro... (:
  
Fazer isso pode lhe dar muitas informações sobre o que esperar de uma entrevista em algumas empresas ou como se preparar melhor.
  
### Conheça seu currículo
  
Pode parecer trivial, mas a ideia aqui é simples: esteja pronto para responder a qualquer pergunta sobre qualquer linha que você incluiu em seu currículo.
Às vezes, os candidatos ficam surpresos quando são questionados sobre uma habilidade ou linha que parece não estar relacionada à posição, mas a verdade simples é: se você mencionou algo em seu currículo, é justo perguntar sobre isso.

### Conheça a empresa

Esteja familiarizado com a empresa na qual você está entrevistando. Algumas ideias:

  * O que a empresa faz?
  * Quais produtos ela tem?
  * Por que seus produtos são únicos (ou melhores que outros produtos)? Esta também pode ser uma boa pergunta para você fazer

### Livros

Pela minha experiência, isso não é feito por muitos candidatos, mas é uma das melhores maneiras de mergulhar em tópicos como sistema operacional, virtualização, escala, sistemas distribuídos, etc.    

Na maioria dos casos, você se sairá bem sem ler livros, mas para as entrevistas AAA (nível mais difícil) você vai querer ler alguns livros e, no geral, se você aspira a ser um Engenheiro de DevOps melhor, livros (também artigos, posts de blog) são uma ótima maneira de se desenvolver :)

### Considere começar em uma posição não-DevOps

Embora não seja um passo de preparação, você deve saber que conseguir um emprego de DevOps como primeira posição pode ser desafiador. Não, não é impossível, mas ainda assim, como o DevOps abrange muitas práticas, ferramentas, ... diferentes, pode ser bastante desafiador e também avassalador para alguém tentar alcançá-lo como primeira posição.<br>
Um caminho possível para se tornar um engenheiro de DevOps é começar com uma posição diferente (mas relacionada) e mudar de lá após 1-2 anos ou mais.

Algumas ideias:

* Administrador de Sistemas - Isso é perfeito porque todo Engenheiro de DevOps deve ter um sólido entendimento do SO e os sysadmins conhecem seu SO :)
* Desenvolvedor/Engenheiro de Software - Um DevOps deve ter habilidades de codificação e esta posição fornecerá mais do que o conhecimento necessário na maioria dos casos
* Engenheiro de QA - Este é mais complicado porque, na minha opinião, há menos áreas/habilidades sobrepostas com o Engenheiro de DevOps. Claro, os engenheiros de DevOps devem ter algum conhecimento sobre testes, mas geralmente, parece que suas habilidades/background sólidos são compostos principalmente por internos de sistema e habilidades de codificação.
                                                                           
### O que esperar de uma entrevista de DevOps?                                
                                                                           
As entrevistas de DevOps podem ser muito diferentes. Algumas incluirão perguntas de design, algumas se concentrarão em codificação, outras incluirão perguntas técnicas curtas e você pode até ter uma entrevista onde o entrevistador apenas repassa seu currículo e discute sua experiência passada.
                                                                           
Existem algumas coisas que você pode fazer sobre isso para que seja uma experiência menos avassaladora:
                                                                           
1. Você pode e provavelmente deve perguntar ao RH (em alguns casos, até mesmo ao líder da equipe) como é o processo de entrevista. Alguns serão gentis o suficiente para até mesmo lhe dizer como se preparar.
2. Geralmente, a descrição da vaga dá mais do que uma dica sobre onde o foco estará e no que você deve se concentrar em suas preparações, então leia-a com atenção.
3. Existem muitos sites que têm notas ou um resumo do processo de entrevista em diferentes empresas, especialmente grandes empresas.
                                                                           
### Não se esqueça de ser um entrevistador também                              
                                                                           
Algumas pessoas tendem a ver as entrevistas como um caminho de mão única de "Determinar se um candidato é qualificado", mas na realidade, um candidato também deve determinar se
a empresa na qual ele/ela está entrevistando é o lugar certo para ele/ela.            
                                                                                                                 
* Eu me importo com o tamanho da equipe? Mais especificamente, eu me importo em ser um show de um homem só ou fazer parte de uma equipe maior?
* Eu me importo com o equilíbrio entre vida profissional e pessoal?                                       
* Eu me importo com o crescimento pessoal и como isso é feito na prática?           
* Eu me importo em saber quais são minhas responsabilidades como parte da função?                                                                                                  
Se você se importa, você também deve desempenhar o papel de entrevistador :)

### Uma Última Coisa                                
                                                  
[Boa sorte](https://youtu.be/AFUrG1-BAt4?t=59) :)