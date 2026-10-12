# Installation / 安装

`communications-paper` is an instruction-only Agent Skill. It needs a compatible host, but no additional runtime dependencies, build step, or installer. Copy the **entire** `skills/communications-paper` folder so its references, metadata, and license travel together.

中文：这是指令型 Skill，无须额外安装运行依赖。请复制完整的 `skills/communications-paper` 文件夹，不要只复制 `SKILL.md`。

## Choose a destination

| Host | Scope | Destination |
| --- | --- | --- |
| Codex CLI / IDE | Personal | `~/.agents/skills/communications-paper/` |
| Codex CLI / IDE | Project | `<project>/.agents/skills/communications-paper/` |
| Claude Code | Personal | `~/.claude/skills/communications-paper/` |
| Claude Code | Project | `<project>/.claude/skills/communications-paper/` |

Choose one scope for each host. For project installation, use the repository in which you will write or review papers. Personal installation applies across local projects.

中文：每个工具选一种安装范围即可；项目安装用于指定论文项目，个人安装用于本机多个项目。

## Copy the skill

Download and extract this repository, or clone it after it has been published. From the `communications-paper-skills` repository root, run the following in macOS, Linux, or WSL for a personal Codex installation:

```sh
skill_destination="$HOME/.agents/skills/communications-paper"
if [ -e "$skill_destination" ] || [ -L "$skill_destination" ]; then
  printf '%s\n' "Already exists; left unchanged: $skill_destination"
else
  mkdir -p "$(dirname "$skill_destination")"
  cp -R skills/communications-paper "$skill_destination"
fi
```

For another host or scope, change `skill_destination` to the corresponding full destination above. For example, use `$HOME/.claude/skills/communications-paper` for personal Claude Code installation. Windows users can create the destination's parent directory and copy the folder with a file manager.

If the destination already exists, the command leaves it unchanged. To update, review the new version, preserve any local edits, and replace the existing skill folder deliberately; a fresh folder avoids retaining obsolete reference files.

中文：从仓库根目录执行命令；需要其他安装位置时，修改 `skill_destination`。已有同名目录或链接时会提示并保持原状。更新前先保存自己的修改，再替换完整文件夹。

## Check discovery and try it

In a fresh Codex CLI or IDE session, open `/skills` or type `$communications-paper`. Codex can also select the skill from its description. Repository discovery scans `.agents/skills` from the working directory up to the repository root. In a fresh Claude Code session, look for the skill in `/skills` and invoke `/communications-paper`.

Try a task with your own evidence, for example:

> Use communications-paper to turn these verified system assumptions and results into a contribution map. Identify missing evidence before drafting claims.

If discovery fails, check that the chosen destination contains `SKILL.md` directly and that the session is using the intended project. Installation paths were checked against the official documentation below; neither host was launched to test this exported package.

中文：在新会话中检查 Skill 列表并显式调用。若未出现，确认目标文件夹内直接包含 `SKILL.md`，且当前项目正确。本导出包未通过实际启动 Codex 或 Claude Code 进行安装测试。

## ChatGPT Work and ZIP files

The release ZIP is a **source repository archive**, not a ChatGPT plugin package. Local folder-copy instructions do not establish a ChatGPT Work import flow. For distribution through OpenAI's plugin system, follow its separate packaging and submission documentation.

中文：ZIP 是源代码仓库压缩包，不是 ChatGPT 插件包；本文不承诺 Work 界面支持直接导入该 ZIP。插件分发需要单独打包。

## Official references

Checked on 2026-10-11:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) — Codex paths, discovery, and invocation.
- [Anthropic: Extend Claude with skills](https://code.claude.com/docs/en/skills) — Claude Code paths and invocation. Local personal skills do not automatically install into Cowork or cloud sessions.
- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins) — the separate plugin distribution format.
