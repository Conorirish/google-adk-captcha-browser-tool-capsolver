# How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver

![English cover for How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver](../../assets/cover.png)

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

本仓库解决的问题是：Google ADK tools need a clear contract for reporting CAPTCHA challenges without passing secrets or ambiguous browser output back to the agent。它展示了如何在自有、模拟或明确授权的目标中接入 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme)，并通过有限重试和明确停止条件避免把验证码页面误当成有效结果。

## Quick Start

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python examples/mock_workflow.py
```

## Responsible Use

仅可用于公开数据、自有系统或明确授权目标。限制请求频率、采集字段与保留期限；遇到敏感数据时停止并人工复核。

## Conclusion

本示例提供可测试、可审查的实现。Developer sharing CapSolver integration examples. 最后的产品入口是 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme)。

## License

MIT
