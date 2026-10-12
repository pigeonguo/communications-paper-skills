# Publishing on GitHub / 发布到 GitHub

The prepared repository has not been published. The export ZIP omits `.git`, so extracting it gives source files without Git history or a configured remote. These steps publish a new repository named `communications-paper-skills` when you choose to run them.

中文：当前交付物尚未发布；ZIP 不包含 `.git`、Git 历史或远程地址。以下步骤供你决定发布时执行。

## Prepare the first commit

Extract the ZIP and open a terminal in the `communications-paper-skills` directory. Review the included README, license, attribution notices, and skill files. Keep private manuscripts and source papers outside this public release.

For an extracted ZIP, initialize Git and create the first commit:

```sh
git init -b main
git add .
git diff --cached --stat
git commit -m "Initial public release"
```

If you are already working in a Git checkout, keep its history and skip initialization. Check `git status` and `git remote -v` before proceeding. The prepared local repository has no Git remote configured.

中文：先检查 README、许可证、署名说明和文件内容，不要加入私人论文材料。ZIP 解压目录需要初始化 Git；若已有 Git 仓库，则保留其历史并检查状态和远程地址。

## Create an empty GitHub repository and push

1. Authenticate Git with your GitHub account.
2. Create a new **public** GitHub repository named `communications-paper-skills`. Leave GitHub's README, license, and `.gitignore` initialization options unchecked because these files are already in this source package.
3. Replace `YOUR-ACCOUNT` below with your GitHub account or organization. Add and inspect the remote, then push:

```sh
git remote add origin https://github.com/YOUR-ACCOUNT/communications-paper-skills.git
git remote -v
git push -u origin main
```

Use your actual branch name if it differs from `main`. If `origin` already exists, inspect its URL before making any change. After the push, check the repository page and follow [the installation guide](INSTALLATION.md) from a fresh download.

中文：在 GitHub 创建同名公开空仓库，不要再次生成 README、许可证或 `.gitignore`。将 `YOUR-ACCOUNT` 替换为你的账户或组织名，核对远程地址后推送。发布后从新下载的文件检查安装说明。

Publishing source on GitHub does not register or publish a ChatGPT plugin. That requires a separate plugin package and publication workflow.

中文：GitHub 开源发布不会自动注册或发布 ChatGPT 插件。

## Official references

Checked on 2026-10-11:

- [GitHub: Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) — initialization, empty repository creation, authentication, and push.
- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins) — separate plugin packaging requirements.

These are manual publishing instructions. No GitHub repository was created and no push was performed while preparing this package.
