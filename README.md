# How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver

A mock-first google adk browser-tool adapter with typed inputs, redacted results, and bounded continuation.

![English cover for How to Build a CAPTCHA Browser Tool for Google ADK with CapSolver](assets/cover.png)

[English](README.md) · [简体中文](docs/zh-CN/README.md) · [日本語](docs/ja/README.md) · [Español](docs/es/README.md) · [Português](docs/pt-BR/README.md) · [한국어](docs/ko/README.md)

## Introduction

Developers using Google ADK can encounter CAPTCHA during a permitted browser or workflow step, causing the automation to stop or return the wrong state. This repository shows how to connect Google ADK with [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme), recognize the challenge, request a solution through an isolated adapter, and resume once with clear stop conditions. It focuses only on the Google ADK integration pattern and does not bind the example to a particular business scenario.

**Content type:** Agent integration. **Primary keyword:** `Google ADK browser automation guide` (keyword-library row 65).

## Problem

Google adk tools need a clear contract for reporting captcha challenges without passing secrets or ambiguous browser output back to the agent. The implementation returns explicit `challenge_detected`, `ready`, or `stopped` states instead of silently guessing.

## Features

- Mock-first and deterministic local demonstration
- Allowlisted hosts and one bounded resume attempt
- CapSolver API isolated behind a small adapter
- Redacted output with structured stop reasons
- Unit tests and CI-ready project layout

## How It Works

1. Validate that the target host is explicitly allowlisted.
2. Classify the browser or workflow observation.
3. Send only the authorized CAPTCHA task through the adapter.
4. Poll with a fixed attempt budget and stop conditions.
5. Resume once and emit a minimal normalized result.

The adapter follows the official [createTask API concept](https://docs.capsolver.com/en/guide/api-createtask/) and [getTaskResult API concept](https://docs.capsolver.com/en/guide/api-gettaskresult/).

## Quick Start

```bash
python -m unittest discover -s tests -v
PYTHONPATH=src python examples/mock_workflow.py
```

## Project Structure

```text
src/captcha_workflow/  bounded workflow and adapter
examples/              offline demonstration
tests/                 behavior and policy checks
docs/                  five localized README files
assets/                shared English cover
```

## Testing

Tests verify the successful mock path, allowlist rejection, and bounded challenge handling. No live key or production target is required.

## Responsible Use

Use only public data, owned systems, or targets for which you have explicit authorization. Respect terms, rate limits, purpose limitation, field minimization, retention limits, and stop conditions. Do not use this example for private or restricted data, credential access, detection evasion, or unbounded collection. Travel, pricing, inventory, personal, financial, employment, or contact data requires a documented lawful purpose and proportionate human review.

## Conclusion

This repository provides a mock-first Google ADK browser-tool adapter with typed inputs, redacted results, and bounded continuation. Developer sharing CapSolver integration examples. The final product reference is [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=google-adk-captcha-browser-tool-capsolver&utm_content=repository-readme).

## License

MIT
