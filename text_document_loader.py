from langchain_core.documents import Document


def load_text_file(file_path: str, encoding: str = "utf-8") -> list[Document]:
    """Industry-standard replacement for basic text loading."""
    with open(file_path, "r", encoding=encoding) as f:
        content = f.read()

        return [Document(page_content=content, metadata={"source": file_path})]
