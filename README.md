# WeChat Production System

**公众号一条龙生产 Skill：从选题核验到发布复盘。**

不用再分别处理选题、写作、去 AI 味、标题、截图、图解、封面和发布检查。一句话交给它，它会按流程产出完整发布包。

## 解决什么问题

普通写作 Prompt 只会“写一篇稿”，但公众号真正要的是：

- 能点开的标题；
- 经得起核验的事实；
- 读者能看懂的结构；
- 可复制执行的教程；
- 真实截图和解释性配图；
- 不像 AI 写的文风；
- 发布前可检查；
- 发布后可复盘。

这个 Skill 把这些串成一条生产流水线。

## 核心能力

| 环节 | 能力 |
|---|---|
| 选题 | 立项卡、差异化角度、淘汰标准 |
| 证据 | `source-ledger.md` 记录来源、截图、置信度 |
| 写作 | 测评、教程、热点、变现、工具对比结构 |
| 去 AI 味 | 删空话、加真实颗粒、改成说话 |
| 标题 | 10 个候选 + 主标题 + 备选 + 风险提示 |
| 配图 | 封面、证据截图、流程图、对比图 |
| 封面 | 内置编辑部纸感、黑板报、Riso、工作台等低 AI 味方案 |
| 检查 | 发布包、图片路径、结构、来源、标题兑现 |
| 复盘 | 记录完读率、分享率、收藏、留言和下次策略 |

## 使用方式

一句话即可：

```text
用 wechat-production-system 写一篇公众号文章，主题：xxxx
```

深度测评：

```text
用 wechat-production-system 深度测评 xxxx
```

教程：

```text
用 wechat-production-system 写一篇 xxxx 教程
```

去 AI 味：

```text
用 wechat-production-system 帮我把这篇稿子去 AI 味
```

起标题：

```text
用 wechat-production-system 给这篇稿子起 10 个标题
```

设计封面：

```text
用 wechat-production-system 给这篇文章设计封面
```

## 执行档位

| 档位 | 场景 | 最低中文字符 | 最低图片 |
|---|---|---:|---:|
| quick | 改标题、改一段、去 AI 味 | 不设硬性下限 | 按需 |
| standard | 普通文章、教程、热点稿 | 2000 | 3 |
| deep | 测评、变现拆解、争议热点 | 3500 | 4 |

禁止用废话凑字数。字数不足时，只按这个顺序扩：真实场景 → 证据截图 → 图解 → 可复制模板 → 失败点 → 人群建议。

## 输出结构

```text
outputs/<slug>/
├── article.md
├── title-options.md
├── publish-check.md
├── research/
│   └── source-ledger.md
├── images/
└── prompts/
```

- `article.md`：正文
- `title-options.md`：10 个标题候选和推荐
- `publish-check.md`：发布前检查
- `research/source-ledger.md`：事实来源台账
- `images/`：封面、截图、图解
- `prompts/`：图片生成提示词

## 手动命令

创建发布包：

```bash
python3 scripts/new_article.py my-article --mode standard
```

发布前检查：

```bash
python3 scripts/preflight.py outputs/my-article --mode standard
```

## 安装

```bash
git clone https://github.com/yjn-pj/wechat-production-system.git \
  ~/.codex/skills/wechat-production-system
```

也可以把本仓库放到其他支持 Codex Skill 的工具目录中使用。

## 内置创作台

这个 Skill 独立可用，不依赖任何外部 Skill。以下能力已经全部内置：

| 内置模块 | 作用 |
|---|---|
| 公众号文风引擎 | 控制节奏、口语感、真实感和去 AI 味 |
| 图位规划器 | 规划封面、证据截图、图解和场景图位置 |
| 图片提示词引擎 | 生成低 AI 味、可复现的图片提示词 |
| 封面设计器 | 提供编辑部纸感、黑板报、Riso、工作台等封面方案 |
| 截图工作台 | 规划证据截图，必要时输出手动截图清单 |
| 图片验证器 | 检查主题匹配、标题区、乱码、小图可读性和风格一致性 |
| 证据台账系统 | 记录事实、来源、URL、截图、置信度和正文引用位置 |
| 发布前检查器 | 检查结构、图片、来源、标题兑现和发布风险 |
| 发布后复盘器 | 沉淀完读率、分享率、收藏、留言和下次策略 |

默认执行原则：

1. 全流程优先使用内置创作台；
2. 质量标准、交付结构和终审判断由本 Skill 控制；
3. 外部 Skill 只作为执行适配器，不改变本 Skill 的标准；
4. 没有外部 Skill 时自动使用内置方案，不需要用户额外安装依赖。

## 致谢

这个 Skill 的部分工作流思想参考并借鉴了社区项目的实践，感谢这些项目提供的灵感：

- **khazix-writer**：公众号长文写作、活人感和多层质检思想
- **baoyu-cover-image**：封面生成流程、尺寸规划和确认机制
- **article-visuals**：图位规划和整套配图思想
- **peituka-basics**：图片提示词规范和低 AI 味视觉表达

说明：以上项目是设计启发，不是运行依赖。本项目已经内置完整流程，可独立使用。

## License

MIT License. See [LICENSE](LICENSE).
