import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2

def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    
    # Add numbers to each mask
    for idx, ann in enumerate(sorted_anns):
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
        
        # Calculate center of mass for the mask
        y_indices, x_indices = np.where(m)
        if len(y_indices) > 0 and len(x_indices) > 0:
            center_y = int(np.mean(y_indices))
            center_x = int(np.mean(x_indices))
            
            # Add text with white color and black edge
            plt.text(center_x, center_y, str(idx+1), 
                    fontsize=12, 
                    color='white',
                    bbox=dict(facecolor='black', alpha=0.5),
                    ha='center', 
                    va='center')
    
    ax.imshow(img)
image = cv2.imread('me.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor

sam_checkpoint = "sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)



masks = mask_generator.generate(image)

plt.figure(figsize=(20,20))
plt.imshow(image)
show_anns(masks)
plt.axis('off')
# plt.show()  # Remove or comment out the show command
plt.savefig('output_image.png', bbox_inches='tight', pad_inches=0)
plt.close()  # Close the figure to free memory