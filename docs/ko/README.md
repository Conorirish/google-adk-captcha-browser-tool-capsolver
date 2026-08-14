# How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver

![English cover for How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver](../../assets/cover.png)

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

이 저장소가 해결하는 문제는 다음과 같습니다. Google ADK tools need a clear contract for reporting CAPTCHA challenges without passing secrets or ambiguous browser output back to the agent. 소유, 모의 또는 명시적으로 승인된 대상에서만 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme)를 연결하고 제한된 재시도와 중지 조건으로 CAPTCHA 페이지를 정상 결과로 오인하지 않도록 합니다.

## Quick Start

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python examples/mock_workflow.py
```

## Responsible Use

공개 데이터, 소유 시스템 또는 승인된 대상에만 사용하세요. 빈도, 필드 및 보존 기간을 제한하고 민감 데이터가 나타나면 중지하여 사람이 검토합니다.

## Conclusion

이 예제는 테스트하고 검토할 수 있는 구현을 제공합니다. Developer sharing CapSolver integration examples. 마지막 제품 링크는 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme)입니다.

## License

MIT
