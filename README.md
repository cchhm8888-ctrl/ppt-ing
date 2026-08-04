# PPT-ING — Presentation Engine V2

> 从资料到可编辑静态或动态PPT：少问一步、少做一轮预览、保留可维护的源文件与媒体映射。

PPT-ING 是一个跨平台 Agent Skill，用于创建、重构、扩展和审计 PPT/PPTX。它将叙事、版式、主题、图片、图表、动画、视频、转场、质量检查和交付包收敛为一条可执行流程。

## V2 解决什么

- 静态PPT：从大纲、文档、数据、图片、参考PPT/PDF生成可编辑PPTX。
- 动态PPT：支持背景视频、自动播放、编辑层动效、媒体导出、动效时间同步与技术审计。
- image2拆分：将预览/参考图重建为图片、文字、线条、节点等可编辑对象，而非整页截图。
- 既有PPT审计：识别页数、媒体、外链、转场和动画时间线，并可从最终PPT直接导出对应视频。

## 三条最短路径

| 路径 | 适用场景 | 处理方式 |
|---|---|---|
| `rapid-static` | 已有大纲和明确风格/模板 | 直接生成可编辑静态PPT，再渲染质检 |
| `studio-static` | 明确要求image2预览或视觉确认 | 只出1–3张代表页，确认后生产整套PPT |
| `dynamic` | 视频、动画、自动播放、动态模板或媒体替换 | 先完成可编辑静态版，再加媒体映射、动效计划和审计 |

已有参考图、模板或已确认风格时，Skill不会再重复询问颜色、版式和密度；只有会改变内容、风格或交付格式的缺失信息才会提问。

## 快速使用

```text
$ppt-ing，根据我的大纲和资料生成一份16:9可编辑PPT；参考我上传的模板，不需要预览，直接出成品并逐页质检。
```

```text
$ppt-ing，根据我的静态PPT做动态版本：视频作为可替换背景，文字、线条和节点必须保持可编辑；自动播放时编辑层与视频同步，并输出媒体映射、动效说明和交付包。
```

## 动态PPT原则

1. 先有可编辑的静态PPT，再添加视频与动画。
2. 视频是独立媒体层；标题、正文、线条、路径、节点和页码必须是原生编辑层。
3. 视频与首个编辑层使用 `With Previous` 同时启动，其余编辑层按 `After Previous` 串行完成，并在视频有效时长内结束。
4. 用户提供最终PPT时，从该PPT的嵌入媒体直接导出交付视频，不能复用可能错配的旧视频目录。
5. 自动化环境无法稳定写入原生动效时，诚实交付静态可编辑PPT和 `motion-plan.json`，不伪称已完成动态效果。

## 内置工具

- `scripts/inspect_pptx.py`：读取PPTX页码、媒体与页面关系。
- `scripts/extract_pptx_media.py`：从PPTX导出媒体并按P01/P02等页面关系命名。
- `scripts/audit_presentation.py`：检查页数、内嵌媒体、外链、转场与时间线存在情况。
- `schemas/presentation-brief.schema.json`：记录8页以上或动态项目的统一制作简报。

## 结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── page-types.md
│   ├── engine-rules.md
│   ├── dynamic-ppt.md
│   ├── delivery-package.md
│   └── qa-checklist.md
├── schemas/
│   └── presentation-brief.schema.json
└── scripts/
    ├── inspect_pptx.py
    ├── extract_pptx_media.py
    └── audit_presentation.py
```

## V2 验收

- 验证 `SKILL.md` YAML 元数据；
- 用真实含视频PPT测试媒体关系、视频导出和审计脚本；
- 静态和动态成品均需完成“渲染 → 检查 → 修复 → 复验”。
