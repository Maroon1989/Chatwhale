import pdfplumber
import re
from langchain.docstore.document import Document
from file_processor import read_jsonl

class TXTDocumentParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.all_chapter_documents = []

    def create_document(self, text_content, chapter):
        '''
        创建一个 Document 实例
        '''
        doc = Document(page_content=text_content)
        doc.metadata = {"chapter": chapter}
        return doc

    def create_document_list(self, text):
        '''
        将一个章节内容的每一小节的文本转换为多个 Document 实例
        '''
        document_list = []
        section_lines = text.split('\n')
        chapter = section_lines[0]
        current_sub_section = None
        for line in section_lines:
            match1 = re.match(r'^[一二三四五六七八九十]、', line)
            # match2 = re.match(r'^\d+(\.\d+)+ .+$',line)
            match2 = re.match(r'^\d+(\.\d+)+\s.+$',line)
            # print(line)
            # match3 = re.match(r'^[1-9][0-9]{0,8}、', line)
            if match1 or match2 :
                print(1)
                if current_sub_section:
                    document_list.append(self.create_document(text_content=''.join(sub_section_text), chapter=chapter))
                current_sub_section = line
                sub_section_text = [line+ '\n']
            elif current_sub_section:
                sub_section_text.append(line+ '\n')
        if current_sub_section:
            document_list.append(self.create_document(text_content=''.join(sub_section_text), chapter=chapter))
        return document_list

    def parse_pdf(self):
        '''
        解析 PDF 文件并转换为 Document 实例列表
        '''
        content = read_jsonl(self.file_name)
        # with pdfplumber.open(self.file_name) as pdf:
        # page_num = len(pdf.pages)
        current_section = None
        # for i in content:
        #     # page = pdf.pages[i]
        #     text = page.extract_text()
        #     text_lines = text.split('\n')
        i = 0
        with open(self.file_name,'r',encoding='utf-8') as content:
            content = content.readlines()
            # content = content.split('\n')
            for line in content:
                # text = line.get("inside","")
                text = line
                match1 = re.match(r'^第[一二三四五六七八九十]+节|第[1-9][0-9]{0,8}节(?!.*\.{6,})', text)
                match2 = re.match(r'^(第[一二三四五六七八九十]+章|第[1-9][0-9]{0,8}章)(?!.*\.{6,})', text)
                # match3 = re.match(r'^[一二三四五六七八九十]、', line)
                # match4 = re.match(r'^[1-9][0-9]{0,8}、', line)
                if match1 or match2 :
                    print(text)
                    if current_section:
                        # print(1)
                        section_text = ''.join(section_text)
                        self.all_chapter_documents.extend(self.create_document_list(section_text))
                    current_section = text
                    section_text = [text+'\n']
                elif current_section:
                    section_text.append(text)
                i+=1
            print(self.file_name + ' ' + str(i+1) + '/' + str(len(content)) + ' 页读写完成', end='\r')
            if current_section:
                section_text = ''.join(section_text)
                self.all_chapter_documents.extend(self.create_document_list(section_text))
    # print(self.all_chapter_documents)
        return self.all_chapter_documents

# 使用示例
parser = TXTDocumentParser(r'D:\sth_funny\citi2024\dataset\bs_challenge_financial_14b_dataset\pdf_txt_file\0b46f7a2d67b5b59ad67cafffa0e12a9f0837790.txt')
# parser = PDFDocumentParser(r'D:\一些比赛\citi2024\Chatwhale\pdf_parser\data\茅台.pdf')
documents = parser.parse_pdf()
#
# print('茅台年报Document实例列表如下\n')
for doc in documents[:]:
    print(doc.metadata)
    print(doc.page_content)
    print('-----------------------------')

print(len(documents))
