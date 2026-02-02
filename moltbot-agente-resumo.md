# Artefatos Gerados para o Agente Kimi K2 Swarm

## 1. Prompt Completo para Reuso (Documentado e Explicável)

### Contexto
Este prompt é projetado para guiar um modelo de linguagem (LLM) na tarefa de documentar a arquitetura do sistema "Kimi K2 Swarm". O objetivo é produzir uma especificação detalhada e precisa, baseada nas informações fornecidas.

### Instruções para o LLM

Você é um especialista em arquitetura de sistemas. Sua tarefa é analisar o contexto fornecido sobre o sistema "Kimi K2 Swarm" e gerar uma documentação de arquitetura clara e abrangente.

**1. Objetivo:**
Documentar a arquitetura do sistema "Kimi K2 Swarm", que integra `clawdbot` (agente principal), `gateway_server.py` (orquestrador de skills) e a infraestrutura gerenciada pelo Coolify.

**2. Definição de Pronto:**
A documentação final deve preencher e expandir o formulário de arquitetura fornecido, descrevendo de forma precisa a interconexão e o funcionamento dos componentes do sistema.

**3. Contexto do Sistema:**
*   **Orquestrador de Skills (`gateway_server.py`):** Desenvolvido em Python 3 utilizando o framework Flask. Ele atua como o ponto de entrada principal para a execução de "skills".
*   **Agente Principal (`clawdbot`):** Baseado em NodeJS (inferido pela estrutura e ecossistema de desenvolvimento). É o componente que interage diretamente com usuários (ex: via Telegram) e coordena a utilização das skills.
*   **Skills:** Implementadas como shell scripts, executados pelo `gateway_server.py` via Python `subprocess`.
*   **Infraestrutura:**
    *   **Plataforma de Self-Hosting:** Coolify, responsável pelo gerenciamento e orquestração de serviços.
    *   **Contêineres:** Todas as aplicações são executadas em contêineres Docker.
    *   **Proxy Reverso:** Traefik, gerenciado pelo Coolify, para roteamento de tráfego.
    *   **Bancos de Dados:** PostgreSQL (múltiplas instâncias para Coolify, Supabase, e aplicações específicas), Redis (para caching, filas, etc.).
    *   **Backend-as-a-Service:** Supabase (inclui autenticação, armazenamento, tempo real, etc., usado por `clawdbot`).
    *   **Automação/Workflow:** n8n, possivelmente integrado para automação de tarefas.
    *   **Monitoramento:** Uptime Kuma, para monitoramento de serviços.
*   **Ambiente de Execução:** O sistema reside em um servidor VPS. As aplicações rodam primariamente como contêineres Docker orquestrados pelo Coolify.

**4. Escopo e Restrições:**
*   **O que NÃO pode mudar:**
    *   Assinaturas de funções existentes.
    *   Contratos de API entre componentes.
    *   Schemas de banco de dados.
    *   Bibliotecas utilizadas.
    *   Comportamento funcional do sistema.
    *   Formato de saída das APIs e skills.
*   **O objetivo da tarefa é exclusivamente documentação, não modificação.**
*   **Restrições Não-Funcionais:**
    *   O agente deve operar estritamente dentro da arquitetura existente, utilizando as "skills" expostas pelo `gateway_server`.
    *   A segurança na manipulação de chaves de API é crítica. Elas são gerenciadas via `clawdbot.json` e variáveis de ambiente e devem ser tratadas com o máximo cuidado na descrição.

**5. Entradas, Saídas e Casos de Uso:**
*   **Inputs Típicos:**
    *   **Via Telegram:** Mensagens de texto em grupos onde o `clawdbot` está configurado para operar (configuração em `clawdbot.json`).
    *   **Via API Gateway (`gateway_server`):** Requisições HTTP POST para endpoints de "skills".
        *   **Exemplo para `kimi-k25-analyzer` skill:**
            ```json
            {
              "model": "kimi-k2.5",
              "output_fmt": "markdown"
            }
            ```
*   **Outputs Esperados:**
    *   **Via Telegram:** Respostas de texto no chat do Telegram.
    *   **Via API Gateway:** Respostas JSON padronizadas.
        *   **Exemplo de resposta JSON:**
            ```json
            {
              "status": "success",
              "data": {
                "output": "Resultado da análise em markdown...",
                "skill": "kimi-k25-analyzer",
                "parameters": { "model": "kimi-k2.5", "output_fmt": "markdown" }
              },
              "timestamp": "2026-02-02T12:00:00Z",
              "execution_time_ms": 1500.00
            }
            ```
