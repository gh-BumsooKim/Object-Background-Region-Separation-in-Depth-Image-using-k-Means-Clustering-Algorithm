def nd_6_sigma(img: np.ndarray, **kwargs) -> np.ndarray:
    for key, value in kwargs.items():
        if key == "sigma":
            _s_level: int = value
        else:
            _s_level: int = 4 # default sigma level
            
    _s_yield: float = 0.0
    
    if _s_level == 1:   _s_yield = 0.69
    elif _s_level == 2: _s_yield = 0.31
    elif _s_level == 3: _s_yield = 0.067
    elif _s_level == 4: _s_yield = 0.0062
    elif _s_level == 5: _s_yield = 0.00023
    elif _s_level == 6: _s_yield = 0.0000034
    else: _s_yield = 0.0062

    _height, _width, _ = img.shape
    _min = int(round(_height * _width * _s_yield, 0)) # min value

    _value = np.unique(img)
    _hist = np.zeros(np.max(_value + 1), dtype=np.uint32)

    for i in range(_height):
        for j in range(_width):
            try:
                _hist[img[i][j][0]] += 1
            except IndexError as e:
                print(e)
                print(i, j, img[i][j][0])

    _hist_b = _hist < _min            
    _id = 0
    for i in range(len(_hist), 0, -1):
        if _hist_b[i-1] == False:
            _id = i
            break
        
    for i in range(_height):
        for j in range(_width):
            if _hist[img[i][j][0]] < _min and img[i][j][0] >= _id:
                img[i][j][:] = np.array([_value[int(len(_value)/2)], _value[int(len(_value)/2)], _value[int(len(_value)/2)]])
                        
    return img
