# WeChat Production System

**公众号选题到发文的一条龙生产系统。**
A production system for WeChat articles: from evidence-based topic selection to publishing-ready packages.

这个 Skill 不是单纯的“写作 Prompt”，而是一套可执行的公众号内容流水线。它把选题、证据核验、结构设计、场景化写作、去 AI 味、标题测试、真实截图、图解、封面设计、发布检查和发布后复盘放进同一个流程里。

## 它适合谁

- 需要持续生产公众号文章的个人创作者
- 写 AI 工具测评、热点解读、变现拆解、教程型内容的作者
- 希望文章既有流量，又不牺牲事实边界的创作者
- 需要把复杂信息改成普通人能看懂的图文内容的人
- 想沉淀一套可复用内容生产 SOP 的团队

## 核心能力

### 1. 选题立项

不是拿到主题就写，而是先判断：

- 目标读者是谁
- 读完能带走什么
- 核心冲突是什么
- 有什么证据
- 有什么不可知风险
- 是否值得写

避免热点复读和空泛观点文。

### 2. 证据核验

关键事实必须写入 `research/source-ledger.md`：

```text
事实 | 来源 | URL | 访问时间 | 截图 | 置信度 | 正文位置
```

优先级：

```text
官方文档 > 官方价格页 > 原作者发布 > 权威媒体 > 一手截图 > 二手分析
```

搜索摘要只能作为线索，不能当作事实。

### 3. 场景化写作

文章优先回答：

- 谁用
- 用在哪一步
- 怎么操作
- 要花多少钱
- 哪里容易失败
- 如何验收结果

技术名词第一次出现必须解释成人话。

### 4. 去 AI 味

固定三轮：

```text
删空话
加真实颗粒
改成说话
```

重点删除：

- 赋能、闭环、重塑、引领未来
- 首先其次最后综上所述
- 只有形容词没有细节的段落
- 机械排比和空洞升华

### 5. 标题系统

每次生成 10 个标题，覆盖：

- 结果型
- 冲突型
- 场景型
- 情绪型
- 教程型

最终输出：

```text
主标题 + 备选标题 + 推荐理由 + 标题风险
```

标题必须能被正文兑现，不允许纯粹标题党。

### 6. 图片系统

每篇标准文章至少有：

1. 封面
2. 真实证据截图
3. 流程图 / 结构图 / 对比图

并明确区分：

- 真实截图
- 图解
- AI 生成视觉

AI 图不能冒充真实截图。

### 7. 发布包

一键创建：

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

### 8. 发布后复盘

记录：

- 阅读完成率
- 分享率
- 收藏、在看、留言
- 首屏流失判断
- 下次保留什么
- 下次禁用什么

让账号偏好逐渐沉淀，而不是每次从零开始。

## 使用方式

### 一句话自动模式

```text
用 wechat-production-system 写一篇 GPT-6 测评公众号文章
```

系统会自动判断：

- 文章类型：测评
- 执行档位：deep
- 是否需要证据核验
- 是否需要截图
- 是否需要图解
- 是否需要多版本标题

### 常用指令

写文章：

```text
用 wechat-production-system 写一篇关于微信 AI 更新的公众号文章
```

写教程：

```text
用 wechat-production-system 写一篇 SkillHub 使用教程
```

改稿：

```text
用 wechat-production-system 帮我把这篇文章去 AI 味
```

起标题：

```text
用 wechat-production-system 给这篇文章起 10 个标题
```

设计封面：

```text
用 wechat-production-system 给这篇文章重新设计封面，不要科技感
```

复盘：

```text
用 wechat-production-system 复盘昨天那篇文章的数据
```

## 执行档位

| 档位 | 场景 | 最低中文字符 | 最低图片 |
|---|---|---:|---:|
| quick | 改标题、改一段、去 AI 味 | 不设硬性下限 | 按需 |
| standard | 普通文章、教程、热点稿 | 2000 | 3 |
| deep | 测评、变现拆解、争议热点 | 3500 | 4 |

禁止用废话凑字数。扩写顺序必须是：

1. 真实场景和输入输出
2. 证据截图和来源解释
3. 流程图或前后对比
4. 可复制模板
5. 失败点和解决办法
6. 不同人群建议
7. 最后才考虑背景

## 手动创建发布包

```bash
python3 scripts/new_article.py my-article --mode standard
```

## 发布前检查

```bash
python3 scripts/preflight.py outputs/my-article --mode standard
```

检查项包括：

- 标题候选
- 文章结构
- 中文字符数
- 图片路径
- 来源章节
- 事实台账

机械检查通过后，仍需人工检查事实、语气、标题承诺和视觉质量。

## 可选依赖

核心功能不依赖其他 Skill。如果安装以下 Skill，效果更好：

| Skill | 作用 |
|---|---|
| khazix-writer | 公众号文风和活人感 |
| article-visuals | 配图规划 |
| peituka-basics | 图片提示词规范 |
| baoyu-cover-image | 封面生成流程 |
| verification | 图片检查 |
| screenshot / browser | 网页截图 |

## 设计原则

1. 证据优先，观点其次
2. 场景优先，概念其次
3. 可复制优先，情绪其次
4. 图片必须降低理解成本
5. 去 AI 味是硬要求
6. 标题承诺必须兑现
7. 输出完整发布包，而不是一段文本
8. 发布后必须沉淀经验

## 目录结构

```text
wechat-production-system/
├── SKILL.md
├── README.md
├── references/
│   ├── de-ai.md
│   ├── evidence.md
│   ├── production-memory.md
│   ├── publishing.md
│   ├── review.md
│   ├── structure.md
│   ├── title.md
│   ├── tutorial.md
│   └── visual.md
└── scripts/
    ├── new_article.py
    └── preflight.py
```

## 安装

复制到 Codex skills 目录：

```bash
git clone <your-repo-url>
cp -r <repo>/wechat-production-system ~/.codex/skills/
```

如果你的仓库根目录就是这个 skill，则：

```bash
git clone <your-repo-url> ~/.codex/skills/wechat-production-system
```

## 许可

MIT License. See [LICENSE](LICENSE).
