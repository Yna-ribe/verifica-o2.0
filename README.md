# Sistema de Controle e Verificação de Acessos

[![Python](https://shields.io)](https://python.org)
[![HTML5](https://shields.io)](https://mozilla.org)
[![CSS3](https://shields.io)](https://mozilla.org)
[![JavaScript](https://shields.io)](https://mozilla.org)

Uma solução web leve e personalizada de controle de acesso e monitoramento digital, projetada especificamente para fornecer governança de dados, rastreabilidade e segurança para micro e pequenas empresas com infraestrutura tecnológica limitada.

---

## Contexto e Justificativa

Pequenas empresas enfrentam riscos elevados de segurança digital devido a orçamentos reduzidos e falta de processos maduros. De acordo com dados do *IBM/Ponemon Institute*:
* **95%** das brechas de segurança foram causadas por **erro humano** (negligência ou acessos indevidos).
* **56%** dos incidentes de segurança no Brasil envolveram armazenamento em nuvem sem proteção adequada.
* **35%** das empresas brasileiras sofreram algum tipo de **vazamento de dados** nos últimos dois anos, afetando principalmente micro e pequenas organizações.

Este sistema mitiga esses riscos fornecendo uma alternativa de **baixo custo, rápida implementação e comportamento profissional**, eliminando a falta de suporte técnico que frequentemente impede essas empresas de aplicarem boas práticas de segurança.

---

## Arquitetura e Tecnologias

Para atender ao foco de simplicidade e baixo custo, a solução utiliza uma arquitetura web leve dividida em módulos bem definidos:

* **Front-End (HTML, CSS e JavaScript):** Interface web responsiva focada na experiência do usuário e na captura de ações locais.
* **Back-End (Python):** Camada responsável por gerenciar de forma segura a autenticação, regras de permissão e a gravação de logs (Auditoria).
* **Persistência de Dados:** Banco de dados relacional ou leve, escalável conforme a necessidade de armazenamento da empresa.

A arquitetura foi projetada de forma modular para suportar **autenticação, autorização e auditoria**, permitindo futuras integrações com métodos de autenticação mais robustos e serviços de diretório (como LDAP ou Active Directory).

---

## ⚙️ Regras de Negócio e Perfis de Acesso

O sistema gerencia a entrada digital cruzando o cargo do colaborador com o fator temporal (dias da semana):

| Perfil | Nível de Permissão | Restrição Temporal |
| :--- | :--- | :--- |
| ** Gerente** | Total / Administrativo | Acesso diário (Livre) |
| ** Analista** | Operacional Avançado | Permitido de **Segunda a Sábado** |
| ** Estagiário**| Restrito | **Apenas nos dias configurados** individualmente pela administração (ex: Terça e Quinta) |

---

## Descrição Funcional (Interface Web)

A aplicação conta com uma interface web totalmente responsiva e dividida em três frentes principais:
* **Tela de Login:** Portal de entrada seguro para a autenticação dos colaboradores.
* **Cadastro de Usuários:** Painel para inserção de novos colaboradores com definição de cargo e parametrização de dias permitidos (para estagiários).
* **Painel Administrativo:** Espaço restrito para controle de privilégios e visualização em tempo real dos logs de tentativas de acesso.

---

## Alinhamento com Boas Práticas de Segurança

O código foi estruturado pensando em cobrir lacunas críticas de infraestrutura através de software:
* **Governança de acessos:** Aplicação prática do princípio do menor privilégio.
* **Monitoramento e detecção:** Centralização de logs de acesso para identificar tentativas anômalas ou falhas em massa.
* **Segregação de ambientes:** Estrutura pronta para operar separando dados administrativos de dados operacionais.

---
