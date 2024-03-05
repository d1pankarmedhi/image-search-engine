import logging

def get_logger(name):
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  
  console_handler = logging.StreamHandler()
  file_handler = logging.FileHandler("file_log.log") # skip incase file saving not required
  
  c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
  f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
  console_handler.setFormatter(c_format)
  file_handler.setFormatter(f_format)

  logger.addHandler(console_handler)
  logger.addHandler(file_handler)

  return logger