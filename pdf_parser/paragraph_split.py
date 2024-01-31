import pdfplumber
import re
from langchain.docstore.document import Document

class PDFDocumentParser:
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
            if match1:
                if current_sub_section:
                    document_list.append(self.create_document(text_content=''.join(sub_section_text), chapter=chapter))
                current_sub_section = line
                sub_section_text = [line + '\n']
            elif current_sub_section:
                sub_section_text.append(line + '\n')
        if current_sub_section:
            document_list.append(self.create_document(text_content=''.join(sub_section_text), chapter=chapter))
        return document_list

    def parse_pdf(self):
        '''
        解析 PDF 文件并转换为 Document 实例列表
        '''
        with pdfplumber.open(self.file_name) as pdf:
            page_num = len(pdf.pages)
            current_section = None
            for i in range(page_num):
                page = pdf.pages[i]
                text = page.extract_text()
                text_lines = text.split('\n')
                for line in text_lines:
                    match = re.match(r'^第[一二三四五六七八九十]+节(?!.*\.{6,})', line)
                    if match:
                        if current_section:
                            section_text = ''.join(section_text)
                            self.all_chapter_documents.extend(self.create_document_list(section_text))
                        current_section = line
                        section_text = [line + '\n']
                    elif current_section:
                        section_text.append(line + '\n')
                print(self.file_name + ' ' + str(i+1) + '/' + str(page_num) + ' 页读写完成', end='\r')
            if current_section:
                section_text = ''.join(section_text)
                self.all_chapter_documents.extend(self.create_document_list(section_text))
        return self.all_chapter_documents

# 使用示例
parser = PDFDocumentParser('pdf_parser\data\茅台.pdf')
documents = parser.parse_pdf()
#
print('茅台年报Document实例列表如下\n')
for doc in documents[:5]:
    print(doc.metadata)
    print(doc.page_content)
    print('-----------------------------')
