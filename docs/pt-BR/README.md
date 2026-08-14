# How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver

![English cover for How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver](../../assets/cover.png)

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

Este repositório resolve o seguinte problema: Google ADK tools need a clear contract for reporting CAPTCHA challenges without passing secrets or ambiguous browser output back to the agent. Ele mostra como conectar o [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme) somente a alvos próprios, simulados ou autorizados, com tentativas limitadas e condições de parada para não confundir CAPTCHA com resultado válido.

## Quick Start

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python examples/mock_workflow.py
```

## Responsible Use

Use somente dados públicos, sistemas próprios ou alvos autorizados. Limite frequência, campos e retenção; pare para revisão humana se houver dados sensíveis.

## Conclusion

O exemplo fornece uma implementação testável e revisável. Developer sharing CapSolver integration examples. A referência final é [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme).

## License

MIT
