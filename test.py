from ljhSpider.download import pdf_download


url = "https://www.biorxiv.org/content/10.1101/2023.06.16.545355v1.full.pdf"
path = "test_wget.pdf"

# pdf_download.download_pdf_requests(url, path)
pdf_download.download_pdf_by_wget(url, path)