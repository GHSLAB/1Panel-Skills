# 1Panel API Skills

> 🎯 **OpenClaw Skill** — 1Panel 服务器管理面板 API 接口文档

本 Skill 提供 1Panel 开源服务器管理面板的完整 API 接口文档，基于官方源码反推整理，覆盖 **23+ 个模块**，**500+ 个 API 接口**。

## 文档版本

| 文件 | 说明 |
|------|------|
| `swagger/doc_v1.json` | API v1（Base Path: `/api/v1`） |
| `swagger/doc_v2.json` | API v2（Base Path: `/api/v2`） |
| `swagger/api_comparison.md` | v1 vs v2 对比报告 |

## 功能模块

| 模块 | 说明 |
|------|------|
| AI | Agent、MCP Server、Ollama |
| Apps | 应用商店、已安装应用 |
| Websites | 网站管理、SSL 证书、反向代理 |
| Containers | Docker 容器管理、Compose |
| Databases | MySQL、PostgreSQL |
| Files | 文件管理、回收站、批量操作 |
| Backups | 备份恢复、云存储 |
| Cronjobs | 定时任务 |
| Runtimes | PHP、Python 等运行时 |
| Hosts | 主机监控、防火墙、SSH |
| Settings | 系统设置、用户管理、SSL |
| Dashboard | 仪表盘、系统信息 |
| Logs | 操作日志、任务日志 |

## 快速开始

### 安装

```bash
# 方式一：使用 npx
npx skills add breadbot86/1Panel-Skills

# 方式二：手动复制
cp -r 1Panel-Skills ~/.openclaw/workspace/skills/
```

首次使用请查看 [SKILL.md](./SKILL.md)。

## 工具脚本

### API 对比脚本

对比两个版本的 Swagger JSON 文档，生成 Markdown 对比报告：

```bash
python compare_api.py swagger/doc_v1.json swagger/doc_v2.json [output.md]
```

- 不带第三个参数：直接输出到终端
- 带第三个参数：输出到指定 `.md` 文件

## 项目结构

```
1Panel-Skills/
├── SKILL.md              # OpenClaw Skill 定义
├── README.md             # 本文件
├── compare_api.py        # API 对比脚本
├── swagger/
│   ├── doc_v1.json       # API v1 源文档
│   ├── doc_v2.json       # API v2 源文档
│   └── api_comparison.md # 版本对比报告
└── docs/                 # 详细 API 文档
```

## Fork from

| 项目 | 说明 |
|------|------|
| 1Panel 官方源码 | https://github.com/1Panel-dev/1Panel |
| 面包机仓库 | https://github.com/breadbot86 |

## License

MIT License
