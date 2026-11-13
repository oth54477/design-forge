# Design Forge

제품 화면의 의도를 인터뷰로 확인하고, 서로 다른 시안을 비교한 뒤, 고른 방향만 구현하고 화면으로 검증하는 디자인 스킬입니다. UI를 한 번에 생성하는 스킬이 아닙니다.

스킬 본문은 [`plugins/design-forge/skills/design-forge/SKILL.md`](plugins/design-forge/skills/design-forge/SKILL.md)입니다. 플러그인 파일은 Claude Code, Codex, Grok가 그 본문을 설치하게 하는 껍데기입니다.

## 설치

### Grok

```bash
grok plugin marketplace add oth54477/design-forge
grok plugin install design-forge --trust
```

### Claude Code

```bash
claude plugin marketplace add oth54477/design-forge
claude plugin install design-forge@design-forge
```

### Codex

```bash
codex plugin marketplace add oth54477/design-forge
codex plugin add design-forge@design-forge
```

새 세션에서 `/design-forge`로 호출합니다.

플러그인을 쓰지 않는 호스트는 스킬 디렉터리만 연결합니다.

```bash
git clone https://github.com/oth54477/design-forge.git
ln -s "$PWD/design-forge/plugins/design-forge/skills/design-forge" ~/.agents/skills/design-forge
```

`~/.claude/skills`, `~/.codex/skills`, `~/.grok/skills`를 따로 쓰는 호스트는 같은 대상에 링크를 하나 더 둡니다.

## 동작

새 화면은 방향을 승인하기 전에 구현으로 들어가지 않습니다. 이미 있는 화면의 작은 수정은 시안 세 개를 다시 만들지 않습니다.

다른 디자인 스킬이 그 컴퓨터에 있으면 단계에서 빌려 씁니다. 없으면 이 저장소 안의 절차로 계속합니다. 의존 스킬을 같이 설치하지는 않습니다.

## English

Design Forge is a skill that interviews for design intent, compares distinct visual directions, and implements only the direction the user approves.

Install the plugin with one of the command pairs above, then start a new session and run `/design-forge`.

## License

MIT. See [LICENSE](LICENSE).
