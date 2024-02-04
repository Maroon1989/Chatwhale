## NInstruct说明

这份文档主要进行NInstruct文件夹内代码的说明、修改步骤以及提交说明。

#### 重要文件说明

1. data_generator.py：原始数据集生成，数据集格式为json，结构大致如下：

   ```json
   {
       'id':数据集的id号
       'security_code':证券代码，如000001.SZ
       'stock_name':证券名称，如万科A
       'stock_code':股票代码，如000001
   }
   ```

2. inferencer:：用于编写各类问题的情况的文件夹，具体操作方式会在下面详述。
3. results：用于存储生成问题结果的文件夹，具体操作方式会在下面详述。

4. main.py：主函数。
5. table_desk.md：所建数据库的说明文档，包含数据库字段等。
6. run.sh：最终执行脚本。

#### 操作流程

1. 打开inferencer，可以发现结构如下所示：

   ![image-20240204224326447](https://github.com/Maroon1989/Chatwhale/blob/main/NInstruct/img_for_md/1.png)

   - strategy：用于生成问题的文件夹，包含classification（问题分类）、keywords（关键词提取）、nl2sql（sql语句生成）三个部分，已经为大家写好了example可供参考。

2. 修改方式：

   - 当编写一个问题时，在classification/keywords/nl2sql文件夹下新建一个py文件，命名为英文，大致描述该问题的内容，下面以classification_example.py为例。

   - 如下所示，定义函数的名称（名称与文件名最好一致，方便后续统一），同时在cur_conversations放入想放入的问题即可。针对目标公司询问的问题，需要遍历data中的证券代码、名称、股票代码等字段保证完整性，也可根据自己需求进行填充与问题角度的丰富。

     ![image-20240204225349904](https://github.com/Maroon1989/Chatwhale/blob/main/NInstruct/img_for_md/2.png)

   - strategy修改好后，进入strategy文件夹下的`__ init __.py`进行修改：

     ![image-20240204225723409](https://github.com/Maroon1989/Chatwhale/blob/main/NInstruct/img_for_md/3.png)

     首先仿照example，import刚刚写好的函数，并放入STRATEGIES的字典中，请保证格式如下：

     ```json
     {
         ’strategy_name‘:{
             'func':'function_name','type':'function_type'
         }
     }
     ```

3. 执行方式

   - bash执行脚本

     在利用data_generator.py加载数据后（不建议加载太多，可以加载10条左右调试一下即可，同时dataset中已经有10条数据，可以不自己加载），在`run.sh`中进行修改：

     ![image-20240204230809883](https://github.com/Maroon1989/Chatwhale/blob/main/NInstruct/img_for_md/4.png)

     如上是一个parser，将--infer后面的名称替换为自己刚刚写好的`strategy_name`即可，然后在文件夹中打开bash，执行：

     ```bash
     bash run.sh
     ```

   - 终端执行

     将`run.sh`的内容黏贴到终端执行即可，能有一样的结果。

   - 结果查询

     可以在`result`文件夹中进行结果查询，生成的是json文件，可以看看是不是符合要求。

#### 提交说明

为了避免冲突，在提交前请遵循以下规定：

1. `run.sh`恢复成上面图片中的初始状态
2. push前请git pull
3. 也可以在GitHub上进行fork后，发起pull request，这样能避免冲突。

