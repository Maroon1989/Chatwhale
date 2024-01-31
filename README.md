# Chatwhale

## 2024-02-01许霁烨更新

### 新增文件：

- paragraph_split.py：PDF内容解析
- get_industry_description.py：读取行业描述的demo

初步完成了年报PDF的内容解析部分，具体内容如下：

### 年报的标题格式为：

- 一级标题：**第X节 XXXX**
- 二级标题：**一/二/三、**

- 三级标题：**（一）**

### 代码实现功能：

**将年报的每一章节的每一段转化成一个Document 实例，并返回总的Document 实例列表**

单个Document实例格式如下：

```python
Document(page_content='一、载有公司法定代表人签字的2022年年度报告原件。\n', metadata={'chapter': '第一节 重要提示、目录和释义'})
```

> 元数据存储的是该段内容属于哪一个**章节**
>
> content存储的是该段内容本身

### 代码结果演示：

![image-20240201010041789](https://xjy-typora.oss-cn-nanjing.aliyuncs.com/image-20240201010041789.png)
