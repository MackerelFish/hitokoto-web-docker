# 句子包

一言开源社区官方提供的语句库，系 `hitokoto.cn` 数据打包集合。语句接口默认使用此库。

## 使用须知
## 本项目基于 https://github.com/hitokoto-osc/sentences-bundle 库
## 自建本地无限速一言api接口，Fork自2024.8.30，添加基于Fastapi运行的HTTP GET接口，测试运行于Python3.10.9510环境下，建议运行在3.10版本

参考： <https://sentences-bundle.hitokoto.cn>
## 原库使用须知
1. 本库遵循 AGPL 开源授权，您在使用本库时需要遵循 AGPL 授权的相关规定。这通常意味着：您在使用、分发、修改、扩充等涉及本库的操作时您需要开源您的修改作品。
*  除我们提供的超链接调用方式不受 AGPL 的开源，传染影响，其余使用方式都需要遵循 AGPL 授权。
2. 本库著作权并非完全由一言网持有。
* 如您是句子的原作者，且不希望您的句子参与公共分享，请您联系我们（`i@loli.online`），我们将移除相关侵权句子。
* 如您是原创句子的作者，这意味着一言是在经过您的确认后获得了拷贝、分发、出版、商业使用等长期授予的权限。当然，如果您想要移除您提交过的句子，我们依旧尊重您的著作权——移除相关句子。
3. 本库由系统自动维护，这意味我们不受理任何 issues, pull request。如果您有相关问题，请通过电邮或者工单系统向我们反馈。

其他条款待补充。

## 使用方法

1. 下载代码到本地你想存放的目录
2. pip安装poetry
3. 点击安装poetry依赖脚本文件创建该目录的虚拟环境
4. 编辑config.json文件自定义你想要的port端口
5. 点击start脚本文件运行api
6. 使用接口为 http://yourhost:yourport/HITOKOTO ，获取一条随机一言

返回值示例
```json
{
    "code":200,
    "message":"success",
    "data":{
        "id":5169,
        "uuid":"833a4fb8-73e7-473a-ac81-7d0398630dd6",
        "hitokoto":"没心没肺，活着不累。",
        "type":"f",
        "from":"网络",
        "from_who":null,
        "creator":"2247",
        "creator_uid":5148,
        "reviewer":4756,
        "commit_from":"web",
        "created_at":"1582967894",
        "length":10
    },
    "hitokoto":"没心没肺，活着不累。"
}
```

## data字段为该一言完整数据集，hitokoto字段为纯文字

## 如有更新自行前往 https://github.com/hitokoto-osc/sentences-bundle 下载sentences目录内json文件替换
