#for depth mapping to 8bit value
def depth_to_rgb_like(frame: np.ndarray) -> np.ndarray:
    max_unique = np.unique(frame)[-1]
    
    if max_unique > 250:
        print("Image was already converted rgb-like")
        print("Failed Depth to RGB-like")
        raise ValueError 
    else:
        mapped_color = np.linspace(0, 255, num=max_unique+1,
                                   endpoint=True, retstep=False,
                                   dtype=np.uint8)

        # Mapping (8bit)
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                color = frame[i][j][0]
                try:
                    frame[i][j][:] = np.array([mapped_color[color], mapped_color[color], mapped_color[color]])
                except IndexError:
                    print(i, j, color)
                    pass
    
    return frame