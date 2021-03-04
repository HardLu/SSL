import os,  glob
import nibabel as nib
import numpy as np
from skimage.transform import resize

# path = r"data/SABS/sabs_CT_normalized/"
# all_label = glob.glob(os.path.join(path, "label*.nii.gz"))
# all_cheat = glob.glob(os.path.join(path, "super*.nii.gz"))
# all_label.sort()
# all_cheat.sort()
# for label_path, cheat_path in zip(all_label, all_cheat):
#     label = nib.load(label_path)
#     affine = label.affine
#     label = label.get_fdata()
#     cheat = nib.load(cheat_path).get_fdata()
#     num = np.unique(cheat)[-1]
#     for l in [4, 5, 6]:
#         num += 1
#         cheat[label==l] = num
#     print(np.unique(cheat))
#     nib.save(nib.Nifti1Image(cheat, affine), cheat_path)

path = r"//48cfceb8-8b77-4141-bba7-da05abd58d95/2018/yflu/third_point/code/fss_pirormask_128/data/SABS/50-200_257-10case/"
image_num = int(len(os.listdir(path))/2)
print(image_num)
for id in range(image_num):
    img_path = os.path.join(path, "image_%s.nii.gz"%id)
    label_path = os.path.join(path, "label_%s.nii.gz"%id)

    img = nib.load(img_path).get_fdata()
    affine = nib.load(img_path).affine
    label = nib.load(label_path).get_fdata()

    img = img[50:200, 50:200, :]
    label = label[50:200, 50:200, :]
    img = resize(img, [257, 257, img.shape[-1]], order=1)
    label = resize(label, [257, 257, label.shape[-1]], order=0)
    nib.save(nib.Nifti1Image(img, affine), img_path)
    nib.save(nib.Nifti1Image(label, affine), label_path)