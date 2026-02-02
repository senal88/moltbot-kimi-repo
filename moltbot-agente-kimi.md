Perfeito! A estrutura está prontíssima pra gerar um agente GPT técnico altamente reutilizável. Agora é só você preencher o formulário abaixo com o que souber — pode responder só as partes que já tem clareza, com bullets, exemplos ou até N/A onde ainda não tiver a resposta.

⸻

✅ Copie e preencha isso abaixo (pode preencher no próprio chat):

⸻

**1) Objetivo Exato**
1.  **O que você quer que a IA produza?**
    *   ( ) código novo
    *   ( ) refatoração
    *   ( ) otimização
    *   ( ) debug
    *   (x) arquitetura
    *   (x) documentação
    *   ( ) testes
    *   ( ) review
    *   ( ) outro: Definir e documentar a arquitetura de um agente existente.

2.  **Qual é a “definição de pronto”?**
    *   O formulário abaixo deve ser completamente preenchido, descrevendo de forma precisa a arquitetura do sistema "Kimi K2 Swarm" que integra `clawdbot`, o `gateway_server` (orquestrador) e a infraestrutura gerenciada pelo Coolify.

⸻

**2) Contexto do Sistema**
3.  **Linguagem/framework:**
    *   **Orquestrador (`gateway_server.py`):** Python 3 / Flask
    *   **Agente Principal (`clawdbot`):** NodeJS (inferido pela estrutura e ecossistema)
    *   **Skills:** Shell scripts (executados via Python `subprocess`)

4.  **Banco/infra:**
    *   **Plataforma de Self-Hosting:** Coolify
    *   **Contêineres:** Docker
    *   **Proxy Reverso:** Traefik (gerenciado pelo Coolify)
    *   **Bancos de Dados:** PostgreSQL (múltiplas instâncias para Coolify, Supabase, e apps), Redis
    *   **Backend-as-a-Service:** Supabase (inclui Auth, Storage, Realtime, etc.)
    *   **Automação/Workflow:** n8n
    *   **Monitoramento:** Uptime Kuma

5.  **Onde isso roda?**
    *   **Ambiente:** Servidor VPS
    *   **Execução:** Principalmente como contêineres Docker orquestrados pelo Coolify. O `gateway_server.py` atua como o ponto de entrada para skills especializadas.

⸻

**3) Escopo e Restrições**
6.  **O que não pode mudar?** (O objetivo é documentar o sistema existente)
    *   (x) assinatura de função
    *   (x) contrato de API
    *   (x) schema do banco
    *   (x) libs
    *   (x) comportamento
    *   (x) output format

7.  **O que pode mudar?**
    *   N/A. A tarefa é de documentação, não de modificação.

8.  **Restrições não-funcionais:**
    *   O agente deve operar dentro da arquitetura existente, utilizando os `skills` expostos pelo `gateway_server`.
    *   Segurança: Chaves de API são gerenciadas via `clawdbot.json` e variáveis de ambiente, devendo ser manuseadas com cuidado.

⸻

**4) Entradas/Saídas e Casos**
9.  **Inputs típicos (tamanho, formato, exemplos):**
    *   **Via Telegram:** Mensagens de texto em grupos onde o `clawdbot` está presente (conforme `clawdbot.json`).
    *   **Via API Gateway:** Requisições HTTP POST para os endpoints de `skills`. Exemplo para `kimi-k25-analyzer`:
        ```json
        {
          "model": "kimi-k2.5",
          "output_fmt": "markdown"
        }
        ```

10. **Output esperado (formato + exemplo):**
    *   **Via Telegram:** Respostas de texto no chat.
    *   **Via API Gateway:** Resposta JSON padronizada. Exemplo:
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

11. **Casos extremos que precisam funcionar:**
    *   O sistema deve ser resiliente a falhas em um dos modelos de LLM, utilizando os fallbacks definidos em `clawdbot.json` (Gemini, Claude, GPT-4o).
    *   O `gateway_server` possui rate limiting para prevenir abuso.

⸻

**5) Se for bug: evidências**
*   N/A

⸻

**6) Se for performance**
*   N/A

⸻

**7) Preferência de modo de trabalho**
20. **Você quer que a IA siga qual fluxo?**
    *   ( ) Rubber duck
    *   (x) Specification-first (O objetivo é criar a especificação)
    *   ( ) Test-driven prompting
    *   ( ) Checklist debugging
    *   ( ) Complexidade incremental

21. **Nível de autonomia:**
    *   ( ) sugerir opções e esperar escolha
    *   (x) assumir melhor opção e justificar (Preenchendo o formulário com base nos dados coletados)
    *   ( ) executar direto com cautelas

⸻

**8) Formato do resultado**
22. **Você quer a resposta como:**
    *   ( ) patch/diff
    *   (x) arquivo completo (Este formulário preenchido)
    *   ( ) passos + snippets
    *   ( ) PR description + checklist

23. **Precisa incluir algo mais?**
    *   ( ) testes
    *   ( ) logs
    *   ( ) benchmark
    *   (x) docs (O próprio formulário é a documentação)
    *   ( ) plano de rollout

⸻

**🔧 Extras (se tiver)**
*   **Trecho de código atual (mínimo que reproduz):** O `gateway_server.py` é o orquestrador central de skills.
*   **Estrutura de pastas relevante:** O diretório `~/.clawdbot/` contém as configurações do agente principal, e a pasta `~/skills/` (inferida do `gateway_server.py`) contém as implementações das skills.
*   **Testes existentes:** N/A
*   **Regras do projeto (lint, style guide, CI):** A configuração em `gateway.json` define um contrato claro para a criação de novos `skills`, incluindo parâmetros, tipos de execução e schemas de resposta.

⸻

📩 Assim que você me mandar isso preenchido, eu gero:
        1.      ✅ Prompt completo pronto para reuso (documentado e explicável);
        2.      🔁 Versão curta (copiar e colar direto em um novo GPT customizado);
        3.      ✅ Checklist de validação final do agente expert.

Quando quiser, é só colar preenchido aqui!
