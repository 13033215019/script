#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版标签分析脚本
"""

import re
from collections import Counter

def analyze_labels(filename):
    """分析标签出现次数"""
    label_counter = Counter()
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line == 'message':
                continue
                
            # 提取标签名称，格式：ACTION~LabelName labelCal cost Xms
            match = re.match(r'([^~]+)~([^\s]+)', line)
            if match:
                action = match.group(1)
                label_name = match.group(2)
                label_counter[label_name] += 1
    
    return label_counter

def print_top_labels(counter, top_n=20):
    """打印出现次数最多的标签"""
    print(f"\n=== 出现次数最多的前{top_n}个标签 ===")
    print(f"{'排名':<4} {'标签名称':<60} {'出现次数':<10}")
    print("-" * 80)
    
    for i, (label, count) in enumerate(counter.most_common(top_n), 1):
        print(f"{i:<4} {label:<60} {count:<10}")

def analyze_by_action(filename):
    """按操作类型分析标签出现次数"""
    action_label_counter = {}
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line == 'message':
                continue
                
            # 提取操作和标签名称
            match = re.match(r'([^~]+)~([^\s]+)', line)
            if match:
                action = match.group(1)
                label_name = match.group(2)
                
                if action not in action_label_counter:
                    action_label_counter[action] = Counter()
                action_label_counter[action][label_name] += 1
    
    return action_label_counter

def print_action_analysis(action_counter):
    """打印按操作类型的分析结果"""
    print(f"\n=== 按操作类型分析 ===")
    
    for action, counter in action_counter.items():
        print(f"\n操作: {action}")
        print(f"总标签数: {sum(counter.values())}")
        print(f"唯一标签数: {len(counter)}")
        
        if counter:
            most_common = counter.most_common(3)
            print("最常见的3个标签:")
            for label, count in most_common:
                print(f"  - {label}: {count}次")

def main():
    filename = 'label_cal.txt'
    
    try:
        print("正在分析标签出现次数...")
        
        # 分析所有标签
        label_counter = analyze_labels(filename)
        
        print(f"总共分析了 {len(label_counter)} 个不同的标签")
        print(f"总标签调用次数: {sum(label_counter.values())}")
        
        # 打印最常见的标签
        print_top_labels(label_counter, 20)
        
        # 按操作类型分析
        action_counter = analyze_by_action(filename)
        print_action_analysis(action_counter)
        
        # 保存详细结果到文件
        with open('label_analysis_results.txt', 'w', encoding='utf-8') as f:
            f.write("标签出现次数详细分析结果\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("所有标签出现次数 (按次数降序排列):\n")
            f.write("-" * 50 + "\n")
            for i, (label, count) in enumerate(label_counter.most_common(), 1):
                f.write(f"{i:3d}. {label:<60} {count:>5}次\n")
            
            f.write(f"\n\n按操作类型分析:\n")
            f.write("=" * 50 + "\n")
            for action, counter in action_counter.items():
                f.write(f"\n操作: {action}\n")
                f.write(f"总标签数: {sum(counter.values())}\n")
                f.write(f"唯一标签数: {len(counter)}\n")
                f.write("最常见的5个标签:\n")
                for label, count in counter.most_common(5):
                    f.write(f"  - {label}: {count}次\n")
        
        print(f"\n详细分析结果已保存到: label_analysis_results.txt")
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {filename}")
    except Exception as e:
        print(f"分析过程中出错: {e}")

if __name__ == "__main__":
    main() 