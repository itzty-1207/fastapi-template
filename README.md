# FastAPI 项目模板

这是一个遵循行业最佳实践的 FastAPI 项目模板，适用于构建可扩展的 Web API 服务。

## 项目结构

```
.
├── app/                        # 应用程序主目录
│   ├── __init__.py
│   ├── main.py                 # 应用入口点（创建 FastAPI 实例、注册路由和中间件）
│   ├── api/                    # API 路由目录
│   │   ├── __init__.py
│   │   └── v1/                 # API v1 版本
│   │       ├── __init__.py
│   │       ├── api.py          # v1 版本路由聚合
│   │       └── endpoints/      # 具体的端点实现
│   │           ├── items.py
│   │           └── users.py
│   ├── core/                   # 核心配置和安全
│   │   ├── __init__.py
│   │   ├── config.py           # 应用配置（使用 pydantic-settings）
│   │   └── security.py         # 安全相关功能（JWT、密码加密等）
│   ├── models/                 # 数据库模型（SQLAlchemy ORM）
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   ├── schemas/                # Pydantic 模型（数据验证和序列化）
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   ├── crud/                   # 数据库操作（创建、读取、更新、删除）
│   │   ├── __init__.py
│   │   ├── base.py             # 基础 CRUD 操作
│   │   ├── item.py
│   │   └── user.py
│   ├── db/                     # 数据库连接和会话管理
│   │   ├── __init__.py
│   │   ├── base.py             # 基础数据库配置
│   │   └── session.py          # 数据库会话管理
│   ├── dependencies/           # 依赖项
│   │   ├── __init__.py
│   │   ├── auth.py             # 认证相关依赖
│   │   └── db.py               # 数据库依赖
│   ├── middleware/             # 自定义中间件
│   │   ├── __init__.py
│   │   └── logging.py          # 日志中间件
│   └── utils/                  # 工具函数
│       ├── __init__.py
│       └── helpers.py
├── tests/                      # 测试目录
│   ├── __init__.py
│   ├── conftest.py             # 测试配置
│   ├── test_items.py
│   └── test_users.py
├── alembic/                    # 数据库迁移文件（Alembic）
├── .env                        # 开发环境变量
├── .env.prod                   # 生产环境变量示例
└── README.md                   # 项目说明文档
```

## 目录说明

### `app/main.py`
应用的入口点，负责创建 FastAPI 实例，注册路由、中间件和异常处理器。

### `app/api/`
API 路由目录，按版本组织。每个版本包含一个 `api.py` 文件用于聚合该版本的所有路由，以及 `endpoints/` 目录存放具体的端点实现。

### `app/core/`
核心配置和安全相关模块：
- `config.py`: 应用配置管理，使用 pydantic-settings 读取环境变量
- `security.py`: 安全相关功能，如密码加密、JWT token 生成和验证

### `app/models/`
数据库模型，使用 SQLAlchemy ORM 定义数据表结构。

### `app/schemas/`
Pydantic 模型，用于：
- 请求数据验证
- 响应数据序列化
- 数据结构定义

### `app/crud/`
数据库操作（Create, Read, Update, Delete）：
- `base.py`: 基础 CRUD 操作类
- `item.py`, `user.py`: 特定模型的 CRUD 操作

### `app/db/`
数据库连接和会话管理：
- `base.py`: 数据库基类配置
- `session.py`: 数据库会话创建和管理

### `app/dependencies/`
FastAPI 依赖项：
- `auth.py`: 认证相关依赖
- `db.py`: 数据库会话依赖

### `app/middleware/`
自定义中间件：
- `logging.py`: 日志中间件

### `app/utils/`
通用工具函数。

### `tests/`
测试目录，结构与 `app/` 目录对应：
- `conftest.py`: pytest 配置和 fixtures
- `test_items.py`, `test_users.py`: 具体的测试文件

### `alembic/`
数据库迁移文件，使用 Alembic 管理。

## 环境变量

项目使用 `.env` 文件管理环境变量：
- `.env`: 开发环境配置
- `.env.prod`: 生产环境配置示例

## 开发指南

### 安装依赖

```bash
# 使用 pip
pip install -r requirements.txt

# 或使用 poetry（如果项目使用 pyproject.toml）
poetry install
```

### 启动开发服务器

```bash
# 使用 uvicorn
uvicorn app.main:app --reload

# 或使用启动脚本（如果存在）
python run.py
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_items.py
```

### 数据库迁移

```bash
# 初始化迁移（首次使用）
alembic init alembic

# 创建新迁移
alembic revision --autogenerate -m "迁移说明"

# 应用迁移
alembic upgrade head
```

## API 文档

项目使用 FastAPI 自动生成 API 文档：
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 部署

推荐使用以下方式部署：
1. 使用 Docker 容器化部署
2. 使用 Gunicorn 作为 WSGI 服务器
3. 配置 Nginx 作为反向代理

## 最佳实践

1. **版本控制**: 所有 API 都应该有版本控制，便于后续升级
2. **数据验证**: 使用 Pydantic 模型进行严格的数据验证
3. **错误处理**: 统一的异常处理机制
4. **日志记录**: 完整的日志记录便于问题排查
5. **安全性**: 使用 HTTPS，正确处理认证和授权
6. **测试**: 编写完整的单元测试和集成测试

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情
