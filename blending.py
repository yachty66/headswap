def blend_layouts(layout1, layout2, head_mask, body_mask):
    """
    Blend two semantic layouts using masks
    Args:
        layout1: Semantic layout of source head image
        layout2: Semantic layout of source body image
        head_mask: Binary mask for head region
        body_mask: Binary mask for body region
    Returns:
        blended_layout: Combined semantic layout
    """
    # Create rest region mask (neither head nor body)
    rest_mask = 1 - (head_mask + body_mask)
    
    # Blend layouts according to Algorithm 1, line 1350:
    # lblend = l1 ⊙ mH + l2 ⊙ mB + 0 ⊙ mr
    blended_layout = (layout1 * head_mask + 
                     layout2 * body_mask + 
                     0 * rest_mask)
    
    return blended_layout