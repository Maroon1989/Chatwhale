# 导入库
import pdfplumber
import re
from tqdm import tqdm
# 设置文件名
file_name = r'G:\zhongyunhua\大学\大三寒假\花旗杯\年报Example'

# 打开 PDF 文件
p = pdfplumber.open(file_name + ".pdf")

# 提取 PDF 页数
page_num = len(p.pages)

# with-open-as 进行 PDF -> TXT
with pdfplumber.open(file_name + ".pdf") as pdf:
    for i in tqdm(range(page_num)):
        
        # 设置当前页
        page = pdf.pages[i]
        
        # 提取当前页面文本
        text = page.extract_text()
        #按行读取text
        text_lines = text.split('\n')
        index=0
        for it in text_lines:
            if "报告期内公司从事的" in it:
                start = text_lines.index(it)
                index=1
                #往后读取知道读取到第一个以一二三四字开头的行
                for j in range(start+1,len(text_lines)):
                    if re.match(r'^[（一二三四五六七八九]',text_lines[j]):
                        end = j
                        break
        if index==1:
            merged_text = ''.join(text_lines[start:end])
            print(merged_text)
            break

        # 若 text 不为空值则写入 TXT 文件
        if text != None:
            
            # 设置 TXT 文件
            f = open(file_name + ".txt", "a", encoding = "utf-8")
            
            # 写入 TXT 文件
            f.write(text)
            
            # 打印当前进度
            print(file_name+' '+str(i+1)+'/'+str(page_num)+' 页读写完成', end='\r')
# 写入完毕
f.close()
