# 图片批量压缩工具

一行命令批量压缩图片

## 安装（以conda举例，也可以使用原生python）
conda env create -f environment.yml

conda activate photo-compress

## 基本用法（默认配置）
python compress_photos.py

## 自定义参数
python compress_photos.py 输入文件夹 输出文件夹 质量 最大尺寸

## 参数说明
输入文件夹: 原始图片目录 (默认: photos)

输出文件夹: 压缩图片目录 (默认: compressed)

质量: 1-100 (默认: 80)

最大尺寸: 像素 (默认: 1200)

## 使用示例
### 1. 创建环境
conda env create -f environment.yml

conda activate photo-compress

### 2. 创建测试文件夹
mkdir photos

放入图片到photos文件夹

### 3. 运行压缩
python compress_photos.py

### 4. 自定义参数
python compress_photos.py ./input ./output 90 1600