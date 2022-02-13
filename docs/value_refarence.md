# Reference of constants
This project includes several connstants.  
Recommending to define required arguments with them at [set_values.py](../set_values.py).  

## Physical constants
### Required
```py
from internal.datas import Const as const
```
---
### const.newtonian_g
 Newtonian constant of gravitation
```math
G =  6.6743 \times 10^{-11} \,\, \mathrm{m^3kg^{-1}s^{-2}}
```
### const.mass_sun 
Solar mass
```math
M_\odot =  2 \times 10^{30} \,\, \mathrm{kg}
```
### const.c
Speed of light
```math
c = 299792458 \,\, \mathrm{m/s}
```

## Image size
### Required
```py
from internal.datas import Image as image
```
---
### image.sd
VGA, SD
```py
 {
     "height": 480,
     "width": 640
 }
```
### image.hd
HD, 720p
```py
 {
     "height": 720,
     "width": 1280
 }
```
### image.fhd
FHD (Full-HD), 1080p, 2K
```py
 {
     "height": 1080,
     "width": 1920
 }
```
### image.qhd
WQHD (Wide Quad-HD),1440p
```py
 {
     "height": 1440,
     "width": 2560
 }
```
### image.uhd
QFHD (Quad Full-HD), UHD 4K (2160p)
```py
 {
     "height": 2160,
     "width": 3840
 }
```
### image.fuhd
FUHD 8K (4320p)
```py
 {
     "height": 4320,
     "width": 7680
 }
```
