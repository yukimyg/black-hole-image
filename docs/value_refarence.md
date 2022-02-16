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
![\begin{align*}
G = 6.6743 \times 10^{-11} \,\, \mathrm{m}^3 \mathrm{kg}^{-1} \mathrm{s}^{-2}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AG+%3D+6.6743+%5Ctimes+10%5E%7B-11%7D+%5C%2C%5C%2C+%5Cmathrm%7Bm%7D%5E3+%5Cmathrm%7Bkg%7D%5E%7B-1%7D+%5Cmathrm%7Bs%7D%5E%7B-2%7D%0A%5Cend%7Balign%2A%7D)

### const.mass_sun

Solar mass  
![\begin{align*}
M_\odot =  2 \times 10^{30} \,\, \mathrm{kg}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AM_%5Codot+%3D++2+%5Ctimes+10%5E%7B30%7D+%5C%2C%5C%2C+%5Cmathrm%7Bkg%7D%0A%5Cend%7Balign%2A%7D)

### const.c

Speed of light  
![\begin{align*}
c = 299792458 \,\, \mathrm{m/s}
\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ac+%3D+299792458+%5C%2C%5C%2C+%5Cmathrm%7Bm%2Fs%7D%0A%5Cend%7Balign%2A%7D)

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
