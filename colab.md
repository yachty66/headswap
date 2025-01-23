1. change requirements file to following:

```
--extra-index-url https://download.pytorch.org/whl/cu117

torch
torchvision
torchaudio
opencv-python
onnxruntime-gpu
face-alignment==1.4.1
imgaug==0.4.0
numpy
huggingface-hub
```

2. go to preprocess.py and change align_img function to following:

```python
def align_img(img, lm, lm3D, mask=None, target_size=224., rescale_factor=102.):
    """
    Return:
        transparams        --numpy.array  (raw_W, raw_H, scale, tx, ty)
        img_new            --PIL.Image  (target_size, target_size, 3)
        lm_new             --numpy.array  (68, 2), y direction is opposite to v direction
        mask_new           --PIL.Image  (target_size, target_size)
    
    Parameters:
        img                --PIL.Image  (raw_H, raw_W, 3)
        lm                 --numpy.array  (68, 2), y direction is opposite to v direction
        lm3D               --numpy.array  (5, 3)
        mask               --PIL.Image  (raw_H, raw_W, 3)
    """

    w0, h0 = img.size
    if lm.shape[0] != 5:
        lm5p = extract_5p(lm)
    else:
        lm5p = lm

    # calculate translation and scale factors using 5 facial landmarks and standard landmarks of a 3D face
    t, s = POS(lm5p.transpose(), lm3D.transpose())
    s = rescale_factor/s

    # processing the image
    img_new, lm_new, mask_new = resize_n_crop_img(img, lm, t, s, target_size=target_size, mask=mask)
    
    # Ensure t values are scalar
    tx = float(t[0][0] if isinstance(t[0], np.ndarray) else t[0])
    ty = float(t[1][0] if isinstance(t[1], np.ndarray) else t[1])
    
    # Create transformation parameters array with scalar values
    trans_params = np.array([float(w0), float(h0), float(s), tx, ty], dtype=np.float32)

    return trans_params, img_new, lm_new, mask_new
```
