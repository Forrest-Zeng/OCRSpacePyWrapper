from ocrspace.errors import TooManyRequestsError
import requests, time

class OCR429ErrorOptions:
  Error = 0
  Wait = 1
  GentleNotification = 2
  IgnoreError = 3

class RequestHandler:
  
  @classmethod
  def get(fail, *args, **kwargs):
    response = requests.get(*args, **kwargs)
    if response.status_code == 429:
      if fail == 0:
        raise TooManyRequestsError("Too many requests.")
      if fail == 1:
        time.sleep(int(response.headers["Retry-After"]))
      if fail == 2:
        return f"429 Error. Retry after {int(response.headers['Retry-After'])}"
      if fail == 3:
        return response.json() 

    else:
      return response.json()

  @classmethod
  def post(fail, *args, **kwargs):
    response = requests.post(*args, **kwargs)
    if response.status_code == 429:
      if fail == 0:
        raise TooManyRequestsError("Too many requests.")
      if fail == 1:
        time.sleep(int(response.headers["Retry-After"]))
      if fail == 2:
        return f"429 Error. Retry after {int(response.headers['Retry-After'])}"
      if fail == 3:
        return response.json() 
    else:
      return response.json()