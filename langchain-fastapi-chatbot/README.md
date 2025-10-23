# langchain-fastapi-chatbot

## 项目简介
该项目是一个基于FastAPI和LangChain的智能聊天机器人，支持从私有文档库加载数据，并提供一个简单易用的Web界面。

## 项目结构
```
langchain-fastapi-chatbot
├── src
│   ├── main.py               # 应用程序入口点
│   ├── api
│   │   ├── __init__.py       # API模块初始化
│   │   └── routes.py         # 定义API路由
│   ├── core
│   │   └── config.py         # 应用程序配置
│   ├── services
│   │   └── chatbot.py        # 聊天机器人核心逻辑
│   ├── loaders
│   │   └── csv_loader.py     # 加载私有文档库
│   ├── embeddings
│   │   └── embeddings.py      # 文本嵌入功能
│   ├── vectorstore
│   │   └── vectorstore.py    # 向量存储功能
│   ├── templates
│   │   └── index.html        # 前端界面
│   └── static
│       └── app.css           # 样式表
├── requirements.txt           # 项目依赖
├── .env.example               # 环境变量示例
├── Dockerfile                 # Docker镜像构建文件
├── docker-compose.yml         # Docker Compose配置
├── tests
│   └── test_chatbot.py       # 单元测试
└── README.md                  # 项目文档
```

## 运行步骤
1. 确保已安装Docker和Docker Compose。
2. 在项目根目录下，运行命令 `docker-compose up --build` 来构建并启动应用程序。
3. 打开浏览器，访问 `http://localhost:8000` 来访问聊天机器人界面。

## 依赖项
请查看 `requirements.txt` 文件以获取项目所需的Python依赖项。

## 环境变量
请参考 `.env.example` 文件以配置应用程序所需的环境变量。