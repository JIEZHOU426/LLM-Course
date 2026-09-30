# kaifa

上传文档到 AnythingLLM 的单页工具。

## 使用方法

用浏览器打开 `upload.html`，选择本地文件与目标工作区，点击「上传并嵌入」即可将文档上传到本地 AnythingLLM 实例（默认 `http://localhost:3001`）并加入指定工作区。

## 配置

编辑 `upload.html` 中的两处配置：

```js
const API_KEY = 'YOUR_API_KEY';   // AnythingLLM Developer API Key
const API_URL = 'http://localhost:3001/api/v1/document/upload';
```

## 注意事项

- API Key 请替换为自己的真实密钥，不要提交到仓库。
- 该页面直接从浏览器调用 API，需保证 AnythingLLM 允许跨域访问。
