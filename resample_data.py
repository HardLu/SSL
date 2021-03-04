import os, glob
import nibabel as nib
from skimage.transform import resize

path = r"/48cfceb8-8b77-4141-bba7-da05abd58d95/2018/yflu/third_point/code/fss_pirormask_128/runs/mySSL__CHAOST2_Superpix_sets_0_1shot/9/interm_preds/"

all_files = os.listdir(path)
for file in all_files:
    file_path = os.path.join(path, file)
    data = nib.load(file_path)
    affine = data.affine
    data = data.get_fdata()

    data = resize(data, [257, 257, data.shape[-1]], order=0)
    nib.save(nib.Nifti1Image(data, affine), file_path)