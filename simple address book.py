f = open('1.txt', encoding='utf-8')
n = eval(f.read())  # str转换为字典
ll = 0
f.close()
while True:
    print('\n请输入想使用的功能（查看【1】，增加【2】），修改【3】，删除【4】，退出并保存【0】')
    x = input('请输入需要使用的功能：')
    a = len(n)
    if x == '查看' or x == '1':
        print('序号\t', '姓名\t', '电话\t', '邮箱')
        for i in range(0, a):
            print('第%d个' % int(i+1), end=' ')
            ll += 1
            for o in n[i].values():
                ll += 1
                print(o, end='  ')
            if ll % 4 == 0:
                print()

    elif x == '增加' or x == '2':
        n.append({})
        j1 = str(input('请输入姓名'))
        j2 = str(input('请输入电话'))
        j3 = str(input('请输入邮箱'))
        n[a]['姓名'] = j1
        n[a]['电话'] = j2
        n[a]['邮箱'] = j3
        print('添加完成')
    elif x == '修改' or x == '3':
        xiu = int(input('请输入要修改的序号：'))-1
        print('序号\t', '姓名\t', '电话\t', '邮箱')
        print('第%d个' % int(xiu+1), end=' ')
        for o in n[xiu].values():
            print(o, end='  ')
        print()
        j1 = str(input('请输入姓名'))
        j2 = str(input('请输入电话'))
        j3 = str(input('请输入邮箱'))
        n[xiu]['姓名'] = j1
        n[xiu]['电话'] = j2
        n[xiu]['邮箱'] = j3
        print('修改完成')
    elif x == '删除' or x == '4':
        xiu = int(input('请输入要删除的序号：')) - 1
        print('######警告删除不可逆！！！！#####')
        print('\n', '序号\t', '姓名\t', '电话\t', '邮箱')
        print('第%d个' % int(xiu + 1), end=' ')
        for o in n[xiu].values():
            print(o, end='  ')
        print('\n')
        print('###### 以上为要删除的内容 #####')
        if input('请输入（我确认删除）:') == '我确认删除':
            del n[xiu]
        else:
            continue
    else:
        break
print('已保存完毕')
f = open('1.txt', 'w', encoding='utf-8')
f.write(str(n))
f.close()