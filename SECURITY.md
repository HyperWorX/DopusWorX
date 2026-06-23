# Security Policy

## Supported versions

DopusWorX is in beta. Only the most recent release gets fixes, so please test
against the latest build before reporting anything.

| Version           | Supported |
| ----------------- | --------- |
| Latest 1.0.0-beta | Yes       |
| Older betas       | No        |

## Reporting a vulnerability

Please do not open a public issue for a security problem.

DopusWorX is a Directory Opus viewer plugin: a native Windows DLL plus a WebView2
layer that renders local files. If you find a way to make it run code, reach
files outside the opened document, or otherwise misbehave on untrusted input,
report it privately using GitHub's **Report a vulnerability** button on the
[Security tab](https://github.com/HyperWorX/DopusWorX/security/advisories/new).

Please include:

- The DopusWorX version and your Directory Opus version
- Your Windows version
- A sample file or steps that trigger the issue
- What you expected to happen

You can expect an acknowledgement within a few days. Once a fix ships you are
welcome to be credited in the release notes if you would like.
