# MikaMakiLite

A simple Telegram bot using AI

# AI configuration file

In a new created file `character.yaml` inside `src/config/` directory:

```config/persona.yaml
persona:
  name: meta-llama/Llama-3.3-70B-Instruct
  
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
- [ ] Create a Docker Container

## Tg Module

- [ ] Follow architecture
- [ ] Integrate FastAPI
- [ ] Create a Docker Container