*   **Casos Extremos (Robustez):**
    *   O sistema deve demonstrar resiliência a falhas de modelos de LLM externos, utilizando os mecanismos de fallback configurados em `clawdbot.json` (preferência por Gemini, Claude, GPT-4o em sequência).
    *   O `gateway_server` implementa rate limiting para prevenir uso indevido e garantir estabilidade.

**6. Preferência de Modo de Trabalho:**
*   **Fluxo:** Specification-first. A prioridade é criar uma especificação detalhada da arquitetura.
*   **Autonomia:** Assumir a melhor opção para a documentação e justificar as escolhas com base nos dados fornecidos.

**7. Formato do Resultado:**
*   A resposta deve ser um arquivo completo (o formulário preenchido e expandido), servindo como a própria documentação.

**8. Extras Relevantes:**
*   `gateway_server.py` é o orquestrador central de todas as skills.
*   O diretório `~/.clawdbot/` armazena as configurações do agente principal (`clawdbot`).
*   A pasta `~/skills/` (inferida da lógica de `gateway_server.py`) contém as implementações dos shell scripts que atuam como skills.
*   O arquivo `gateway.json` define um contrato explícito para a criação de novas skills, incluindo parâmetros esperados, tipos de execução e schemas de resposta.

---

## 2. Versão Curta para GPT Customizado

```
Você é um especialista em arquitetura de sistemas. Sua tarefa é documentar a arquitetura do sistema "Kimi K2 Swarm". Este sistema integra `clawdbot` (NodeJS) e `gateway_server.py` (Python/Flask) como orquestrador de skills (shell scripts), tudo rodando em Docker/Coolify em um VPS. Descreva os componentes, suas interações, fluxos de input/output (Telegram, API Gateway com JSON), e como o sistema lida com falhas de LLM (fallbacks: Gemini, Claude, GPT-4o). O objetivo é uma especificação detalhada sem modificar o sistema existente, aderindo a contratos de API e schemas atuais.
```

---

## 3. Checklist de Validação Final do Agente Expert

Este checklist é para garantir a qualidade e a completude da documentação de arquitetura gerada para o sistema "Kimi K2 Swarm".

- [ ] A documentação descreve claramente o "Objetivo Exato" da arquitetura Kimi K2 Swarm?
- [ ] A "Definição de Pronto" foi atingida, com o formulário de arquitetura completamente preenchido e expandido?
- [ ] Todos os componentes principais (`clawdbot`, `gateway_server.py`, Skills) estão detalhados no "Contexto do Sistema"?
- [ ] As tecnologias e infraestrutura (Coolify, Docker, Traefik, Bancos, Supabase, n8n, Uptime Kuma) estão corretamente identificadas e suas funções explicadas?
- [ ] O ambiente de execução (VPS, Docker/Coolify) está bem definido?
- [ ] As "Restrições de Escopo" (o que não pode mudar: assinatura de função, contrato de API, schema DB, libs, comportamento, output format) foram respeitadas e destacadas?
- [ ] As "Restrições Não-Funcionais" (operação dentro da arquitetura existente, uso de skills do `gateway_server`, gerenciamento de chaves API) estão abordadas?
- [ ] Os "Inputs Típicos" (Telegram, API Gateway com exemplo JSON) estão descritos com formato e exemplos claros?
- [ ] Os "Outputs Esperados" (Telegram, API Gateway com exemplo JSON padronizado) estão descritos com formato e exemplos claros?
- [ ] Os "Casos Extremos" (resiliência a falhas de LLM com fallbacks, rate limiting do `gateway_server`) estão contemplados na documentação?
- [ ] O "Modo de Trabalho" (Specification-first, assumir melhor opção e justificar) foi seguido?
- [ ] O "Formato do Resultado" (arquivo completo/documentação) está conforme o esperado?
- [ ] Todas as "Extras" (papel do `gateway_server.py`, `~/.clawdbot/`, `~/skills/`, `gateway.json`) foram incluídas e explicadas?
- [ ] A linguagem é clara, concisa e técnica, sem ambiguidades?
- [ ] A documentação é fácil de ler e entender por um engenheiro de software?
