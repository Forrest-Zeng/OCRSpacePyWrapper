from request import RequestHandler, OCR429ErrorOptions
from errors import NoDataError, LanguageNotFoundError
from languages import OCRLanguage

class OCREngine:
  Engine1 = 1
  Engine2 = 2


class OCRClient:
  def __init__(
    self, 
    key,
    endpoint="https://api.ocr.space/parse/image"
  ):
    """
    :param key: OCRSpace API Key
    :param endpoint: (optional) OCRSpace API Endpoint 
    """
    self.endpoint = endpoint
    self.key = key

  def post(self, *, url=None, file=None, base64Image=None, filetype=None, OCREngine=OCREngine.Engine1, language=OCRLanguage.English, isOverlayRequired=False, detectOrientation=False, isCreateSearchablePdf=False, isSearchablePdfHideTextLayer=False, scale=False, isTable=False, fail=OCR429ErrorOptions.Error):
    """
    Returns the text for a given image in JSON format in a POST request to the endpoint.

    One of url, file, or base64Image is required.
    
    :param url: (optional) an absolute url path to a readable resource
    :param file: (optional) a filepath to a local resource
    :param base64Image: (optional) a base64 encoding of a resource
    :param filetype: (optional) overwrites the automatic file type detection
    :param OCREngine: (optional) which OCR engine to use, see: https://ocr.space/OCRAPI#ocrengine
    :param language: (optional) which language to use, only for engine type 1
    :param isOverlayRequired: (optional) if true, returns the coordinates of the bounding boxes for each word
    :param detectOrientation: (optional) if true, autorotate the image to have horizontal text
    :param isCreateSearchablePdf: (optional) if true, generates a searchable PDF file
    :param isSearchablePdfHideTextLayer: (optional) if true, renders text layer hidden, only applies if isCreateSearchablePdf is true
    :param scale: (optional) if true, scales up low resolution files to improve quality of results
    :param isTable: (optional) if true, makes sure OCR engine parses line by line
    :param fail: (optional) how to respond to 429 errors, 0 for raising an error, 1 for waiting until the timeout is over (often a long time), and 2 for return a string with errors
    :return: result in JSON format
    """    
    if language not in OCRLanguage.languages:
      raise LanguageNotFoundError("Invalid language.")

    data_body = {
      "apikey": self.key,
      "OCREngine": OCREngine,
      "language": language,
      "isOverlayRequired": isOverlayRequired,
      "detectOrientation": detectOrientation,
      "isCreateSearchablePdf": isCreateSearchablePdf,"isSearchablePdfHideTextLayer": isSearchablePdfHideTextLayer,
      "scale": scale,
      "isTable": isTable
    }
    if filetype:
      data_body["filetype"] = filetype
    file_body = {}
    if file:
      file_data = open(file,"rb")
      file_body["filename"] = file_data
      return RequestHandler.post(self.endpoint, files=file_body, data=data_body)
    if url:
      data_body["url"] = url
      return RequestHandler.post(self.endpoint, data=data_body)
    if base64Image:
      data_body["base64Image"] = base64Image
      return RequestHandler.post(self.endpoint, data=data_body)
    raise NoDataError("Please supply one of file, url, or base64Image.")

  def get(self, *, url=None, filetype=None, OCREngine=OCREngine.Engine1, language=OCRLanguage.English, isOverlayRequired=False, detectOrientation=False, isCreateSearchablePdf=False, isSearchablePdfHideTextLayer=False, scale=False, isTable=False, fail=OCR429ErrorOptions.Error):
    """
    Returns the text for a given image in JSON format in a GET request to the imageURL endpoint.
    
    :param url: an absolute url path to a readable resource
    :param filetype: (optional) overwrites the automatic file type detection
    :param OCREngine: (optional) which OCR engine to use, see: https://ocr.space/OCRAPI#ocrengine
    :param language: (optional) which language to use, only for engine type 1
    :param isOverlayRequired: (optional) if true, returns the coordinates of the bounding boxes for each word
    :param detectOrientation: (optional) if true, autorotate the image to have horizontal text
    :param isCreateSearchablePdf: (optional) if true, generates a searchable PDF file
    :param isSearchablePdfHideTextLayer: (optional) if true, renders text layer hidden, only applies if isCreateSearchablePdf is true
    :param scale: (optional) if true, scales up low resolution files to improve quality of results
    :param isTable: (optional) if true, makes sure OCR engine parses line by line
    :param fail: (optional) how to respond to 429 errors, 0 for raising an error, 1 for waiting until the timeout is over (often a long time), and 2 for return a string with errors
    :return: result in JSON format
    """    
    if language not in OCRLanguage.languages:
      raise LanguageNotFoundError("Invalid language.")

    data_body = {
      "OCREngine": OCREngine,
      "language": language,
      "isOverlayRequired": isOverlayRequired,
      "detectOrientation": detectOrientation,
      "isCreateSearchablePdf": isCreateSearchablePdf,"isSearchablePdfHideTextLayer": isSearchablePdfHideTextLayer,
      "scale": scale,
      "isTable": isTable
    }
    if url:
      data_body["url"] = url
    if filetype:
      data_body["filetype"] = filetype
    url = self.endpoint + f"url?apikey={self.key}"
    for header in data_body:
      url += f"&{header}={data_body[header]}"
    return RequestHandler.get(url)
    raise NoDataError("Please supply url for image")