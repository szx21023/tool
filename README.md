# tool
小工具、小套件

- convex_polygon.py: 最大凸多邊形
- ![image](https://user-images.githubusercontent.com/63580311/139645733-ebcdc7f2-3a47-4937-b22f-f428bec2fa56.gif)

```
# example
from convex_polygon import convex_polygon
import pandas as pd
import numpy as np

data = np.random.random(size=(50, 2))
df = pd.DataFrame(data).rename(columns={0: 'x', 1: 'y'})
point_l = convex_polygon(df, 'x', 'y')

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
output_notebook()

p = figure(width=400, height=400)
p.circle(df['x'], df['y'], color='red')
p.circle([p[0] for p in point_l], [p[1] for p in point_l], color="navy")
p.line([p[0] for p in point_l], [p[1] for p in point_l], color="navy")
show(p)
```
