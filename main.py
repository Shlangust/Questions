import pandas as pd


xls = pd.ExcelFile('_100 questions.xlsx')
data_frame_dict = {}

for sheet_name in xls.sheet_names:
  data_frame_dict[sheet_name] = pd.read_excel(xls, sheet_name, index_col=0)

def get_sample_and_delete(sheet_name):
  sample_obj = data_frame_dict[sheet_name].sample()
  data_frame_dict[sheet_name].drop(sample_obj.index, inplace=True)
  return sample_obj
a = get_sample_and_delete('школьники')


print(len(data_frame_dict['школьники'].index))