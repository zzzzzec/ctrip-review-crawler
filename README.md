# 携程酒店评论爬取

## 项目简介

本项目用于爬取携程网指定城市的酒店信息，包含开业时间，客房数，位置信息等，并将结果保存为 JSON 文件。

## 使用方法

1. **克隆项目**

   ```bash
   git clone <项目地址>
   cd xiecheng
   ```

2. **创建虚拟环境**

   使用 Conda 创建虚拟环境：

   ```bash
   conda create -n xiecheng_env python=3.11 -y
   conda activate xiecheng_env
   ```

3. **安装依赖**

   使用 `requirements.txt` 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. **运行项目**

   修改 `main.py` 中的配置参数（如 `cityId`、`numHotelPages` 和 `numCommentPages`），然后运行：

   ```bash
   python main.py
   ```
