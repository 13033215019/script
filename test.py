# 找出json和描述不符合的数据
json_data = [
    {
        "fieldLabel": "发票代码",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "发票号码", 
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "开票日期",
        "value": "20", 
        "valueDesc": "显示不必填"
    },
    {
        "fieldLabel": "币种",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "税率",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "税额合计",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "金额合计",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "校验码",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "价税合计",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "不可抵扣",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "发票附件",
        "value": "20",
        "valueDesc": "显示不必填"
    },
    {
        "fieldLabel": "归属人",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "身份证号",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "人员信息完整性",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "是否内部员工发票",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "是否代开发票",
        "value": "20",
        "valueDesc": "显示不必填"
    },
    {
        "fieldLabel": "是否国内（不含港澳台）旅客运输",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "出发城市",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "到达城市",
        "value": "10",
        "valueDesc": "不显示"
    },
    {
        "fieldLabel": "是否为进口增值税",
        "value": "10",
        "valueDesc": "不显示"
    }
]

desc = {
    "不显示": [
        "发票代码", "发票号码", "币种", "税率", "税额合计", "金额合计", 
        "校验码", "价税合计", "不可抵扣", "归属人", "身份证号", 
        "人员信息完整性", "是否内部员工发票", "是否代开发票", 
        "是否国内（不含港澳台）旅客运输", "出发城市", "到达城市", 
        "是否为进口增值税"
    ],
    "显示不必填": [
        "开票日期", "发票附件"
    ]
}

mismatches = []

for item in json_data:
    shouldNotShow = item["fieldLabel"] in desc["不显示"]
    shouldShowNotRequired = item["fieldLabel"] in desc["显示不必填"]
    
    if shouldNotShow and item["value"] != "10":
        mismatches.append(f'{item["fieldLabel"]} 应该不显示但value不是10')
    
    if shouldShowNotRequired and item["value"] != "20":
        mismatches.append(f'{item["fieldLabel"]} 应该显示不必填但value不是20')
    
    if not shouldNotShow and not shouldShowNotRequired:
        mismatches.append(f'{item["fieldLabel"]} 在描述中未定义')

print("不符合的数据：", mismatches)
