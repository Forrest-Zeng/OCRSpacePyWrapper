import requests

class OCRClient:
  def __init__(self,key,endpoint="https://api.ocr.space/parse/image"):
    self.endpoint=endpoint
    self.key=key

  def post(self, url=None, file=None, base64Image=None,filetype=None,OCREngine=1,language="eng",isOverlayRequired=False,detectOrientation=False,isCreateSearchablePdf=False,isSearchablePdfHideTextLayer=False,scale=False,isTable=False):
    languages=["ara"
    "bul",
    "chs",
    "cht",
    "hrv",
    "cze",
    "dan",
    "dut",
    "eng",
    "fin",
    "fre",
    "ger",
    "gre",
    "hun",
    "kor",
    "ita",
    "jpn",
    "pol",
    "por",
    "rus",
    "slv",
    "spa",
    "swe",
    "tur"]
    if language not in languages:
      raise AttributeError("Attribute language is not a valid language")
    data_body={
      "apikey":self.key,
      "OCREngine":OCREngine,
      "language":language,
      "isOverlayRequired":isOverlayRequired,
      "detectOrientation":detectOrientation,
      "isCreateSearchablePdf":isCreateSearchablePdf,"isSearchablePdfHideTextLayer":isSearchablePdfHideTextLayer,
      "scale":scale,
      "isTable":isTable
    }
    if filetype:
      data_body["filetype"]=filetype
    file_body={}
    if file:
      file_data = open(file,"rb")
      file_body["filename"] = file_data
      return requests.post(self.endpoint,files=file_body,data=data_body).json()
      file_data.close()
    elif url:
      data_body["url"]=url
    elif base64Image:
      data_body["base64Image"]=base64Image
    return requests.post(self.endpoint,files=file_body,data=data_body)
    
    

