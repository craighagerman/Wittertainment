import os
from pathlib import Path



class DevData:
  DATA = "data"
  EXTERNAL = "external"
  INTERIM = "interim"
  PROCESSED = "processed"
  RAW = "raw"
  
  
  def __init__(self):
    self._notebook_dir = os.path.dirname(os.path.realpath(__file__))
    p = Path(self._notebook_dir)
    self._project_dir = p.parent.parent
    self._data_dir = os.path.join(self._project_dir, self.DATA)

  @property
  def project_dir(self):
    return self._project_dir

  @property
  def data_dir(self):
    return self._data_dir

  @property
  def notebook_dir(self):
    return self._notebook_dir

  @property
  def external_dir(self):
    return os.path.join(self.data_dir, self.EXTERNAL)

  @property
  def interim_dir(self):
    return os.path.join(self.data_dir, self.INTERIM)

  @property
  def processed_dir(self):
    return os.path.join(self.data_dir, self.PROCESSED)

  @property
  def raw_dir(self):
    return os.path.join(self.data_dir, self.RAW)


if __name__ == "__main__":
  d = DevData()
  print("-"*80)
  print(f"external dir:\t {d.external_dir}\texists: {os.path.exists(d.external_dir)}")
  print(f"interim dir:\t {d.interim_dir}\texists: {os.path.exists(d.interim_dir)}")
  print(f"processed dir:\t {d.processed_dir}\texists: {os.path.exists(d.processed_dir)}")
  print(f"raw dir:\t\t{d.raw_dir}\t\texists: {os.path.exists(d.raw_dir)}")
  print("-" * 80)