'''
Created on May 9, 2019

@author: user
'''
import os

f_name = [];
single_name = ('p03', 'p08','p16','p17','p35','p36')
label_name = ('p33', 'p34')
with open('feature.name', 'r') as f_name_file:
    for line in f_name_file:
        f_name.append(line.strip())
         
# print(f_name);
# os.mknod('feature.seq')
with open('feature.data', 'r') as f_data_file:
    with open('feature.seq', 'a') as f_seq_file:
        f_line_seq = ''
        for line in f_data_file:
            f_data_line = []
            f_line_seq = ''
            f_data_line = line.strip().split('\t')
            for x in range(len(f_data_line)):
                value = f_data_line[x]
                temp =  f_name[x]
                if label_name.__contains__(temp):
                    continue
                if single_name.__contains__(temp):
                    f_line_seq = f_line_seq + temp + '_' + value + ' '
                elif value.__eq__('1'):
                    f_line_seq = f_line_seq + temp + ' '                
            f_line_seq = f_line_seq + '\n'
            f_seq_file.write(f_line_seq)