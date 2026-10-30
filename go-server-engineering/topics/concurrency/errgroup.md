# errgroup

独立专题，按需阅读；不属于生命周期主题的必读步骤。尚未进行用法实验。

## 基本语义与来源

本轮核对的 golang.org/x/sync v0.23.0 中，WithContext 建立任务组与派生 context；首个登记函数的非 nil 错误触发取消；Wait 等待登记函数返回并取得首个错误。普通 nil 返回不会触发相同的失败取消，Wait 返回时也会取消关联 context。

取消需要任务配合；未登记的子 goroutine 需要由调用方另行管理。详见 [锁定版本源码](https://github.com/golang/sync/blob/f75267d8412fc1dfd12b343644a7ea46e4d9c85d/errgroup/errgroup.go#L43-L112)。

## 后续内容

按具体问题补充最小用法、错误传播和取消实验。[实验占位](../../labs/errgroup-cancellation/README.md)
