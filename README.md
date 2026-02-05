# 🦜 《生成式深度学习（第 2 版）》代码仓库

本仓库是 O’Reilly 出版图书 《Generative Deep Learning: Teaching Machines to Paint, Write, Compose and Play》（生成式深度学习：教会机器绘画、写作、作曲与博弈）第二版 的官方代码仓库。

[O’Reilly 官方链接](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/)

<img src="img/book_cover.png" width="300px">

## 📖 书籍章节

以下是本书的章节结构概览：

*第一部分：生成式深度学习导论*

1. 生成建模（Generative Modeling）
2. 深度学习（Deep Learning）

*第二部分：方法*

3. 变分自编码器（Variational Autoencoders）
4. 生成对抗网络（Generative Adversarial Networks）
5. 自回归模型（Autoregressive Models）
6. 归一化流（Normalizing Flows）
7. 能量模型（Energy-Based Models）
8. 扩散模型（Diffusion Models）

*第三部分：应用*

9. Transformer
10. Advanced GANs
11. 音乐生成
12. 世界模型（World Models）
13. 多模态模型（Multimodal Models）
14. 总结

## 🚀 快速开始

### Kaggle API

为了下载书中使用的一些数据集，你需要一个 Kaggle 账号以及 API Token。使用 Kaggle API 的步骤如下：

1. 注册一个 [Kaggle 账号](https://www.kaggle.com).
2. 进入个人主页的 Account（账户）标签页
3. 点击 Create API Token，这将下载一个名为 'kaggle.json' 的文件，其中包含你的 API 凭据

### .env 文件

在项目根目录下创建一个名为 `.env`的文件，内容如下（将 Kaggle 用户名和 API Key 替换为你自己 kaggle.json 中的值）：

```
JUPYTER_PORT=8888
TENSORBOARD_PORT=6006
KAGGLE_USERNAME=<你的_kaggle_用户名>
KAGGLE_KEY=<你的_kaggle_key>
```

与本书配套的 Notebook 位于 `/notebooks` 目录中，并按章节与示例进行组织。

## 🏞️ 数据下载

本代码仓库内置了一个数据下载辅助脚本。

运行以下命令，并从下列数据集名称中选择一个：

```
bash scripts/download.sh [faces, bricks, recipes, flowers, wines, cellosuites, chorales]
```

## 📈 Tensorboard

TensorBoard 可用于监控实验过程并可视化模型训练进度。

运行以下脚本以启动 TensorBoard：
* `<CHAPTER>` - 章节编号 (e.g. `03_vae`)
* `<EXAMPLE>` - 具体示例 (e.g. `02_vae_fashion`)

```
bash scripts/tensorboard.sh <CHAPTER> <EXAMPLE>
```

随后可在本地浏览器中访问 TensorBoard（端口由`.env`文件指定），例如：

```
http://localhost:6006
```


## 📦 其他资源

本书中的部分示例改编自 Keras 官方网站提供的优秀开源实现[Keras website](https://keras.io/examples/generative/)强烈建议查阅该资源，其中会不断增加新的模型与示例。


