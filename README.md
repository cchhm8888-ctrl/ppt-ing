# PPT-ING Presentation Engine v5

用于 Codex 的可编辑 PowerPoint 制作技能。支持新建、重设计、扩展、重建与审查演示文稿。

## 工作流程

一次需求收集 → 参考研究 → 完整方案确认 → 选择视觉参考路径 → 原生可编辑对象制作 → PowerPoint 渲染与质量检查。

提供三条路径：直接按方案构建、无文字版式参考重建、完整页面参考与 FigEdit 分解。包含设计系统、版式库、字体与形状规范、动画规则、JSON Schema 和审计脚本。

## 安装

将整个仓库放在 Codex 技能目录中的 `ppt-ing` 文件夹。仓库为私有时，需要先获得访问权限。

```powershell
git clone https://github.com/cchhm8888-ctrl/ppt-ing.git "$env:USERPROFILE\.codex\skills\ppt-ing"
```

如果目标目录已存在，请先备份，避免覆盖本地修改。重新打开 Codex 后，在对话中使用 `$ppt-ing`。

示例：`$ppt-ing 根据我的资料制作一份 16:9 的中文产品介绍 PPT。`

## 依赖与能力

本仓库是技能与规范包。实际制作需使用 Codex 的 Presentations 能力；完整页面分解路径使用 FigEdit，概念视觉素材按需使用 imagegen。视觉与动画 QA 需要真实 PowerPoint 环境。相关能力需在使用环境中单独可用。

## 文件

- `SKILL.md`：主流程与质量门槛。
- `agents/openai.yaml`：技能界面元数据。
- `references/`：需求、设计、模板、重建、动画与 QA 规范。
- `schemas/`：v5 brief 与 slide spec 的 JSON Schema。
- `scripts/`：演示文稿与动画审计脚本。
- `tests/`：合同与 Schema 检查。

## 验证

```powershell
python tests/run_contract_tests.py
python -m pip install pytest jsonschema
python -m pytest tests/test_contracts.py -q
```
