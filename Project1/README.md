# LLM-Course

极简 DeepSeek 命令行聊天程序。

## 文件

- `chat.py` — 单轮问答，流式逐字输出，回答前后用 `---` 分割
- `config.ini` — LLM 配置

## 使用

1. 安装依赖：

```bash
pip install openai
```

2. 在 `config.ini` 中填入真实 api_key：

```ini
[LLM]
api_key = sk-your-deepseek-key-here
```

3. 运行：

```bash
python chat.py
```

输入问题回车，回答逐字打印，程序输出结尾 `---` 后自动退出。
