# pairwise-lens-vignette-ca

## 领域

游戏、图形与多媒体

## 主题

镜头暗角与色差校正

## 说明

焦距查表、通道分缩放与浮点计算。

初始状态下 `imaging/lens_vignette_ca.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
