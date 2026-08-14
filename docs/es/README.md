# How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver

![English cover for How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver](../../assets/cover.png)

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

Este repositorio resuelve el problema siguiente: Google ADK tools need a clear contract for reporting CAPTCHA challenges without passing secrets or ambiguous browser output back to the agent. Muestra cómo conectar [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme) solo con objetivos propios, simulados o autorizados, usando reintentos limitados y condiciones de parada para no confundir un CAPTCHA con un resultado válido.

## Quick Start

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python examples/mock_workflow.py
```

## Responsible Use

Use solo datos públicos, sistemas propios u objetivos autorizados. Limite frecuencia, campos y retención; deténgase para revisión humana si aparecen datos sensibles.

## Conclusion

El ejemplo ofrece una implementación comprobable y revisable. Developer sharing CapSolver integration examples. La referencia final es [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme).

## License

MIT
