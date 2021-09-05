class OCRClient:
  def __init__(self,key):
    self.key=key

  def raw_post(file,language="eng",isOverlayRequired):
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
    

