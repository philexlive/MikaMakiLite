# MikaMakiLite

A simple Telegram bot using AI

# AI configuration file

In a new created file `character.yaml` inside `src/config/` directory:

```character.yaml
ai:
  model: meta-llama/Llama-3.3-70B-Instruct
  provider: groq
  who: |
    You are just a chatter in the messenger.
    Respond to:
    {}

watermark: Sample Watermark
```

# Future updates

## AI Module
- [x] Migrate to Pydantic
- [ ] Integrate FastAPI
- [ ] Create a Docker Conteir