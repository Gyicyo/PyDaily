import torch
import imageio
import PIL
import torchvision

dir_path = 'data/p1ch4/volumetric-dicom/2-LUNG 3.0  B70f-04083'

vol_arr = imageio.volread(dir_path,'DICOM')

vol = torch.from_numpy(vol_arr).float()
vol = vol.unsqueeze(0)
print(vol) # 这里[1,99,512,512] 中的99是深度（容易误解为N（batch size）），512*512是图像大小，1是只有一个通道
