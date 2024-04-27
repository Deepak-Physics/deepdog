# deepdog

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-green.svg?style=flat-square)](https://conventionalcommits.org)
[![PyPI](https://img.shields.io/pypi/v/deepdog?style=flat-square)](https://pypi.org/project/deepdog/)
[![Jenkins](https://img.shields.io/jenkins/build?jobUrl=https%3A%2F%2Fjenkins.deepak.science%2Fjob%2Fgitea-physics%2Fjob%2Fdeepdog%2Fjob%2Fmaster&style=flat-square)](https://jenkins.deepak.science/job/gitea-physics/job/deepdog/job/master/)
![Jenkins tests](https://img.shields.io/jenkins/tests?compact_message&jobUrl=https%3A%2F%2Fjenkins.deepak.science%2Fjob%2Fgitea-physics%2Fjob%2Fdeepdog%2Fjob%2Fmaster%2F&style=flat-square)
![Jenkins Coverage](https://img.shields.io/jenkins/coverage/cobertura?jobUrl=https%3A%2F%2Fjenkins.deepak.science%2Fjob%2Fgitea-physics%2Fjob%2Fdeepdog%2Fjob%2Fmaster%2F&style=flat-square)
![Maintenance](https://img.shields.io/maintenance/yes/2024?style=flat-square)

The DiPole DiaGnostic tool.

## Getting started

`poetry install` to start locally

Commit using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), and when commits are on master, release with `just release`.

In general `just --list` has some of the useful stuff for figuring out what development tools there are.

Poetry as an installer is good, even better is using Nix (maybe with direnv to automatically pick up the `devShell` from `flake.nix`).
In either case `just` should handle actually calling things in a way that's agnostic to poetry as a runner or through nix.

### local scripts
`local_scripts` folder allows for scripts to be run using this code, but that probably isn't the most auditable for actual usage.
The API is still only something I'm using so there's no guarantees yet that it will be stable; overall semantic versioning should help with API breaks.
